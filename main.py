import LRU
import FIFO
import create_data
import plot

a = create_data.Dane()  #tworzymy dane
a.stworz_losowe_dane()

for i in range(1, 51):

    with open(f"data/{i}.csv", "r") as file:
        data = file.readlines()

    reference_string = []
    for line in data:           #odczytujemy dane z pliku i wpisujemy je do listy
        numbers = line.split()           # split() zmienia dane z pliku w listę
        for number in numbers:
            reference_string.append(number)

    LRU.LRU_algorithm(reference_string)        #uruchamiamy algorytm LRU
    FIFO.FIFO_algorithm(reference_string)      #uruchamiamy algorytm FIFO


plot.combine_results()          #tworzymy gotowy plik z danymi pod wykres
plot.create_plot()              #tworzymy wykres
