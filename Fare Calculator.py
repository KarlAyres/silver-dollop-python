#Fare prices and distance thresholds
fare1 = float(3.61)
fare1_distance = int(10)
fare2 = float(4.48)
fare2_distance = int(20)
fare3 = float(5.15)
fare3_distance = int(35)
fare4 = float(6.89)
fare4_distance = int(65)
fare5 = float(8.86)

#Fare cap limits
cap_limit_weekday = float(16.10)
cap_limit_weekend = float(8.05)

#Off-peak fare price modifier
offpeak_modifier = float(0.7)

#On-peak travel times
onpeak_morning_start = str('0630')
onpeak_morning_finish = str('1000')
onpeak_afternoon_start = str('1500')
onpeak_afternoon_finish = str('1900')

#Initialise accumulator variable
subtotal_trip_fare = 0

#Prompt user for travel day
travel_day = input('Enter the travel day: ')
#Input validation
while travel_day not in ['Monday', 'monday', 'Tuesday', 'tuesday', 'Wednesday', 'wednesday', 'Thursday', 'thursday', 'Friday', 'friday', 'Saturday',
                         'saturday', 'Sunday', 'sunday']:
    print('ERROR: Enter a valid travel day')
    travel_day = input('Enter the travel day: ')
    
#Prompt user for number of trips
number_of_trips = int(input('Enter the number of trips: '))
#Input validation
while number_of_trips <=0:
    print('ERROR: Enter a valid number of trips')
    number_of_trips = int(input('Enter the number of trips: '))

#Prompt user for individual trip details
for trip in range(1, number_of_trips+1):
    #Trip start time
    start_time = str(input('Enter trip (' + str(trip) + ') start time (HHMM): '))
    #Input validation
    while start_time < str(0) or start_time > str(2400):
        print('ERROR: Enter a valid start time')
        start_time = str(input('Enter trip (' + str(trip) + ') start time (HHMM): '))
    #Trip end time
    end_time = str(input('Enter trip (' + str(trip) + ') end time (HHMM): '))
    #Input validation
    while end_time < str(0) or end_time > str(2400):
        print('ERROR: enter a valid end time')
        end_time = str(input('Enter trip (' + str(trip) + ') end time (HHMM): '))
    #Trip distance
    trip_distance = int(input('Enter trip (' +str(trip) + ') distance (km): '))
    #Input validation
    while trip_distance <= 0:
        print ('ERROR: Enter a valid trip distance')
        trip_distance = int(input('Enter trip (' +str(trip) + ') distance (km): '))
        
    #Display formatting
    print('\t')
       
    #Determine which fare to apply    
    if trip_distance <= fare1_distance:
        subfare = fare1
    elif trip_distance <= fare2_distance:
        subfare = fare2
    elif trip_distance <= fare3_distance:
        subfare = fare3
    elif trip_distance <= fare4_distance:
        subfare = fare4
    elif trip_distance > fare4_distance:
        subfare = fare5
     
    #Determine if on or off peak apply modifier if necessary
    if travel_day not in ['Saturday', 'saturday', 'Sunday', 'sunday'] and onpeak_morning_start < start_time < onpeak_morning_finish or onpeak_afternoon_start < start_time < onpeak_afternoon_finish:      
        travel_time = 'peak'
        trip_fare = subfare
    else:
        travel_time = 'off peak'
        trip_fare = subfare * offpeak_modifier
        
    #Display individual trip details
    print('-- Trip (', trip,') - ', trip_distance, 'km, ', travel_time, ': $', format(trip_fare, ".2f"), sep='') 
    print('\t')
    
    #Accumulator
    subtotal_trip_fare += trip_fare

#Display fare summary
print('---------------------------------')
print('Fare Summary:')
print('\t')
print('Subtotal: $', format(subtotal_trip_fare, ".2f"), sep='')

#Determine which fare cap limit to apply
if travel_day in ['Monday', 'monday', 'Tuesday', 'tuesday', 'Wednesday', 'wednesday', 'Thursday', 'thursday', 'Friday', 'friday'] and subtotal_trip_fare >= cap_limit_weekday:
    print('Daily cap reached.')
    print('\t')
    print('Total fare: $16.10')

elif travel_day in ['Saturday', 'saturday', 'Sunday', 'sunday'] and subtotal_trip_fare >= cap_limit_weekend:
    print('Daily cap reached.')
    print('\t')
    print('Total fare: $8.05')

#Display total fare details
else:
    print('Total fare: $', format(subtotal_trip_fare, ".2f"), sep='')

#Display formatting
print('\t')

#Display end message
print('---------------------------------')
print('\t')
print('Have a nice day!')