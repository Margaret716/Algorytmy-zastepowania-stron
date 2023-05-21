
def LRU_algorithm(reference_string):

    queue = [0, 0, 0]   #in this list, subsequent numbers determined by the LRU algorithm will be stored in the appropriate order
    LRU_hits = 0        

    queue[0] = reference_string[0]       #setting startup state 
    counter = [1, 0, 0]                  #The "counter" list will store how many times each number from the "queue" list repeats

    for i in range(1, len(reference_string)):   #loop the list

        if reference_string[i] in queue:
            LRU_hits += 1                                    #If the encountered value is already in the list, we add 1 to the "hit" value
            counter[queue.index(reference_string[i])] = 1    # we also set the value of the counter for that cell as 1

        else:

            if i == 1:                                       #solving problem of firsts runs
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
                queue[counter.index((max(counter)))] = reference_string[i]   # finds the oldest one, in the "queue" table we change the value at that index
                counter[counter.index(max(counter))] = 0                     # setting its age on 0 in counter list
                                                                             # it'is important to do it in this order

          # queue is ending, so we increase all numbers in counter list by one
            counter[0] += 1
            counter[1] += 1
            counter[2] += 1

    missing_LRU = len(reference_string) - LRU_hits      #calculare number of missings and saving it to the file 
    with open("results/LRU_results.csv", "a") as w:
        w.write(f"{missing_LRU} ")
