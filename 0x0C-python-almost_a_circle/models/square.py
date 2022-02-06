#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The class Square, which inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ instanciation of a Square object"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """the overloading str method """
        return '[Square] ('+str(self.id)+') '+str(self.x)+'/'+str(self.y) +\
            ' - '+str(self.size)


    @property
    def size(self):
        """ the size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ the size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update the data"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

if __name__ == '__main__':
    main()
