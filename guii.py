# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import Canvas, simpledialog, messagebox
import numpy as np
from alg_genetyczny import GeneticAlgorithm
from siec_sensorow import SensorNetwork

class SensorNetworkApp(tk.Tk):
    def __init__(self, network, ga):
        super().__init__()
        self.title("Sensor Network Simulation")
        self.network = network
        self.ga = ga
        self.best_solution = np.ones(network.num_sensors)
        self.canvas = Canvas(self, width=600, height=600, bg='white')
        self.canvas.pack()
        self.draw_buttons()
        self.draw_network_with_ranges()
        self.update_interval = 1000
        self.simulation_running = True
        self.simulation_time = 0
        self.start_simulation()

    def draw_buttons(self):
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)
        self.button_ranges = tk.Button(self.button_frame, text="Pokaż zasięgi", command=self.draw_network_with_ranges)
        self.button_ranges.pack(side=tk.LEFT)
        self.button_battery = tk.Button(self.button_frame, text="Pokaż stan baterii", command=self.draw_network_with_battery)
        self.button_battery.pack(side=tk.LEFT)
        self.button_stop = tk.Button(self.button_frame, text="Zatrzymaj symulację", command=self.stop_simulation)
        self.button_stop.pack(side=tk.RIGHT)
    
    def draw_legend(self):
        offset_y = 550
        self.canvas.create_oval(10, offset_y, 30, offset_y + 20, fill='red')
        self.canvas.create_text(50, offset_y + 10, anchor='w', text='- cele')
        self.canvas.create_oval(150, offset_y, 170, offset_y + 20, fill='blue')
        self.canvas.create_text(190, offset_y + 10, anchor='w', text='- aktywne sensory')
        self.canvas.create_oval(290, offset_y, 310, offset_y + 20, fill='gray')
        self.canvas.create_text(330, offset_y + 10, anchor='w', text='- uśpione sensory')

    def draw_network_with_ranges(self):
        self.canvas.delete("all")
        self.draw_grid()
        self.draw_legend()  
        scale = 4
        offset = 40
        for target in self.network.targets:
            x, y = target * scale + offset
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='red', outline='red')
        for i, sensor in enumerate(self.network.sensors):
            x, y = sensor * scale + offset
            color = 'blue' if self.best_solution[i] == 1 and self.network.sensor_battery[i] > 0 else 'gray'
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill=color, outline=color)
            if self.best_solution[i] == 1 and self.network.sensor_battery[i] > 0:
                range_circle = self.network.sensor_range * scale
                self.canvas.create_oval(x-range_circle, y-range_circle, x+range_circle, y+range_circle, outline='green', dash=(4, 4))

    def draw_network_with_battery(self):
        self.canvas.delete("all")
        self.draw_grid()
        scale = 4
        offset = 40
        for target in self.network.targets:
            x, y = target * scale + offset
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='red', outline='red')
        self.sensor_texts = []
        for i, sensor in enumerate(self.network.sensors):
            x, y = sensor * scale + offset
            color = 'blue' if self.best_solution[i] == 1 and self.network.sensor_battery[i] > 0 else 'gray'
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill=color, outline=color)
            text_id = self.canvas.create_text(x, y-10, text=f"{self.network.sensor_battery[i]}", font=('Arial', 8), fill='black')
            self.sensor_texts.append(text_id)

    def draw_grid(self):
        scale = 4
        offset = 40
        for i in range(0, 120, 10):
            x = i * scale + offset
            self.canvas.create_line(x, offset, x, 600 - offset, fill='darkgray', dash=(2, 5))
            self.canvas.create_line(offset, x, 600 - offset, x, fill='darkgray', dash=(2, 5))
            self.canvas.create_text(x, offset/2, text=str(i), font=('Arial', 8))
            self.canvas.create_text(offset/2, x, text=str(i), font=('Arial', 8))

    def update_simulation(self):
        if not self.simulation_running:
            return
        self.ga.evolve()
        self.best_solution = self.ga.best_solution

        for i in range(self.network.num_sensors):
            if self.best_solution[i] == 1:
                self.network.sensor_battery[i] -= 10
            else:
                self.network.sensor_battery[i] -= 5

        self.network.sensor_battery = np.maximum(self.network.sensor_battery, 0)
        self.draw_network_with_ranges()
        self.simulation_time += self.update_interval / 1000

        if np.all(self.network.sensor_battery == 0):
            self.stop_simulation()
        else:
            self.after(self.update_interval, self.update_simulation)

    def start_simulation(self):
        self.update_simulation()

    def stop_simulation(self):
        self.simulation_running = False
        print(f"Czas życia sieci: {self.simulation_time} sekund")
        self.ga.plot_coverage_over_time()

def run_gui(network, ga):
    app = SensorNetworkApp(network, ga)
    app.mainloop()
