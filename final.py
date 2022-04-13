import requests

#calculating nearest airports
def Nearst_airport():
    latitude=28.4504
    longitude=77.2837

#api parameters
    Endpoint='https://api.lufthansa.com/v1'
    Near_airport=f'references/airports/nearest/{latitude},{longitude}'
    Auth_key={'Authorization': 'Bearer 8mw94bekyew3ba9phmns37zs'}

#request and response of endpoints
    req=requests.get(f'{Endpoint}/{Near_airport}', headers=Auth_key)
    response=req.json()
    airport=response['NearestAirportResource']['Airports']['Airport']
    list1=[]
    for i in range(5):
        airport_name=airport[i]['AirportCode']
        list1.append(airport_name)
    return list1	#a list of nearest airport codes.

Airports=Nearst_airport()   #calling nearest airport fucntion

def terminalTime(Airports):
    Time='2022-04-12T00:00'	#input time to calculate
    Endpoint='https://api.lufthansa.com/v1'
    Auth_key={'Authorization': 'Bearer 8mw94bekyew3ba9phmns37zs'}
    for item in Airports:
        flight_status=f'operations/flightstatus/departures/{item}/{Time}'
        req1=requests.get(f'{Endpoint}/{flight_status}', headers=Auth_key)
        if 199<req1.status_code<300: # if flight code is success.
            response1=req1.json()
            status=response1['FlightStatusResource']['Flights']['Flight'][0]

            AAirport_code=status['Arrival']['AirportCode']
            A_terminal=status['Arrival']['Terminal']
            arrival_time=status['Arrival']['ActualTimeLocal'] ['DateTime']	#change this to status['Arrival']['EstimatedTimeLocal'] ['DateTime'] if you input future time 
            print(f'arrival airport code is {AAirport_code} in Terminal {A_terminal} on date,time{arrival_time}')

        else:
            print(f'no flight of lufthansa airline from {item} Airport on given time') 
terminalTime(Airports)

