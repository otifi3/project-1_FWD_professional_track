#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np


# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[3]:


def get_filters():
    
    
    
    
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city=input('chicago or new york city or washington')
    while city not in (CITY_DATA.keys()):
        print ('you should chose from chicago or new york city or washington')
        city=input('chicago or new york city or washington').lower()
        
    #get filter
        
    filter= input('filter data by month , day , both or none').lower()
    while filter not in (['month','day','both','none']):
        print('you should make choice from these choices')
        filter = input('filter data by month , day , both or none').lower()
        
    #get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june','july','august','september','october','november','december']
    if filter == 'month' or filter =='both':
        month=input('which month?').lower()
        while month not in months:
            print('you should write name of the month in a right way')
            month = input('which month').lower()
    else:
        month ='all'
    
    
    #get user input for day of week (all, monday, tuesday, ... sunday)
    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if filter =='day'or filter=='both':
        day=input('which day?').title()
        while day not in days:
            print('you should write name of the day in a right way')
            day=input('which day?').title()
    else:
        day='all'
    
    print('-'*40)
    return city, month, day




def load_data(city, month, day):
    
    
    
    data=pd.read_csv(CITY_DATA[city])
    
    
    
    data["Start Time"]=pd.to_datetime(data['Start Time'])
    #extract month with datetime
    data['month']=data["Start Time"].dt.month
    #extract day of the week with datetime
    data['day_of_week']=data["Start Time"].dt.day_name()
    #extract hour with datetime
    data['hour']=data['Start Time'].dt.hour
    
    
    #filter by month and make new data frame

    if month != 'all':
        months=['january','february','march','april','may','june','july','august','september','october','november','december']
        month=months.index(month)+1
        
        data=data[data['month']==month]
        
        
    #filter by day and make new data frame
    if day != 'all':
        data=data[data['day_of_week']==day.title()]
    
    
    return data


def time_stats(data):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(data['month'].mode()[0])


    # TO DO: display the most common day of week
    print(data['day_of_week'].mode()[0])



    # TO DO: display the most common start hour
    print(data['hour'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(data['Start Station'].mode()[0])
    


    # TO DO: display most commonly used end station
    print(data['End Station'].mode()[0])



    # TO DO: display most frequent combination of start station and end station trip
    S_E_S=data.groupby(['Start Station','End Station'])
    #sort this groups and take the first group value in this group and sort it in descending order
    print(S_E_S.size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



    

def trip_duration_stats(data):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(data['Trip Duration'].sum())
    


    # TO DO: display mean travel time
    print(data['Trip Duration'].mean())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



    
def user_stats(data,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print( data['User Type'].value_counts())


    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    #make if condetion if the city not washington becuse washington does not have gender or year of birth 
    if city != 'washington':
        print(data['Gender'].value_counts())
        print(data['Birth Year'].mode()[0])
        print(data['Birth Year'].max())
        print(data['Birth Year'].min())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[4]:


def main():
    while True:
        city, month, day = get_filters()
        data = load_data(city, month, day)
        time_stats(data)
        station_stats(data)
        trip_duration_stats(data)
        user_stats(data,city)
        


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




