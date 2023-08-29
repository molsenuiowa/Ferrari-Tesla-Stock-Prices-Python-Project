#Function 1
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def plot_ferrari_tesla_high_low_prices():
    # Load the data from the CSV files
    ferrari_df = pd.read_csv('C:/Users/micha/Ferrari.csv')
    tesla_df = pd.read_csv('C:/Users/micha/Tesla.csv')

    # Convert the 'Date' column to datetime format
    ferrari_df['Date'] = pd.to_datetime(ferrari_df['Date'])
    tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

    # Set the years for the x-axis
    start_year = 2015
    end_year = 2023
    years = mdates.YearLocator()   # every year
    years_fmt = mdates.DateFormatter('%Y')

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the high values for Ferrari
    ax.plot(ferrari_df['Date'], ferrari_df['High'], label='Ferrari High', color='red')

    # Plot the low values for Ferrari
    ax.plot(ferrari_df['Date'], ferrari_df['Low'], label='Ferrari Low', color='blue')

    # Plot the high values for Tesla
    ax.plot(tesla_df['Date'], tesla_df['High'], label='Tesla High', color='green')

    # Plot the low values for Tesla
    ax.plot(tesla_df['Date'], tesla_df['Low'], label='Tesla Low', color='orange')

    # Set the title and axis labels
    ax.set_title('Ferrari and Tesla High/Low Prices')
    ax.set_xlabel('Year')
    ax.set_ylabel('Price ($)')

    # Set the x-axis limits
    start_date = dt.date(start_year, 1, 1)
    end_date = dt.date(end_year, 1, 1)
    ax.set_xlim(start_date, end_date)

    # Format the x-axis to show years
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)

    # Set the legend
    ax.legend()

    # Display the plot
    plt.show()

#This line chart can help to visualize and compare the high and low stock prices of Ferrari and Tesla over time
#How have the stock prices of Ferrari and Tesla changed over the years?
#Are there any patterns or trends in the stock prices of these companies?
#How do the high and low prices of each company compare to each other?
#Have there been any significant events or changes that have affected the stock prices of these companies?
#By visualizing the data in this way, we can gain insights into the historical performance of these companies and use that information to inform investment decisions or other business strategies. 
#We can also use this chart to make predictions about future trends in the stock prices of these companies, although it's important to note that past performance is not always a reliable indicator of future performance.
 
#Function 2
import numpy as np

def plot_ferrari_tesla_volume():
    # Load the data from the CSV files
    ferrari_df = pd.read_csv('C:/Users/micha/Ferrari.csv')
    tesla_df = pd.read_csv('C:/Users/micha/Tesla.csv')

    # Convert the 'Date' column to datetime format
    ferrari_df['Date'] = pd.to_datetime(ferrari_df['Date'])
    tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

    # Filter the data to the years 2015-2023
    start_date = pd.to_datetime('2015-01-01')
    end_date = pd.to_datetime('2023-01-01')
    ferrari_df = ferrari_df[(ferrari_df['Date'] >= start_date) & (ferrari_df['Date'] < end_date)]
    tesla_df = tesla_df[(tesla_df['Date'] >= start_date) & (tesla_df['Date'] < end_date)]

    # Calculate the highest and lowest volumes for each year
    ferrari_volumes = []
    tesla_volumes = []
    years = np.arange(2015, 2023)
    for year in years:
        ferrari_year_df = ferrari_df[ferrari_df['Date'].dt.year == year]
        tesla_year_df = tesla_df[tesla_df['Date'].dt.year == year]
        ferrari_volume_high = ferrari_year_df['Volume'].max()
        ferrari_volume_low = ferrari_year_df['Volume'].min()
        tesla_volume_high = tesla_year_df['Volume'].max()
        tesla_volume_low = tesla_year_df['Volume'].min()
        ferrari_volumes.append((ferrari_volume_high, ferrari_volume_low))
        tesla_volumes.append((tesla_volume_high, tesla_volume_low))

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the highest and lowest volumes for Ferrari
    ferrari_volumes = np.array(ferrari_volumes)
    ax.plot(years, ferrari_volumes[:, 0], label='Ferrari Highest Volume', color='red')
    ax.plot(years, ferrari_volumes[:, 1], label='Ferrari Lowest Volume', color='blue')

    # Plot the highest and lowest volumes for Tesla
    tesla_volumes = np.array(tesla_volumes)
    ax.plot(years, tesla_volumes[:, 0], label='Tesla Highest Volume', color='green')
    ax.plot(years, tesla_volumes[:, 1], label='Tesla Lowest Volume', color='orange')

    # Set the title and axis labels
    ax.set_title('Ferrari and Tesla Highest/Lowest Volumes')
    ax.set_xlabel('Year')
    ax.set_ylabel('Volume')

    # Set the x-axis limits
    ax.set_xlim(2015, 2022)

    # Set the legend
    ax.legend()

    # Display the plot
    plt.show()


#Function 3

def extract_yearly_open_close_columns(csv_path, start_year, end_year):
    df = pd.read_csv(csv_path, parse_dates=['Date'], index_col='Date')
    yearly_data = df.groupby(df.index.year).agg({'Open': 'first', 'Close': 'last'})
    filtered_data = yearly_data.loc[start_year:end_year]
    return filtered_data['Open'], filtered_data['Close']

def plot_yearly_open_close_prices(Ferrari_csv, Tesla_csv, start_year, end_year):
    Ferrari_open, Ferrari_close = extract_yearly_open_close_columns(Ferrari_csv, start_year, end_year)
    Tesla_open, Tesla_close = extract_yearly_open_close_columns(Tesla_csv, start_year, end_year)

    fig, ax = plt.subplots()
    ax.plot(Ferrari_open.index, Ferrari_open, label="Ferrari Open", marker='o')
    ax.plot(Ferrari_close.index, Ferrari_close, label="Ferrari Close", marker='o')
    ax.plot(Tesla_open.index, Tesla_open, label="Tesla Open", marker='o')
    ax.plot(Tesla_close.index, Tesla_close, label="Tesla Close", marker='o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Stock Price")
    ax.set_title("Yearly Opening and Closing Stock Prices")
    ax.legend()
    plt.xticks(range(start_year, end_year+1))
    plt.show()

# Paths to CSV files for Ferrari and Tesla
Ferrari_csv = r'C:\Users\micha\Ferrari Tesla Project Comp Thinking\ferrari.csv'
Tesla_csv = r'C:\Users\micha\Ferrari Tesla Project Comp Thinking\tesla.csv'

# Specify start and end years
start_year = 2015
end_year = 2023

# Call the function to plot the graph
plot_yearly_open_close_prices(Ferrari_csv, Tesla_csv, start_year, end_year)