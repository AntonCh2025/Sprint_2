class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment    


yemelya = EmployeeSalary.get_email('Емеля', 40, 2)
vitek = EmployeeSalary.get_hours('Витя', 3, 'vitek@dog.cat')

print(f'Мыло Емели: {yemelya.email}')
print(f'Часики Витька: {vitek.hours}')

for emp in (yemelya, vitek):
    print(f'{emp.name} отработал {emp.hours} часов и получает {emp.salary()}. Было {emp.rest_days} выходных')

EmployeeSalary.set_hourly_payment(100)

for emp in (yemelya, vitek):
    print(f'{emp.name} отработал {emp.hours} часов и получает {emp.salary()}. Было {emp.rest_days} выходных')
