# -*- coding: utf-8 -*-

import numpy as np
import random
from siec_sensorow import SensorNetwork

class GeneticAlgorithm:
    def __init__(self, sensor_network, population_size, num_generations, mutation_rate):
        self.sensor_network = sensor_network # sieć sensorów
        self.population_size = population_size # wielkość populacji (obszaru)
        self.num_generations = num_generations # liczba generacji
        self.mutation_rate = mutation_rate # wsk mutacji
        self.population = np.random.randint(0, 2, (population_size, sensor_network.num_sensors)) # przechowuje populację rozw
        self.lifetime = 0 # ilosc generacji
        self.coverage_history = [] # sprawności pokrycia w kazdej generacji

    def evolve(self): 
        for generation in range(self.num_generations):
            fitness_scores = np.array([self.sensor_network.fitness(individual) for individual in self.population])
            selected_population = self.selection(fitness_scores)
            self.population = self.crossover(selected_population)
            self.mutate()

            best_fitness_index = np.argmax(fitness_scores)
            best_fitness = fitness_scores[best_fitness_index]
            best_individual = self.population[best_fitness_index]
            active_sensors = self.sensor_network.sensors[(best_individual == 1) & (self.sensor_network.sensor_battery > 0)]
            
            coverage_fitness, battery_fitness = self.sensor_network.evaluate_fitness_components(best_individual)
            self.coverage_history.append(coverage_fitness)
            print(f"Generacja {generation}, Najlepsza sprawność: {best_fitness:.4f}, Sprawność pokrycia: {coverage_fitness:.4f}, Sprawność zużycia baterii: {battery_fitness:.4f}")
            
            self.lifetime += 1
            if np.all(self.sensor_network.sensor_battery == 0):
                break

        self.best_solution = best_individual
        active_sensors = self.sensor_network.sensors[self.best_solution == 1]
        print("Najlepsze znalezione rozwiązanie (współrzędne aktywnych sensorów):")
        for sensor in active_sensors:
            print(sensor)
        print(f"Czas życia sieci: {self.lifetime} generacji")

    def plot_coverage_over_time(self):
        import matplotlib.pyplot as plt
        plt.plot(range(len(self.coverage_history)), self.coverage_history)
        plt.xlabel('Generacje')
        plt.ylabel('Sprawność pokrycia')
        plt.title('Pokrycie w czasie')
        plt.grid(True)
        plt.show()

    def selection(self, fitness_scores):
        probabilities = fitness_scores - fitness_scores.min()
        if probabilities.sum() > 0:
            probabilities /= probabilities.sum()
        else:
            probabilities = np.ones(self.population_size) / self.population_size
        selected_indices = np.random.choice(range(self.population_size), size=self.population_size, p=probabilities)
        return self.population[selected_indices]

    def crossover(self, population):
        offspring = []
        for i in range(0, self.population_size, 2):
            point = random.randint(1, self.sensor_network.num_sensors - 1)
            parent1 = population[i]
            parent2 = population[(i+1) % self.population_size]
            child1 = np.concatenate([parent1[:point], parent2[point:]])
            child2 = np.concatenate([parent2[:point], parent1[point:]])
            offspring.extend([child1, child2])
        return np.array(offspring)

    def mutate(self): # 0->1, 1->0, dodatkowa różnorodność do populacji
        mutation_mask = np.random.rand(self.population_size, self.sensor_network.num_sensors) < self.mutation_rate
        self.population = (self.population + mutation_mask) % 2

