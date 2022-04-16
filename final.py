import requests

# change this auth key
Authentication_key = {'Authorization': 'Bearer wyg2rd58f2jqdmb29bysqge'}


# calculating nearest airports
def Nearst_airport(Auth_key):
    latitude = 51.1657   
    longitude = 10.4515

    # api parameters
    Endpoint = 'https://api.lufthansa.com/v1'
    Near_airport = f'references/airports/nearest/{latitude},{longitude}'

    # request and response of endpoints
    req = requests.get(f'{Endpoint}/{Near_airport}', headers=Auth_key)
    response = req.json()
    airport = response['NearestAirportResource']['Airports']['Airport']

    list1 = []
    for i in range(5):
        airport_name = airport[i]['AirportCode']
        list1.append(airport_name)
    return list1  # a list of nearest airport codes.


# calling nearest airport fucntion
Airport_list = Nearst_airport(Auth_key=Authentication_key)


def terminalTime(Airports, Auth_key):
    Time = '2022-04-17T00:00'  # input time to calculate
    Endpoint = 'https://api.lufthansa.com/v1'
    for item in Airports:
        flight_status = f'operations/flightstatus/departures/{item}/{Time}'
        req1 = requests.get(f'{Endpoint}/{flight_status}', headers=Auth_key)
        if 199 < req1.status_code < 300:  # if flight code is success.
            response1 = req1.json()
            status = response1['FlightStatusResource']['Flights']['Flight'][0]
            Departure_airport = status['Departure']['AirportCode']
            AAirport_code = status['Arrival']['AirportCode']
            try:
                arrival_time = status['Arrival']['ActualTimeLocal']
                A_terminal = status['Arrival']['Terminal']
            except KeyError:
                A_terminal="N/A"
                arrival_time=status['Arrival']['ScheduledTimeLocal']

            print(
                f'Departed from {Departure_airport} and arrival airport code is {AAirport_code} in Terminal {A_terminal} on {arrival_time}')

        else:
            print(
                f'no flight of lufthansa airline from {item} Airport on given date')

