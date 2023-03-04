# Importing all the classes
from Customer import Customer
from Vehicle import Vehicle
from Service import Service
from Mechanic import Mechanic
from Invoice import Invoice
from Service import ServiceType

# Create a customer object
customer = Customer(1, 'James', 'Jones', '816-897-9862', '123 Main Street')
customer.setFirstName('James')
customer.setLastName('Jones')

# Create a vehicle object
vehicle = Vehicle('AD-89034', 'Nissan', 'Altima', 'Silver')
vehicle.setColor('Silver')

# Create two mechanic object
mechanic = Mechanic(1, 'Hans', 'K', '555-555-5555', '123 Main Street')
mechanic.setFirstName('Hans')
mechanic.setLastName('K')

mechanic2 = Mechanic(2, 'Kevin', 'P', '555-555-5555', '322 New Street')

# Create service objects
services = [
Service(1, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.DIAGNOSTICS, '2022-03-13', mechanic),
Service(2, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.OIL_REPLACEMENT, '2022-03-13', mechanic),
Service(3, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.OIL_FILTER_PARTS, '2022-03-13', mechanic),
Service(4, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.TIRE_REPLACEMENT, '2022-03-13', mechanic),
Service(5, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.TIRE, '2022-03-13'),
Service(6, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.TIRE, '2022-03-13')
]

services[4].setMechanic(mechanic2)
services[5].setMechanic(mechanic2)

# Associate services with mechanic
mechanic.addService(services[0])
mechanic.addService(services[1])
mechanic.addService(services[2])
mechanic.addService(services[3])
mechanic2.addService(services[4])
mechanic2.addService(services[5])
    
# Create an invoice object
invoice = Invoice(1, customer.getCustomerId(), '2022-03-13', 21.5, 11.5)
invoice.addService(services[0])
invoice.addService(services[1])
invoice.addService(services[2])
invoice.addService(services[3])
invoice.addService(services[4])

# Create a function to generate an invoice
def generateInvoice(customer, vehicle, invoice, services):
    # Calculate the subtotal
    subtotal = sum([service.getServiceCost() for service in services])
    # Calculate the total
    total = subtotal + invoice.getTaxes() - invoice.getDiscount()
    customer_services = []
    # Get the services for the customer
    for service in services:
        if service.getCustomerId() == customer.getCustomerId():
            customer_services.append(service)

    # Print the invoice
    print('Customer Name:', customer.getFirstName(), customer.getLastName())
    print('Cell Phone Number:', customer.getPhoneNumber())
    print('Date:', invoice.getInvoiceDate())
    # Print the mechanics names for the customer
    mechanics = []
    print('Mechanic Name: ', end='')
    for service in customer_services:
        if service.getMechanic() not in mechanics:
            mechanics.append(service.getMechanic())
            print(service.getMechanic().getFirstName(), service.getMechanic().getLastName(), end=', ')
    print()
    
    print('Vehicle Type:', vehicle.getMake(), vehicle.getModel(), '(', vehicle.getVehicleId(), ')')
    print('Vehicle Color:', vehicle.getColor())
    print()
    
    print('Services')
    service_count = {}
    for service in customer_services:
        if service.getServiceType() not in service_count:
            service_count[service.getServiceType()] = 1
        else:
            service_count[service.getServiceType()] += 1
    for service in service_count:
        if service_count[service] > 1:
            print(service.name, '(',service_count[service],')', 'Price:', service.value * service_count[service])
        else:
            print(service.name, 'Price:', service.value)
            
    print('Taxes:', invoice.getTaxes())
    print('Total:', subtotal)
    print('Discount:', invoice.getDiscount())
    print('Final Amount:', total)

# Call the function
if __name__ == '__main__':
    generateInvoice(customer, vehicle, invoice, services)