import random

class Dane:

    def __init__(self):
        """inicjujemy dane klasy"""

    def stworz_losowe_dane(self):

        file_to_delete = open("results/LRU_results.csv", "w")   #usuwamy pozostałości w plikach przechowujących wyniki
        file_to_delete.close()                                  #po poprzednim uruchomieniu programu

        file_to_delete = open("results/FIFO_results.csv", "w")
        file_to_delete.close()

        file_to_delete = open("results/results.csv", "w")
        file_to_delete.close()

        for number in range(1, 51):                             #tworzymy 50 plików w folderze data o nazwach 1-50.csv
            with open(f"data/{number}.csv", "w") as f:
                for _ in range(0, 100):                         #zapisujemy do nich 100 losowych liczb z zakresu 1-15 jedna pod drugą
                    f.write(f"{random.randint(1, 15)}\n")
                f.close()