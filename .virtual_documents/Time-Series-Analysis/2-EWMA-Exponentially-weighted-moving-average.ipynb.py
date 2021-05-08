import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")


airline = pd.read_csv('airline_passengers.csv',index_col="Month")


airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)


airline.head()


airline['6-month-SMA']=airline['Thousands of Passengers'].rolling(window=6).mean()
airline['12-month-SMA']=airline['Thousands of Passengers'].rolling(window=12).mean()


airline.head()


airline.plot()


airline['EWMA12'] = airline['Thousands of Passengers'].ewm(span=12).mean()


airline[['Thousands of Passengers','EWMA12']].plot()
