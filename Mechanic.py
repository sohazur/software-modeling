class Mechanic:
    def __init__(self, mechanicId, firstName, lastName, phoneNumber, address):
        self.__mechanicId = mechanicId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phoneNumber = phoneNumber
        self.__address = address
        self.__services = []

    def getMechanicId(self):
        return self.__mechanicId

    def getFirstName(self):
        return self.__firstName

    def setFirstName(self, firstName):
        self.__firstName = firstName
        
    def getLastName(self):
            return self.__lastName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def getPhoneNumber(self):
        return self.__phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def addService(self, service):
        self.__services.append(service)

    def getServices(self):
        return self.__services
