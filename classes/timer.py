class Timer:
    def __init__( self, hour=0, minute=0, second=0 ):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"

    def next_second(self):
        self.__second += 1
        if self.__second > 59:
            self.__second = 0
            self.__minute += 1
        if self.__minute > 59:
            self.__minute = 0
            self.__hour += 1
        if self.__hour > 23:
            self.__hour = 0

    def prev_second(self):
        self.__second -= 1
        if self.__second < 0:
            self.__second = 59
            self.__minute -= 1
        if self.__minute < 0:
            self.__minute = 59
            self.__hour -= 1
        if self.__hour < 0 :
            self.__hour = 23

if __name__ == "__main__":
    timer = Timer()
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)
