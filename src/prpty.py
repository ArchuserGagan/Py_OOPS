#mypy : ignore-errors
#@property - decorator used to define  method as a property (it can be accessed like an attribute)
# benifit : add additional logic when read,write or delete attributes
# gives you getter, setter and deleter method

#mypy : ignore-errors
class Rectange:
    def __init__(self,width,height) -> None:  #they are raw here meant to be used in class
        self._width = width       #one underscore makes it a private/protected class
        self._height = height

    @property
    def width(self) -> str:
        return f"{self._width:.1f}cm"     #now we have to access height and width with property decorator

    @property
    def height(self) -> str:
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater then zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater then zero")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rectangle = Rectange(3,4)
del rectangle.width
rectangle.width = 5
print(rectangle.height)
print(rectangle.width)