# Creator: Nicolas Euliarte Veliez
# Date of Creation: 28th Jan 2020
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import glob
import matplotlib.pyplot as plt
import numpy as np
import sys
from datetime import datetime
import statsmodels.api as sm
from dateutil.relativedelta import relativedelta
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

# intialize data of lists for number of homicide convictions
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
dates_list = []


# ----------------------------------------------------------------------------------------------------------------------
def calcNatSum(file):
    return np.sum([
        file.iloc[0, 1], file.iloc[0, 5],
        file.iloc[0, 9], file.iloc[0, 13],
        file.iloc[0, 17], file.iloc[0, 21],
        file.iloc[0, 25], file.iloc[0, 29],
        file.iloc[0, 33], file.iloc[0, 37],
        file.iloc[0, 41], file.iloc[0, 45]
    ])


for date in tFNames:
    dates_list.append(datetime.strptime(date, '%m/%y'))

sumCrimes = [calcNatSum(Files[0]), calcNatSum(Files[1]),
             calcNatSum(Files[2]), calcNatSum(Files[3]),
             calcNatSum(Files[4]), calcNatSum(Files[5]),
             calcNatSum(Files[6]), calcNatSum(Files[7]),
             calcNatSum(Files[8]), calcNatSum(Files[9]),
             calcNatSum(Files[10]), calcNatSum(Files[11]),
             calcNatSum(Files[12]), calcNatSum(Files[13]),
             calcNatSum(Files[14]), calcNatSum(Files[15]),
             calcNatSum(Files[16]), calcNatSum(Files[17]),
             calcNatSum(Files[18])
             ]

# time series ----------------------------------------------------------------------------------------------------------
df = pd.DataFrame({
    'Date': [
        '2014/01', '2014/02', '2014/03', '2014/04', '2014/05',
        '2014/06', '2014/07', '2014/08', '2014/09', '2014/10',
        '2014/11', '2014/12', '2015/01', '2015/02', '2015/03',
        '2015/04', '2015/05', '2015/06', '2015/07'],
    'Amount': sumCrimes
})
df.set_index(
    'Date',
    inplace=True
)

rmean = df.rolling(2).mean()
rstd = df.rolling(2).std()

# Rolling mean data
print("Rolling mean data")
print("Original dataset:")
print(df)
print("Standard deviation:")
print(rstd)
print("Rolling mean")
print(rmean)

fig = plt.figure()

og = plt.plot(
    df,
    color='red',
    label='original'
)

mean = plt.plot(
    rmean,
    color='green',
    label='Rolling mean'
)

std = plt.plot(
    rstd,
    color='blue',
    label='Rolling std'
)

plt.xticks(rotation=90)
plt.title("rolling mean and std")
plt.legend()

plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# Arima prediction modelling
def arimaModelling(df):
    # Data adjustment
    start = datetime.strptime("2014/01", "%Y/%m")
    dates_list = [start + relativedelta(months=x) for x in range(0, 19)]
    df['index'] = dates_list
    df.set_index(['index'], inplace=True)
    df.index.name = None
    df.columns = ['Original_Amount']

    # ARIMA model
    mod = sm.tsa.statespace.SARIMAX(df.Original_Amount, trend='n', order=(1, 0, 0), seasonal_order=(1, 1, 1, 12))
    results = mod.fit()
    start = datetime.strptime("2015/07", "%Y/%m")
    dates_list = [start + relativedelta(months=x) for x in range(1, 12)]
    future = pd.DataFrame(index=dates_list, columns=df.columns)

    df = pd.concat([df, future])
    df['Forecast'] = results.predict(start=18, end=35, dynamic=True)
    df[['Original_Amount', 'Forecast']].iloc[-24:].plot()

    plt.title("Prediction model of the number of convictions per month")
    plt.show()
    print(df)


arimaModelling(df)
