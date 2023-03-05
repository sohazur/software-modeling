# Importing all the classes
from Customer import Customer
from Vehicle import Vehicle
from Service import Service
from Mechanic import Mechanic
from Invoice import Invoice
from Service import ServiceType

# Create customer objects
customer = Customer(1, 'James', 'Jones', '816-897-9862', '123 Main Street')
customer.setFirstName('James')
customer.setLastName('Jones')

customer2 = Customer(2, 'John', 'Smith', '816-897-9862', '322 New Street')

# Create vehicle objects
vehicle = Vehicle('AD-89034', 'Nissan', 'Altima', 'Silver', 2014)
vehicle.setColor('Silver')

vehicle2 = Vehicle('AD-84512', 'Mitshubishu', 'Attrage', 'Silver', 2017)

# Create two mechanic object
mechanic = Mechanic(1, 'Hans', 'K', '555-555-5555', '123 Main Street')
mechanic.setFirstName('Hans')
mechanic.setLastName('K')

mechanic2 = Mechanic(2, 'Kevin', 'P', '555-555-5555', '322 New Street')

# Create service objects for customer 1 and 2
services = [
Service(1, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.DIAGNOSTICS, 'March 13, 2022', mechanic),
Service(2, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.OIL_REPLACEMENT, 'March 13, 2022', mechanic),
Service(3, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.OIL_FILTER_PARTS, 'March 13, 2022', mechanic),
Service(4, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.TIRE_REPLACEMENT, 'March 13, 2022', mechanic),
Service(5, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.TIRE, 'March 13, 2022'),
Service(6, customer.getCustomerId(), vehicle.getVehicleId(), ServiceType.TIRE, 'March 13, 2022'),
Service(7, customer2.getCustomerId(), vehicle2.getVehicleId(), ServiceType.TIRE, 'March 13, 2022'),
Service(8, customer2.getCustomerId(), vehicle2.getVehicleId(), ServiceType.TIRE, 'March 13, 2022'),
Service(9, customer2.getCustomerId(), vehicle2.getVehicleId(), ServiceType.OIL_FILTER_PARTS, 'March 13, 2022'),
]

# Set mechanic for services
services[4].setMechanic(mechanic2)
services[5].setMechanic(mechanic2)
services[6].setMechanic(mechanic2)
services[7].setMechanic(mechanic2)
services[8].setMechanic(mechanic)

# Associate services with mechanic
mechanic.addService(services[0])
mechanic.addService(services[1])
mechanic.addService(services[2])
mechanic.addService(services[3])
mechanic2.addService(services[4])
mechanic2.addService(services[5])
mechanic2.addService(services[6])
mechanic2.addService(services[7])
mechanic.addService(services[8])
    
# Create invoice objects
invoice = Invoice(1, customer.getCustomerId(), 'March 13, 2022', 21.5, 11.5)
invoice.addService(services[0])
invoice.addService(services[1])
invoice.addService(services[2])
invoice.addService(services[3])
invoice.addService(services[4])
invoice.addService(services[5])

invoice2 = Invoice(2, customer2.getCustomerId(), 'March 13, 2022', 10.5, 9.5)
invoice2.addService(services[6])
invoice2.addService(services[7])
invoice2.addService(services[8])


# Create a function to generate an invoice
def generateInvoice(customer, vehicle, invoice, services):
    # Calculate the subtotal
    subtotal = sum([service.getServiceCost() if service.getCustomerId() == customer.getCustomerId() else 0 for service in services])
    # Calculate the total
    total = subtotal + invoice.getTaxes() - invoice.getDiscount()
    customer_services = []
    # Get the services for the customer
    for service in services:
        if service.getCustomerId() == customer.getCustomerId():
            customer_services.append(service)

    # Print the invoice
    print("\033[1m" + 'Invoice' + "\033[0m")
    print("\033[1m" + 'Invoice Number:' + "\033[0m", invoice.getInvoiceId())
    print()
    print("\033[1m" + 'Customer Name:' + "\033[0m", customer.getFirstName(), customer.getLastName())
    print("\033[1m" + 'Cell Phone Number:' + "\033[0m", customer.getPhoneNumber())
    print("\033[1m" + 'Date:' + "\033[0m", invoice.getInvoiceDate())
    # Print the mechanics names for the customer
    mechanics = []
    print("\033[1m" + 'Mechanic Name: ' + "\033[0m", end='')
    for service in customer_services:
        if service.getMechanic() not in mechanics:
            mechanics.append(service.getMechanic())
            print(service.getMechanic().getFirstName(), service.getMechanic().getLastName(), end=', ')
    print()
    # Print the vehicle information
    print("\033[1m" + 'Vehicle Type:' + "\033[0m", vehicle.getMake(), vehicle.getModel(), '(', vehicle.getYear(), ')')
    print("\033[1m" + 'Vehicle Color:' + "\033[0m", vehicle.getColor())
    print("\033[1m" + 'Vehicle ID:' + "\033[0m", vehicle.getVehicleId())
    print()
    
    print("\033[1m" + 'Services' + "\033[0m")
    # Print the services for the customer
    service_costs = {
        'DIAGNOSTICS' : 15.0,
        'OIL_REPLACEMENT': 120.0,
        'OIL_FILTER_PARTS': 35.0,
        'TIRE_REPLACEMENT': 50.0,
        'TIRE': 80.0
    }
    service_count = {}
    for service in customer_services:
        if service.getServiceType() not in service_count:
            service_count[service.getServiceType()] = 1
        else:
            service_count[service.getServiceType()] += 1
    # Print the services with quantity and the price
    for service in service_count:
        if service_count[service] > 1:
            print(service.name, '(',service_count[service],')', 'Price:', service_count[service] * service_costs[service.name])
        else:
            print(service.name, 'Price:', service_costs[service.name])
    # Print the subtotal, taxes, discount and total
    print('Taxes:', invoice.getTaxes())
    print('Total:', subtotal)
    print('Discount:', invoice.getDiscount())
    print("\033[1m" + 'Final Amount:' + "\033[0m", total)

# Call the function
if __name__ == '__main__':
    # Generate the invoice for customer 1
    generateInvoice(customer, vehicle, invoice, services)
    print()
    print()
    # Generate the invoice for customer 2
    generateInvoice(customer2, vehicle2, invoice2, services)