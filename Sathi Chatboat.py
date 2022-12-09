from geopy.geocoders import Nominatim#importing geopy library
while True:#while loop so the whole code could be repeated
    #printing the home page 
    print("Welcome To Sathi ")
    print(1,"Emergency")
    print(2,"Emergency Detail's")
    #while loop for user so user can enter a valid input
    while True:
        user1 = int(input("Enter The S.no Of the above Output: "))
        if user1 == 1 or user1 == 2:
            break
        else:
            print("Enter 1 or 2")
            pass
    #coditional statement for Opting Emergency
    if user1 == 1:
        # calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")
        # entering the location name
        getLoc = loc.geocode("India")
        # printing address
        print(getLoc.address)
        # printing latitude and longitude
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)
        
    # coditional statement for Opting Emergency detail's  
    if user1 == 2:
        print("Emergency Telephone Numbers In India")
        a = "Gas leakage - 1906 \nTourist Helpline - 1363\nChild Helpline - 1098\nDisaster management - 104\nWomen Helpline - 181\nPolice - 100\nAmbulance - 108\nFire brigade - 101"
        print(a)
    #code to get out of the sathi app loop
    print("To Quit type Y/N")
    x = input().upper()
    if x == "Y":
        print("Thank you for Using sathi")
        break
    else:
        pass
    













