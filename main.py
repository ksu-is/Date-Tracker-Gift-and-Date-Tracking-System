import csv

# Create Lists
names = []
dates = []
gifts = []
events = []



# save information for future use
def save_data():
    with open('profile_database.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in zip(names, dates, gifts, events):
            writer.writerow(row)

# pull data
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

data_pull()
running = True

while running:
    print("Date and Gift Tracker")
    print("1. Add New Profile")
    print("2. Search Profile")
    print("3. Add/Update Gift Ideas")
    print("4. Exit")

    user_select = input("Select Option (1-4): ")

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
            print("*** Profile Found ***")
            print("Name: " + names[n])
            print("Date: " + dates[n])
            print("Event: " + events [n])
            print("Gifts: " + gifts [n])
        else:
            print("Profile Not Found.")

    elif user_select == "3":
        search = input("Whose gift is this for? ")
        if search in names:
            n = names.index(search)
            print("Gift Ideas: " + gifts[n])
            new_gift = input("Enter new gift idea: ")
            gifts[n] = gifts[n] + ", " + new_gift
            save_data()
            print("Gifts Updated.")
        else:
            print("Profile Not Found.")
        

    elif user_select == "4":
        print("Exiting.")
        running = False