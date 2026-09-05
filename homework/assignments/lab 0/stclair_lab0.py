# ------ STEP 1: DATA CLEANING -------

import pandas as pd
import numpy as np
import re

df = pd.read_csv('DS6021_F26/data/DS6021-Fall26-Anonymized.csv')

print(df.head())
print(df.info())
print(df.isnull().sum())

# Clean - extract first number from any string
def get_first_number(val):
    if pd.isna(val) or val == '':
        return np.nan
    match = re.search(r'\d+', str(val))
    return float(match.group()) if match else np.nan

df['Temperature'] = df['What is your ideal outdoor temperature (in Fahrenheit)?'].apply(get_first_number)
df['Sleep_Hours'] = df['How many hours do you sleep in a typical night?'].apply(get_first_number)
df['States_Visited'] = df['How many US states have you visited?'].apply(get_first_number)

print("\nCleaned columns:")
print(df[['Temperature', 'Sleep_Hours', 'States_Visited']].head(10))

# ------ STEP 2: UNIVARIABLE AND BIVARIABLE EXPLORATION -------

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))

# UNIVARIATE 
plt.subplot(2, 3, 1)
df['Rate your proficiency with Python'].hist(bins=5, edgecolor='black')
plt.title('Python Proficiency Distribution')
plt.xlabel('Proficiency (1-5)')
plt.ylabel('Count')

plt.subplot(2, 3, 2)
df['Sleep_Hours'].hist(bins=10, edgecolor='black')
plt.title('Sleep Hours Distribution')
plt.xlabel('Hours')
plt.ylabel('Count')

plt.subplot(2, 3, 3)
df['States_Visited'].hist(bins=15, edgecolor='black')
plt.title('US States Visited Distribution')
plt.xlabel('Number of States')
plt.ylabel('Count')

plt.subplot(2, 3, 4)
df['What is your favorite season?'].value_counts().plot(kind='bar')
plt.title('Favorite Season')
plt.xlabel('Season')
plt.ylabel('Count')
plt.xticks(rotation=45)

plt.subplot(2, 3, 5)
df['What type of phone do you have?'].value_counts().plot(kind='bar')
plt.title('Phone Type')
plt.xlabel('Phone')
plt.ylabel('Count')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('univariate_exploration.png')
print("\nUnivariate plot saved as 'univariate_exploration.png'")

# BIVARIATE 
plt.figure(figsize=(12, 8))

# Relationship 1: Python proficiency vs SQL usage
plt.subplot(2, 2, 1)
sql_yes = df[df['Have you ever used SQL?'] == 'Yes']['Rate your proficiency with Python']
sql_no = df[df['Have you ever used SQL?'] == 'No']['Rate your proficiency with Python']
plt.boxplot([sql_yes, sql_no], labels=['Used SQL', 'No SQL'])
plt.title('Python Proficiency by SQL Usage')
plt.ylabel('Python Proficiency (1-5)')

# Relationship 2: Git proficiency vs Python proficiency
plt.subplot(2, 2, 2)
plt.scatter(df['Rate your proficiency with git/github'],
            df['Rate your proficiency with Python'],
            alpha=0.6)
plt.title('Git vs Python Proficiency')
plt.xlabel('Git/Github Proficiency (1-5)')
plt.ylabel('Python Proficiency (1-5)')

# Relationship 3: Sleep hours vs Python proficiency
plt.subplot(2, 2, 3)
plt.scatter(df['Sleep_Hours'],
            df['Rate your proficiency with Python'],
            alpha=0.6)
plt.title('Sleep Hours vs Python Proficiency')
plt.xlabel('Sleep Hours')
plt.ylabel('Python Proficiency (1-5)')

# Relationship 4: Temperature preference vs favorite season
plt.subplot(2, 2, 4)
seasons = df['What is your favorite season?'].unique()
for season in seasons:
    temps = df[df['What is your favorite season?'] == season]['Temperature']
    plt.scatter([season]*len(temps), temps, alpha=0.6, label=season)
plt.title('Temperature Preference by Season')
plt.xlabel('Favorite Season')
plt.ylabel('Ideal Temperature (F)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('bivariate_exploration.png')
print("Bivariate plot saved as 'bivariate_exploration.png'")

plt.show()

# ------ STEP 3: REFLECTIONS -------

# 1. Anything surprising about the dataset?
    # The dataset has very consistent sleep patterns with almost everyone sleeps 8 hours.
    # Most people have iPhones and there are very few Android users). The temperature preferences
    # vary a lot even within favorite seasons (people who like Spring wanted temps
    # from 65 to 80 degrees). Skills are somewhat correlated and people good at Git tend
    # to be good at Python too.

# 2. Two cleaning decisions and why:
    # Decision 1: 
        # Temperature and Sleep Hours - I took the FIRST NUMBER from ranges
        # instead of the midpoint. For example, "70-85" became 70, not 77.5.
        # This is because taking the first number is simpler and preserves the lower bound 
        # value that someone gave. 
            # Alternative: Could have taken the midpoint, but that would have been more
            # complex and the extra precision wouldn't be meaningful.
    
    # Decision 2: 
        # States Visited - I extracted just the first number from entries like
        # "35-40 if you count driving through" and threw away the comment.
        # The question asks "how many states", which needs a single number. Taking the 
        # first number keeps it simple and consistent.
            # Alternative: Could have tried to use all numbers and take the average, but that
            # would be more complex and the extra precision wouldn't be meaningful.

# 3. Why use Python instead of Excel/Google Sheets?
    # In Excel/Sheets, cleaning is manual and not repeatable. If the data changes or you
    # get new responses, you'd have to clean it all over again by hand. There's no record
    # of what you did, so someone else can't verify your work or fix mistakes. If you
    # accidentally delete or change a cell, you lose data with no way to audit what happened.
    # Python creates a script that shows exactly what cleaning steps were done, can be run
    # again automatically, and can handle much larger datasets. This is critical in business
    # because data cleaning mistakes can lead to wrong conclusions and bad decisions.

# KEY FINDINGS SUMMARY
    
    # Univariate Analysis: 
        # The class is dominated by a few consistent patterns. Most students
        # sleep 8 hours per night, with very little variation. Python proficiency ranges from 1-5,
        # with most students rating themselves 3-4. The majority of students prefer Fall or Spring
        # as their favorite season. Nearly all students (85 out of 86) have iPhones, showing extreme
        # uniformity in phone choice. States visited varies much more widely, from 3 to 47 states,
        # suggesting diverse backgrounds and travel histories.
    
    # Bivariate Analysis: 
        # There is a moderate positive correlation between Git and Python
        # proficiency, with students skilled in one tending to be skilled in the other, suggesting 
        # they often learn programming tools together. Students who have used SQL tend to have 
        # slightly higher Python proficiency ratings than those who haven't, indicating that database
        # experience correlates with general coding ability. Temperature preferences vary 
        # significantly within each season preference, meaning students who like
        # the same season don't necessarily want the same temperature.