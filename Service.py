from enum import Enum

class ServiceType(Enum):
    DIAGNOSTICS = 1
    OIL_REPLACEMENT = 2
    OIL_FILTER_PARTS = 3
    TIRE_REPLACEMENT = 4
    TIRE = 5

class Service:
    def __init__(self, serviceId, customerId, vehicleId, serviceType, serviceDate, mechanic=None):
        self.__serviceId = serviceId
        self.__customerId = customerId
        self.__vehicleId = vehicleId
        self.__serviceType = serviceType
        self.__serviceDate = serviceDate
        self.__mechanic = mechanic

    def getServiceId(self):
        return self.__serviceId

    def getCustomerId(self):
        return self.__customerId

    def getVehicleId(self):
        return self.__vehicleId

    def getServiceType(self):
        return self.__serviceType

    def getServiceCost(self):
        if self.__serviceType.value == 1:
            return 15.0
        elif self.__serviceType.value == 2:
            return 120.0
        elif self.__serviceType.value == 3:
            return 35.0
        elif self.__serviceType.value == 4:
            return 50.0
        elif self.__serviceType.value == 5:
            return 80.0
    def getServiceDate(self):
        return self.__serviceDate

    def getMechanic(self):
        return self.__mechanic

    def setMechanic(self, mechanic):
        self.__mechanic = mechanic