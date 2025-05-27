# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import simpledialog, messagebox
from siec_sensorow import SensorNetwork
from alg_genetyczny import GeneticAlgorithm
from guii import run_gui

def run_algorithm(network):
    ga = GeneticAlgorithm(network, population_size=100, num_generations=50, mutation_rate=0.001)
    ga.evolve()

    print("\nWspółrzędne aktywnych sensorów:")
    active_sensors = network.sensors[ga.best_solution == 1]
    for i, sensor in enumerate(active_sensors):
        print(f"Sensor {i}: {sensor}")

    return ga

def main():
    root = tk.Tk()
    root.withdraw()

    num_targets = None
    while num_targets is None:
        try:
            num_targets = simpledialog.askinteger("Liczba celów", "Podaj liczbę celów (1-20):", minvalue=1, maxvalue=20)
            if num_targets is None:
                print("Anulowano wprowadzanie liczby celów.")
                return
            if not (1 <= num_targets <= 20):
                raise ValueError
        except ValueError:
            messagebox.showerror("Błąd", "Proszę podać poprawną wartość liczby celów (1-20).")
            num_targets = None

    num_sensors = None
    while num_sensors is None:
        try:
            num_sensors = simpledialog.askinteger("Liczba Sensorów", "Podaj liczbę sensorów (1-90):", minvalue=1, maxvalue=90)
            if num_sensors is None:
                print("Anulowano wprowadzanie liczby sensorów.")
                return
            if not (1 <= num_sensors <= 90):
                raise ValueError
        except ValueError:
            messagebox.showerror("Błąd", "Proszę podać poprawną wartość liczby sensorów (1-90).")
            num_sensors = None
    
    sensor_range = None
    while sensor_range is None:
        try:
            sensor_range = simpledialog.askinteger("Zasięg Sensorów", "Podaj zasięg sensorów (10-90):", minvalue=10, maxvalue=90)
            if sensor_range is None:
                print("Anulowano wprowadzanie zasięgu sensorów.")
                return
            if not (10 <= sensor_range <= 90):
                raise ValueError
        except ValueError:
            messagebox.showerror("Błąd", "Proszę podać poprawną wartość zasięgu sensorów (10-90).")
            sensor_range = None    
            
    network = SensorNetwork(num_targets=num_targets, num_sensors=num_sensors, sensor_range=sensor_range, sensor_battery_capacity=100)           

    ga = run_algorithm(network)

    run_gui(network, ga)

if __name__ == "__main__":
    main()
