import requests
import re

BASE_URL = 'https://intranet.ktmb.com.my/e-ticket'

def get_train_url(ORIGIN, DESTINATION, DATE):
    return BASE_URL + '/Ajax/GetTrainList.aspx?Origin='+ORIGIN+'&Destination='+DESTINATION+'&Tarikh='+DATE

def get_coach_url(ORIGIN, DESTINATION, DATE, TRAIN):
    return BASE_URL + '/Ajax/CoachList.aspx?Jalan=O&Origin='+ORIGIN+'&Destination='+DESTINATION+'&Train='+TRAIN+'&Tarikh='+DATE

def display_available_trains(ORIGIN, DESTINATION, DATE):
    trains = requests.get(get_train_url(ORIGIN,DESTINATION,DATE))
    trains = trains.json()

    for i, train in enumerate(trains):
        train_number = train['TMT_TNM_NUMBER']
        train_name = train['TNM_NAME']
        train_departure_time = train['Departure'][-5:]
        # train_departure_time = train_departure_time[-5:]
        train_arrival_time = train['Arrival'][-5:]
        # train_arrival_time = train_arrival_time[-5:]

        coaches = requests.get(get_coach_url(ORIGIN,DESTINATION,DATE,train_number))
        avail_num = re.findall('<td>Availbility</td><td>:</td><td>(\S+)</td>', coaches.text)
        coach_availability = max(avail_num)
        print ('%2d %5s %-30s Depart:%-5s -t Arrival:%-5s Availability: %s' % (i+1, train_number, train_name, train_departure_time, train_arrival_time, coach_availability))

# display_available_trains('7300','19100','31-Aug-2017')