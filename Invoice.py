class Invoice:
    def __init__(self, invoice_id, service_id, invoice_date, taxes, discount, total):
        self.invoice_id = invoice_id
        self.service_id = service_id
        self.invoice_date = invoice_date
        self.taxes = taxes
        self.discount = discount
        self.total = total

    def get_invoice_id(self):
        return self.invoice_id

    def get_service_id(self):
        return self.service_id

    def get_invoice_date(self):
        return self.invoice_date

    def get_taxes(self):
        return self.taxes

    def get_discount(self):
        return self.discount

    def get_total(self):
        return self.total

    def set_taxes(self, taxes):
        self.taxes = taxes

    def set_discount(self, discount):
        self.discount = discount

    def set_total(self, total):
        self.total = total

    def calculate_total(self):
        return self.total + self.taxes - self.discount