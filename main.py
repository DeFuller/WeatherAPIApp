import requests

api_key = "ecc443e9a03101c3cd788b91e96ccb83"

"""
The main function runs an infinite loop: 
    prompting the user for input (city or zip code)
    then presenting the data
    then prompting the user for a response on whether to repeat
"""


def main():
    while True:
        # Prompt user for a valid City or ZIP code
        locale = input("Please enter a valid city or ZIP code: ")
        # Capture the locale into the request link
        link = f"https://api.openweathermap.org/data/2.5/forecast?appid={api_key}&q={locale}"

        # get response
        response = get_data(link)

        # if the request was unsucclessful continue the loop
        if response:
            present_data(response)

        rerun = input("Rerun loop? (y/n) : ")
        if not rerun.lower().startswith("y"):
            print("Bye!")
            break


"""
This fucntion sends a GET request using the requests library
The input validity is determined by the response
    a 404 means the user messed up the city/zip prompt
It returns the JSON data from the server as a dict in case the request was successfully made
An error warning is issued in case the request was not sent at all
"""


def get_data(link):

    # Send a GET request from the openweathermap servers
    try:
        print(f"Connecting to server : req = {link}")
        r = requests.get(link)

        # if the response is invalid, return False
        if r.status_code != 200:
            # Handle invalid city
            if r.status_code == 404:
                print(f"Invalid data input: {r.json()['message']}")
            else:
                print(r.json()['message'])
            return False

        # if the response is valid data, return the reponce JSON data as a dictionery
        return r.json()

    # if an error occured return False
    except:
        print("Server connection was unsuccessful")
        return False


"""
This function draws 2 tables
    City Information
        City name and country
        City coordinates (longitude|latitude)
    Weather Forecast in 3 hour intervals
        time | short description | temperature | humidity | wind speeds | long description
"""


def present_data(data):

    # city information
    city = f" City    >>  {data['city']['name']}, {data['city']['country']}"
    coord = f" lat|lon >>  {data['city']['coord']['lat']}|{data['city']['coord']['lon']}"
    # generate spacer pattern and print the header
    spacer = "+" + ("-" * (max(len(city), len(coord)) - 1)) + "+"
    print("\n" + spacer)
    print(city)
    print(coord)
    print(spacer + "\n")

    # forecast table
    # format at table head
    header = " Time                   Weather         Temp(K)         Humidity        Wind Speeds     Description "
    spacer = "+" + "-" * len(header) + "+"
    print(spacer)
    print(header)
    print(spacer)

    # print rows
    for forecast in data["list"]:
        time = forecast['dt_txt']  # time forcasted
        weather = forecast['weather'][0]['main']  # short weather description
        # long description
        weather_desc = forecast['weather'][0]['description']
        temp = forecast['main']['temp']  # average temperature in Kelvin
        humidity = forecast['main']['humidity']  # humidity level
        wind = forecast['wind']['speed']  # wind speeds

        print(
            f" {time}\t{weather}\t\t{temp}\t\t{humidity}\t\t{wind}\t\t{weather_desc}")

    print(spacer + "\n")


main()
