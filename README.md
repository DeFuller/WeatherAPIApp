For your class project we will be creating an application to interact with a webservice in order to obtain data. Your program will use all of the information you’ve learned in the class in order to create a useful application.  
Your program must prompt the user for their city or zip code and request weather forecast data from https://openweathermap.org.  Your program must display the weather information in an READABLE format to the user.  

**Requirements:**   
- [x] Create a Python Application which asks the user for their zip code or city.
- [x] Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/  
- [x] Display the weather forecast in a readable format to the user.
- [x] Use comments within the application where appropriate in order to document what the program is doing.  
- [x] Use functions including a main function.  
- [x] Allow the user to run the program multiple times.
- [x] Validate whether the user entered valid data. If valid data isn’t presented notify the user.  
- [x] Use the Requests library in order to request data from the webservice.  
- [x] Use Python 3.  
- [x] Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.

**Project Notes**:  
- [x] Sign up for API Key http://openweathermap.org/appid  
- [x] The API key will look something similar to this: `d5751b1a9e2e4b2b8c7983646072da8b`
- [x] Make a connection to the API using the Requests library.


### Sample output

```sh
Please enter a valid city or ZIP code: New York
Connecting to server : req = https://api.openweathermap.org/data/2.5/forecast?appid=ecc443e9a03101c3cd788b91e96ccb83&q=New York

+---------------------------+
 City    >>  New York, US
 lat|lon >>  40.7143|-74.006
+---------------------------+

+----------------------------------------------------------------------------------------------------+
 Time                   Weather         Temp(K)         Humidity        Wind Speeds     Description 
+----------------------------------------------------------------------------------------------------+
 2022-04-27 18:00:00    Clouds          285.76          35              7.22            broken clouds
 2022-04-27 21:00:00    Clouds          285.14          35              8.89            broken clouds
 2022-04-28 00:00:00    Clouds          282.65          43              7.32            broken clouds
 2022-04-28 03:00:00    Clear           278.42          52              7.46            clear sky
 2022-04-28 06:00:00    Clear           276.87          54              7.48            clear sky
 2022-04-28 09:00:00    Clouds          276.06          60              7.68            broken clouds
 2022-04-28 12:00:00    Clouds          277.51          52              8.2             scattered clouds
 2022-04-28 15:00:00    Clouds          281.01          38              9.68            scattered clouds
 2022-04-28 18:00:00    Clouds          284.25          25              9.81            broken clouds
 2022-04-28 21:00:00    Clear           284.58          26              10.01           clear sky
 2022-04-29 00:00:00    Clear           282.25          33              8.39            clear sky
 2022-04-29 03:00:00    Clear           280.68          36              7.09            clear sky
 2022-04-29 06:00:00    Clear           279.31          40              6.37            clear sky
 2022-04-29 09:00:00    Clear           278.09          43              6.76            clear sky
 2022-04-29 12:00:00    Clear           278.5           41              8.04            clear sky
 2022-04-29 15:00:00    Clear           283.38          25              8.28            clear sky
 2022-04-29 18:00:00    Clear           287.59          19              8.56            clear sky
 2022-04-29 21:00:00    Clear           288.11          22              8.19            clear sky
 2022-04-30 00:00:00    Clear           285.62          32              7.01            clear sky
 2022-04-30 03:00:00    Clear           282.9           39              6.26            clear sky
 2022-04-30 06:00:00    Clear           281.41          41              4.49            clear sky
 2022-04-30 09:00:00    Clear           280.33          43              3.86            clear sky
 2022-04-30 12:00:00    Clear           281.36          42              3.54            clear sky
 2022-04-30 15:00:00    Clear           285.31          35              3.32            clear sky
 2022-04-30 18:00:00    Clear           288.77          31              2.91            clear sky
 2022-04-30 21:00:00    Clouds          290.16          33              2.83            broken clouds
 2022-05-01 00:00:00    Clouds          288.28          41              2.51            broken clouds
 2022-05-01 03:00:00    Clouds          286.09          47              0.72            few clouds
 2022-05-01 06:00:00    Clear           284.46          54              1.41            clear sky
 2022-05-01 09:00:00    Clear           283.08          58              2.29            clear sky
 2022-05-01 12:00:00    Clear           284.1           51              2.68            clear sky
 2022-05-01 15:00:00    Clouds          288.86          37              0.82            scattered clouds
 2022-05-01 18:00:00    Clouds          291.15          33              2.32            broken clouds
 2022-05-01 21:00:00    Clouds          290.44          39              5.76            broken clouds
 2022-05-02 00:00:00    Clouds          287.53          52              5.32            overcast clouds
 2022-05-02 03:00:00    Clouds          286.29          63              4.02            broken clouds
 2022-05-02 06:00:00    Clouds          285.87          66              2.9             broken clouds
 2022-05-02 09:00:00    Clouds          285.96          61              3.86            overcast clouds
 2022-05-02 12:00:00    Rain            285.02          89              4.52            light rain
 2022-05-02 15:00:00    Rain            285.73          96              3.35            moderate rain
+----------------------------------------------------------------------------------------------------+

Rerun loop? (y/n) : 
```
