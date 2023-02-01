import pandas as pd
import geopy.geocoders as gg
import os 


geolocator = gg.Nominatim(user_agent="your email or app name goes here")
new_address = input("Please enter the address you would like to check: ")
location = geolocator.geocode(new_address)
new_lat = location.latitude
new_long = location.longitude 
print(new_lat, new_long)

i = int(input("Which row is this going to?"))


def convertLat(i):
    df = pd.read_csv("St_Marxer_Spreadsheet.csv", sep = ";")
    df.loc[i, 'decimal(8,6) latitude'] = new_lat
    df.to_csv("St_Marxer_Spreadsheet.csv")
    print(new_lat)

def convertLong(i): 
    df = pd.read_csv("St_Marxer_Spreadsheet.csv", sep = ";")
    df.loc[i, 'decimal(9,6) longitude'] = new_long
    df.to_csv("St_Marxer_Spreadsheet.csv")
    print(new_long)
        
convertLat(i)
convertLong(i)