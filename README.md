# Maksymalizacja czasu życia sieci sensorowej – algorytm genetyczny
Projekt implementuje algorytm genetyczny do optymalizacji czasu życia sieci sensorowej. System maksymalizuje pokrycie celów przy minimalnym zużyciu energii sensorów.
## Opis problemu
Sieć sensorowa składa się z określonej liczby sensorów i celów. Sensory mają ograniczoną baterię i zasięg działania. Algorytm genetyczny szuka optymalnego rozwiązania – które sensory aktywować, aby pokryć wszystkie cele jak najdłużej.
## Funkcjonalności
- Algorytm genetyczny z selekcją, krzyżowaniem i mutacją
- Wizualizacja sieci sensorowej w GUI (Tkinter)
- Wyświetlanie zasięgu działania sensorów
- Monitoring stanu baterii w czasie rzeczywistym
- Wykres sprawności pokrycia w czasie
- Automatyczne zatrzymanie po wyczerpaniu baterii
## Struktura projektu
1. main.py inicjalizuje sieć sensorów i uruchamia algorytm genetyczny.
2. sieci_sensorow.py reprezentuje sieci i funkcje fitness
3. alg_genetyczny.py ewoluuje populację rozwiązań, oceniając je za pomocą 
metod z modułu sieci_sensorow.py. 
4. guii.py wizualizuje sieć sensorów i umożliwia użytkownikowi interakcję z 
symulacją.

## Diagramy
Diagramy przypadków użycia:
<img width="745" height="270" alt="diag p uz" src="https://github.com/user-attachments/assets/e117b752-120b-48bc-97fa-04f3cfd9c220" />

<img width="371" height="527" alt="diag p uz2" src="https://github.com/user-attachments/assets/92c91606-ff49-4a94-9047-78477acb5435" />

Diagram klas:
<img width="927" height="510" alt="diag kl" src="https://github.com/user-attachments/assets/218d4d30-f6b9-43ed-b924-97b4d36aef62" />

## Instalacja
### Wymagania
- Python 3.x
- matplotlib
- numpy
### Instalacja bibliotek
```bash
pip install matplotlib numpy
```
## Uruchomienie programu
Wpisz w konsoli: python main.py

## Korzystanie z programu
### Konfiguracja symulacji
Po uruchomieniu pojawią się okna dialogowe. Wprowadź dane (sugerowane wartości):
- Liczba celów: 10 - 20
- Liczba sensorów: 50 - 90
- Zasięg sensora: 30 - 50
### Korzystanie z interfejsu
- Kliknij "Pokaż zasięgi", aby zobaczyć promienie działania aktywnych urządzeń.
- Kliknij "Pokaż stan baterii", aby zobaczyć procentowe naładowanie nad sensorami.
- Kliknij "Zatrzymaj symulację", aby przerwać obliczenia.

## Przykładowe wyniki (Testy)
### Test 1: 
- Liczba celów: 10 
- Liczba sensorów: 50 
- Zasięg sensora: 30 
<img width="755" height="406" alt="test1" src="https://github.com/user-attachments/assets/5d6a2400-aca3-4566-b495-2212017e2ae6" />

Pomimo tego, że algorytm dąży do najlepszych rozwiązań, przypadkowe mutacje, które niekoniecznie są korzystne, zdarzają się. Jednakże, algorytm szybko naprawia swoje błędy, co widać na wykresie. Po serii nieudanych rozwiązań, algorytm ustala się ponownie dla pokrycia 100%. 

### Test 2: 
- Liczba celów: 15 
- Liczba sensorów: 50 
- Zasięg sensora: 50
<img width="755" height="402" alt="test2" src="https://github.com/user-attachments/assets/e01781c7-1595-48b1-b35b-7e3e91c8f860" />

Sensory działały w miarę poprawnie. Na wykresie widać, że raz sensor, który miał w swoim zasięgu cel, wszedł w stan uśpienia. Może być to spowodowane nieustannym szukaniem dobrego rozwiązania. 
