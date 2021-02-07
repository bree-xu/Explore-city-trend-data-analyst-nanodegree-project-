import pandas as pds
import numpy
import matplotlib.pyplot as plt

# import data files
helsinki_data = pds.read_csv(r"/home/bree/PycharmProjects/Explore_weather_trends/helsinki_data.csv")
global_data = pds.read_csv(r"/home/bree/PycharmProjects/Explore_weather_trends/global_data.csv")


# Define function to calculate moving average
def mv_avg(x, w):
    return x.rolling(w).mean()
#    return np.convolve(x, np.ones(w), 'valid')/w


# Calculating moving average for the global and local data
global_mv_avg = mv_avg(global_data['avg_temp'], 7)
helsinki_mv_avg = mv_avg(helsinki_data['avg_temp'], 7)


# Plotting Data using matplotlib Library
plt.plot(helsinki_data['year'], helsinki_mv_avg, label='Helsinki')
plt.plot(global_data['year'], global_mv_avg, label="Global")
plt.legend()
plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("Helsinki Average Temperature")
plt.show()


