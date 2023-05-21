
def FIFO_algorithm(reference_string):

    queue = [0] * 3     #creating label with 3 elements
    FIFO_hits = 0       

    for ref_val in reference_string:    #loop the list
        if ref_val in queue:
            FIFO_hits += 1              # If the encountered value is already in the list, we add 1 to the "hit" value
            continue                    # we return to 7th line

        queue[2] = queue[1]             #setting numbers in FIFO algorithm order
        queue[1] = queue[0]
        queue[0] = ref_val

    missing_FIFO = len(reference_string) - FIFO_hits    #calculating missings number and saving it to the file
    with open("results/FIFO_results.csv", "a") as w:
        w.write(f"{missing_FIFO} ")
