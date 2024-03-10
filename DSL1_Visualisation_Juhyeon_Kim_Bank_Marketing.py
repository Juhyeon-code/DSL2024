# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:38:14 2024

@author: kimju
"""

#import numpy, pandas, matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Set the font of the chart 
from matplotlib import rc
plt.rcParams['axes.unicode_minus'] = False

""" This data is a csv file 
    containing customers' information for bank marketing.
"""

#Read CSV data and check head of data
bank = pd.read_csv('C:\\Users\\kimju\\Data Science Lab\\DSL1_Visualization/bank.csv')
print(bank.head())

#Check the data : info and missing values
bank.info()
bank.isnull().sum()

""" Create a line plot to see 
    what kind of jobs are in each month 
    the last contacted the bank since the last campaign.
    
    First, only the required rows are extracted 
    from the existing data frame.
    In particular, rows corresponding to Month rearrange data 
    in chronological order.

    After that, the data frame is modified to fit 
    the desired visualization.
    After sorting in ascending order based on Month,
    For each month of Month, find the count for each category of job.
"""

#Extracting the data needed and creating a new dataframe named 'bank_cus'
bank_cus_info = bank[['month','age','job','marital','education','balance','housing']]
bank_cus = bank_cus_info.sort_values(by='month')
print(bank_cus)

#Set new columns in new dataframe 'month_counts'
desired_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
bank_cus['month'] = pd.Categorical(bank_cus['month'], categories=desired_order, ordered=True)

month_counts_c = bank_cus.groupby(['month', 'job']).size().reset_index(name='count')
month_counts = month_counts_c.sort_values(by=['month', 'count'], ascending=[True, False])

print(month_counts)

#Make linplot about Monthly count of new customers by job
def lineplot(month_counts, jobs):
    """ This line plot puts Month on the x-axis,
        On the y-axis, the number of Counts for each job come out.

        The title of this line plot is set to 'Monthly Count of Job'
        Set the label for each axis.

        Turn on the grid so that each count value can be seen clearly
        Match the yticks code from 0 to 851 every 100 intervals.

        Put a legend on it, and show the graph.
    """
    for job in jobs:
        plt.plot(month_counts[month_counts['job'] == job]['month'], month_counts[month_counts['job'] == job]['count'], label = job, marker = "x")

    plt.title('Monthly Count of Jobs')
    plt.xlabel('Month')
    plt.ylabel('Count')
    
    plt.grid(True)
    plt.yticks(range(0, 851, 100))
    
    plt.legend()
    plt.show()
    

plt.figure(figsize = (11, 6))

lineplot(month_counts, jobs = month_counts['job'].unique())

""" Bank Customer's Age - Education 
    relation for next campaign by pie chart

    First, only the required rows are extracted 
    from the existing data frame.
    

    In the newly created data frame 'bank_c'
    age creates a new group every 10 years,
    Count values of age_group for each category of education are counted.
"""

#Select customer's information data and make new data frame at 'bank_c'
bank_cus_age = bank[['age','job','marital','education','balance','housing']]

#sort by 'age'
bank_c = bank_cus_age.sort_values(by='age')
print(bank_c)

#Count and ckeck each education category in the 'education' column
edu_categories = bank_c['education'].value_counts()
print(edu_categories)

#Create 'age_group' with a range of 10 years
age_bins = range(0, bank_c['age'].max()+20, 20)
age_labels = ['{}-{}'.format(i, i+19) for i in age_bins[:-1]]

bank_c['age_group'] = pd.cut(bank_c['age'], bins=age_bins, labels=age_labels)

#Set new columns in new dataframe 'age_group_counts'
age_group_counts = bank_c.groupby(['education', 'age_group']).size().reset_index(name = 'count')

print(age_group_counts)

#Make 4 pie chart
#About counts of age groups for each item in the education category.
""" To draw a pie chart based on the four items of education,

    To make this chart look good, set the size to (11,8)
    Create four subsplots consisting of 2x2.

    Set the color code of this pie chart to a variable called colors.

    After that, we create a pie chart using the value for age_group_counts
    The title of each pie chart is the category name of education

    At the end, add a legend to the whole thing.
"""
#Set pie plot's figure size
plt.figure(figsize = (11, 8))

#First subplot_primary
plt.subplot(2,2,1)
pri_counts = age_group_counts[age_group_counts['education'] == 'primary']

#Set pie chart's color
colors = ['#C382AB', '#FF6D68', '#F5CCD1','#90AFC5', '#88B04B' ]

#Configuring a pie chart excluding labels
plt.pie(pri_counts['count'], autopct = '%1.1f%%', startangle = 90, textprops = {'fontsize': 10}, colors = colors)
plt.axis('equal')
plt.title('primary_age')

#Second subplot_secondary
plt.subplot(2,2,2)
sec_counts = age_group_counts[age_group_counts['education'] == 'secondary']
colors = ['#C382AB', '#FF6D68', '#F5CCD1','#90AFC5', '#88B04B' ]
plt.pie(sec_counts['count'], autopct = '%1.1f%%', startangle = 90, textprops = {'fontsize': 10}, colors = colors)
plt.axis('equal')
plt.title('secondary_age')

#Thrid subplot_tertiary
plt.subplot(2,2,3)
ter_counts = age_group_counts[age_group_counts['education'] == 'tertiary']
colors = ['#C382AB', '#FF6D68', '#F5CCD1','#90AFC5', '#88B04B' ]
plt.pie(ter_counts['count'], autopct = '%1.1f%%', startangle = 90, textprops = {'fontsize': 10}, colors = colors)
plt.axis('equal')
plt.title('tertiary_age')

#Fourth subplot_unknown
plt.subplot(2,2,4)
un_counts = age_group_counts[age_group_counts['education'] == 'unknown']
colors = ['#C382AB', '#FF6D68', '#F5CCD1','#90AFC5', '#88B04B' ]
plt.pie(un_counts['count'], autopct = '%1.1f%%', startangle = 90, textprops = {'fontsize': 10}, colors = colors)
plt.axis('equal')
plt.title('unknown_age')

#Make legend include four chart
plt.legend(age_group_counts['age_group'].unique(), title = 'Age Groups', bbox_to_anchor = (1, 0.5))

#Make more clear layout
plt.tight_layout()

#show
plt.show()

""" Bank Customer's Campaign-poutcome 
    relation for next campaign by Bar plot 
    
    First, only the required rows are extracted 
    from the existing data frame.
    
    In the newly created data frame 'bank_cam'
    compaign creates a new group every 10 times,
    Count values of campaign_group for each category of poutcomes are counted.
"""

#Extracting the data needed and creating a new dataframe named 'bank_cam'
bank_cam_info = bank[['campaign','poutcome','previous']]
bank_cam = bank_cam_info.sort_values(by='campaign')
print(bank_cam)

#Create 'campaign' with a range of 10
cam_bins = range(0, bank_cam['campaign'].max()+10, 10)
cam_labels = ['{}-{}'.format(i, i+9) for i in cam_bins[:-1]]

bank_cam['campaign_group'] = pd.cut(bank_cam['campaign'], bins = cam_bins, labels = cam_labels)

#Set new columns in new dataframe 'cam_age_group'
cam_age_group = bank_cam.groupby(['campaign_group', 'poutcome']).size().reset_index(name = 'count')
C = cam_age_group.sort_values(by = 'campaign_group')
print(C)

zero_nine = C[C['campaign_group'] == '0-9']
zero_nine['poutcome']

#Make bar plot of campaign'0-9'
""" Below is the code for two bar plots.
    First, the code for 0-9.
    Set the color of each bar plot Title, x-label, y-label.

    After that, set the legend to appear by color.
"""
#Extract of '0-9' at C dataframe
zero_nine = C[C['campaign_group'] == '0-9']

#Set colors of bars
colors = {'failure': 'red', 'other': 'orange', 'success': 'yellow', 'unknown': 'limegreen'}

bars = plt.bar(zero_nine['poutcome'], zero_nine['count'], color = [colors[p] for p in zero_nine['poutcome']])

# add title and label of bar plot
plt.title('Count by poutcome for campaign_group 0-9')
plt.xlabel('poutcome')
plt.ylabel('Count')

legend_labels = zero_nine['poutcome'].unique()
plt.legend(bars, legend_labels, title = 'Poutcome')

# show graph
plt.show()

E_zero_nine = C[C['campaign_group'] != '0-9']
E_zero_nine.sort_values(by = 'campaign_group')

#Make bar plot of campaign except '0-9'
""" Below is the code for second bar plot.
    Set the color of each bar plot
    
    To make this chart look good, set the size to (11,8)
    Create four subsplots consisting of 2x3.

    Set the color code of this pie chart to a variable called colors.
    
    Set the color of each bar plot Title, x-label, y-label.

    After that, set the legend of each graph to appear by color.
"""
#Extract of '0-9' at C dataframe
E_zero_nine = C[C['campaign_group'] != '0-9']

plt.figure(figsize = (11, 8))
colors = {'failure': 'red', 'other': 'orange', 'success': 'yellow', 'unknown': 'limegreen'}

#Make supplot
#'10-19'
plt.subplot(2,3,1)
ten = E_zero_nine[E_zero_nine['campaign_group'] == '10-19']
ten_bars = plt.bar(ten['poutcome'], ten['count'], color = [colors[p] for p in E_zero_nine['poutcome']])

legend_labels = E_zero_nine['poutcome'].unique()
plt.legend(ten_bars, legend_labels, title = 'Poutcome')
plt.title('10-19')
plt.xlabel('poutcome')
plt.ylabel('Count')

#'20-29'
plt.subplot(2,3,2)
tw = E_zero_nine[E_zero_nine['campaign_group'] == '20-29']
tw_bars = plt.bar(tw['poutcome'], tw['count'], color = [colors[p] for p in E_zero_nine['poutcome']])

plt.legend(tw_bars, legend_labels, title = 'Poutcome')
plt.title('20-29')
plt.xlabel('poutcome')
plt.ylabel('Count')


#'30-39'
plt.subplot(2,3,3)
th = E_zero_nine[E_zero_nine['campaign_group'] == '30-39']
th_bars = plt.bar(th['poutcome'], th['count'], color = [colors[p] for p in E_zero_nine['poutcome']])

plt.legend(th_bars, legend_labels, title = 'Poutcome')
plt.title('30-39')
plt.xlabel('poutcome')
plt.ylabel('Count')

#'40-49'
plt.subplot(2,3,4)
fo = E_zero_nine[E_zero_nine['campaign_group'] == '40-49']
fo_bars = plt.bar(fo['poutcome'], fo['count'], color = [colors[p] for p in E_zero_nine['poutcome']])

plt.legend(fo_bars, legend_labels, title = 'Poutcome')
plt.title('40-49')
plt.xlabel('poutcome')
plt.ylabel('Count')

#'50-59'
plt.subplot(2,3,5)
fif = E_zero_nine[E_zero_nine['campaign_group'] == '50-59']
fif_bars = plt.bar(fif['poutcome'], fif['count'], color = [colors[p] for p in E_zero_nine['poutcome']])

plt.legend(fif_bars, legend_labels, title = 'Poutcome')
plt.title('50-59')
plt.xlabel('poutcome')
plt.ylabel('Count')

#'60-69'
plt.subplot(2,3,6)
six = E_zero_nine[E_zero_nine['campaign_group'] == '60-69']
six_bars = plt.bar(six['poutcome'], six['count'], color = [colors[p] for p in E_zero_nine['poutcome']])

plt.legend(six_bars, legend_labels, title = 'Poutcome')
plt.title('60-69')
plt.xlabel('poutcome')
plt.ylabel('Count')

#Make title
plt.suptitle('Count by poutcome for campaign_group', fontsize=16)

#Make more clear layout
plt.tight_layout()

# show graph
plt.show()