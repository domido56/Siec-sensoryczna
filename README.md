# Maksymalizacja czasu życia sieci sensorowej za pomocą metody metaheurystycznej: algorytm genetyczny

## Specyfikacja wymagań
Cel projektu:
Celem projektu jest maksymalizacja czasu życia sieci sensorowej przy użyciu algorytmu genetycznego.

Opis problemu:
Sieć sensorowa składająca się z określonej liczby sensorów i celów, gdzie sensory mają ograniczoną baterię i określony zasięg. Celem jest maksymalne pokrycie celów przy minimalnym zużyciu energii.

Wymagania funkcjonalne:
- Implementacja algorytmu genetycznego. 
- Wizualizacja sieci sensorowej w GUI. 
- Wyświetlanie zasięgu działania sensorów. 
- Wyświetlanie stanu baterii sensorów. 
- Automatyczne zatrzymanie symulacji po wyczerpaniu baterii sensorów. 

Wymagania niefunkcjonalne: 
- System powinien działać płynnie i efektywnie. 
- Interfejs powinien być intuicyjny i łatwy w obsłudze. 
- System powinien działać stabilnie i być odporny na błędy.

## Architektura systemu
Opis struktury systemu:
Program składa się z trzech głównych modułów: main.py, sieci_sensorow.py oraz 
alg_genetyczny.py. 

Moduł ‘main.py’: 
Jest odpowiedzialny za uruchomienie aplikacji. Pobiera od użytkownika zasięg 
sensorów za pomocą ‘simpledialog’. Inicjalizuje sieci sensorów z określoną liczbą 
celów, sensorów, zasięgiem oraz pojemnością baterii. Uruchamia algorytm genetyczny, 
wyświetla współrzędne aktywnych sensorów oraz uruchamia interfejs graficzny (GUI). 

Moduł ‘sieci_sensorow.py’: 
Zajmuje się reprezentacją sieci sensorów (klasa SensorNetwork) oraz oceną 
sprawności rozwiązań. Składa się z funkcji: 
- ‘__init__’: inicjalizuje sieć z określoną liczbą celów, sensorów, zasięgiem oraz 
pojemnością baterii.
- ‘fitness’: oblicza sprawność danego rozwiązania (uwzględniając pokrycie celów 
i zużycie baterii).
- ‘evaluate_fitness_components’: ocenia komponenty sprawności dla danego 
rozwiązania, takie jak pokrycie celów i zużycie baterii.
- ‘minimize_active_sensors’: minimalizuje liczbę aktywnych sensorów 
(optymalizuje rozwiązanie).
- ‘calculate_coverage’: oblicza pokrycie celów przez aktywne sensory.
  
Moduł ‘alg_genetyczny.py’: Zawiera implementację algorytmu genetycznego. Składa się z klasy GeneticAlgorithm i 
takich funkcji jak: 
- ‘__init__’: inicjalizuje algorytm z określonymi parametrami.
- ‘evolve’: przeprowadza proces ewolucji przez określoną liczbę generacji, 
oceniając sprawność rozwiązań, dokonując: selekcji, krzyżowania oraz mutacji 
populacji.
- ‘plot_coverage_over_time’: rysuje wykres - zmianę pokrycia w czasie.
- ‘selection’: realizuje selekcję rozwiązań na podstawie ich sprawności. 
- ‘crossover’: realizuje krzyżowanie rozwiązań w celu generowania potomstwa. 
- ‘mutate’: wprowadza mutacje do populacji, żeby zapewnić różnorodność 
rozwiązań.

Moduł ‘guii.py’: 
Zajmuje się interfejsem graficznym aplikacji. Składa się z klasy SensorNetworkApp i 
takich funkcji jak: 
- ‘__init__’: inicjalizuje interfejs, tworzy przyciski i rysuje sieć sensorów.
- ‘draw_buttons’: tworzy przyciski do sterowania symulacją. 
- ‘draw_legend’: rysuje legendę. 
- ‘draw_network_with_ranges’: rysuje sieć sensorów z zasięgami. 
- ‘draw_network_with_battery’: rysuje sieć sensorów ze stanem baterii. 
- ‘draw_grid’: rysuje siatkę. 
- ‘update_simulation’: aktualizuje stan symulacji. 
- ‘start_simulation’: rozpoczyna symulację. 
- ‘stop_simulation’: zatrzymuje symulację. 

Integracja systemu: 
1. ‘main.py’ inicjalizuje sieć sensorów i uruchamia algorytm genetyczny. 
2. ‘alg_genetyczny.py’ ewoluuje populację rozwiązań, oceniając je za pomocą 
metod z modułu ‘sieci_sensorow.py’. 
3. ‘guii.py’ wizualizuje sieć sensorów i umożliwia użytkownikowi interakcję z 
symulacją.

## Diagramy
Diagramy przypadków użycia:

Diagram klas:
