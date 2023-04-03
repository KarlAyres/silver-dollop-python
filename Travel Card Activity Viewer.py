"""
    The program keeps a log of activity on a travel card. The activity is read from a text file
    and records are pulled as requested. Activity includes travel times, tap on/off, stations
    travelled, and balance.
"""

# Intialise empty lists to remove duplicates
cards_no_dupes = []
stations_no_dupes = []

# Prompt user for log file
print('Travel Card Activity Viewer')
print('---------------------------')
travel_card_log_file = input('Enter the travel card log file name: ')

# Open and verify file
try:
    card_log = open(travel_card_log_file, 'r')

# Exception handler
except FileNotFoundError:
    travel_card_log_file = input('File not found, please enter a valid card log file name: ')
    card_log = open(travel_card_log_file, 'r')

# Process file and create variable for number of lines
num_lines = len(card_log.readlines())

# Initialise file format variable for file validation
file_format = 'correct'

# Interpret records into a master list, and validate file format
card_log = open(travel_card_log_file, 'r')
card_log_list = []
for line in card_log:
    record = line.split(',')
    if file_format == 'correct':
        if len(record) != 5:
            file_format = 'incorrect'
        elif record[0] < str(1000000) or record[0] > str(1899999):
            file_format = 'incorrect'
        elif record[1] < str(0) or record[1] >= str(24):
            file_format = 'incorrect'
        elif record[2] not in ['on', 'off', ]:
            file_format = 'incorrect'
        else:
            card_id = record[0].strip()
            time_on = record[1].strip()
            tap = record[2].strip()
            suburb = record[3].strip()
            balance = record[4].strip()
            card_log_list.append([card_id, time_on, tap, suburb, balance])

# Close the file
card_log.close()


# 'All Activity' user menu function
def user_all_activity():
    # Display menu formatting
    print('All Activity:')
    print('==================================================')
    print('Card    Time  Tap   Station         Balance')
    print('--------------------------------------------------')

    # Display all card activity
    for line in range(num_lines):
        print('{:1} {:2} {:5} {:15} ${}'.format(card_log_list[line][0], card_log_list[line][1], card_log_list[line][2],
                                                card_log_list[line][3], card_log_list[line][4]))


# Return a list of records matching a chosen card number
def card_list_func(number):
    # Initialise empty list
    cards = []

    # Loop over master list, appending cards list with matching records
    for card_record in range(num_lines):
        if card_log_list[card_record][0] == number:
            cards.append(card_log_list[card_record])
    return cards


# 'Cards' user menu function
def user_card():
    # Create list of card numbers, removing duplicates
    for line in range(num_lines):
        if card_log_list[line][0] not in cards_no_dupes:
            cards_no_dupes.append(card_log_list[line][0])

    # Display formatting
    print('Cards')
    print('-------')

    # Display card numbers
    for line in cards_no_dupes:
        print(line)

    # Initiate a variable for the while loop
    keep_going = 'y'

    # While loop condition
    while keep_going != 'n':

        # Prompt user for a card number
        card_number = input('Enter a card number: ')

        # Call the card_list_func to return a list of matching card numbers
        matching_cards = card_list_func(card_number)

        # Display matching records
        if len(matching_cards) >= 1:
            print('Card Activity [', card_number, ']')
            print('==================================================')
            print('Card    Time  Tap   Station         Balance')
            print('--------------------------------------------------')

            for card_record in matching_cards:
                print('{:1} {:2} {:5} {:15} ${}'.format(card_record[0], card_record[1], card_record[2], card_record[3],
                                                        card_record[4]))

            # Prompt user if they wish to enter another card number
            keep_going = input('Do you wish to enter another card number? (y/n): ')

        else:
            # If no matching cards, reprompt or exit to main menu
            keep_going = input('No matching cards, do you wish to enter another card number? (y/n): ')


# Return a list of records matching a chosen station
def station_list_func(station):
    # Intialise empty list
    stations = []

    # Loop over master list, appending stations list with matching records
    for station_record in range(num_lines):
        if card_log_list[station_record][3] == station:
            stations.append(card_log_list[station_record])
    return stations


# 'Station' user menu function
def user_station():
    # Create list of stations, removing duplicates
    for line in range(num_lines):
        if card_log_list[line][3] not in stations_no_dupes:
            stations_no_dupes.append(card_log_list[line][3])

    # Display formatting
    print('Stations')
    print('----------')

    # Display stations
    for line in stations_no_dupes:
        print(line)

    # Intiate a variable for the while loop
    keep_going = 'y'

    # While loop condition
    while keep_going != 'n':

        # Prompt user for a station
        station = input('Enter a station: ')

        # Call the station_list_func to return a list of matching stations
        matching_stations = station_list_func(station)

        # Display matching records
        if len(matching_stations) >= 1:
            print('Station Activity [', station, ']')
            print('==================================================')
            print('Card    Time  Tap   Station         Balance')
            print('--------------------------------------------------')

            for station_record in matching_stations:
                print('{:1} {:2} {:5} {:15} ${}'.format(station_record[0], station_record[1], station_record[2],
                                                        station_record[3], station_record[4]))

            # Prompt user if they wish to enter another station
            keep_going = input('Do you wish to enter another station? (y/n): ')


        else:
            # If no matching stations, reprompt or exit to main menu
            keep_going = input('No matching stations, do you wish to enter another station? (y/n): ')


# Return a list of records matching a chosen time
def time_list_func(start_time, end_time):
    # Initialise empty list
    times = []

    # Loop over master list, appending times list with matching records
    for time_record in range(num_lines):
        if card_log_list[time_record][1] > start_time and card_log_list[time_record][1] < end_time:
            times.append(card_log_list[time_record])
    return times


# 'Time' user menu function
def user_time():
    # Initiate a variable for the while loop
    keep_going = 'y'

    # While loop condition
    while keep_going != 'n':

        # Prompt user for a start and end time
        start_time = input('Enter start time (HH): ')
        end_time = input('Enter end time (HH): ')

        # Call the times_list_func to return a list of matching times
        matching_times = time_list_func(start_time, end_time)

        # Display matching records
        if len(matching_times) >= 1:
            print('Time Activity [', start_time, ':00 to ', end_time, ':00]:', sep='')
            print('==================================================')
            print('Card    Time  Tap   Station         Balance')
            print('--------------------------------------------------')

            for time_record in matching_times:
                print('{:1} {:2} {:5} {:15} ${}'.format(time_record[0], time_record[1], time_record[2], time_record[3],
                                                        time_record[4]))

            # Prompt user if they wish to enter another time
            keep_going = input('Do you wish to enter another time? (y/n): ')

        else:
            # If no matching times, reprompt or exit to main menu
            keep_going = input('No matching times, do you wish to enter another time? (y/n): ')


# Main function
def main():
    # File format validation
    if file_format == 'incorrect':
        print('** Reading travel card data ...')
        print('** ERROR! File is not correctly formatted.')

    else:
        # Display information for correctly formatted file
        print('** Reading travel card data ...')
        print('** Success! Retrieved', num_lines, 'records\n')

        # Main menu formatting
        print('Activity menu')
        print('--------------')
        print('[A]ll\n[C]ard\n[S]tation\n[T]rip\n')

        # Prompt user to select a menu item
        activity_menu = input('> Select item or [Q]uit: ')

        # While loop condition to quit
        while activity_menu != 'q' and activity_menu != 'Q':

            # [A]ll activity
            if activity_menu == 'A' or activity_menu == 'a':
                user_all_activity()

            # [C]ard
            elif activity_menu == 'C' or activity_menu == 'c':
                user_card()

            # [S]tation
            elif activity_menu == 'S' or activity_menu == 's':
                user_station()

            # [T]
            elif activity_menu == 'T' or activity_menu == 't':
                user_time()

            # Invalid selection error
            else:
                print('\n> ERROR: Invalid selection')

            # Main menu formatting
            print('\nActivity menu')
            print('--------------')
            print('[A]ll\n[C]ard\n[S]tation\n[T]rip\n')
            activity_menu = input('> Select item or [Q]uit: ')

    # Display end message
    print('Have a nice day!')


main()
