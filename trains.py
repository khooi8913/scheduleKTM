import requests
import re

BASE_URL = 'https://intranet.ktmb.com.my/e-ticket'

def get_train_url(ORIGIN, DESTINATION, DATE):
    '''
    :param ORIGIN: Origin Station Code
    :param DESTINATION: Destination Station Code
    :param DATE: Date Formatted in (DD-MMM-YYYY)
    :return: URL for Schedule Retrieval
    '''
    return BASE_URL + '/Ajax/GetTrainList.aspx?Origin='+ORIGIN+'&Destination='+DESTINATION+'&Tarikh='+DATE

def get_coach_url(ORIGIN, DESTINATION, DATE, TRAIN):
    '''
    :param ORIGIN: Origin Station Code
    :param DESTINATION: Destination Station Code
    :param DATE: Date Formatted in (DD-MMM-YYYY)
    :param TRAIN: Train Number
    :return: URL for Train Coach Details Retrieval
    '''
    return BASE_URL + '/Ajax/CoachList.aspx?Jalan=O&Origin='+ORIGIN+'&Destination='+DESTINATION+'&Train='+TRAIN+'&Tarikh='+DATE

def display_available_trains(ORIGIN, DESTINATION, DATE):
    '''
    :param ORIGIN: Origin Station Code
    :param DESTINATION: Destination Station Code
    :param DATE: Date Formatted in (DD-MMM-YYYY)
    :return: List of Trains with Details
    '''
    trains = requests.get(get_train_url(ORIGIN,DESTINATION,DATE))
    print (trains.text)
    trains = trains.json()
    print (trains)
    complete_schedule = []

    for i, train in enumerate(trains):
        train_number = train['TMT_TNM_NUMBER']
        train_name = train['TNM_NAME']
        train_departure_time = train['Departure'][-5:]
        train_arrival_time = train['Arrival'][-5:]

        coaches = requests.get(get_coach_url(ORIGIN,DESTINATION,DATE,train_number))

        avail_num = re.findall('<td>Availbility</td><td>:</td><td>(\S+)</td>', coaches.text)
        coach_availability = max(avail_num)

        complete_schedule.append({'tNum':str(train_number), 'tName':train_name, 'tDepart':train_departure_time, 'tArrive':train_arrival_time, 'tAvail':coach_availability})
    return complete_schedule
