import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Which city (chicago, new york city, washington) would you like to analyze? ").lower()
    while city not in ("chicago", "new york city", "washington"):
       print("Please choose a city: chicago, new york city or washington")
       city = input("Which city (chicago, new york city, washington) would you like to analyze? ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month (all, january, february, ..., june) would you like to analyze?").lower()
    # while loop
    while month not in("all", "january", "february", "march", "april", "may", "june", "july"):
        print("Please choose a month: all, january, february, ..., june")
        month = input("Which month (all, january, february, ..., june) would you like to analyze?")
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day (all, monday, tuesday, ..., sunday) of week would you like to analyze?").lower()
    while day not in ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
        print("Please choose a day: all, monday, tuesday, ..., friday")
        day = input("Which day (all, monday, tuesday, ..., sunday) of week would you like to analyze?")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        
    df = pd.read_csv(CITY_DATA[city])
    
    
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # dict for translating month 
    month_dict = {'january' : 1, 'february': 2, 'march': 3, 'april' : 4, 'may' : 5, 'june' : 6}
    
    # start
    # filter month
    if month != 'all':
        df = df.where(df['month'] == month_dict[month])

    
    # filter day
    if day not in ('all'):
        day = day.capitalize()
    if day != 'all':
        df = df.where(df['day'] == day)
    
    # ende
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # dict für übersetzung monate und tage
    month_dict = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6: 'June'}

    # TO DO: display the most common month
    most_common_month = month_dict[int(df['month'].mode()[0])]
    print("The most common month is: {}".format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day'].mode()[0]
    print("The most common day is: {}".format(most_common_day_of_week))


    # TO DO: display the most common start hour
    most_common_hour = int(df['hour'].mode()[0])
    print("The most common hour is: {} o'clock".format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comm_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(comm_start_station))

    # TO DO: display most commonly used end station
    comm_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(comm_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    # concernate start & end
    start_station = pd.Series(df['Start Station'])
    end_station = pd.Series(df['End Station'])
    start_and_end = start_station + " // " + end_station
   
    
    comm_start_and_end_station = start_and_end.mode()[0]
    print("The most commonly used combination of start and end station is: {}".format(comm_start_and_end_station))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

 
    # TO DO: display total travel time
    total_travel_time = pd.to_timedelta(df['Trip Duration'].sum(), unit = 's')
    print("Total travel time is {}".format(total_travel_time))

    # TO DO: display mean travel time
    total_mean_time = pd.to_timedelta(df['Trip Duration'].mean(), unit = 's')
    print('Mean travel time is {}'.format(total_mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print('Counts of user types is\n{}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\nCounts of gender is: \n{}'.format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
    
        print('\nUsers earliest birth year is: {} \nUsers most recent birth year is: {} \nUsers most common birth year is: {}'. format(earliest, most_recent, most_common))

    df = df.dropna()
    
    view_data = input('\n Would you like to view 5 rows of individual trip data? Enter yes or no. ').lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_data = input('Do you wish to continue? Enter yes or no. ').lower()
        if view_data == 'no':
            break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
