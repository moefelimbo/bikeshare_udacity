import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    while True:
        city = input("\nSelect a city from the following:\nChicago\nNew York City\nWashington\n\n").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("\nInvalid input! Try again. ")
            continue
            # goes back to the while loop and repeats
        else:
            break
            # breaks the loop and goes to the next one

        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nSelect all or one month from the period of Jan to June.\n\n").lower()
        if month not in ("all","jan", "feb", "march", "april", "may", "june"):
            print("\nInvalid input! Try again. ")
            continue
        else:
            break

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nSelect a day or all days.\n\n").lower()
        if day not in ("all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"):
            print("\nInvalid input! ")
            continue
        else:
            break

    print('-'*40)
    return city.title(), month.capitalize(), day.capitalize()



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
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.dayofweek
    df["hour"] = df["Start Time"].dt.hour
    if month != "All":
        months = ["Jan", "Feb", "March", "April", "May", "June"]
        month = months.index(month) + 1

        df = df[df["month"] == month]

    if day != "All":
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = days.index(day)
        df = df[df["day"] == day]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    commonMonth = df["month"].mode()[0]
    print("The most common month is:\n", commonMonth)

    # TO DO: display the most common day of week
    commonDay = df["day"].mode()[0]
    print("The most common day is:\n", commonDay)

    # TO DO: display the most common start hour
    commonHour = df["hour"].mode()[0]
    print("The most common hour is:\n", commonHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startStation = df["Start Station"].value_counts().idxmax()
    print("The most common start station:\n", startStation)

    # TO DO: display most commonly used end station
    endStation = df["End Station"].value_counts().idxmax()
    print("The most common end station:\n", endStation)

    # TO DO: display most frequent combination of start station and end station trip
    StartEndStation = df.groupby(["Start Station", "End Station"]).count()
    print("The most frequent combination of start and end station is:\n", startStation, "\n",endStation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TotalTravelTime = sum(df["Trip Duration"])
    print("Total travel time (in seconds) is:\n", TotalTravelTime)

    # TO DO: display mean travel time
    MeanTravelTime = df["Trip Duration"].mean()
    print("Mean travel time (in seconds) is:\n", MeanTravelTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userTypesCount = df["User Type"].value_counts()
    print("The count of users by type is:\n", userTypesCount)

    # TO DO: Display counts of gender
    try:
        gendersCount = df['Gender'].value_counts()
        print('\nGender Types:\n', gendersCount)
    except KeyError:
        print("\nNo available data for the selected city.\n")

    try:
        Earliest = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest)
    except KeyError:
        print("No available data for the selected city.\n")

    try:
        Recent = df['Birth Year'].max()
        print('\nMost Recent Year:', Recent)
    except KeyError:
        print("No available data for the selected city.\n")

    try:
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
        print("No available data for the selected city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    # ask the user whether he/she wants to display 5 rows of raw data
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data?\n').lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


main()
