def prepare_search_data(data):
    search_object = handle_search_data(data)
    return_object = {
        'search_object': search_object,
        'result_object': get_last_search(search_object)
    }
    return return_object

def handle_search_data(data):
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

def get_last_search(search):
    return {
        'city': search['city'],
        'weather': search['weather_main'],
        'temperature': search['temperature'],
        'icon': search['weather_icon']
    }

    
def kelvinToCelsius(temp):
    return temp - 273.15