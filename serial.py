"""Python serial number generator"""
class SerialGenerator:
    """Machine to create unique incrementing serial numbers
    >>> serial = SerialGenerator(start=100)
    >>> serial.generate()
    100
    >>> serial.generate()
    101
    >>> serial.generate()
    102
    >>> serial.reset()
    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a new generator, starting at start"""
        self.start = self.next = start
    def __repr__(self):
        """Show representation"""
        return f"<SerialGenerator start={self.start} next={self.next}>"
    def generate(self):
        """Return next serial"""
        self.next += 1
        return self.next - 1
    def reset(self):
        """Reset number to original start"""
        self.next = self.start
        
#python3 -m doctest -v serial.py
#python3 serial.py , or
#ipython3
#%run serial.py       
#help(SerialGenerator)
serial = SerialGenerator(start=100)#Create a SerialGenerator object with a starting value of 100
print(serial)#<SerialGenerator start=100 next=100>
print(serial.generate())#100
print(serial.generate())#101
print(serial.generate())#102
serial.reset()
print(serial.generate())#100
