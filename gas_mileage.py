# ==========================================
# Good

def milesPerGallon( miles, gallons):
    if gallons == 0:
        return 0.0
    elif gallons > 0:
        total = miles / gallons
        return total


# ==========================================
# Good

def createNotebook():
    myList = []
    return myList

# ==========================================
# Good

def recordTrip (note_list, date_trip, miles_traveled, gallons_pumped):
#     list, string, float, float
    my_Dic = {'date': date_trip, 'miles': miles_traveled, 'gallons': gallons_pumped}
    note_list.append(my_Dic)


# ==========================================
# Good
def listTrips(note_list):
    new_list = []
    if note_list == []:
        return note_list
    else:
        for num in note_list:
            miles = num['miles']
            gallons = num['gallons']
            total_ans = milesPerGallon( miles, gallons)
            new_list.append("On " + num['date'] + ": " + str(miles) + " miles traveled using "+ str(gallons) + ' gallons ' + str(total_ans) +" MPG")
        return new_list


# ==========================================
# Good
def calculateMPG(note_list):
    total_miles = 0
    total_gallons = 0
    if len(note_list) == 0:
        return 0.0
    else:
        for num in note_list:
            total_miles += num['miles']
            total_gallons += num['gallons']
    my_ans = milesPerGallon(total_miles, total_gallons)
    return float(my_ans)

# ==========================================
# Good

def formatMenu():
    my_list = ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']
    return my_list

# ==========================================
# Good

def formatMenuPrompt( ):
    return 'Eneter an option: '

# ==========================================
# Good
def getUserString(prompt_for_input):
    a = input(prompt_for_input)
    a = a.strip()
    while a =='':
        a = input(prompt_for_input)
        a = a.strip()
    return a

# ==========================================
# Good

def getUserFloat(prompt_for_input):
    while True:
        userinput = input(prompt_for_input)
        try:
            if float (userinput) > 0.0:
                return float(userinput)
        except:
            print('You cant convert that string to a float')

# ==========================================
# Good

def getDate ():
    date = input('Enter the date: ')
    date = date.strip()
    while date =='':
        date = input("Enter the date: ")
        date = date.strip()
    return date

# ==========================================
# Good

def getMiles():
    # getUserFloat("Enter miles: ")
    while True:
        amount_of_miles = input("Enter Miles: ")
        try:
            if float(amount_of_miles) > 0.0:
                return float(amount_of_miles)
        except:
            print('You cant convert that string to a float')

# ==========================================
# Good
def getGallons ():
    while True:
        amount_of_gallons = input("Enter Gallons: ")
        try:
            if float(amount_of_gallons) > 0.0:
                return  float(amount_of_gallons)
        except:
            print('You cant convert that string to a float')


# ==========================================
# Good

def recordTripAction(note_list):
    recordTrip(note_list,getDate(),getGallons(),getMiles())
    print('Your inputs successfully saved. ')

# ==========================================
# Good

def listTripsAction (note_list):
    a = listTrips(note_list)
    if len(a) == 0:
        print("No trips are recorded. ")
    else:
        for item in a:
            print(item)


# ==========================================
# Good

def calculateMPGAction(note_list):
    a = calculateMPG(note_list)
    if a == 0.0:
        print("There is not trips recorded. ")
    else:
        print('average= '+str(a) +'mpg')

# ==========================================
# Good
import sys
def quitAction (index):
    print("The program is ending...")
    sys.exit ( 0 )

# ==========================================
# Good
def applyAction(index_dic, choice_str):
    if choice_str == 'r':
        recordTripAction(index_dic)
    elif choice_str == 'l':
        listTripsAction(index_dic)
    elif choice_str == 'c':
        calculateMPGAction(index_dic)
    elif choice_str == 'q':
        quitAction(index_dic)
    else: print("Your input is invalid. ")

# ==========================================
#

def main ():
    notebook = createNotebook()
    menu = formatMenu()
    choice = ''
    while choice != 'q':
        for line in menu:
            print(line)
        prompt = formatMenuPrompt()
        choice = getUserString(prompt)
        applyAction(notebook, choice)


# ==========================================
if __name__ == '__main__':
    main()













