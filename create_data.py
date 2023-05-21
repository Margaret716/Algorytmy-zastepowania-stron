import random

class Data:

    def __init__(self):
        """Initialization of class data"""

    def create_random_data(self):

        file_to_delete = open("results/LRU_results.csv", "w")   #  removing remnants of the files from the previous run
        file_to_delete.close()                                 

        file_to_delete = open("results/FIFO_results.csv", "w")
        file_to_delete.close()

        file_to_delete = open("results/results.csv", "w")
        file_to_delete.close()

        for number in range(1, 51):                             #creating 50 files in directory "data"
            with open(f"data/{number}.csv", "w") as f:
                for _ in range(0, 100):                         #saving in each file 100 random numbers from 1 to 15
                    f.write(f"{random.randint(1, 15)}\n")
                f.close()
