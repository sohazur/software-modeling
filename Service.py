from enum import Enum

class ServiceType(Enum):
    DIAGNOSTICS = 15.00
    OIL_REPLACEMENT = 120.00
    OIL_FILTER_PARTS = 35.00
    TIRE_REPLACEMENT = 100.00
    TIRE = 160.00

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
        return self.__serviceType.value

    def getServiceDate(self):
        return self.__serviceDate

    def getMechanic(self):
        return self.__mechanic

    def setMechanic(self, mechanic):
        self.__mechanic = mechanic