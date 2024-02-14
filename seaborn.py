# -*- coding: utf-8 -*-
"""seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u3jPu3hucJcDhwMo3bJARbccnQl41cA6
"""

pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
#Load sample dataset
tips=sns.load_dataset("tips")
#create a scatter plot
sns.scatterplot(x="total_bill",y="tip",data=tips)
plt.title("scatter plot of total bill vs .tip")
plt.xlabel("TOTAL BILL ($)")
plt.ylabel("TIP ($)")
plt.show

import pandas as pd
#import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Load sample dataset
#tips=sns.load_dataset("tips")
df=pd.read_csv("/content/plot.csv")
#create a scatter plot
sns.scatterplot(x="total_bill",y="tip",data=tips)
plt.title("scatter plot of total bill vs .tip")
plt.xlabel("TOTAL BILL ($)")
plt.ylabel("TIP ($)")
plt.show

import seaborn as sns
import matplotlib.pyplot as plt
diamonds=sns.load_dataset("diamonds")
print(diamonds.head())
#create a scatter plot
sns.scatterplot(x="carat", y="price", data=diamonds)
# Add title and labels
plt.title("Diamond Carat vs Price")
plt.xlabel("Carat")
plt.ylabel("Price")
# Show plot
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
# Load the dots dataset from Seaborn
dots= sns.load_dataset("dots")
print(dots.head())
# Create a scatter plot
sns.scatterplot(x="time", y="firing_rate", data=dots)
# Add title and labels
plt.title("Firing Rate over Time")
plt.xlabel("Time")
plt.ylabel("Firing Rate")
# Show plot
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
iris= sns.load_dataset("iris")
print(iris.head())
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation matrix of iris dataset")
plt.show

import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("planets")
print(iris.head())
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation matrix of sample dataset")
plt.show