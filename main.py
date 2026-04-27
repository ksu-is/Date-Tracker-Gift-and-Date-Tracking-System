import csv
from datetime import datetime, timedelta

# Create Lists
names = []
dates = []
gifts = []
events = []

# Save information for future use
def save_data():
    with open('profile_database.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in zip(names, dates, events, gifts):
            writer.writerow(row)

# Pull data
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
        pass

# Setup alter notice
def date_warning():
    # additional date gets rid of time
    today = datetime.now().date()
    print("Checking Upcoming Events >>>>>>>")
    
    for d in range(len(dates)):
        this_year = today.year
        date_str = dates[d] + "/" + str(this_year)
        try:
            # additional date gets rid of time
            event_date = datetime.strptime(date_str, "%m/%d/%Y").date()
            
            time_diff = event_date - today
            days_left = time_diff.days
            
            if days_left == 0:
                print("TODAY: " + names[d] + " has a " + events[d] + "!")
            elif 0 < days_left <= 7:
                print("REMINDER: " + names[d] + "'s " + events[d] + " is in " + str(days_left) + " days.")
        except:
            pass 

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
        name_input = input("Enter Full Name: ")
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
        search = input("Enter Name: ")
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
        search = input("Who is this gift for? ")
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
        search = input("Name being updated: ")
        if search in names:
            n = names.index(search)
            new_name = input("Enter updated name: ")
            names[n] = new_name
            save_data()
            print("Name Updated.")
        else:
            print("PROFILE NOT FOUND")

    elif user_select == "5":
        search = input("Name of the profile to DELETE: ")
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