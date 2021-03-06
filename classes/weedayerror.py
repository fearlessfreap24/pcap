class WeekDayError(Exception):
    pass
	

class Weeker:
    __days = { 'Sun' : 0,
            'Mon' : 1,
            'Tue': 2,
            'Wed': 3,
            'Thu': 4,
            'Fri': 5,
            'Sat': 6 }

    def __init__(self, day):
        if day in Weeker.__days:
            self.__today = Weeker.__days[day]
        else:
            raise WeekDayError

    def __str__(self):
        for item in self.__days:
            if self.__days[item] == self.__today:
                return item


    def add_days(self, n):
        self.__today = (self.__today + n) % 7

    def subtract_days(self, n):
        self.__today = (self.__today - n) % 7


if __name__ == "__main__":
    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print("Sorry, I can't serve your request.")
