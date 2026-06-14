from jinja2.utils import soft_unicode


class Employee:
    def work(self):
        print("Employee working hours is 8 hours")




class Manager(Employee):
    def manage_team(self):
        print("Managing team")
    def work(self):
        print("Manager is managing work")



soubhik = Manager()
soubhik.manage_team()
soubhik.work()