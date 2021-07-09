import plotly.figure_factory as ff 
import pandas as pd 
import random
import csv
import plotly.graph_objects as go 
import statistics

df= pd.read_csv("medium_data.csv")
data=df["reading_time"].to_list()

mean=0

#code to find the mean of 100 data points a 1000 times and plot it
#function to get the mean of given data samples
#pass the number of data points you want as "counter"
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0, len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return(mean)

#function to plot the mean on the graph
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

sampling_mean=0

#to call the random function 1000 times
def setup():
    mean_list=[]
    for i in range(0, 1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    sampling_mean=statistics.mean(mean_list)
    print("Mean of sampling distribution: ", sampling_mean)

setup()
    
#to find the population mean
population_mean= statistics.mean(data)
print("Population mean: ", population_mean)

std_deviation=statistics.stdev(data)

zscore=(sampling_mean-population_mean)/std_deviation
print(zscore)
