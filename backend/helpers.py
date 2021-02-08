def prepareSearchData(data):
    search_object = handleSearchData(data)
    return {
        'search_object': search_object,
        'result_object': getLastSearch(search_object)
    }


def handleSearchData(data):
    return {
        'city'               : data['name'],
        'long'               : int(data['coord']['lon']),
        'lat'                : int(data['coord']['lat']),
        'weather_main'       : data['weather'][0]['main'],
        'weather_description': data['weather'][0]['description'],
        'weather_icon'       : data['weather'][0]['icon'],
        'temperature'        : int(data['main']['temp']),
        'feels_like'         : int(data['main']['feels_like']),
        'temp_min'           : int(data['main']['temp_min']),
        'temp_max'           : int(data['main']['temp_max']),
        'pressure'           : int(data['main']['pressure']),
        'humidity'           : int(data['main']['humidity']),
        'visibility'         : int(data['visibility']),
        'wind_speed'         : int(data['wind']['speed']),
        'wind_deg'           : int(data['wind']['deg']),
        'clouds'             : int(data['clouds']['all'])
    }


def getLastSearch(search):
    return {
        'id'                 : search.get('id', ''),
        'city'               : search['city'],
        'long'               : search['long'],
        'lat'                : search['lat'],
        'weather_main'       : search['weather_main'],
        'weather_description': search['weather_description'],
        'weather_icon'       : search['weather_icon'],
        'temperature'        : search['temperature'],
        'feels_like'         : search['feels_like'],
        'temp_min'           : search['temp_min'],
        'temp_max'           : search['temp_max'],
        'pressure'           : search['pressure'],
        'humidity'           : search['humidity'],
        'visibility'         : search['visibility'],
        'wind_speed'         : search['wind_speed'],
        'wind_deg'           : search['wind_deg'],
        'clouds'             : search['clouds']
    }

    
def kelvinToCelsius(temp):
    return round(temp - 273.15)

