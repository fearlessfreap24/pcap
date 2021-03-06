class QueueError(BaseException):  # Choose base class for the new exception.
    def __init__(self):
        BaseException.__init__(self)
        return self


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        try:
            val = self.__queue[0]
            del self.__queue[0]
            return val
        except:
            raise QueueError

    def getlength(self):
        return len(self.__queue)


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        return Queue.getlength(self) == 0

if __name__ == "__main__":
    que = Queue()
    que.put(1)
    que.put("dog")
    que.put(False)
    try:
        for i in range(4):
            print(que.get())
    except:
        print("Queue error")

    print("\n\n")

    que = SuperQueue()
    que.put(1)
    que.put("dog")
    que.put(False)
    for i in range(4):
        if not que.isempty():
            print(que.get())
        else:
            print("Queue empty")
