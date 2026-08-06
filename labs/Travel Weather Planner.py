#creating all required variable and assigning Boolean value
distance_mi = 2
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

if distance_mi <= 0:
    print('False')
elif distance_mi <= 1:
    if is_raining == False:
        print('True')
    else:
        print('False')
elif distance_mi <= 6:
    if has_bike == True and is_raining == False:
        print('True')
    else:
        print('False')
elif distance_mi > 6:
    if has_ride_share_app == True:
        print('True')
    elif has_car == True:
        print('True')
    else:
        print('False')
else:
    pass

