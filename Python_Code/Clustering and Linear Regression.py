# Creator: Nicolas Euliarte Veliez
# Date of Creation: 28th Jan 2020
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import glob
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path
import scipy
import os
import csv
import seaborn as sns
from pandas._libs.parsers import na_values
from scipy import stats
import operator as op
from sklearn.cluster import KMeans
import statsmodels.formula.api as smf
from statistics import mean
from datetime import datetime
import statsmodels.api as sm
from dateutil.relativedelta import relativedelta
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from pandas.plotting import scatter_matrix
from sklearn.neural_network import MLPClassifier
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
# ----------------------------------------------------------------------------------------------------------------------
# Shows the whole thing no cut-offs

np.set_printoptions(threshold=sys.maxsize)

# Gets the files and the information -----------------------------------------------------------------------------------
fileNames = glob.glob("Data/*.csv")
Files = []


# For ease of access knowing the correct entry of the data -------------------------------------------------------------
def dataAddToArray():
    date = pd.read_csv('Data/01-2014.csv')
    Files.append(date)
    Files[0]["Month and Year"] = "January-2014"
    date = pd.read_csv('Data/02-2014.csv')
    Files.append(date)
    Files[1]["Month and Year"] = "February-2014"
    date = pd.read_csv('Data/03-2014.csv')
    Files.append(date)
    Files[1]["Month and Year"] = "March-2014"
    date = pd.read_csv('Data/04-2014.csv')
    Files.append(date)
    Files[3]["Month and Year"] = "April-2014"
    date = pd.read_csv('Data/05-2014.csv')
    Files.append(date)
    Files[4]["Month and Year"] = "May-2014"
    date = pd.read_csv('Data/06-2014.csv')
    Files.append(date)
    Files[5]["Month and Year"] = "June-2014"
    date = pd.read_csv('Data/07-2014.csv')
    Files.append(date)
    Files[6]["Month and Year"] = "July-2014"
    date = pd.read_csv('Data/08-2014.csv')
    Files.append(date)
    Files[7]["Month and Year"] = "August-2014"
    date = pd.read_csv('Data/09-2014.csv')
    Files.append(date)
    Files[8]["Month and Year"] = "September-2014"
    date = pd.read_csv('Data/10-2014.csv')
    Files.append(date)
    Files[9]["Month and Year"] = "October-2014"
    date = pd.read_csv('Data/11-2014.csv')
    Files.append(date)
    Files[10]["Month and Year"] = "November-2014"
    date = pd.read_csv('Data/12-2014.csv')
    Files.append(date)
    Files[11]["Month and Year"] = "December-2014"
    date = pd.read_csv('Data/01-2015.csv')
    Files.append(date)
    Files[12]["Month and Year"] = "January-2015"
    date = pd.read_csv('Data/02-2015.csv')
    Files.append(date)
    Files[13]["Month and Year"] = "February-2015"
    date = pd.read_csv('Data/03-2015.csv')
    Files.append(date)
    Files[14]["Month and Year"] = "March-2015"
    date = pd.read_csv('Data/04-2015.csv')
    Files.append(date)
    Files[15]["Month and Year"] = "April-2015"
    date = pd.read_csv('Data/05-2015.csv')
    Files.append(date)
    Files[16]["Month and Year"] = "May-2015"
    date = pd.read_csv('Data/06-2015.csv')
    Files.append(date)
    Files[17]["Month and Year"] = "June-2015"
    date = pd.read_csv('Data/07-2015.csv')
    Files.append(date)
    Files[18]["Month and Year"] = "July-2015"


# data frame -----------------------------------------------------------------------------------------------------------
dataAddToArray()

# All the titles i.e. the months
tFNames = [
    '01/14', '02/14', '03/14', '04/14', '05/14',
    '06/14', '07/14', '08/14', '09/14', '10/14',
    '11/14', '12/14', '01/15', '02/15', '03/15',
    '04/15', '05/15', '06/15', '07/15'
]

# initialize data of lists for number of homicide convictions
data = {
    'location': [Files[0].iloc[1, 0], Files[0].iloc[2, 0], Files[0].iloc[3, 0],
                 Files[0].iloc[4, 0], Files[0].iloc[5, 0], Files[0].iloc[6, 0],
                 Files[0].iloc[7, 0], Files[0].iloc[8, 0], Files[0].iloc[9, 0],
                 Files[0].iloc[10, 0], Files[0].iloc[11, 0], Files[0].iloc[12, 0],
                 Files[0].iloc[13, 0], Files[0].iloc[14, 0], Files[0].iloc[15, 0],
                 Files[0].iloc[16, 0], Files[0].iloc[17, 0], Files[0].iloc[18, 0],
                 Files[0].iloc[19, 0], Files[0].iloc[20, 0], Files[0].iloc[21, 0],
                 Files[0].iloc[22, 0], Files[0].iloc[23, 0], Files[0].iloc[24, 0],
                 Files[0].iloc[25, 0], Files[0].iloc[26, 0], Files[0].iloc[27, 0],
                 Files[0].iloc[28, 0], Files[0].iloc[29, 0], Files[0].iloc[30, 0],
                 Files[0].iloc[31, 0], Files[0].iloc[32, 0], Files[0].iloc[33, 0],
                 Files[0].iloc[34, 0], Files[0].iloc[35, 0], Files[0].iloc[36, 0],
                 Files[0].iloc[37, 0], Files[0].iloc[38, 0], Files[0].iloc[39, 0],
                 Files[0].iloc[40, 0], Files[0].iloc[41, 0], Files[0].iloc[42, 0]],
    'Jan14': [
        Files[0].iloc[1, 1], Files[0].iloc[2, 1], Files[0].iloc[3, 1],
        Files[0].iloc[4, 1], Files[0].iloc[5, 1], Files[0].iloc[6, 1],
        Files[0].iloc[7, 1], Files[0].iloc[8, 1], Files[0].iloc[9, 1],
        Files[0].iloc[10, 1], Files[0].iloc[11, 1], Files[0].iloc[12, 1],
        Files[0].iloc[13, 1], Files[0].iloc[14, 1], Files[0].iloc[15, 1],
        Files[0].iloc[16, 1], Files[0].iloc[17, 1], Files[0].iloc[18, 1],
        Files[0].iloc[19, 1], Files[0].iloc[20, 1], Files[0].iloc[21, 1],
        Files[0].iloc[22, 1], Files[0].iloc[23, 1], Files[0].iloc[24, 1],
        Files[0].iloc[25, 1], Files[0].iloc[26, 1], Files[0].iloc[27, 1],
        Files[0].iloc[28, 1], Files[0].iloc[29, 1], Files[0].iloc[30, 1],
        Files[0].iloc[31, 1], Files[0].iloc[32, 1], Files[0].iloc[33, 1],
        Files[0].iloc[34, 1], Files[0].iloc[35, 1], Files[0].iloc[36, 1],
        Files[0].iloc[37, 1], Files[0].iloc[38, 1], Files[0].iloc[39, 1],
        Files[0].iloc[40, 1], Files[0].iloc[41, 1], Files[0].iloc[42, 1]],

    'Feb14': [
        Files[1].iloc[1, 1], Files[1].iloc[2, 1], Files[1].iloc[3, 1],
        Files[1].iloc[4, 1], Files[1].iloc[5, 1], Files[1].iloc[6, 1],
        Files[1].iloc[7, 1], Files[1].iloc[8, 1], Files[1].iloc[9, 1],
        Files[1].iloc[10, 1], Files[1].iloc[11, 1], Files[1].iloc[12, 1],
        Files[1].iloc[13, 1], Files[1].iloc[14, 1], Files[1].iloc[15, 1],
        Files[1].iloc[16, 1], Files[1].iloc[17, 1], Files[1].iloc[18, 1],
        Files[1].iloc[19, 1], Files[1].iloc[20, 1], Files[1].iloc[21, 1],
        Files[1].iloc[22, 1], Files[1].iloc[23, 1], Files[1].iloc[24, 1],
        Files[1].iloc[25, 1], Files[1].iloc[26, 1], Files[1].iloc[27, 1],
        Files[1].iloc[28, 1], Files[1].iloc[29, 1], Files[1].iloc[30, 1],
        Files[1].iloc[31, 1], Files[1].iloc[32, 1], Files[1].iloc[33, 1],
        Files[1].iloc[34, 1], Files[1].iloc[35, 1], Files[1].iloc[36, 1],
        Files[1].iloc[37, 1], Files[1].iloc[38, 1], Files[1].iloc[39, 1],
        Files[1].iloc[40, 1], Files[1].iloc[41, 1], Files[1].iloc[42, 1]],

    'March14': [
        Files[2].iloc[1, 1], Files[2].iloc[2, 1], Files[2].iloc[3, 1],
        Files[2].iloc[4, 1], Files[2].iloc[5, 1], Files[2].iloc[6, 1],
        Files[2].iloc[7, 1], Files[2].iloc[8, 1], Files[2].iloc[9, 1],
        Files[2].iloc[10, 1], Files[2].iloc[11, 1], Files[2].iloc[12, 1],
        Files[2].iloc[13, 1], Files[2].iloc[14, 1], Files[2].iloc[15, 1],
        Files[2].iloc[16, 1], Files[2].iloc[17, 1], Files[2].iloc[18, 1],
        Files[2].iloc[19, 1], Files[2].iloc[20, 1], Files[2].iloc[21, 1],
        Files[2].iloc[22, 1], Files[2].iloc[23, 1], Files[2].iloc[24, 1],
        Files[2].iloc[25, 1], Files[2].iloc[26, 1], Files[2].iloc[27, 1],
        Files[2].iloc[28, 1], Files[2].iloc[29, 1], Files[2].iloc[30, 1],
        Files[2].iloc[31, 1], Files[2].iloc[32, 1], Files[2].iloc[33, 1],
        Files[2].iloc[34, 1], Files[2].iloc[35, 1], Files[2].iloc[36, 1],
        Files[2].iloc[37, 1], Files[2].iloc[38, 1], Files[2].iloc[39, 1],
        Files[2].iloc[40, 1], Files[2].iloc[41, 1], Files[2].iloc[42, 1]],

    'April14': [
        Files[3].iloc[1, 1], Files[3].iloc[2, 1], Files[3].iloc[3, 1],
        Files[3].iloc[4, 1], Files[3].iloc[5, 1], Files[3].iloc[6, 1],
        Files[3].iloc[7, 1], Files[3].iloc[8, 1], Files[3].iloc[9, 1],
        Files[3].iloc[10, 1], Files[3].iloc[11, 1], Files[3].iloc[12, 1],
        Files[3].iloc[13, 1], Files[3].iloc[14, 1], Files[3].iloc[15, 1],
        Files[3].iloc[16, 1], Files[3].iloc[17, 1], Files[3].iloc[18, 1],
        Files[3].iloc[19, 1], Files[3].iloc[20, 1], Files[3].iloc[21, 1],
        Files[3].iloc[22, 1], Files[3].iloc[23, 1], Files[3].iloc[24, 1],
        Files[3].iloc[25, 1], Files[3].iloc[26, 1], Files[3].iloc[27, 1],
        Files[3].iloc[28, 1], Files[3].iloc[29, 1], Files[3].iloc[30, 1],
        Files[3].iloc[31, 1], Files[3].iloc[32, 1], Files[3].iloc[33, 1],
        Files[3].iloc[34, 1], Files[3].iloc[35, 1], Files[3].iloc[36, 1],
        Files[3].iloc[37, 1], Files[3].iloc[38, 1], Files[3].iloc[39, 1],
        Files[3].iloc[40, 1], Files[3].iloc[41, 1], Files[3].iloc[42, 1]],

    'May14': [
        Files[4].iloc[1, 1], Files[4].iloc[2, 1], Files[4].iloc[3, 1],
        Files[4].iloc[4, 1], Files[4].iloc[5, 1], Files[4].iloc[6, 1],
        Files[4].iloc[7, 1], Files[4].iloc[8, 1], Files[4].iloc[9, 1],
        Files[4].iloc[10, 1], Files[4].iloc[11, 1], Files[4].iloc[12, 1],
        Files[4].iloc[13, 1], Files[4].iloc[14, 1], Files[4].iloc[15, 1],
        Files[4].iloc[16, 1], Files[4].iloc[17, 1], Files[4].iloc[18, 1],
        Files[4].iloc[19, 1], Files[4].iloc[20, 1], Files[4].iloc[21, 1],
        Files[4].iloc[22, 1], Files[4].iloc[23, 1], Files[4].iloc[24, 1],
        Files[4].iloc[25, 1], Files[4].iloc[26, 1], Files[4].iloc[27, 1],
        Files[4].iloc[28, 1], Files[4].iloc[29, 1], Files[4].iloc[30, 1],
        Files[4].iloc[31, 1], Files[4].iloc[32, 1], Files[4].iloc[33, 1],
        Files[4].iloc[34, 1], Files[4].iloc[35, 1], Files[4].iloc[36, 1],
        Files[4].iloc[37, 1], Files[4].iloc[38, 1], Files[4].iloc[39, 1],
        Files[4].iloc[40, 1], Files[4].iloc[41, 1], Files[4].iloc[42, 1]],

    'June14': [
        Files[5].iloc[1, 1], Files[5].iloc[2, 1], Files[5].iloc[3, 1],
        Files[5].iloc[4, 1], Files[5].iloc[5, 1], Files[5].iloc[6, 1],
        Files[5].iloc[7, 1], Files[5].iloc[8, 1], Files[5].iloc[9, 1],
        Files[5].iloc[10, 1], Files[5].iloc[11, 1], Files[5].iloc[12, 1],
        Files[5].iloc[13, 1], Files[5].iloc[14, 1], Files[5].iloc[15, 1],
        Files[5].iloc[16, 1], Files[5].iloc[17, 1], Files[5].iloc[18, 1],
        Files[5].iloc[19, 1], Files[5].iloc[20, 1], Files[5].iloc[21, 1],
        Files[5].iloc[22, 1], Files[5].iloc[23, 1], Files[5].iloc[24, 1],
        Files[5].iloc[25, 1], Files[5].iloc[26, 1], Files[5].iloc[27, 1],
        Files[5].iloc[28, 1], Files[5].iloc[29, 1], Files[5].iloc[30, 1],
        Files[5].iloc[31, 1], Files[5].iloc[32, 1], Files[5].iloc[33, 1],
        Files[5].iloc[34, 1], Files[5].iloc[35, 1], Files[5].iloc[36, 1],
        Files[5].iloc[37, 1], Files[5].iloc[38, 1], Files[5].iloc[39, 1],
        Files[5].iloc[40, 1], Files[5].iloc[41, 1], Files[5].iloc[42, 1]],

    'July14': [
        Files[6].iloc[1, 1], Files[6].iloc[2, 1], Files[6].iloc[3, 1],
        Files[6].iloc[4, 1], Files[6].iloc[5, 1], Files[6].iloc[6, 1],
        Files[6].iloc[7, 1], Files[6].iloc[8, 1], Files[6].iloc[9, 1],
        Files[6].iloc[10, 1], Files[6].iloc[11, 1], Files[6].iloc[12, 1],
        Files[6].iloc[13, 1], Files[6].iloc[14, 1], Files[6].iloc[15, 1],
        Files[6].iloc[16, 1], Files[6].iloc[17, 1], Files[6].iloc[18, 1],
        Files[6].iloc[19, 1], Files[6].iloc[20, 1], Files[6].iloc[21, 1],
        Files[6].iloc[22, 1], Files[6].iloc[23, 1], Files[6].iloc[24, 1],
        Files[6].iloc[25, 1], Files[6].iloc[26, 1], Files[6].iloc[27, 1],
        Files[6].iloc[28, 1], Files[6].iloc[29, 1], Files[6].iloc[30, 1],
        Files[6].iloc[31, 1], Files[6].iloc[32, 1], Files[6].iloc[33, 1],
        Files[6].iloc[34, 1], Files[6].iloc[35, 1], Files[6].iloc[36, 1],
        Files[6].iloc[37, 1], Files[6].iloc[38, 1], Files[6].iloc[39, 1],
        Files[6].iloc[40, 1], Files[6].iloc[41, 1], Files[6].iloc[42, 1]],

    'Aug14': [
        Files[7].iloc[1, 1], Files[7].iloc[2, 1], Files[7].iloc[3, 1],
        Files[7].iloc[4, 1], Files[7].iloc[5, 1], Files[7].iloc[6, 1],
        Files[7].iloc[7, 1], Files[7].iloc[8, 1], Files[7].iloc[9, 1],
        Files[7].iloc[10, 1], Files[7].iloc[11, 1], Files[7].iloc[12, 1],
        Files[7].iloc[13, 1], Files[7].iloc[14, 1], Files[7].iloc[15, 1],
        Files[7].iloc[16, 1], Files[7].iloc[17, 1], Files[7].iloc[18, 1],
        Files[7].iloc[19, 1], Files[7].iloc[20, 1], Files[7].iloc[21, 1],
        Files[7].iloc[22, 1], Files[7].iloc[23, 1], Files[7].iloc[24, 1],
        Files[7].iloc[25, 1], Files[7].iloc[26, 1], Files[7].iloc[27, 1],
        Files[7].iloc[28, 1], Files[7].iloc[29, 1], Files[7].iloc[30, 1],
        Files[7].iloc[31, 1], Files[7].iloc[32, 1], Files[7].iloc[33, 1],
        Files[7].iloc[34, 1], Files[7].iloc[35, 1], Files[7].iloc[36, 1],
        Files[7].iloc[37, 1], Files[7].iloc[38, 1], Files[7].iloc[39, 1],
        Files[7].iloc[40, 1], Files[7].iloc[41, 1], Files[7].iloc[42, 1]],

    'Sept14': [
        Files[8].iloc[1, 1], Files[8].iloc[2, 1], Files[8].iloc[3, 1],
        Files[8].iloc[4, 1], Files[8].iloc[5, 1], Files[8].iloc[6, 1],
        Files[8].iloc[7, 1], Files[8].iloc[8, 1], Files[8].iloc[9, 1],
        Files[8].iloc[10, 1], Files[8].iloc[11, 1], Files[8].iloc[12, 1],
        Files[8].iloc[13, 1], Files[8].iloc[14, 1], Files[8].iloc[15, 1],
        Files[8].iloc[16, 1], Files[8].iloc[17, 1], Files[8].iloc[18, 1],
        Files[8].iloc[19, 1], Files[8].iloc[20, 1], Files[8].iloc[21, 1],
        Files[8].iloc[22, 1], Files[8].iloc[23, 1], Files[8].iloc[24, 1],
        Files[8].iloc[25, 1], Files[8].iloc[26, 1], Files[8].iloc[27, 1],
        Files[8].iloc[28, 1], Files[8].iloc[29, 1], Files[8].iloc[30, 1],
        Files[8].iloc[31, 1], Files[8].iloc[32, 1], Files[8].iloc[33, 1],
        Files[8].iloc[34, 1], Files[8].iloc[35, 1], Files[8].iloc[36, 1],
        Files[8].iloc[37, 1], Files[8].iloc[38, 1], Files[8].iloc[39, 1],
        Files[8].iloc[40, 1], Files[8].iloc[41, 1], Files[8].iloc[42, 1]],

    'Oct14': [
        Files[9].iloc[1, 1], Files[9].iloc[2, 1], Files[9].iloc[3, 1],
        Files[9].iloc[4, 1], Files[9].iloc[5, 1], Files[9].iloc[6, 1],
        Files[9].iloc[7, 1], Files[9].iloc[8, 1], Files[9].iloc[9, 1],
        Files[9].iloc[10, 1], Files[9].iloc[11, 1], Files[9].iloc[12, 1],
        Files[9].iloc[13, 1], Files[9].iloc[14, 1], Files[9].iloc[15, 1],
        Files[9].iloc[16, 1], Files[9].iloc[17, 1], Files[9].iloc[18, 1],
        Files[9].iloc[19, 1], Files[9].iloc[20, 1], Files[9].iloc[21, 1],
        Files[9].iloc[22, 1], Files[9].iloc[23, 1], Files[9].iloc[24, 1],
        Files[9].iloc[25, 1], Files[9].iloc[26, 1], Files[9].iloc[27, 1],
        Files[9].iloc[28, 1], Files[9].iloc[29, 1], Files[9].iloc[30, 1],
        Files[9].iloc[31, 1], Files[9].iloc[32, 1], Files[9].iloc[33, 1],
        Files[9].iloc[34, 1], Files[9].iloc[35, 1], Files[9].iloc[36, 1],
        Files[9].iloc[37, 1], Files[9].iloc[38, 1], Files[9].iloc[39, 1],
        Files[9].iloc[40, 1], Files[9].iloc[41, 1], Files[9].iloc[42, 1]],

    'Nov14': [
        Files[10].iloc[1, 1], Files[10].iloc[2, 1], Files[10].iloc[3, 1],
        Files[10].iloc[4, 1], Files[10].iloc[5, 1], Files[10].iloc[6, 1],
        Files[10].iloc[7, 1], Files[10].iloc[8, 1], Files[10].iloc[9, 1],
        Files[10].iloc[10, 1], Files[10].iloc[11, 1], Files[10].iloc[12, 1],
        Files[10].iloc[13, 1], Files[10].iloc[14, 1], Files[10].iloc[15, 1],
        Files[10].iloc[16, 1], Files[10].iloc[17, 1], Files[10].iloc[18, 1],
        Files[10].iloc[19, 1], Files[0].iloc[20, 1], Files[10].iloc[21, 1],
        Files[10].iloc[22, 1], Files[10].iloc[23, 1], Files[10].iloc[24, 1],
        Files[10].iloc[25, 1], Files[10].iloc[26, 1], Files[10].iloc[27, 1],
        Files[10].iloc[28, 1], Files[10].iloc[29, 1], Files[10].iloc[30, 1],
        Files[10].iloc[31, 1], Files[10].iloc[32, 1], Files[0].iloc[33, 1],
        Files[10].iloc[34, 1], Files[10].iloc[35, 1], Files[10].iloc[36, 1],
        Files[10].iloc[37, 1], Files[10].iloc[38, 1], Files[10].iloc[39, 1],
        Files[10].iloc[40, 1], Files[10].iloc[41, 1], Files[10].iloc[42, 1]],

    'Dec15': [
        Files[11].iloc[1, 1], Files[11].iloc[2, 1], Files[11].iloc[3, 1],
        Files[11].iloc[4, 1], Files[11].iloc[5, 1], Files[11].iloc[6, 1],
        Files[11].iloc[7, 1], Files[11].iloc[8, 1], Files[11].iloc[9, 1],
        Files[11].iloc[10, 1], Files[11].iloc[11, 1], Files[11].iloc[12, 1],
        Files[11].iloc[13, 1], Files[11].iloc[14, 1], Files[11].iloc[15, 1],
        Files[11].iloc[16, 1], Files[11].iloc[17, 1], Files[11].iloc[18, 1],
        Files[11].iloc[19, 1], Files[11].iloc[20, 1], Files[11].iloc[21, 1],
        Files[11].iloc[22, 1], Files[11].iloc[23, 1], Files[11].iloc[24, 1],
        Files[11].iloc[25, 1], Files[11].iloc[26, 1], Files[11].iloc[27, 1],
        Files[11].iloc[28, 1], Files[11].iloc[29, 1], Files[11].iloc[30, 1],
        Files[11].iloc[31, 1], Files[11].iloc[32, 1], Files[11].iloc[33, 1],
        Files[11].iloc[34, 1], Files[11].iloc[35, 1], Files[11].iloc[36, 1],
        Files[11].iloc[37, 1], Files[11].iloc[38, 1], Files[11].iloc[39, 1],
        Files[11].iloc[40, 1], Files[11].iloc[41, 1], Files[11].iloc[42, 1]],

    'Jan15': [
        Files[12].iloc[1, 1], Files[12].iloc[2, 1], Files[12].iloc[3, 1],
        Files[12].iloc[4, 1], Files[12].iloc[5, 1], Files[12].iloc[6, 1],
        Files[12].iloc[7, 1], Files[12].iloc[8, 1], Files[12].iloc[9, 1],
        Files[12].iloc[10, 1], Files[12].iloc[11, 1], Files[12].iloc[12, 1],
        Files[12].iloc[13, 1], Files[12].iloc[14, 1], Files[12].iloc[15, 1],
        Files[12].iloc[16, 1], Files[12].iloc[17, 1], Files[12].iloc[18, 1],
        Files[12].iloc[19, 1], Files[12].iloc[20, 1], Files[12].iloc[21, 1],
        Files[12].iloc[22, 1], Files[12].iloc[23, 1], Files[12].iloc[24, 1],
        Files[12].iloc[25, 1], Files[12].iloc[26, 1], Files[12].iloc[27, 1],
        Files[12].iloc[28, 1], Files[12].iloc[29, 1], Files[12].iloc[30, 1],
        Files[12].iloc[31, 1], Files[12].iloc[32, 1], Files[12].iloc[33, 1],
        Files[12].iloc[34, 1], Files[12].iloc[35, 1], Files[12].iloc[36, 1],
        Files[12].iloc[37, 1], Files[12].iloc[38, 1], Files[12].iloc[39, 1],
        Files[12].iloc[40, 1], Files[12].iloc[41, 1], Files[12].iloc[42, 1]],

    'Feb15': [
        Files[13].iloc[1, 1], Files[13].iloc[2, 1], Files[13].iloc[3, 1],
        Files[13].iloc[4, 1], Files[13].iloc[5, 1], Files[13].iloc[6, 1],
        Files[13].iloc[7, 1], Files[13].iloc[8, 1], Files[13].iloc[9, 1],
        Files[13].iloc[10, 1], Files[13].iloc[11, 1], Files[13].iloc[12, 1],
        Files[13].iloc[13, 1], Files[13].iloc[14, 1], Files[13].iloc[15, 1],
        Files[13].iloc[16, 1], Files[13].iloc[17, 1], Files[13].iloc[18, 1],
        Files[13].iloc[19, 1], Files[13].iloc[20, 1], Files[13].iloc[21, 1],
        Files[13].iloc[22, 1], Files[13].iloc[23, 1], Files[13].iloc[24, 1],
        Files[13].iloc[25, 1], Files[13].iloc[26, 1], Files[13].iloc[27, 1],
        Files[13].iloc[28, 1], Files[13].iloc[29, 1], Files[13].iloc[30, 1],
        Files[13].iloc[31, 1], Files[13].iloc[32, 1], Files[13].iloc[33, 1],
        Files[13].iloc[34, 1], Files[13].iloc[35, 1], Files[13].iloc[36, 1],
        Files[13].iloc[37, 1], Files[13].iloc[38, 1], Files[13].iloc[39, 1],
        Files[13].iloc[40, 1], Files[13].iloc[41, 1], Files[13].iloc[42, 1]],

    'March15': [
        Files[14].iloc[1, 1], Files[14].iloc[2, 1], Files[14].iloc[3, 1],
        Files[14].iloc[4, 1], Files[14].iloc[5, 1], Files[14].iloc[6, 1],
        Files[14].iloc[7, 1], Files[14].iloc[8, 1], Files[14].iloc[9, 1],
        Files[14].iloc[10, 1], Files[14].iloc[11, 1], Files[14].iloc[12, 1],
        Files[14].iloc[13, 1], Files[14].iloc[14, 1], Files[14].iloc[15, 1],
        Files[14].iloc[16, 1], Files[14].iloc[17, 1], Files[14].iloc[18, 1],
        Files[14].iloc[19, 1], Files[14].iloc[20, 1], Files[14].iloc[21, 1],
        Files[14].iloc[22, 1], Files[14].iloc[23, 1], Files[14].iloc[24, 1],
        Files[14].iloc[25, 1], Files[14].iloc[26, 1], Files[14].iloc[27, 1],
        Files[14].iloc[28, 1], Files[14].iloc[29, 1], Files[14].iloc[30, 1],
        Files[14].iloc[31, 1], Files[14].iloc[32, 1], Files[14].iloc[33, 1],
        Files[14].iloc[34, 1], Files[14].iloc[35, 1], Files[14].iloc[36, 1],
        Files[14].iloc[37, 1], Files[14].iloc[38, 1], Files[14].iloc[39, 1],
        Files[14].iloc[40, 1], Files[14].iloc[41, 1], Files[14].iloc[42, 1]],

    'April15': [
        Files[15].iloc[1, 1], Files[15].iloc[2, 1], Files[15].iloc[3, 1],
        Files[15].iloc[4, 1], Files[15].iloc[5, 1], Files[15].iloc[6, 1],
        Files[15].iloc[7, 1], Files[15].iloc[8, 1], Files[15].iloc[9, 1],
        Files[15].iloc[10, 1], Files[15].iloc[11, 1], Files[15].iloc[12, 1],
        Files[15].iloc[13, 1], Files[15].iloc[14, 1], Files[15].iloc[15, 1],
        Files[15].iloc[16, 1], Files[15].iloc[17, 1], Files[15].iloc[18, 1],
        Files[15].iloc[19, 1], Files[15].iloc[20, 1], Files[15].iloc[21, 1],
        Files[15].iloc[22, 1], Files[15].iloc[23, 1], Files[15].iloc[24, 1],
        Files[15].iloc[25, 1], Files[15].iloc[26, 1], Files[15].iloc[27, 1],
        Files[15].iloc[28, 1], Files[15].iloc[29, 1], Files[15].iloc[30, 1],
        Files[15].iloc[31, 1], Files[15].iloc[32, 1], Files[15].iloc[33, 1],
        Files[15].iloc[34, 1], Files[15].iloc[35, 1], Files[15].iloc[36, 1],
        Files[15].iloc[37, 1], Files[15].iloc[38, 1], Files[15].iloc[39, 1],
        Files[15].iloc[40, 1], Files[15].iloc[41, 1], Files[15].iloc[42, 1]],

    'May15': [
        Files[16].iloc[1, 1], Files[16].iloc[2, 1], Files[16].iloc[3, 1],
        Files[16].iloc[4, 1], Files[16].iloc[5, 1], Files[16].iloc[6, 1],
        Files[16].iloc[7, 1], Files[16].iloc[8, 1], Files[16].iloc[9, 1],
        Files[16].iloc[10, 1], Files[16].iloc[11, 1], Files[16].iloc[12, 1],
        Files[16].iloc[13, 1], Files[16].iloc[14, 1], Files[16].iloc[15, 1],
        Files[16].iloc[16, 1], Files[16].iloc[17, 1], Files[16].iloc[18, 1],
        Files[16].iloc[19, 1], Files[16].iloc[20, 1], Files[16].iloc[21, 1],
        Files[16].iloc[22, 1], Files[16].iloc[23, 1], Files[16].iloc[24, 1],
        Files[16].iloc[25, 1], Files[16].iloc[26, 1], Files[16].iloc[27, 1],
        Files[16].iloc[28, 1], Files[16].iloc[29, 1], Files[16].iloc[30, 1],
        Files[16].iloc[31, 1], Files[16].iloc[32, 1], Files[16].iloc[33, 1],
        Files[16].iloc[34, 1], Files[16].iloc[35, 1], Files[16].iloc[36, 1],
        Files[16].iloc[37, 1], Files[16].iloc[38, 1], Files[16].iloc[39, 1],
        Files[16].iloc[40, 1], Files[16].iloc[41, 1], Files[16].iloc[42, 1]],

    'June15': [
        Files[17].iloc[1, 1], Files[17].iloc[2, 1], Files[17].iloc[3, 1],
        Files[17].iloc[4, 1], Files[17].iloc[5, 1], Files[17].iloc[6, 1],
        Files[17].iloc[7, 1], Files[17].iloc[8, 1], Files[17].iloc[9, 1],
        Files[17].iloc[10, 1], Files[17].iloc[11, 1], Files[17].iloc[12, 1],
        Files[17].iloc[13, 1], Files[17].iloc[14, 1], Files[17].iloc[15, 1],
        Files[17].iloc[16, 1], Files[17].iloc[17, 1], Files[17].iloc[18, 1],
        Files[17].iloc[19, 1], Files[17].iloc[20, 1], Files[17].iloc[21, 1],
        Files[17].iloc[22, 1], Files[17].iloc[23, 1], Files[17].iloc[24, 1],
        Files[17].iloc[25, 1], Files[17].iloc[26, 1], Files[17].iloc[27, 1],
        Files[17].iloc[28, 1], Files[17].iloc[29, 1], Files[17].iloc[30, 1],
        Files[17].iloc[31, 1], Files[17].iloc[32, 1], Files[17].iloc[33, 1],
        Files[17].iloc[34, 1], Files[17].iloc[35, 1], Files[17].iloc[36, 1],
        Files[17].iloc[37, 1], Files[17].iloc[38, 1], Files[17].iloc[39, 1],
        Files[17].iloc[40, 1], Files[17].iloc[41, 1], Files[17].iloc[42, 1]],

    'July15': [
        Files[18].iloc[1, 1], Files[18].iloc[2, 1], Files[18].iloc[3, 1],
        Files[18].iloc[4, 1], Files[18].iloc[5, 1], Files[18].iloc[6, 1],
        Files[18].iloc[7, 1], Files[18].iloc[8, 1], Files[18].iloc[9, 1],
        Files[18].iloc[10, 1], Files[18].iloc[11, 1], Files[18].iloc[12, 1],
        Files[18].iloc[13, 1], Files[18].iloc[14, 1], Files[18].iloc[15, 1],
        Files[18].iloc[16, 1], Files[18].iloc[17, 1], Files[18].iloc[18, 1],
        Files[18].iloc[19, 1], Files[18].iloc[20, 1], Files[18].iloc[21, 1],
        Files[18].iloc[22, 1], Files[18].iloc[23, 1], Files[18].iloc[24, 1],
        Files[18].iloc[25, 1], Files[18].iloc[26, 1], Files[18].iloc[27, 1],
        Files[18].iloc[28, 1], Files[18].iloc[29, 1], Files[18].iloc[30, 1],
        Files[18].iloc[31, 1], Files[18].iloc[32, 1], Files[18].iloc[33, 1],
        Files[18].iloc[34, 1], Files[18].iloc[35, 1], Files[18].iloc[36, 1],
        Files[18].iloc[37, 1], Files[18].iloc[38, 1], Files[18].iloc[39, 1],
        Files[18].iloc[40, 1], Files[18].iloc[41, 1], Files[18].iloc[42, 1]],
}

# Create DataFrame
df = pd.DataFrame(data)
list_d = []

def calculateSumCrimes(file, x):
    return np.sum(
        [
            file.iloc[x, 1], file.iloc[x, 5],
            file.iloc[x, 9], file.iloc[x, 13],
            file.iloc[x, 17], file.iloc[x, 21],
            file.iloc[x, 25], file.iloc[x, 29],
            file.iloc[x, 33], file.iloc[x, 37],
            file.iloc[x, 41], file.iloc[x, 45]
        ])


# ----------------------------------------------------------------------------------------------------------------------
# calculates the number of national crimes
def calNatsum(file):
    return np.sum(
        [
            file.iloc[0, 1], file.iloc[0, 5],
            file.iloc[0, 9], file.iloc[0, 13],
            file.iloc[0, 17], file.iloc[0, 21],
            file.iloc[0, 25], file.iloc[0, 29],
            file.iloc[0, 33], file.iloc[0, 37],
            file.iloc[0, 41], file.iloc[0, 45]
        ])


for date in tFNames:
    list_d.append(datetime.strptime(date, '%m/%y'))

sumCrimes = [calNatsum(Files[0]), calNatsum(Files[1]),
             calNatsum(Files[2]), calNatsum(Files[3]),
             calNatsum(Files[4]), calNatsum(Files[5]),
             calNatsum(Files[6]), calNatsum(Files[7]),
             calNatsum(Files[8]), calNatsum(Files[9]),
             calNatsum(Files[10]), calNatsum(Files[11]),
             calNatsum(Files[12]), calNatsum(Files[13]),
             calNatsum(Files[14]), calNatsum(Files[15]),
             calNatsum(Files[16]), calNatsum(Files[17]),
             calNatsum(Files[18])]


# ----------------------------------------------------------------------------------------------------------------------
# Clustering
def clust(file, x, y):
    kmeans = KMeans(
        n_clusters=6,
        init='random',
        max_iter=1000,
        random_state=5).fit(
        file.iloc[1:, [25, 27]]
    )

    centroids_df = pd.DataFrame(
        kmeans.cluster_centers_,
        columns=list(
            file.iloc[1:, [25, 27]].columns.values
        )
    )

    fig, ax = plt.subplots(1, 1)

    file.iloc[1:, [25, 27]].plot.scatter(
        x=x,
        y=y,
        c=kmeans.labels_, colormap='jet',
        ax=ax,
        mark_right=False
    )

    centroids_df.plot.scatter(
        x=x,
        y=y,
        ax=ax,
        s=80,
        mark_right=False
    )
    plt.title('Number of Fraud And Forgery Convictions\n vs Number of Fraud And Forgery Unsuccessful' + tFNames[i])
    plt.show()


i = 0
x = 'Number of Fraud And Forgery Convictions'
y = 'Number of Fraud And Forgery Unsuccessful'

while i < 19:
    for File in Files:
        # clust(
        #     # removing london for a better view of the clustering model
        #     Files[i].drop(Files[0].index[24]),
        #     x,
        #     y
        # )
        i = i + 1


# ----------------------------------------------------------------------------------------------------------------------

def clust2(file, x, y):
    kmeans = KMeans(
        n_clusters=3,
        init='random',
        max_iter=1000,
        random_state=5).fit(
        file.iloc[1:, [13, 15]]
    )

    centroids_df = pd.DataFrame(
        kmeans.cluster_centers_,
        columns=list(
            file.iloc[1:, [13, 15]].columns.values
        )
    )

    fig, ax = plt.subplots(1, 1)

    file.iloc[1:, [13, 15]].plot.scatter(
        x=x,
        y=y,
        c=kmeans.labels_, colormap='jet',
        ax=ax,
        mark_right=False
    )

    centroids_df.plot.scatter(
        x=x,
        y=y,
        ax=ax,
        s=80,
        mark_right=False
    )
    plt.title('Number of Burglary Convictions\n vs Number of Burglary Unsuccessful ' + tFNames[i])
    plt.show()


i = 0
x = 'Number of Burglary Convictions'
y = 'Number of Burglary Unsuccessful'

while i < 19:
    for File in Files:
        # clust2(
        #     # removing london for a better view of the clustering model
        #     Files[i].drop(Files[0].index[24]),
        #     x,
        #     y
        # )
        i = i + 1

# ----------------------------------------------------------------------------------------------------------------------
# Clustering in report

def calculateSumCrimes(file, x):
    return np.sum(
        [
            file.iloc[x, 1], file.iloc[x, 5],
            file.iloc[x, 9], file.iloc[x, 13],
            file.iloc[x, 17], file.iloc[x, 21],
            file.iloc[x, 25], file.iloc[x, 29],
            file.iloc[x, 33], file.iloc[x, 37],
            file.iloc[x, 41], file.iloc[x, 45]
        ])

clust_data = pd.DataFrame({
    'population': [
        965.42, 669.32, 852.52,
        1059.27, 0, 498.89,
        1053.32, 1762.38, 772.27,
        924, 0, 1832.75,
        916.2, 2812.57, 0,
        1844.25, 1184.37, 0,
        1846.48, 1498.3, 0,
        1087.66, 1423.07, 8908.08,
        903.68, 747.62, 320.27,
        0, 1101.66, 0,
        1154.2, 1402.92, 1131.05,
        758.56, 1189.93, 1703.84,
        0, 571.01, 0,
        2916.46, 2320.21, 720.06
    ],

    'Jan14': [
        Files[0].iloc[1, 1], Files[0].iloc[2, 1], Files[0].iloc[3, 1],
        Files[0].iloc[4, 1], Files[0].iloc[5, 1], Files[0].iloc[6, 1],
        Files[0].iloc[7, 1], Files[0].iloc[8, 1], Files[0].iloc[9, 1],
        Files[0].iloc[10, 1], Files[0].iloc[11, 1], Files[0].iloc[12, 1],
        Files[0].iloc[13, 1], Files[0].iloc[14, 1], Files[0].iloc[15, 1],
        Files[0].iloc[16, 1], Files[0].iloc[17, 1], Files[0].iloc[18, 1],
        Files[0].iloc[19, 1], Files[0].iloc[20, 1], Files[0].iloc[21, 1],
        Files[0].iloc[22, 1], Files[0].iloc[23, 1], Files[0].iloc[24, 1],
        Files[0].iloc[25, 1], Files[0].iloc[26, 1], Files[0].iloc[27, 1],
        Files[0].iloc[28, 1], Files[0].iloc[29, 1], Files[0].iloc[30, 1],
        Files[0].iloc[31, 1], Files[0].iloc[32, 1], Files[0].iloc[33, 1],
        Files[0].iloc[34, 1], Files[0].iloc[35, 1], Files[0].iloc[36, 1],
        Files[0].iloc[37, 1], Files[0].iloc[38, 1], Files[0].iloc[39, 1],
        Files[0].iloc[40, 1], Files[0].iloc[41, 1], Files[0].iloc[42, 1]],

    'Feb14': [
        Files[1].iloc[1, 1], Files[1].iloc[2, 1], Files[1].iloc[3, 1],
        Files[1].iloc[4, 1], Files[1].iloc[5, 1], Files[1].iloc[6, 1],
        Files[1].iloc[7, 1], Files[1].iloc[8, 1], Files[1].iloc[9, 1],
        Files[1].iloc[10, 1], Files[1].iloc[11, 1], Files[1].iloc[12, 1],
        Files[1].iloc[13, 1], Files[1].iloc[14, 1], Files[1].iloc[15, 1],
        Files[1].iloc[16, 1], Files[1].iloc[17, 1], Files[1].iloc[18, 1],
        Files[1].iloc[19, 1], Files[1].iloc[20, 1], Files[1].iloc[21, 1],
        Files[1].iloc[22, 1], Files[1].iloc[23, 1], Files[1].iloc[24, 1],
        Files[1].iloc[25, 1], Files[1].iloc[26, 1], Files[1].iloc[27, 1],
        Files[1].iloc[28, 1], Files[1].iloc[29, 1], Files[1].iloc[30, 1],
        Files[1].iloc[31, 1], Files[1].iloc[32, 1], Files[1].iloc[33, 1],
        Files[1].iloc[34, 1], Files[1].iloc[35, 1], Files[1].iloc[36, 1],
        Files[1].iloc[37, 1], Files[1].iloc[38, 1], Files[1].iloc[39, 1],
        Files[1].iloc[40, 1], Files[1].iloc[41, 1], Files[1].iloc[42, 1]],

    'March14': [
        Files[2].iloc[1, 1], Files[2].iloc[2, 1], Files[2].iloc[3, 1],
        Files[2].iloc[4, 1], Files[2].iloc[5, 1], Files[2].iloc[6, 1],
        Files[2].iloc[7, 1], Files[2].iloc[8, 1], Files[2].iloc[9, 1],
        Files[2].iloc[10, 1], Files[2].iloc[11, 1], Files[2].iloc[12, 1],
        Files[2].iloc[13, 1], Files[2].iloc[14, 1], Files[2].iloc[15, 1],
        Files[2].iloc[16, 1], Files[2].iloc[17, 1], Files[2].iloc[18, 1],
        Files[2].iloc[19, 1], Files[2].iloc[20, 1], Files[2].iloc[21, 1],
        Files[2].iloc[22, 1], Files[2].iloc[23, 1], Files[2].iloc[24, 1],
        Files[2].iloc[25, 1], Files[2].iloc[26, 1], Files[2].iloc[27, 1],
        Files[2].iloc[28, 1], Files[2].iloc[29, 1], Files[2].iloc[30, 1],
        Files[2].iloc[31, 1], Files[2].iloc[32, 1], Files[2].iloc[33, 1],
        Files[2].iloc[34, 1], Files[2].iloc[35, 1], Files[2].iloc[36, 1],
        Files[2].iloc[37, 1], Files[2].iloc[38, 1], Files[2].iloc[39, 1],
        Files[2].iloc[40, 1], Files[2].iloc[41, 1], Files[2].iloc[42, 1]],

    'April14': [
        Files[3].iloc[1, 1], Files[3].iloc[2, 1], Files[3].iloc[3, 1],
        Files[3].iloc[4, 1], Files[3].iloc[5, 1], Files[3].iloc[6, 1],
        Files[3].iloc[7, 1], Files[3].iloc[8, 1], Files[3].iloc[9, 1],
        Files[3].iloc[10, 1], Files[3].iloc[11, 1], Files[3].iloc[12, 1],
        Files[3].iloc[13, 1], Files[3].iloc[14, 1], Files[3].iloc[15, 1],
        Files[3].iloc[16, 1], Files[3].iloc[17, 1], Files[3].iloc[18, 1],
        Files[3].iloc[19, 1], Files[3].iloc[20, 1], Files[3].iloc[21, 1],
        Files[3].iloc[22, 1], Files[3].iloc[23, 1], Files[3].iloc[24, 1],
        Files[3].iloc[25, 1], Files[3].iloc[26, 1], Files[3].iloc[27, 1],
        Files[3].iloc[28, 1], Files[3].iloc[29, 1], Files[3].iloc[30, 1],
        Files[3].iloc[31, 1], Files[3].iloc[32, 1], Files[3].iloc[33, 1],
        Files[3].iloc[34, 1], Files[3].iloc[35, 1], Files[3].iloc[36, 1],
        Files[3].iloc[37, 1], Files[3].iloc[38, 1], Files[3].iloc[39, 1],
        Files[3].iloc[40, 1], Files[3].iloc[41, 1], Files[3].iloc[42, 1]],

    'May14': [
        Files[4].iloc[1, 1], Files[4].iloc[2, 1], Files[4].iloc[3, 1],
        Files[4].iloc[4, 1], Files[4].iloc[5, 1], Files[4].iloc[6, 1],
        Files[4].iloc[7, 1], Files[4].iloc[8, 1], Files[4].iloc[9, 1],
        Files[4].iloc[10, 1], Files[4].iloc[11, 1], Files[4].iloc[12, 1],
        Files[4].iloc[13, 1], Files[4].iloc[14, 1], Files[4].iloc[15, 1],
        Files[4].iloc[16, 1], Files[4].iloc[17, 1], Files[4].iloc[18, 1],
        Files[4].iloc[19, 1], Files[4].iloc[20, 1], Files[4].iloc[21, 1],
        Files[4].iloc[22, 1], Files[4].iloc[23, 1], Files[4].iloc[24, 1],
        Files[4].iloc[25, 1], Files[4].iloc[26, 1], Files[4].iloc[27, 1],
        Files[4].iloc[28, 1], Files[4].iloc[29, 1], Files[4].iloc[30, 1],
        Files[4].iloc[31, 1], Files[4].iloc[32, 1], Files[4].iloc[33, 1],
        Files[4].iloc[34, 1], Files[4].iloc[35, 1], Files[4].iloc[36, 1],
        Files[4].iloc[37, 1], Files[4].iloc[38, 1], Files[4].iloc[39, 1],
        Files[4].iloc[40, 1], Files[4].iloc[41, 1], Files[4].iloc[42, 1]],

    'June14': [
        Files[5].iloc[1, 1], Files[5].iloc[2, 1], Files[5].iloc[3, 1],
        Files[5].iloc[4, 1], Files[5].iloc[5, 1], Files[5].iloc[6, 1],
        Files[5].iloc[7, 1], Files[5].iloc[8, 1], Files[5].iloc[9, 1],
        Files[5].iloc[10, 1], Files[5].iloc[11, 1], Files[5].iloc[12, 1],
        Files[5].iloc[13, 1], Files[5].iloc[14, 1], Files[5].iloc[15, 1],
        Files[5].iloc[16, 1], Files[5].iloc[17, 1], Files[5].iloc[18, 1],
        Files[5].iloc[19, 1], Files[5].iloc[20, 1], Files[5].iloc[21, 1],
        Files[5].iloc[22, 1], Files[5].iloc[23, 1], Files[5].iloc[24, 1],
        Files[5].iloc[25, 1], Files[5].iloc[26, 1], Files[5].iloc[27, 1],
        Files[5].iloc[28, 1], Files[5].iloc[29, 1], Files[5].iloc[30, 1],
        Files[5].iloc[31, 1], Files[5].iloc[32, 1], Files[5].iloc[33, 1],
        Files[5].iloc[34, 1], Files[5].iloc[35, 1], Files[5].iloc[36, 1],
        Files[5].iloc[37, 1], Files[5].iloc[38, 1], Files[5].iloc[39, 1],
        Files[5].iloc[40, 1], Files[5].iloc[41, 1], Files[5].iloc[42, 1]],

    'July14': [
        Files[6].iloc[1, 1], Files[6].iloc[2, 1], Files[6].iloc[3, 1],
        Files[6].iloc[4, 1], Files[6].iloc[5, 1], Files[6].iloc[6, 1],
        Files[6].iloc[7, 1], Files[6].iloc[8, 1], Files[6].iloc[9, 1],
        Files[6].iloc[10, 1], Files[6].iloc[11, 1], Files[6].iloc[12, 1],
        Files[6].iloc[13, 1], Files[6].iloc[14, 1], Files[6].iloc[15, 1],
        Files[6].iloc[16, 1], Files[6].iloc[17, 1], Files[6].iloc[18, 1],
        Files[6].iloc[19, 1], Files[6].iloc[20, 1], Files[6].iloc[21, 1],
        Files[6].iloc[22, 1], Files[6].iloc[23, 1], Files[6].iloc[24, 1],
        Files[6].iloc[25, 1], Files[6].iloc[26, 1], Files[6].iloc[27, 1],
        Files[6].iloc[28, 1], Files[6].iloc[29, 1], Files[6].iloc[30, 1],
        Files[6].iloc[31, 1], Files[6].iloc[32, 1], Files[6].iloc[33, 1],
        Files[6].iloc[34, 1], Files[6].iloc[35, 1], Files[6].iloc[36, 1],
        Files[6].iloc[37, 1], Files[6].iloc[38, 1], Files[6].iloc[39, 1],
        Files[6].iloc[40, 1], Files[6].iloc[41, 1], Files[6].iloc[42, 1]],

    'Aug14': [
        Files[7].iloc[1, 1], Files[7].iloc[2, 1], Files[7].iloc[3, 1],
        Files[7].iloc[4, 1], Files[7].iloc[5, 1], Files[7].iloc[6, 1],
        Files[7].iloc[7, 1], Files[7].iloc[8, 1], Files[7].iloc[9, 1],
        Files[7].iloc[10, 1], Files[7].iloc[11, 1], Files[7].iloc[12, 1],
        Files[7].iloc[13, 1], Files[7].iloc[14, 1], Files[7].iloc[15, 1],
        Files[7].iloc[16, 1], Files[7].iloc[17, 1], Files[7].iloc[18, 1],
        Files[7].iloc[19, 1], Files[7].iloc[20, 1], Files[7].iloc[21, 1],
        Files[7].iloc[22, 1], Files[7].iloc[23, 1], Files[7].iloc[24, 1],
        Files[7].iloc[25, 1], Files[7].iloc[26, 1], Files[7].iloc[27, 1],
        Files[7].iloc[28, 1], Files[7].iloc[29, 1], Files[7].iloc[30, 1],
        Files[7].iloc[31, 1], Files[7].iloc[32, 1], Files[7].iloc[33, 1],
        Files[7].iloc[34, 1], Files[7].iloc[35, 1], Files[7].iloc[36, 1],
        Files[7].iloc[37, 1], Files[7].iloc[38, 1], Files[7].iloc[39, 1],
        Files[7].iloc[40, 1], Files[7].iloc[41, 1], Files[7].iloc[42, 1]],

    'Sept14': [
        Files[8].iloc[1, 1], Files[8].iloc[2, 1], Files[8].iloc[3, 1],
        Files[8].iloc[4, 1], Files[8].iloc[5, 1], Files[8].iloc[6, 1],
        Files[8].iloc[7, 1], Files[8].iloc[8, 1], Files[8].iloc[9, 1],
        Files[8].iloc[10, 1], Files[8].iloc[11, 1], Files[8].iloc[12, 1],
        Files[8].iloc[13, 1], Files[8].iloc[14, 1], Files[8].iloc[15, 1],
        Files[8].iloc[16, 1], Files[8].iloc[17, 1], Files[8].iloc[18, 1],
        Files[8].iloc[19, 1], Files[8].iloc[20, 1], Files[8].iloc[21, 1],
        Files[8].iloc[22, 1], Files[8].iloc[23, 1], Files[8].iloc[24, 1],
        Files[8].iloc[25, 1], Files[8].iloc[26, 1], Files[8].iloc[27, 1],
        Files[8].iloc[28, 1], Files[8].iloc[29, 1], Files[8].iloc[30, 1],
        Files[8].iloc[31, 1], Files[8].iloc[32, 1], Files[8].iloc[33, 1],
        Files[8].iloc[34, 1], Files[8].iloc[35, 1], Files[8].iloc[36, 1],
        Files[8].iloc[37, 1], Files[8].iloc[38, 1], Files[8].iloc[39, 1],
        Files[8].iloc[40, 1], Files[8].iloc[41, 1], Files[8].iloc[42, 1]],

    'Oct14': [
        Files[9].iloc[1, 1], Files[9].iloc[2, 1], Files[9].iloc[3, 1],
        Files[9].iloc[4, 1], Files[9].iloc[5, 1], Files[9].iloc[6, 1],
        Files[9].iloc[7, 1], Files[9].iloc[8, 1], Files[9].iloc[9, 1],
        Files[9].iloc[10, 1], Files[9].iloc[11, 1], Files[9].iloc[12, 1],
        Files[9].iloc[13, 1], Files[9].iloc[14, 1], Files[9].iloc[15, 1],
        Files[9].iloc[16, 1], Files[9].iloc[17, 1], Files[9].iloc[18, 1],
        Files[9].iloc[19, 1], Files[9].iloc[20, 1], Files[9].iloc[21, 1],
        Files[9].iloc[22, 1], Files[9].iloc[23, 1], Files[9].iloc[24, 1],
        Files[9].iloc[25, 1], Files[9].iloc[26, 1], Files[9].iloc[27, 1],
        Files[9].iloc[28, 1], Files[9].iloc[29, 1], Files[9].iloc[30, 1],
        Files[9].iloc[31, 1], Files[9].iloc[32, 1], Files[9].iloc[33, 1],
        Files[9].iloc[34, 1], Files[9].iloc[35, 1], Files[9].iloc[36, 1],
        Files[9].iloc[37, 1], Files[9].iloc[38, 1], Files[9].iloc[39, 1],
        Files[9].iloc[40, 1], Files[9].iloc[41, 1], Files[9].iloc[42, 1]],

    'Nov14': [
        Files[10].iloc[1, 1], Files[10].iloc[2, 1], Files[10].iloc[3, 1],
        Files[10].iloc[4, 1], Files[10].iloc[5, 1], Files[10].iloc[6, 1],
        Files[10].iloc[7, 1], Files[10].iloc[8, 1], Files[10].iloc[9, 1],
        Files[10].iloc[10, 1], Files[10].iloc[11, 1], Files[10].iloc[12, 1],
        Files[10].iloc[13, 1], Files[10].iloc[14, 1], Files[10].iloc[15, 1],
        Files[10].iloc[16, 1], Files[10].iloc[17, 1], Files[10].iloc[18, 1],
        Files[10].iloc[19, 1], Files[0].iloc[20, 1], Files[10].iloc[21, 1],
        Files[10].iloc[22, 1], Files[10].iloc[23, 1], Files[10].iloc[24, 1],
        Files[10].iloc[25, 1], Files[10].iloc[26, 1], Files[10].iloc[27, 1],
        Files[10].iloc[28, 1], Files[10].iloc[29, 1], Files[10].iloc[30, 1],
        Files[10].iloc[31, 1], Files[10].iloc[32, 1], Files[0].iloc[33, 1],
        Files[10].iloc[34, 1], Files[10].iloc[35, 1], Files[10].iloc[36, 1],
        Files[10].iloc[37, 1], Files[10].iloc[38, 1], Files[10].iloc[39, 1],
        Files[10].iloc[40, 1], Files[10].iloc[41, 1], Files[10].iloc[42, 1]],

    'Dec15': [
        Files[11].iloc[1, 1], Files[11].iloc[2, 1], Files[11].iloc[3, 1],
        Files[11].iloc[4, 1], Files[11].iloc[5, 1], Files[11].iloc[6, 1],
        Files[11].iloc[7, 1], Files[11].iloc[8, 1], Files[11].iloc[9, 1],
        Files[11].iloc[10, 1], Files[11].iloc[11, 1], Files[11].iloc[12, 1],
        Files[11].iloc[13, 1], Files[11].iloc[14, 1], Files[11].iloc[15, 1],
        Files[11].iloc[16, 1], Files[11].iloc[17, 1], Files[11].iloc[18, 1],
        Files[11].iloc[19, 1], Files[11].iloc[20, 1], Files[11].iloc[21, 1],
        Files[11].iloc[22, 1], Files[11].iloc[23, 1], Files[11].iloc[24, 1],
        Files[11].iloc[25, 1], Files[11].iloc[26, 1], Files[11].iloc[27, 1],
        Files[11].iloc[28, 1], Files[11].iloc[29, 1], Files[11].iloc[30, 1],
        Files[11].iloc[31, 1], Files[11].iloc[32, 1], Files[11].iloc[33, 1],
        Files[11].iloc[34, 1], Files[11].iloc[35, 1], Files[11].iloc[36, 1],
        Files[11].iloc[37, 1], Files[11].iloc[38, 1], Files[11].iloc[39, 1],
        Files[11].iloc[40, 1], Files[11].iloc[41, 1], Files[11].iloc[42, 1]],

    'Jan15': [
        Files[12].iloc[1, 1], Files[12].iloc[2, 1], Files[12].iloc[3, 1],
        Files[12].iloc[4, 1], Files[12].iloc[5, 1], Files[12].iloc[6, 1],
        Files[12].iloc[7, 1], Files[12].iloc[8, 1], Files[12].iloc[9, 1],
        Files[12].iloc[10, 1], Files[12].iloc[11, 1], Files[12].iloc[12, 1],
        Files[12].iloc[13, 1], Files[12].iloc[14, 1], Files[12].iloc[15, 1],
        Files[12].iloc[16, 1], Files[12].iloc[17, 1], Files[12].iloc[18, 1],
        Files[12].iloc[19, 1], Files[12].iloc[20, 1], Files[12].iloc[21, 1],
        Files[12].iloc[22, 1], Files[12].iloc[23, 1], Files[12].iloc[24, 1],
        Files[12].iloc[25, 1], Files[12].iloc[26, 1], Files[12].iloc[27, 1],
        Files[12].iloc[28, 1], Files[12].iloc[29, 1], Files[12].iloc[30, 1],
        Files[12].iloc[31, 1], Files[12].iloc[32, 1], Files[12].iloc[33, 1],
        Files[12].iloc[34, 1], Files[12].iloc[35, 1], Files[12].iloc[36, 1],
        Files[12].iloc[37, 1], Files[12].iloc[38, 1], Files[12].iloc[39, 1],
        Files[12].iloc[40, 1], Files[12].iloc[41, 1], Files[12].iloc[42, 1]],

    'Feb15': [
        Files[13].iloc[1, 1], Files[13].iloc[2, 1], Files[13].iloc[3, 1],
        Files[13].iloc[4, 1], Files[13].iloc[5, 1], Files[13].iloc[6, 1],
        Files[13].iloc[7, 1], Files[13].iloc[8, 1], Files[13].iloc[9, 1],
        Files[13].iloc[10, 1], Files[13].iloc[11, 1], Files[13].iloc[12, 1],
        Files[13].iloc[13, 1], Files[13].iloc[14, 1], Files[13].iloc[15, 1],
        Files[13].iloc[16, 1], Files[13].iloc[17, 1], Files[13].iloc[18, 1],
        Files[13].iloc[19, 1], Files[13].iloc[20, 1], Files[13].iloc[21, 1],
        Files[13].iloc[22, 1], Files[13].iloc[23, 1], Files[13].iloc[24, 1],
        Files[13].iloc[25, 1], Files[13].iloc[26, 1], Files[13].iloc[27, 1],
        Files[13].iloc[28, 1], Files[13].iloc[29, 1], Files[13].iloc[30, 1],
        Files[13].iloc[31, 1], Files[13].iloc[32, 1], Files[13].iloc[33, 1],
        Files[13].iloc[34, 1], Files[13].iloc[35, 1], Files[13].iloc[36, 1],
        Files[13].iloc[37, 1], Files[13].iloc[38, 1], Files[13].iloc[39, 1],
        Files[13].iloc[40, 1], Files[13].iloc[41, 1], Files[13].iloc[42, 1]],

    'March15': [
        Files[14].iloc[1, 1], Files[14].iloc[2, 1], Files[14].iloc[3, 1],
        Files[14].iloc[4, 1], Files[14].iloc[5, 1], Files[14].iloc[6, 1],
        Files[14].iloc[7, 1], Files[14].iloc[8, 1], Files[14].iloc[9, 1],
        Files[14].iloc[10, 1], Files[14].iloc[11, 1], Files[14].iloc[12, 1],
        Files[14].iloc[13, 1], Files[14].iloc[14, 1], Files[14].iloc[15, 1],
        Files[14].iloc[16, 1], Files[14].iloc[17, 1], Files[14].iloc[18, 1],
        Files[14].iloc[19, 1], Files[14].iloc[20, 1], Files[14].iloc[21, 1],
        Files[14].iloc[22, 1], Files[14].iloc[23, 1], Files[14].iloc[24, 1],
        Files[14].iloc[25, 1], Files[14].iloc[26, 1], Files[14].iloc[27, 1],
        Files[14].iloc[28, 1], Files[14].iloc[29, 1], Files[14].iloc[30, 1],
        Files[14].iloc[31, 1], Files[14].iloc[32, 1], Files[14].iloc[33, 1],
        Files[14].iloc[34, 1], Files[14].iloc[35, 1], Files[14].iloc[36, 1],
        Files[14].iloc[37, 1], Files[14].iloc[38, 1], Files[14].iloc[39, 1],
        Files[14].iloc[40, 1], Files[14].iloc[41, 1], Files[14].iloc[42, 1]],

    'April15': [
        Files[15].iloc[1, 1], Files[15].iloc[2, 1], Files[15].iloc[3, 1],
        Files[15].iloc[4, 1], Files[15].iloc[5, 1], Files[15].iloc[6, 1],
        Files[15].iloc[7, 1], Files[15].iloc[8, 1], Files[15].iloc[9, 1],
        Files[15].iloc[10, 1], Files[15].iloc[11, 1], Files[15].iloc[12, 1],
        Files[15].iloc[13, 1], Files[15].iloc[14, 1], Files[15].iloc[15, 1],
        Files[15].iloc[16, 1], Files[15].iloc[17, 1], Files[15].iloc[18, 1],
        Files[15].iloc[19, 1], Files[15].iloc[20, 1], Files[15].iloc[21, 1],
        Files[15].iloc[22, 1], Files[15].iloc[23, 1], Files[15].iloc[24, 1],
        Files[15].iloc[25, 1], Files[15].iloc[26, 1], Files[15].iloc[27, 1],
        Files[15].iloc[28, 1], Files[15].iloc[29, 1], Files[15].iloc[30, 1],
        Files[15].iloc[31, 1], Files[15].iloc[32, 1], Files[15].iloc[33, 1],
        Files[15].iloc[34, 1], Files[15].iloc[35, 1], Files[15].iloc[36, 1],
        Files[15].iloc[37, 1], Files[15].iloc[38, 1], Files[15].iloc[39, 1],
        Files[15].iloc[40, 1], Files[15].iloc[41, 1], Files[15].iloc[42, 1]],

    'May15': [
        Files[16].iloc[1, 1], Files[16].iloc[2, 1], Files[16].iloc[3, 1],
        Files[16].iloc[4, 1], Files[16].iloc[5, 1], Files[16].iloc[6, 1],
        Files[16].iloc[7, 1], Files[16].iloc[8, 1], Files[16].iloc[9, 1],
        Files[16].iloc[10, 1], Files[16].iloc[11, 1], Files[16].iloc[12, 1],
        Files[16].iloc[13, 1], Files[16].iloc[14, 1], Files[16].iloc[15, 1],
        Files[16].iloc[16, 1], Files[16].iloc[17, 1], Files[16].iloc[18, 1],
        Files[16].iloc[19, 1], Files[16].iloc[20, 1], Files[16].iloc[21, 1],
        Files[16].iloc[22, 1], Files[16].iloc[23, 1], Files[16].iloc[24, 1],
        Files[16].iloc[25, 1], Files[16].iloc[26, 1], Files[16].iloc[27, 1],
        Files[16].iloc[28, 1], Files[16].iloc[29, 1], Files[16].iloc[30, 1],
        Files[16].iloc[31, 1], Files[16].iloc[32, 1], Files[16].iloc[33, 1],
        Files[16].iloc[34, 1], Files[16].iloc[35, 1], Files[16].iloc[36, 1],
        Files[16].iloc[37, 1], Files[16].iloc[38, 1], Files[16].iloc[39, 1],
        Files[16].iloc[40, 1], Files[16].iloc[41, 1], Files[16].iloc[42, 1]],

    'June15': [
        Files[17].iloc[1, 1], Files[17].iloc[2, 1], Files[17].iloc[3, 1],
        Files[17].iloc[4, 1], Files[17].iloc[5, 1], Files[17].iloc[6, 1],
        Files[17].iloc[7, 1], Files[17].iloc[8, 1], Files[17].iloc[9, 1],
        Files[17].iloc[10, 1], Files[17].iloc[11, 1], Files[17].iloc[12, 1],
        Files[17].iloc[13, 1], Files[17].iloc[14, 1], Files[17].iloc[15, 1],
        Files[17].iloc[16, 1], Files[17].iloc[17, 1], Files[17].iloc[18, 1],
        Files[17].iloc[19, 1], Files[17].iloc[20, 1], Files[17].iloc[21, 1],
        Files[17].iloc[22, 1], Files[17].iloc[23, 1], Files[17].iloc[24, 1],
        Files[17].iloc[25, 1], Files[17].iloc[26, 1], Files[17].iloc[27, 1],
        Files[17].iloc[28, 1], Files[17].iloc[29, 1], Files[17].iloc[30, 1],
        Files[17].iloc[31, 1], Files[17].iloc[32, 1], Files[17].iloc[33, 1],
        Files[17].iloc[34, 1], Files[17].iloc[35, 1], Files[17].iloc[36, 1],
        Files[17].iloc[37, 1], Files[17].iloc[38, 1], Files[17].iloc[39, 1],
        Files[17].iloc[40, 1], Files[17].iloc[41, 1], Files[17].iloc[42, 1]],

    'July15': [
        Files[18].iloc[1, 1], Files[18].iloc[2, 1], Files[18].iloc[3, 1],
        Files[18].iloc[4, 1], Files[18].iloc[5, 1], Files[18].iloc[6, 1],
        Files[18].iloc[7, 1], Files[18].iloc[8, 1], Files[18].iloc[9, 1],
        Files[18].iloc[10, 1], Files[18].iloc[11, 1], Files[18].iloc[12, 1],
        Files[18].iloc[13, 1], Files[18].iloc[14, 1], Files[18].iloc[15, 1],
        Files[18].iloc[16, 1], Files[18].iloc[17, 1], Files[18].iloc[18, 1],
        Files[18].iloc[19, 1], Files[18].iloc[20, 1], Files[18].iloc[21, 1],
        Files[18].iloc[22, 1], Files[18].iloc[23, 1], Files[18].iloc[24, 1],
        Files[18].iloc[25, 1], Files[18].iloc[26, 1], Files[18].iloc[27, 1],
        Files[18].iloc[28, 1], Files[18].iloc[29, 1], Files[18].iloc[30, 1],
        Files[18].iloc[31, 1], Files[18].iloc[32, 1], Files[18].iloc[33, 1],
        Files[18].iloc[34, 1], Files[18].iloc[35, 1], Files[18].iloc[36, 1],
        Files[18].iloc[37, 1], Files[18].iloc[38, 1], Files[18].iloc[39, 1],
        Files[18].iloc[40, 1], Files[18].iloc[41, 1], Files[18].iloc[42, 1]],

})


def clust3(file):
    kmeans = KMeans(
        n_clusters=3,
        init='random',
        max_iter=1000,
        random_state=5).fit(
        file.iloc[1:, [0, 1]]
    )

    centroids_df = pd.DataFrame(
        kmeans.cluster_centers_,
        columns=list(
            file.iloc[1:, [0, 1]].columns.values
        )
    )

    fig, ax = plt.subplots(1, 1)

    file.iloc[1:, [0, 1]].plot.scatter(
        x='Jan14',
        y='population',
        c=kmeans.labels_, colormap='jet',
        ax=ax,
        mark_right=False
    )

    centroids_df.plot.scatter(
        x='Jan14',
        y='population',
        ax=ax,
        s=80,
        mark_right=False
    )
    plt.xlabel("Count")
    plt.title('Population\n vs Homicides')
    plt.show()

clust3(clust_data)

# ----------------------------------------------------------------------------------------------------------------------
# implementing linear regression
# population crime rate

# population - https://www.statista.com/statistics/971694/county-population-england/ population figures
population_arr = [
    965.42, 669.32,
    852.52, 1059.27,
    0, 498.89,
    1053.32, 1762.38,
    772.27, 924,
    0, 1832.75,
    916.2, 2812.57,
    0, 1844.25,
    1184.37, 0,
    1846.48, 1498.3,
    0, 1087.66,
    1423.07, 8908.08,
    903.68, 747.62,
    320.27, 0,
    1101.66, 0,
    1154.2, 1402.92,
    1131.05, 758.56,
    1189.93, 1703.84,
    0, 571.01,
    0, 2916.46,
    2320.21, 720.06
]

locations = [
    Files[0].iloc[1, 0], Files[0].iloc[2, 0], Files[0].iloc[3, 0],
    Files[0].iloc[4, 0], Files[0].iloc[5, 0], Files[0].iloc[6, 0],
    Files[0].iloc[7, 0], Files[0].iloc[8, 0], Files[0].iloc[9, 0],
    Files[0].iloc[10, 0], Files[0].iloc[11, 0], Files[0].iloc[12, 0],
    Files[0].iloc[13, 0], Files[0].iloc[14, 0], Files[0].iloc[15, 0],
    Files[0].iloc[16, 0], Files[0].iloc[17, 0], Files[0].iloc[18, 0],
    Files[0].iloc[19, 0], Files[0].iloc[20, 0], Files[0].iloc[21, 0],
    Files[0].iloc[22, 0], Files[0].iloc[23, 0], Files[0].iloc[24, 0],
    Files[0].iloc[25, 0], Files[0].iloc[26, 0], Files[0].iloc[27, 0],
    Files[0].iloc[28, 0], Files[0].iloc[29, 0], Files[0].iloc[30, 0],
    Files[0].iloc[31, 0], Files[0].iloc[32, 0], Files[0].iloc[33, 0],
    Files[0].iloc[34, 0], Files[0].iloc[35, 0], Files[0].iloc[36, 0],
    Files[0].iloc[37, 0], Files[0].iloc[38, 0], Files[0].iloc[39, 0],
    Files[0].iloc[40, 0], Files[0].iloc[41, 0], Files[0].iloc[42, 0]
]


def linearReg(fileNum):
    collection_crimes = []
    for i in range(1, 43):
        collection_crimes.append(calculateSumCrimes(Files[fileNum], i))

    df = pd.DataFrame({
        'Population': population_arr,
        'Crimes': collection_crimes
    })

    lrm = smf.ols(
        formula='Crimes ~ Population',
        data=df
    ).fit()

    print(lrm.params)
    print(df)

    df.plot(
        kind='scatter',
        x='Population',
        y='Crimes'
    )

    x = pd.DataFrame({
        'Population': [100]
    })

    prediction = lrm.predict(x)

    print("Prediction")
    print(prediction)

    print("P-values")
    print(lrm.pvalues)

    # working with line of best fit ---------
    xs = np.array(population_arr, dtype=np.float64)
    ys = np.array(collection_crimes, dtype=np.float64)

    # get the m and b for equation
    def bestft(xs, ys):
        m = (
                    (mean(xs) * mean(ys)) - mean(xs * ys)
            ) / (
                    (
                            mean(xs) * mean(xs)) - mean(xs * xs)
            )

        b = (mean(ys) - m * mean(xs))
        return m, b

    m, b = bestft(xs, ys)

    # do equation for best fit
    regression_l = [
        (m * x) + b for x in xs
    ]

    # plot
    plt.scatter(xs, ys)
    plt.plot(
        xs,
        regression_l,
        color="red"
    )
    plt.title(tFNames[fileNum])
    plt.show()


i = 0

while i < 19:
    for File in Files:
        # linearReg(i)
        i = i + 1

# ----------------------------------------------------------------------------------------------------------------------
# implementing linear regression
# population crime rate

# population - https://www.statista.com/statistics/971694/county-population-england/ population figures
population_arr = [
    965.42, 669.32,
    852.52, 1059.27,
    0, 498.89,
    1053.32, 1762.38,
    772.27, 924,
    0, 1832.75,
    916.2, 2812.57,
    0, 1844.25,
    1184.37, 0,
    1846.48, 1498.3,
    0, 1087.66,
    1423.07,
    903.68, 747.62,
    320.27, 0,
    1101.66, 0,
    1154.2, 1402.92,
    1131.05, 758.56,
    1189.93, 1703.84,
    0, 571.01,
    0, 2916.46,
    2320.21, 720.06
]

locations = [
    Files[0].iloc[1, 0], Files[0].iloc[2, 0], Files[0].iloc[3, 0],
    Files[0].iloc[4, 0], Files[0].iloc[5, 0], Files[0].iloc[6, 0],
    Files[0].iloc[7, 0], Files[0].iloc[8, 0], Files[0].iloc[9, 0],
    Files[0].iloc[10, 0], Files[0].iloc[11, 0], Files[0].iloc[12, 0],
    Files[0].iloc[13, 0], Files[0].iloc[14, 0], Files[0].iloc[15, 0],
    Files[0].iloc[16, 0], Files[0].iloc[17, 0], Files[0].iloc[18, 0],
    Files[0].iloc[19, 0], Files[0].iloc[20, 0], Files[0].iloc[21, 0],
    Files[0].iloc[22, 0], Files[0].iloc[23, 0],
    Files[0].iloc[25, 0], Files[0].iloc[26, 0], Files[0].iloc[27, 0],
    Files[0].iloc[28, 0], Files[0].iloc[29, 0], Files[0].iloc[30, 0],
    Files[0].iloc[31, 0], Files[0].iloc[32, 0], Files[0].iloc[33, 0],
    Files[0].iloc[34, 0], Files[0].iloc[35, 0], Files[0].iloc[36, 0],
    Files[0].iloc[37, 0], Files[0].iloc[38, 0], Files[0].iloc[39, 0],
    Files[0].iloc[40, 0], Files[0].iloc[41, 0], Files[0].iloc[42, 0]
]


def calculateSumCrimes(file, x):
    return np.sum(
        [
            file.iloc[x, 1], file.iloc[x, 5],
            file.iloc[x, 9], file.iloc[x, 13],
            file.iloc[x, 17], file.iloc[x, 21],
            file.iloc[x, 25], file.iloc[x, 29],
            file.iloc[x, 33], file.iloc[x, 37],
            file.iloc[x, 41], file.iloc[x, 45]
        ])


def linearReg2(fileNum):
    collection_crimes = []
    for i in range(1, 42):
        collection_crimes.append(calculateSumCrimes(Files[fileNum], i))

    df = pd.DataFrame({
        'Population': population_arr,
        'Crimes': collection_crimes
    })

    lrm = smf.ols(
        formula='Crimes ~ Population',
        data=df
    ).fit()

    print(lrm.params)
    print(df)

    df.plot(
        kind='scatter',
        x='Population',
        y='Crimes'
    )

    x = pd.DataFrame({
        'Population': [100]
    })

    prediction = lrm.predict(x)

    print("Prediction")
    print(prediction)

    print("P-values")
    print(lrm.pvalues)

    # working with line of best fit ---------
    xs = np.array(population_arr, dtype=np.float64)
    ys = np.array(collection_crimes, dtype=np.float64)

    # get the m and b for equation
    def bestft(xs, ys):
        m = (
                    (mean(xs) * mean(ys)) - mean(xs * ys)
            ) / (
                    (
                            mean(xs) * mean(xs)) - mean(xs * xs)
            )

        b = (mean(ys) - m * mean(xs))
        return m, b

    m, b = bestft(xs, ys)

    # do equation for best fit
    regression_l = [
        (m * x) + b for x in xs
    ]

    # plot
    plt.scatter(xs, ys)
    plt.plot(
        xs,
        regression_l,
        color="red"
    )
    plt.title(tFNames[fileNum])
    plt.show()


i = 0

while i < 19:
    for File in Files:
        linearReg2(i)
        i = i + 1
