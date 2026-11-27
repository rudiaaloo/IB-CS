def set_foo(self, foo):
    self.__foo = foo #mutator: because idk how 

    #claud: 


#example of inheritance 
class WirelessDevice:
    def __init__(self, mac_address):
        self.__mac_address = mac_address 

    def get_mac_address(self): 
        return self.__mac_address 

class Laptop(WirelessDevice):
    def __init__(self, mac_address, has_wired_connection):
        super().__init__mac_address = mac_address
        self.has_wired_connection = has_wired_connection