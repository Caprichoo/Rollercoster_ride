print("Welcome to Roller-coaster Ride")
height = float(input("What's your height in cms.? "))
bill = 0

if height >= 120:
    print("Can ride")

    age = int(input("What's your age? "))
    if age < 12:
        bill = 5
        print(f'bill ${bill}')
    if age <= 18:
        bill = 7
        print(f'bill ${bill}')
    else:
        bill = 12
        print(f'bill ${bill}')

    want_photos = input("Do you want photos? Y or N ? ")
    if want_photos == 'Y':
        bill += 3
        print(f"Your final bill is {bill}:  $")

else:
    print("Can't ride")
