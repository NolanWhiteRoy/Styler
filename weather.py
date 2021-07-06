import json, requests
import os

#Function to get weather data from location
def weather_info(country_input, state_input, city_input):
    #Search for the correct state code and country code according to the user's input
    with open('iso.json', encoding="utf8") as file:
        data = json.load(file)
        key_list = list(data.keys())
        val_list = list(data.values())
        for val in val_list:
            #search for country code
            dict_val = dict(val)
            if dict_val['name'] == country_input:
                country_index = val_list.index(val, 0, len(val_list))
                country_code = key_list[country_index]
            division_keys_list = list(dict_val['divisions'].keys())
            division_values_list = list(dict_val['divisions'].values())
            for state in dict_val['divisions']:
                #search for state code
                if dict_val['divisions'][state].startswith(state_input):
                    state_index = division_values_list.index(dict_val['divisions'][state], 0,
                    len(division_values_list))
                    state_substring = division_keys_list[state_index]
                    state_code = state_substring[3:]
#Create api url using state and country code
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    API_KEY = os.getenv("API_KEY")

    try:
        URL = BASE_URL + "q=" + city_input + "," + state_code + "," + country_code + "&appid=" + API_KEY
        
        response = requests.get(URL)

        if response.status_code == 200:
            path = 'weatherdata.json'
            data = response.json()
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)
            main = data['main']
            temperature = round(main['temp'] - 273)
            feels_like = round(main['feels_like'] - 273)
            report = data['weather']
            weather_id = report[0]['id']
            wind = data['wind']
            speed = wind['speed'] * 3.6
            degree = wind['deg']
            direction = ""
            #generate the degree of wind
            if 0 <= degree <= 22.5:
                direction = "N"
            elif 22.5 < degree < 67.5:
                direction = "NE"
            elif 67.5 <= degree <= 112.5:
                direction = "E"
            elif 112.5 < degree < 157.5:
                direction = "SE"
            elif 157.5 <= degree <= 202.5:
                direction = "S"
            elif 202.5 < degree < 247.5:
                direction = "SW"
            elif 247.5 <= degree <= 292.5:
                direction = "W"
            elif 292.5 < degree < 337.5:
                direction = "NW"
            elif 337.5 <= degree <= 360:
                direction = "N"

            wind_value = direction + " " + str(round(speed)) + "km/h"
            list_values = [temperature, wind_value, weather_id, report[0]['description'], feels_like]
            return list_values
        else:
            # showing the error message
            print("Error in the HTTP request")
    except:
        print("An error has occurred, please check your values and their spelling!")