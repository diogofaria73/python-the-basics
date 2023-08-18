athletes_infos = []
continue_asking = True
want_to_calculate_average_note_by_athlete = False

while continue_asking != False:
    skater_name = input('Enter skater name: ')
    skater_note = float(input('Enter skater note: '))
    athletes_infos.append([skater_name, skater_note])
    continue_asking = input('Do you want to continue? [Y/n]: ').lower() == 'y'

    if continue_asking == False:
        want_to_calculate_average_note_by_athlete = input(
            'Do you want to see the average note by athlete? [Y/n]: ').lower() == 'y'

        if want_to_calculate_average_note_by_athlete == True:
            for athlete in athletes_infos:
                athlete_name = athlete[0]
                athlete_note = athlete[1]
                print(
                    f'{athlete_name} average note is: {athlete_note / len(athletes_infos)}')
        break
