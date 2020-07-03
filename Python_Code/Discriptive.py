# Creator: Nicolas Euliarte Veliez
# Date of Creation: 28th Jan 2020
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import glob
import matplotlib.pyplot as plt
import numpy as np
import sys
from datetime import datetime
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from pandas.plotting import scatter_matrix
from scipy.stats import ttest_1samp
from matplotlib.artist import setp

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

# # Print the output.
# print(df)
#
# # [Row,Column]
# print('[Row,Column]\n ', df.iloc[3, 1])
#
# # Gets a column i.e jan 2014 for all locations
# print('Gets a column i.e jan 2014 for all locations\n ', df.iloc[:, 1])
#
# # Gets a row i.e every month for a location
# print('Gets a row i.e every month for a location \n', df.iloc[1])
#
# # Mean number of assaults in jan14 in all locations
# print('Mean number of assaults in jan14 in all locations\n ', np.mean(df.iloc[:, 1]))

# Making bar graphs from individual months for every month -------------------------------------------------------------
def drawGraph1(file, x, y):
    # print(file05_2014.columns)

    file[[x, y]].drop([0]).plot.bar()  # drops first column (national) to not show
    Columns = file.iloc[:, 0].drop([0])  # get row names

    plt.title(tFNames[i])
    plt.ylabel("Conviction count")
    plt.xlabel("")
    plt.xticks([i for i, _ in enumerate(Columns)], Columns)
    plt.show()

    print(x)
    print("Mean of convictions: ", file[x].drop([0]).mean())
    print("Median of convictions: ", file[x].drop([0]).median())
    print("Mode if convictions: ", file[x].drop([0]).mode())
    print("Standard deviation: ", file[x].drop([0]).std())
    print("Variance: ", file[x].drop([0]).var())
    print("Description for number of Conviction: \n", file[x].drop([0]).describe())

    print('\n', y)
    print("Mean of convictions: ", file[y].drop([0]).mean())
    print("Median of convictions: ", file[y].drop([0]).median())
    print("Mode if convictions: ", file[y].drop([0]).mode())
    print("Standard deviation: ", file[y].drop([0]).std())
    print("Variance: ", file[y].drop([0]).var())
    print("Description for number of Conviction: \n", file[y].drop([0]).describe())

    print('\n Covariance and Correlation:')
    print("Covariance ",
          np.cov(file[x].drop([0]),
                 file[y].drop([0])))
    print("Correlation from covariance ",
          np.corrcoef(file[x].drop([0]),
                      file[y].drop([0])))

    print("Correlation ",
          file[y].drop([0]).corr(file[x].drop([0]),
                       method='pearson',
                       min_periods=1))

    a = file[x].drop([0]).mean()
    print("Mean: ", a)
    tset, pval = ttest_1samp(file[x].drop([0]), 3)
    print("p-values: ", pval)

    if pval < 0.05:
        print("We are rejecting H0")
    else:
        print("WE are accepting  H0")


i = 0
while i < 19:
    for File in Files:
        # print(tFNames[i])
        # drawGraph1(
        #     File,
        #     'Number of Homicide Convictions',
        #     'Number of Public Order Offences Convictions'
        # )
        i = i + 1


def numHomicide(i, z):
    x = df.iloc[:, 0]
    y = df.iloc[:, z]

    plt.bar(x, y)
    plt.xlabel('number of homicide convictions')
    plt.xticks(rotation=90)
    plt.title(tFNames[i])
    plt.show()

i = 0
z = 1
while i < 19:
    numHomicide(i, z)
    i = i + 1
    z = z + 1

# ----------------------------------------------------------------------------------------------------------------------
def calcNatSum(file):
    return np.sum(
        [file.iloc[0, 1], file.iloc[0, 5],
         file.iloc[0, 9], file.iloc[0, 13],
         file.iloc[0, 17], file.iloc[0, 21],
         file.iloc[0, 25], file.iloc[0, 29],
         file.iloc[0, 33], file.iloc[0, 37],
         file.iloc[0, 41], file.iloc[0, 45]
         ])

def numOfConvictions():
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
                 calcNatSum(Files[18])]

    for crimes in sumCrimes:
        sumCrimesVals = sumCrimes + crimes


    # Plotting the sum of crimes
    plt.plot(dates_list, sumCrimes)
    plt.xticks(rotation=90)
    plt.title("Total of Crimes vs Months")
    plt.xlabel("Month")
    plt.ylabel("Crime rate")
    plt.show()

    a = sumCrimesVals.mean()
    print("Mean: ", a)
    tset, pval = ttest_1samp(sumCrimesVals, 30)
    print("p-values: ", pval)

    if pval < 0.05:
        print("Rejecting H0")
    else:
        print("Accepting H0")


# numOfConvictions()

# box plotting ---------------------------------------------------------------------------------------------------------
def drawGraph2(file, x, y):
    # drops first column (national) to not show
    file.boxplot([x, y])

    plt.title(tFNames[i])
    plt.ylabel("Number")
    plt.xticks(rotation=10)
    plt.show()


i = 0
while i < 19:
    for File in Files:
        # drawGraph2(
        #     File,
        #     'Number of Theft And Handling Convictions',
        #     'Number of Theft And Handling Unsuccessful'
        # )
        i = i + 1


# scatter matrix -------------------------------------------------------------------------------------------------------
def drawGraph3(file):
    axs = scatter_matrix(file.rename(columns={
        'Number of Homicide Convictions': 'Homicides',
        'Number of Offences Against The Person Convictions': 'Against Person',
        'Number of Sexual Offences Convictions': 'Sexual Offence',
        'Number of Burglary Convictions': 'Burglary',
        'Number of Robbery Convictions': 'Robbery',
        'Number of Theft And Handling Convictions': 'Theft/Handling',
        'Number of Fraud And Forgery Convictions': 'Fraud/Forgery',
        'Number of Criminal Damage Convictions': 'Damage',
        'Number of Drugs Offences Convictions': 'Drugs',
        'Number of Public Order Offences Convictions': 'Public Order',
        'Number of All Other Offences (excluding Motoring) Convictions': 'Other',
        'Number of Motoring Offences Convictions': 'Motoring'
    }),
        alpha=0.2,
        figsize=(12, 12),
        diagonal='kde')

    n = len(file.columns)
    # print(len(file.columns))

    for x in range(n):
        for y in range(n):
            # to get the axis of subplots
            ax = axs[x, y]
            # to make x axis name vertical
            ax.xaxis.label.set_rotation(90)
            # to make y axis name horizontal
            ax.yaxis.label.set_rotation(0)
            # to make sure y axis names are outside the plot area
            ax.yaxis.labelpad = 15
            # to make sure x axis names are outside the plot area
            ax.xaxis.labelpad = 15
    plt.show()

i = 0
while i < 19:
    for File in Files:
        da = Files[i].drop(Files[i].index[0])[['Number of Homicide Convictions',
                                               'Number of Offences Against The Person Convictions',
                                               'Number of Sexual Offences Convictions',
                                               'Number of Burglary Convictions',
                                               'Number of Robbery Convictions',
                                               'Number of Theft And Handling Convictions',
                                               'Number of Fraud And Forgery Convictions',
                                               'Number of Criminal Damage Convictions',
                                               'Number of Drugs Offences Convictions',
                                               'Number of Public Order Offences Convictions',
                                               'Number of All Other Offences (excluding Motoring) Convictions',
                                               'Number of Motoring Offences Convictions'
                                               ]]
        # drawGraph3(da)
        i = i + 1

# pair plot ------------------------------------------------------------------------------------------------------------
def drawGraph4(file):
    g = sns.pairplot(file.rename(columns={
        'Number of Homicide Convictions': 'Homicides',
        'Number of Offences Against The Person Convictions': 'Against Person',
        'Number of Sexual Offences Convictions': 'Sexual Offence',
        'Number of Burglary Convictions': 'Burglary',
        'Number of Robbery Convictions': 'Robbery',
        'Number of Theft And Handling Convictions': 'Theft/Handling',
        'Number of Fraud And Forgery Convictions': 'Fraud/Forgery',
        'Number of Criminal Damage Convictions': 'Damage',
        'Number of Drugs Offences Convictions': 'Drugs',
        'Number of Public Order Offences Convictions': 'Public Order',
        'Number of All Other Offences (excluding Motoring) Convictions': 'Other',
        'Number of Motoring Offences Convictions': 'Motoring'
    }),
        height=1.5)

    g.fig.draw(
        g.fig.canvas.get_renderer()
    )  # required, as matplotlib calculates ticks during draw time
    for ax in g.axes.flat:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    plt.show()

i = 0
while i < 19:
    for File in Files:
        da = Files[i].drop(Files[i].index[0])[['Number of Homicide Convictions',
                                               'Number of Offences Against The Person Convictions',
                                               'Number of Sexual Offences Convictions',
                                               'Number of Burglary Convictions',
                                               'Number of Robbery Convictions',
                                               'Number of Theft And Handling Convictions',
                                               'Number of Fraud And Forgery Convictions',
                                               'Number of Criminal Damage Convictions',
                                               'Number of Drugs Offences Convictions',
                                               'Number of Public Order Offences Convictions',
                                               'Number of All Other Offences (excluding Motoring) Convictions',
                                               'Number of Motoring Offences Convictions'
                                               ]]
        # drawGraph4(da)
        i = i + 1
