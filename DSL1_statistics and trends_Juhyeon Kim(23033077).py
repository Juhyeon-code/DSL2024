import matplotlib.pyplot as plt
import pandas as pd

# Make proper dataframe : years and countries
def worldbank_data():
    # Read the file
    file_name = "climate_change.csv"  # 변수명 변경
    df = pd.read_csv(file_name, skiprows=4)
    df = df.drop(columns=['Country Code', 'Indicator Code', "Unnamed: 68"])
    df = df.dropna(how='all')
    df.columns = ['Country', 'Indicator'] + [str(col) for col in df.columns[2:]]
    df.set_index(['Country', 'Indicator'], inplace=True)
    df.fillna(0, inplace=True)
    
    # From 2004 to 2023, 20 years
    years_21 = ['200{}'.format(i) for i in range(4, 10)] + ['201{}'.format(i) for i in range(0, 3)] + ['202{}'.format(i) for i in range(0, 4)]
    years_21_df = df[years_21]
    
    # From 1960 to 1970, 20 years
    years_20 = ['196{}'.format(i) for i in range(0, 10)] + ['197{}'.format(i) for i in range(0, 10)]
    years_20_df = df[years_20]

    return years_20_df, years_21_df


def analyze(years_20_df, years_21_df):
    
    # Choose three countries
    # France : High
    # Thailand : Middle
    # Afghanistan : Low
    three_countries = ['France', 'Thailand', 'Afghanistan']  
    
    # Choose two indicators
    two_indicators = ['Urban population (% of total population)', 'CO2 emissions from liquid fuel consumption (% of total)'] 
    
    # Choose graph color : three
    pastel_colors = ['#FFD1DC', '#ADD8E6', '#E1BEE7']
    
    for idx, indicator_name in enumerate(two_indicators):
        print(f"{indicator_name} over Time")
        plt.figure()
        for i, country in enumerate(three_countries):
            plt.plot(years_21_df.loc[(country, indicator_name)].index, years_21_df.loc[(country, indicator_name)], label=country, color=pastel_colors[i])
        plt.xlabel('Year')
        plt.ylabel(indicator_name)
        plt.title(f'{indicator_name} over Time')
        plt.legend()
        plt.show()

def statistics():
    years_20_df, years_21_df = worldbank_data()
    
    # years_20_df.describe()
    print("\nSummary Statistics for years_20_df:")
    print(years_20_df.describe())
    
    # years_21_df.describe()
    print("Summary Statistics for years_21_df:")
    print(years_21_df.describe())
    
    #analyze function
    analyze(years_20_df, years_21_df)

if __name__ == '__main__':
    statistics()