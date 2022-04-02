'''
W tym pliku znajdziesz kod odpowiedzialny za wyświetlanie zdarzeń z kalendarza.
Do zmiany zachowania funkcji list_calendar wykorzystaj strategię ListingStrategy.
'''

class ListingStrategy:
    def begin(self):
        pass

    def event(self, title, date, time):
        pass

    def end(self):
        pass

class TextData(ListingStrategy):
    def begin(self):
        pass

    def event(self, title, date, time):
        print(f'Title: {title}\nDate: {date}, {time}')

    def end(self):
        pass

class ICalendarData(ListingStrategy):
    def begin(self):
        print(f'BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VTIMEZONE\nTZID:Europe/Warsaw\nX-LIC-LOCATION:Europe/Warsaw\nEND:VTIMEZONE')
    def event(self, title, date, time):

        timeAndDateToDisplay = self.prepareTimeAndDate(time,date)

        print(f'DTSTART:{timeAndDateToDisplay}\nDTEND:{timeAndDateToDisplay}\nSUMMARY:{title}\nEND:VEVENT')

    def end(self):
        print('END:VCALENDAR')

    def prepareTimeAndDate(self,time,date):
        splitTime = time.split(':')
        splitDate = date.split('.')
        timeAndDateToDisplay = ''

        for element in splitDate:
            timeAndDateToDisplay += element

        timeAndDateToDisplay += 'T'

        for element in splitTime:
            timeAndDateToDisplay += element

        timeAndDateToDisplay += '00'

        return timeAndDateToDisplay

def list_calendar(calendar, listing_strategy):
    listing_strategy.begin()

    for event in calendar:
        listing_strategy.event(event.get('title'),event.get('date'),event.get('time'))

    listing_strategy.end()