import pandas as pd
import matplotlib.pyplot as plt


def combine_results():
    FIFO_results_list = []
    LRU_results_list = []

    """ 
        We read the results from files and enter them into the respective lists, 
        in order to later create a file composed of two columns. 
        The data for the chart will be read from this file.
        
    """

    with open('results/FIFO_results.csv', 'r') as f:
        data = f.readlines()

        for line in data:
            numbers = line.split()
            for number in numbers:
                FIFO_results_list.append(int(number))

    with open('results/LRU_results.csv', 'r') as f:
        data = f.readlines()

        for line in data:
            numbers = line.split()
            for number in numbers:
                LRU_results_list.append(int(number))

    for i in range(0, 50):
        with open('results/results.csv', 'a') as r:
            r.write(f"{FIFO_results_list[i]} {LRU_results_list[i]}\n")

    results = pd.read_csv('results/results.csv', sep=" ", header=None)
    df_results = pd.DataFrame(results)
    df_results.columns = ["FIFO", "LRU"]

    with open(f"results/results_statistic.csv", "w") as w:
        w.write(f"{df_results.describe()}")


def create_plot():

    """     Creating a chart from data in results.csv

                            STRUCTURE IN THE FILE
            Number of missings for FIFO   |   Number of missings for LRU

    """

    stat = pd.read_csv('results/results.csv', sep=' ', header=None)
    df_stat = pd.DataFrame(stat)
    df_stat.columns = ["FIFO", "LRU"]

    print(df_stat)

    plt.plot(df_stat["FIFO"], label='FIFO')
    plt.plot(df_stat["LRU"], label='LRU')
    plt.title("Comparison of FIFO and LRU")
    plt.ylabel("Missing pages")
    plt.xlabel("Próby [l.p.]")
    plt.legend()

    plt.show()

