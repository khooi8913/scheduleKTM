import requests
import json

BASE_URL = 'https://intranet.ktmb.com.my/e-ticket'

def get_station_url():
    '''
    :return: URL for Station List Retrieval
    '''
    return BASE_URL + '/Ajax/GetOriginDest.aspx?Param=function () {    var e = new Date;    var t = e.getDate();    var n = e.getMonth();    var r = e.getFullYear();    var i = new Date;    var s = i.getHours();    var o = i.getMinutes();    var u = i.getSeconds();    if (o < 10) o = "0" + o;    var a = t + n + r + s + o + u;    return a}&_=1503752251659'

def stations():
    '''
    :return: HashMap contain all states and stations
    '''
    response = requests.get(get_station_url())
    response = json.loads(response.text)
    return response

def display_stations(STATE):
    '''
    :param STATE: Name of desired state
    :param STATIONS: List of all stations
    :return: HashMap of a list of stations in the specified state
    '''
    STATE = STATE.upper()
    try:
        if STATE=='ALL':
            return STATIONS
        else:
            return STATIONS[STATE]
    except KeyError:
        print ('ERROR: Invalid state entered.')
        return None

def get_station_name(CODE):
    for states in STATIONS:
        for station in STATIONS[states]:
            if station['Code'] == CODE:
                return station['Nama']
    return 'INVALID STATION CODE'

STATIONS = stations()