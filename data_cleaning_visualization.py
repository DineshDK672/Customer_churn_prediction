import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# To display all the columns without truncating
pd.set_option('display.max_columns', None)

df = pd.read_csv(
    "WA_Fn-UseC_-Telco-Customer-Churn.csv")
df = df.drop(['customerID'], axis=1)
# print(df.head())

# Change 'TotalCharges' to numeric values
df['TotalCharges'] = pd.to_numeric(df.TotalCharges, errors='coerce')
print(df.isna().sum())  # To check for null values

# To see the rows with null values in 'TotalCharges'
print(df[np.isnan(df['TotalCharges'])])

print(df[df['tenure'] == 0].index)  # To check for rows with 'tenure' 0

df.drop(labels=df[df['tenure'] == 0].index, axis=0, inplace=True)
# There should be no more null values in 'TotalCharges'

print(df[np.isnan(df['TotalCharges'])])

#   To convert numeric values in 'SeniorCitizen' to 'Yes'/'No'
print(df['SeniorCitizen'].unique())  # To find unique values in 'SeniorCitizen'
df["SeniorCitizen"] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
print(df['SeniorCitizen'].unique())

print(df.dtypes)

# Data Visualization

g_labels = df['gender'].unique()
c_labels = df['Churn'].unique()
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Gender Chart
wedges1, texts1, autotexts1 = ax1.pie(df['gender'].value_counts(
), labels=g_labels, autopct='%1.1f%%', startangle=90)
ax1.set_title("Chart 1: Gender")
ax1.axis('equal')
ax1.legend(wedges1, g_labels, title="Genders")

# Churn Chart
wedges2, texts2, autotexts2 = ax2.pie(df['Churn'].value_counts(), labels=c_labels,
                                      autopct='%1.1f%%', startangle=180)
ax2.set_title("Chart 2: Churn %")
ax2.axis('equal')
ax2.legend(wedges2, c_labels, title="Churned")

plt.tight_layout()
plt.show()

print(df['Churn'].value_counts())
print(df['Churn'].groupby(by=df['gender']
                          ).value_counts().sort_index(level='Churn'))

plt.figure(figsize=(6, 6))
c_labels = df['Churn'].unique()
values = df['Churn'].value_counts()
colors = ['#ff6666', '#66b3ff']
colors_gender = ['#ffb3e6', '#c2c2f0', '#ffb3e6', '#c2c2f0']
gender_values = df['Churn'].groupby(by=df['gender']).value_counts(
).sort_index(level='Churn')
g_labels = gender_values.index.get_level_values(level='gender')
explode = (0.3, 0.3)
size = 3

plt.pie(values, labels=c_labels, radius=10, explode=explode, colors=colors, startangle=90,
        wedgeprops=dict(width=size, edgecolor='w'))
plt.pie(gender_values, labels=g_labels, autopct='%1.1f%%', radius=10 - size, colors=colors_gender, startangle=90,
        wedgeprops=dict(width=size, edgecolor='w'))
plt.title('Churn Distribution w.r.t Gender: Male(M), Female(F)',
          fontsize=15, y=1.1)
plt.axis('equal')
plt.tight_layout()
plt.show()
