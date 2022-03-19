class addEvent:
    def __init__(self,title,date,time):
        self.title = title
        self.date = date
        self.time = time
    def __str__(self):
        text = "Title: {}\nDate: {}, {}".format(
            self.title, self.date,self.time
        )
        return text

class addValue:

    def title():
        title = input("Title: ")
        return title

    def date():
        date = input("Date (DD.MM.YYYY): ")
        return date

    def time():
        time = input("Time (HH:MM): ")
        return time

#addEvent(addValue.title(),addValue.date(),addValue.time())
#print(addEvent(addValue.title(),addValue.date(),addValue.time()))