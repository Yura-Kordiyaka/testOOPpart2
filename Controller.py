from framework.models import Model
from models.plant import Plant
from models.employee import Employee
from models.salon import Salon


class Controller():
    def create_plant(self):
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        plant = Plant(id, location, name, director_id)
        plant.save()

    def create_employee(self):
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.save()

    def create_salon(self):
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        salon = Salon(id, location, name, director_id)
        salon.save()

    def search_salon(self):
        id = int(input("ID: "))
        salon = Salon.get_by_id(id)
        print(salon)

    def search_plant(self):
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)

    def search_employee(self):
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)

    def general(self, choose):
        if choose == 1:
            self.create_plant()
        elif choose == 2:
            self.create_employee()
        elif choose == 3:
            self.create_salon()
        elif choose == 4:
            self.search_plant()
        elif choose == 5:
            self.create_employee()
        elif choose == 6:
            self.search_salon()
