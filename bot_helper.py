import stations
import trains

def list_of_states():
    str_states = 'List of States:\n'
    for counter, states in enumerate(stations.STATIONS):
        str_states += str(counter+1) + ' ' + states + '\n'
    return  str_states

def list_station(STATE):
    try:
        list_stations = stations.display_stations(STATE)
        if list_stations == None:
            return 'ERROR: Invalid parameter entered!'
        else:
            str_station = 'List of stations in ' + STATE + ': \n'
            for counter, station in enumerate(list_stations):
                str_station += str(counter+1) + ' ' + station['Nama'] + ' ' + station['Code'] + '\n'
            return str_station
    except KeyError:
        return 'ERROR: Unexpected Error Occurred!'

def list_train(ORIGIN, DESTINATION, DATE):
    try:
        list_trains = trains.display_available_trains(ORIGIN,DESTINATION,DATE)
        print (list_trains)
        if list_trains == []:
            return 'ERROR: No data available.'
        else:
            str_train = 'Trains from ' + stations.get_station_name(ORIGIN) + ' to ' + stations.get_station_name(DESTINATION) + ' on ' + DATE.upper() + ':\n'
            for counter, train in enumerate(list_trains):
                str_train += str(counter+1) + ' ' + train['tNum'] + ' ' + train['tName'] + ' Depart:' + train['tDepart'] + ' Arrive:' + train['tArrive'] + ' Availability:' + train['tAvail'] + '\n\n'
            return str_train
    except KeyError:
        return 'ERROR: Unexpected Error Occurred!'