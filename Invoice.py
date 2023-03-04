class Invoice:
    def __init__(self, invoiceId, customerId, invoiceDate, taxes, discount):
        self.__invoiceId = invoiceId
        self.__customerId = customerId
        self.__invoiceDate = invoiceDate
        self.__taxes = taxes
        self.__discount = discount
        self.__services = []

    def getInvoiceId(self):
        return self.__invoiceId

    def getCustomerId(self):
        return self.__customerId

    def getInvoiceDate(self):
        return self.__invoiceDate

    def getTaxes(self):
        return self.__taxes

    def setTaxes(self, taxes):
        self.__taxes = taxes

    def getDiscount(self):
        return self.__discount

    def setDiscount(self, discount):
        self.__discount = discount

    def getServices(self):
        return self.__services

    def addService(self, service):
        self.__services.append(service)