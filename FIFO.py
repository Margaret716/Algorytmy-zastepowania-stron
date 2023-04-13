
def FIFO_algorithm(reference_string):

    queue = [0] * 3     #tworzenie 3 elementowej tablicy -równoznaczne z queue = [0, 0, 0]
    FIFO_hits = 0       #ustalam wartość początkową dla wartości hit

    for ref_val in reference_string:    #loopujemy przez listę liczb, które funkcja dostaje jako argument
        if ref_val in queue:
            FIFO_hits += 1              #jeśli napotkana wartość znajduje się już w liście dodajemy 1 do warości hit
            continue                    #i wracamy do linii 7

        queue[2] = queue[1]             #tutaj ustawiamy kolejność konkretnych liczb względem algorytmu FIFO
        queue[1] = queue[0]
        queue[0] = ref_val

    missing_FIFO = len(reference_string) - FIFO_hits    #obliczamy liczbę missingów i zapisujemy wynik do pliku
    with open("results/FIFO_results.csv", "a") as w:
        w.write(f"{missing_FIFO} ")
