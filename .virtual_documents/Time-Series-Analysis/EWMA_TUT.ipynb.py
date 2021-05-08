import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")


airline = pd.read_csv('airline_passengers.csv',index_col="Month")


airline


#Now giving days to our dataset
#earlier we only had year and month
airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index) 


airline.head()


airline.plot()


#using this we create new columns
airline['6-month-SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()


airline['12-month-SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()


airline['un-month-SMA'] = airline['Thousands of Passengers'].mean()


airline


airline.plot()


airline['EWMA-12'] = airline[]
