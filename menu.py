
#plik menu.py z klasami Menu oraz MenuCommand, ExitCommand

events = []

class Menu:

    def menu():
        print("\nMenu\n======\n"
              "1. New event\n"
              "2. List calendar\n"
              "3. Export calendar to iCalendar\n"
              "4. Exit\n")

    menu()

    def newEvent():
        title = input("Title: ")
        date = input("Date (DD.MM.YYYY): ")
        time = input("Time (HH:MM): ")
        date_time = date + ', ' + time
        events[title] = date_time

    def listCalendar():
        for title in events:
            date_time = events[title]
            print('\nEvents\n======\n','Title:', title, '\nDate:', date_time,'\n')

    option = int(input("Enter your option: "))

    while option != 4:
        if option == 1:
            # dodaj nowe wydarzenie w formacie TITLE(txt),DATE(dd.mm.yyyy),TIME(hh:mm)
            newEvent()

        elif option == 2:
            # wypisz zapisane wydarzenia
            listCalendar()
        elif option == 3:
            # export do icallendar
            print("opcja 3")
        else:
            print("Valid option")
        menu()
        option = int(input("Enter your option: "))


class MenuCommand:
    pass

class ExitCommand:
    pass