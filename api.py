import requests
import json
import airport_codes_flow
import csv

def jprint(obj):
    data = json.dumps(obj, sort_keys=True, indent=4)
    print(data)

def req():
    air1 = input("Departure: ")
    air2 = input("Arrival: ")
    csvFilePath = open('airport_codes.csv', encoding='utf-8', errors='ignore')
    fieldnames = ("ident", "type", "name", "elevation", "continent", "iso_country", "iso_region", "municipal", "gps_code",
                  "iata_code", "local_code", "coordinates")
    reader = csv.DictReader(csvFilePath, fieldnames, restval=None, dialect='excel')
    coordinates,name,continent,country = [],[],[],[]
    for row in reader:
        coordinates.append(row['coordinates'].replace(" ",''))
        name.append(row['name'])
        continent.append(row['continent'])
        country.append(row['iso_country'])

    search_coor_dep = coordinates[name.index(air1)]
    search_coor_arr = coordinates[name.index(air1)]
    api_points_dep = "https://api.weather.gov/points/"+search_coor_dep
    api_points_arr = "https://api.weather.gov/points/"+search_coor_arr
    response_dep = requests.get(api_points_dep)
    response_arr = requests.get(api_points_arr)
    response_dep = response_dep.json()
    response_arr = response_arr.json()
    if "properties" not in response_dep: print('Your departure airport is not found.')
    elif "properties" not in response_arr: print('Your arrival airport is not found.')
    else:
        forecast_info_dep = requests.get(response_dep["properties"]["forecast"])
        forecast_info_dep = forecast_info_dep.json()
        forecast_info_arr = requests.get(response_arr["properties"]["forecast"])
        forecast_info_arr = forecast_info_arr.json()
    print('What information are you looking for? Please Enter following selections:')
    detail = input('temperature windSpeed windDirection shortForecast detailedForcast\n')
    print('The information of departure airport')
    for i in range(13):
        print(forecast_info_dep['properties']['periods'][i]['name']+": ", end = '')
        print(forecast_info_dep['properties']['periods'][i][detail])
    print('\nThe information of arrival airport')
    for i in range(13):
        print(forecast_info_dep['properties']['periods'][i]['name'] + ": ", end='')
        print(forecast_info_dep['properties']['periods'][i][detail])

if __name__ == '__main__':
    req()
