class Vehicle:
    def __init__(self, vehicleId, make, model, color, year):
        self.__vehicleId = vehicleId
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year

    def getVehicleId(self):
        return self.__vehicleId

    def getMake(self):
        return self.__make

    def setMake(self, make):
        self.__make = make

    def getModel(self):
        return self.__model

    def setModel(self, model):
        self.__model = model

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color
        
    def getYear(self):
        return self.__year
    
    def setYear(self, year):
        self.__year = year