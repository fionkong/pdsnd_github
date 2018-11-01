# Udacity bikeshare hw
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please input the city: ').lower()
        if city.lower() == 'chicago':
            break
        elif city.lower() == "new york city":
            break
        elif city.lower() == "washington":
            break
        else:
            print('That is no valid input. Please re-enter!')
            continue

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please input the month, type in "all" to set no filter: ').lower()
        if month.lower() == 'january':
            break
        elif month.lower() == 'february':
            break
        elif month.lower() == 'march':
            break
        elif month.lower() == 'april':
            break
        elif month.lower() == 'may':
            break
        elif month.lower() == 'june':
            break
        elif month.lower() == 'all':
            break
        else:
            print('That is no  valid input. Please re-enter!')
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please input a day, type in "all" to set no filter: ').lower()
        if day.lower() == 'monday':
            break
        elif day.lower() == 'tuesday':
            break
        elif day.lower() == 'wednesday':
            break
        elif day.lower() == 'thursday':
            break
        elif day.lower() == 'friday':
            break
        elif day.lower() == 'saturday':
            break
        elif day.lower() == 'sunday':
            break
        elif day.lower() == 'all':
            break
        else:
            print('That is no valid input. Please re-enter!')
            continue

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month:', common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week:', common_day_of_week)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common start station:', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station:', common_end)

    # display most frequent combination of start station and end station trip
    common_trip = (df['Start Station']+df['End Station']).mode()[0]
    print('The most common trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()

    #print("Total travel time: ", total_travel)
    minute, second = divmod(total_travel, 60)
    hour, minute = divmod(minute, 60)
    print('Total travel time: {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()

    #print("Mean travel time: ", mean_travel)
    m, s = divmod(mean_travel, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('Mean travel time: {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration: {} minutes and {} seconds.'.format(m, s))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print ("Counts of User Type: ", user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print ("Counts of gender:    ", count_gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birthdate = df['Birth Year'].min()
        most_recent_birthdate = df['Birth Year'].max()
        most_common_birthdate = df['Birth Year'].mode()
        print("Earliest year of birth:     ", earliest_birthdate)
        print("Most recent year of birth: ", most_recent_birthdate)
        print("Most common year of birth: ", most_common_birthdate)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, current_line):
    """Displays five lines of data if the user specifies that they would like to."""

    print('\nDisplay data...\n')
    start_time = time.time()

    display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    display = display.lower()
    if display == 'yes' or display == 'y':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_data(df, current_line)
    if display == 'no' or display == 'n':
        return
    else:
        print("\nInvalid entry. Please try again.")
        return display_data(df, current_line)

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
        display_data(df, 0)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
