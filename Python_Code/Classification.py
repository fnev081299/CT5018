# Creator: Nicolas Euliarte Veliez
# Date of Creation: 28th Jan 2020
# ----------------------------------------------------------------------------------------------------------------------

import glob
import sys
import pandas as pd
import numpy as np
import pydot
from sklearn.tree import DecisionTreeClassifier
from pandas.plotting import register_matplotlib_converters
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image

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

pd.set_option("display.max_rows", None, "display.max_columns", None)


def mean1(file, x):
    return file.iloc[x, 1]


locations = Files[0].iloc[:, 0]
crimes = []

locarr = []

for x in range(0, 43):
    arr = []
    for i in range(0, 17):
        arr.append(mean1(Files[i], x))
    locarr.append(np.mean(arr))

population = [
    48852.59, 965.42,
    669.32, 852.52,
    1059.27, 0,
    498.89, 1053.32,
    1762.38, 772.27,
    924, 0,
    1832.75, 916.2,
    2812.57, 0,
    1844.25, 1184.37,
    0, 1846.48,
    1498.3, 0,
    1087.66, 1423.07,
    8908.08, 903.68,
    747.62, 320.27,
    0, 1101.66,
    0, 1154.2,
    1402.92, 1131.05,
    758.56, 1189.93,
    1703.84, 0,
    571.01, 0,
    2916.46, 2320.21,
    720.06
]

p = []
for z in population:
    if z != 0:
        p.append((z) / 48852.59)
    else:
        p.append(0)

g = []
for x in range(0, 43):
    g.append(locarr[x] * p[x])

m = np.sum(locarr)
print(m)

# homicide convictions
# 1 - minor level
# 2 = mid level
# 3 = high level
classifaction = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 2, 1, 1, 1, 1, 2,
                 1, 1, 1, 1, 3, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 2, 2, 1]

data_des = pd.DataFrame({
    'Mean Conviction': locarr,
    'Precentage of public': p,
    'Value': g,
    "Class": classifaction,
})

data_cols = ['Mean Conviction', 'Precentage of public']

x = data_des.iloc[:, 0:2]
y = data_des.iloc[:, 3]

print(data_des)
# print(x)
# print(y)

# ----------------------------------------------------------------------------------------------------------------------
# implementing classification
# classifying the risk level of an area

# number of homicide convictions in location
# Percentage of population in area
# Output the risk level of area in range 1-3
def AreaRiskClassification():
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

    dt = DecisionTreeClassifier(min_samples_split=3, random_state=99)
    dt.fit(X_train, y_train)

    y_pred = dt.predict(X_test)
    print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))

    dot_data = StringIO()
    export_graphviz(dt, out_file=dot_data,
                    filled=True,
                    special_characters=True,
                    class_names=['1', '2', '3']
                    )

    # creates a decision tree image
    graph = pydot.graph_from_dot_data(dot_data.getvalue())
    graph[0].write_png('convictions.png')
    Image(graph[0].create_png())

    # testing = [murders, percentage of population]
    test = [40, 0.4]  # high risk example
    # test = [10, .2]  # mid risk example
    # test = [1, .02]  # low risk example

    predicted_class = dt.predict(np.reshape(test, [1, -1]))
    print("Risk level of area: ", predicted_class)

AreaRiskClassification()
