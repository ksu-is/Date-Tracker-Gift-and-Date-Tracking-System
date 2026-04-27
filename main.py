# Holds previous data input from the user to read and write
import csv
# Datetime tool used to create alerts for upcoming events
from datetime import datetime, timedelta

# Create lists
names = []
dates = []
gifts = []
events = []

# Saves information in CSV filefor future use
def save_data():
    with open('profile_database.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in zip(names, dates, events, gifts):
            writer.writerow(row)

# Pull data from the CSV file
def data_pull():
    try:
        with open('profile_database.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                names.append(row[0])
                dates.append(row[1])
                events.append(row[2])
                gifts.append(row[3])
    except FileNotFoundError:
        pass # If no file start with blank 

# Setup alter notice
def date_warning():
    # Additional date gets rid of time (hours/min)
    today = datetime.now().date()
    print("Checking Upcoming Events >>>>>>>")
    
    for d in range(len(dates)):
        this_year = today.year
        date_str = dates[d] + "/" + str(this_year)
        try:
            # Converts string into calendar date
            event_date = datetime.strptime(date_str, "%m/%d/%Y").date()
            
            # Subtracts today from event date to see the difference
            time_diff = event_date - today
            days_left = time_diff.days
            
            # Triggers an alert if it is day of event
            if days_left == 0:
                print("TODAY: " + names[d] + " has a " + events[d] + "!")
            #Trigger alert if it is within 1-7 days of event
            elif 0 < days_left <= 7:
                print("REMINDER: " + names[d] + "'s " + events[d] + " is in " + str(days_left) + " days.")
        except:
            pass # Skips dates with incorrect format

data_pull()

date_warning()

running = True

while running:
    print("Date and Gift Tracker >>>>>>>")
    print("1. Add New Profile")
    print("2. Search Profile")
    print("3. Add/Update Gift Ideas")
    print("4. Update Name")
    print("5. Delete Profile")
    print("6. Exit")

    user_select = input("Select Option (1-6): ")

    if user_select == "1":
        
        # Ask user for input
        name_input = input("Enter Full Name: ").title()
        date_input = input("Enter Date (MM/DD): ")
        event_input = input("Type (Birthday/Anniversary/One-Time): ")
        gift_input = input("Enter Gift: ")

        names.append(name_input)
        dates.append(date_input)
        events.append(event_input)
        gifts.append(gift_input)
        
        save_data()
        print("New Profile Saved.")

    elif user_select == "2":
        search = input("Enter Name: ").title()
        if search in names:
            n = names.index(search)
            print("**** PROFILE FOUND ****")
            print("Name: " + names[n])
            print("Date: " + dates[n])
            print("Event: " + events [n])
            print("Gifts: " + gifts [n])
        else:
            print("PROFILE NOT FOUND.")

    elif user_select == "3":
        search = input("Who is this gift for? ").title()
        if search in names:
            n = names.index(search)
            print("Gift Ideas: " + gifts[n])
            new_gift = input("Enter new gift idea: ")
            gifts[n] = gifts[n] + ", " + new_gift
            save_data()
            print("Gifts Updated.")
        else:
            print("PROFILE NOT FOUND.")
        
    elif user_select == "4":
        search = input("Name being updated: ").title()
        if search in names:
            n = names.index(search)
            new_name = input("Enter updated name: ")
            names[n] = new_name
            save_data()
            print("Name Updated.")
        else:
            print("PROFILE NOT FOUND")

    elif user_select == "5":
        search = input("Name of the profile to DELETE: ").title()
        if search in names:
            n = names.index(search)
            
            confirm = input("Are you sure you want to delete " + names[n] + "? (yes/no): ")
            
            if confirm.lower() == "yes":
                names.pop(n)
                dates.pop(n)
                gifts.pop(n)
                events.pop(n)
                
                save_data() 
                print("PROFILE DELETED.")
            else:
                print("DELETE CANCELED.")
        else:
            print("PROFILE NOT FOUND.")        

    elif user_select == "6":
        print("EXITING.")
        running = False