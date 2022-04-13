# Lufthansa_airline
 get nearest airport info and find all flight from that airport with terminals
 notes: change {'Authorization': 'Bearer {Your_API_token}'} with your access token from lufthansa get api token.
 if Time provided is in future(eg 2022-04-15)but today is (2022-04-14) use this code on function terminalTime()
                        arrival_time
 status['Arrival']['EstimatedTimeLocal'] ['DateTime']
 else if past use
 status['Arrival']['ActualTimeLocal'] ['DateTime']


 if key error occours , remove the key and print the value  and find the right one to use

