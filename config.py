#------- IMPORTS ---------------------
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

#------- GLOBAL VARIABLES ------------
EURO_PORTFOLIO = ["BNP.PA", "DBK.DE"]
US_PORTFOLIO = ["AAPL", "NFLX"]
START_DATE = pd.Timestamp("2020-01-02")


