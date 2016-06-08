from array_queue import ArrayQueue

""" Tracks a shop's list of clients using a queue """
""" By Felipe Pineda 4/2/16 """
""" <fopineda95@gmail.com """


class ShopTracker:

    def __init__(self):
        self._listQueue = ArrayQueue()
        
        
    def startDay(self):
        """ Starts the day off by starting the listing process """
        
        alpha = raw_input("Please enter the name (Enter End when done): ")
        while alpha != "End":
             self._listQueue.enqueue(alpha)
             alpha = raw_input("Please enter the name (Enter End when done): ")
        print len(self._listQueue) , "client(s) left"

    def addMore(self):
        """ Restarts the listing process again to add more names """
        
        alpha = raw_input("Please enter the name (Enter End when done): ")
        while alpha != "End":
             alpha = raw_input("Please enter the name (Enter End when done): ")
             self._listQueue.enqueue(alpha)
        print len(self._listQueue) , "client(s) left"        

    def endDay(self):
        """ Ends the day by clearing out the queue"""
        while len(self._listQueue) != 0:
            self._listQueue.dequeue()
        print len(self._listQueue) , "client(s) left"
        

    def getLength(self):
        """ Return length of elements in queue """
        return len(self._listQueue)

    def primero(self):
        """ Prints out the first name in the queue (will not remove) """
        if len(self._listQueue) == 0:
            #raise Empty('Queue is empty')
            print "You have no client(s) left"
        else:
            return self._listQueue.first()

    def getNext(self):
        """ Return the first name in the queue (will remove) """
        if len(self._listQueue) == 0:
            #raise Empty('Queue is empty')
            print "You have no client(s) left"
        else:
            return self._listQueue.dequeue()


class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  print "list is empty"
    


s = ShopTracker()
