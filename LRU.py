
def LRU_algorithm(reference_string):

    queue = [0, 0, 0]   #w tej liście będą przechowywane kolejne liczby, które wyznaczy w odpowiedniej kolejności LRU
    LRU_hits = 0        #ustalam wartość początkową dla wartości hit

    queue[0] = reference_string[0]       #ustalam stan początkowy
    counter = [1, 0, 0]                  #lista counter będzie przechowywała ile razy powtarza się dana liczba z listy queue


    for i in range(1, len(reference_string)):   #loopuje przez listę podaną w argumencie funkcji

        if reference_string[i] in queue:
            LRU_hits += 1                                    #jeśli napotkana wartość znajduje się już w liście dodajemy 1 do warości hit
            counter[queue.index(reference_string[i])] = 1    # i ustawiamy wartość countera dla tej komórki jako 1

        else:

            if i == 1:                                       #tutaj potrzeba było zawrzeć stan dla początkowych uruchomień
                queue[1] = reference_string[i]
                counter[1] = 1
                counter[0] = 2
                continue

            elif i == 2:
                queue[2] = reference_string[i]
                counter[1] = 2
                counter[2] = 1
                counter[0] = 3
                continue


            else:
                queue[counter.index((max(counter)))] = reference_string[i]   # to znajduje najstarszą, w tabeli queue zmieniamy wartość po tym indeksie
                counter[counter.index(max(counter))] = 0                     # ustawiam jej wiek o tym indeksie  na 0 w liście counter,
                                                                             # musi być w takiej kolejności, inaczej najstarsza będze drugą najstarszą

          # kończy się kolejka, więc zwiększamy wszystkie wartości zawarte w counterze o 1
            counter[0] += 1
            counter[1] += 1
            counter[2] += 1

    missing_LRU = len(reference_string) - LRU_hits      #obliczamy liczbę missingów i zapisujemy wynik do pliku
    with open("results/LRU_results.csv", "a") as w:
        w.write(f"{missing_LRU} ")
