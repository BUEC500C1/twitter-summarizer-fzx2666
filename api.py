import requests
import json
import airport_codes_flow
import csv

def jprint(obj):
    data = json.dumps(obj, sort_keys=True, indent=4)
    print(data)

def req():
    csvFilePath = open('airport_codes.csv', encoding='utf-8', errors='ignore')
    fieldnames = (
    "ident", "type", "name", "elevation", "continent", "iso_country", "iso_region", "municipal", "gps_code",
    "iata_code", "local_code", "coordinates")
    reader = csv.DictReader(csvFilePath, fieldnames, restval=None, dialect='excel')
    coordinates,name,continent,country = [],[],[],[]
    for row in reader:
        coordinates.append(row['coordinates'].replace(" ",''))
        name.append(row['name'])
        continent.append(row['continent'])
        country.append(row['iso_country'])
    api_points = "https://api.weather.gov/points/"+coordinates[2]
    response = requests.get(api_points)
    response = response.json()
    if
    print(response["properties"]["forecast"])
    forecast_info = requests.get(response["properties"]["forecast"])
    forecast_info = forecast_info.json()
    jprint(forecast_info)


if __name__ == '__main__':
    req()
