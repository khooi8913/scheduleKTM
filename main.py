import argparse
import time
import stations #To be integrated
import trains

def today_date():
    return time.strftime('%d-%b-%Y').upper()

def main():
    parser = argparse.ArgumentParser('Simple KTM Schedule & Availability Retriever')
    parser.add_argument('-o','--origin',required=True,help='Origin Code')
    parser.add_argument('-d','--destination',required=True,help='Destination Code')
    parser.add_argument('-t1','--date1', default=today_date(), help='Date (e.g. Format "31-AUG-2017"')
    # parser.add_argument('-r','--return', default=False, help='Return Trip')
    # parser.add_argument('-t2','--date2', help='Return Trip Date')

    args = parser.parse_args()
    # print (args.origin, args.destination, args.date1)
    print ('Trains from',args.origin,'to',args.destination,'on',args.date1,':')
    trains.display_available_trains(str(args.origin), str(args.destination), args.date1)
if __name__ == '__main__':
    main()
