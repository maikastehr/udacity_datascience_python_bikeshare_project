# Nanodegree Datascience
# Bikeshare python project
Udacity nanodegree program - python project - bikeshare data analysis

## What i've learned
This project was there to get known to the python libraries numpry and pandas. As well as get more practice in working with Python and DataFrames. A readme file was created to give more information on what happens in my bikeshare.py file.

## What it's about
Bikeshare data from three different US contries (Chicago, Washington, New York City) has been automatically transformed and prepared for further calculations. It is an interactive project with User input to get more details on what the user would like to analyze within the given data. For example the User recieves details about most used bikesharing stations per city.

## Used functions
Get user information and make sure one of the correct options was choosen. In this example for the city.
```
city = input("Which city (chicago, new york city, washington) would you like to analyze? ").lower()
    while city not in ("chicago", "new york city", "washington"):
       print("Please choose a city: chicago, new york city or washington")
       city = input("Which city (chicago, new york city, washington) would you like to analyze? ")
```

Get the necessary date-formatting using pandas library:
```
df['Start Time'] = pd.to_datetime(df["Start Time"])
df['month'] = df['Start Time'].dt.month
````
Get the filtered data with 'where' function from library. Filter the before given user input.
```
if month != 'all':
    df = df.where(df['month'] == month_dict[month])
```

Get the most values with 'mode' function:
```
most_common_month = month_dict[int(df['month'].mode()[0])]
print("The most common month is: {}".format(most_common_month))
```

Get different statisticial data using 'sum', 'mean', 'value_counts', 'min', 'max' etc.
```
total_travel_time = pd.to_timedelta(df['Trip Duration'].sum(), unit = 's')
total_mean_time = pd.to_timedelta(df['Trip Duration'].mean(), unit = 's')
```

Get the first 5 rows of the data. Let the user interact if he wants to see 5 more rows:
```
start_loc = 0
while (view_data == 'yes'):
    print(df.iloc[start_loc : start_loc + 5])
    start_loc += 5
    view_data = input('Do you wish to continue? Enter yes or no. ').lower()
    if view_data == 'no':
        break
```