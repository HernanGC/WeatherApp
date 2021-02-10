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


    
def kelvinToCelsius(temp):
    return round(temp - 273.15)

def decodeRequestBody(requestBody):
    return decodedRequestToString(requestBody.decode('utf-8'))

def decodedRequestToString(decodedRequest):
    return decodedRequest.replace('"', '')