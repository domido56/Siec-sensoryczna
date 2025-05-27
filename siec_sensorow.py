# -*- coding: utf-8 -*-

import numpy as np

class SensorNetwork:
    def __init__(self, num_targets, num_sensors, sensor_range, sensor_battery_capacity):
        self.num_targets = num_targets 
        self.num_sensors = num_sensors
        self.sensor_range = sensor_range
        self.sensor_battery_capacity = sensor_battery_capacity
        self.targets = np.random.randint(0, 100, (num_targets, 2))
        self.sensors = np.random.randint(0, 100, (num_sensors, 2))
        self.sensor_battery = np.full(num_sensors, sensor_battery_capacity)

    def fitness(self, solution): 
        coverage_fitness, battery_fitness = self.evaluate_fitness_components(solution)
        return coverage_fitness * battery_fitness

    def evaluate_fitness_components(self, solution): 
        active_sensors = self.sensors[(solution == 1) & (self.sensor_battery > 0)] 
        coverage = np.zeros(self.num_targets) 
        over_coverage_penalty = 0
        
        for i, target in enumerate(self.targets): 
            distances = np.sqrt(np.sum((active_sensors - target) ** 2, axis=1)) 
            sensors_covering = np.sum(distances <= self.sensor_range) 
            if sensors_covering > 0: 
                coverage[i] = 1 
        total_coverage = np.sum(coverage) / self.num_targets 
        battery_usage = np.sum(solution * self.sensor_battery_capacity) / (self.num_sensors * self.sensor_battery_capacity) 
        coverage_fitness = total_coverage - 0.1 * over_coverage_penalty / self.num_targets 
        battery_fitness = 1 - battery_usage 
        
        return coverage_fitness, battery_fitness

    def minimize_active_sensors(self, solution, active_sensors):
        minimal_solution = solution.copy() 
        active_sensors_indices = np.where(solution==1)[0] 
        
        for sensor_index in active_sensors_indices: 
            minimal_solution[sensor_index] = 0 
            new_coverage = self.calculate_coverage(minimal_solution) 
            

        if np.sum(new_coverage) < np.sum(self.calculate_coverage(solution)):
            minimal_solution[sensor_index] = 1 
           
        return minimal_solution
    
    def calculate_coverage(self, solution):
        active_sensors = self.sensors[(solution == 1) & (self.sensor_battery > 0)]
        coverage = np.zeros(self.num_targets)  
        
        for i, target in enumerate(self.targets):
            distances = np.sqrt(np.sum((active_sensors - target) ** 2, axis=1))
            if np.any(distances <= self.sensor_range):
                coverage[i] = 1
         
        return coverage
                

