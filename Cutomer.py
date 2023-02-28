class Customer:
    def __init__(self, customerId, firstName, lastName, phoneNumber, address):
        self.__customerId = customerId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phoneNumber = phoneNumber
        self.__address = address

    def getCustomerId(self):
        return self.__customerId

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