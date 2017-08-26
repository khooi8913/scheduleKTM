import requests
import json

STATION_LIST = 'https://intranet.ktmb.com.my/e-ticket/Ajax/GetOriginDest.aspx?Param=function () {    var e = new Date;    var t = e.getDate();    var n = e.getMonth();    var r = e.getFullYear();    var i = new Date;    var s = i.getHours();    var o = i.getMinutes();    var u = i.getSeconds();    if (o < 10) o = "0" + o;    var a = t + n + r + s + o + u;    return a}&_=1503752251659'

def stations():
    '''
    :return: JSON containing all the stations in all states
    '''
    response = requests.get(STATION_LIST)
    response = json.loads(response.text)
    return response

def display_all_stations():
    '''
    :return: Displays all the available stations
    '''
    stations_all_states = stations()
    for states in stations_all_states:
        display_stations(states, stations_all_states)

def display_stations(STATE, STATIONS=stations()):
    '''
    :param STATE: Complete name of the desired state
    :return: Displays the available stations in the specified state
    '''
    try:
        stations_all_states = STATIONS
        stations_specified_state = stations_all_states[STATE.upper()]

        print ('Stations in',STATE,':')

        for i, station in enumerate(stations_specified_state):
            print ('%2d %-25s (%5s)' % (i+1, station['Nama'], station['Code']))
    except KeyError:
        print ('Invalid state entered!')

# display_all_stations()