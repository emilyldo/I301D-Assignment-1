# Emily Do
# I310D Assignment 1
# Description of Program: 
# This program runs an analysis on the 2018 U.S. voting rates and the U.S. citizen voting-age population demographics, 
# specifically educational attainment and poverty status.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

vote = pd.read_csv('/Users/emilydo/US_Citizen_Voting_Clean.csv')
vote.head()
print(len(vote))
print(type(vote))
for col in vote.columns:
    print(col, type(vote[col][0]))
vote.describe()
vote.hist('voting_rate')
plt.ylabel('frequency')
vote.hist('bachelors_more_pct')
plt.ylabel('frequency')
vote.hist('below_poverty_pct')
plt.ylabel('frequency')
print(vote[['bachelors_more_pct', 'voting_rate']].corr())
vote.plot.scatter(x='bachelors_more_pct', y='voting_rate')
print(vote[['below_poverty_pct', 'voting_rate']].corr())
vote.plot.scatter(x='below_poverty_pct', y='voting_rate')