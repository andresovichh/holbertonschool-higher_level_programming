#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The class Square, which inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ instanciation of a Square object"""

        super().__init__(size, size, x, y, id)
    
        
    @property
    def size(self):
        """ the size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ the size setter"""
        self.width = size
        self.height = size
    
    

if __name__ == '__main__':
    main()