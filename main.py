import LRU
import FIFO
import create_data
import plot

a = create_data.Data()  #creating data
a.create_random_data()

for i in range(1, 51):

    with open(f"data/{i}.csv", "r") as file:
        data = file.readlines()

    reference_string = []
    for line in data:           #reading data from files and writing them to the list
        numbers = line.split()           # split() change data from file to list
        for number in numbers:
            reference_string.append(number)

    LRU.LRU_algorithm(reference_string)        #run LRU algorithm
    FIFO.FIFO_algorithm(reference_string)      #run FIFO algorithm


plot.combine_results()          #creating file with data ready to convert them to a plot
plot.create_plot()              #creating the plot
