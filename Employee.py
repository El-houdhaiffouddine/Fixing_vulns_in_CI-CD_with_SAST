from database import delete_user, display_user_infos, display_user_infos_by_id, display_users_infos,add_users, update_salary, update_user_f_name, update_user_l_name 
from Gender import Gender
class Employee:

    def __init__(self, f_name:str, l_name:str,gender:Gender, salary:float, id:int=None):
        
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.id = id if id is not None else None
        self.salary = salary

    @property
    def get_f_name(self):

        return self.f_name
    
    @get_f_name.setter
    def set_f_name(self,f_name):

        self.f_name = str(f_name)
    
    @property
    def get_l_name(self):

        return self.l_name
    
    @get_l_name.setter
    def set_l_name(self, l_name):

        self.l_name = str(l_name)

    @property
    def get_id(self):

        return self.id
    
    @get_id.setter
    def set_id(self, id):
       
       self.id = int(id)

    @property
    def get_salary(self):

        return self.salary

    @get_salary.setter
    def set_salary(self, salary):

        self.salary = float(salary)

    @property
    def get_email(self):

        return str(self.f_name.replace(" ","").lower()+"."+self.l_name.replace(" ","").lower()+"@cybersecurity.fr")
    
    @get_email.setter
    def set_email(self, email):

        self.email = str(self.f_name.replace(" ","").lower()+"."+self.l_name.lower()+"@cybersecurity.fr")

    @property
    def get_gender(self):
        
        return self.gender

    @get_gender.setter
    def set_gender(self, gender:Gender):

        self.gender = gender

    @staticmethod
    def add_employee(e):
        try:
            add_users(e.f_name,e.l_name,e.gender,e.salary)
        except Exception as e:

            print(f"{e}")

    @staticmethod
    def delete_employee(id):
        try:
            delete_user(id)
        except Exception as e:
            print(f"{e}")

    @staticmethod
    def update_employee(id:int,new_f_name:str=None,new_l_name:str=None,new_salary:float=None):
        try:    
               if new_f_name is not None: update_user_f_name(id,new_f_name)
               if new_l_name is not None: update_user_l_name(id,new_l_name)
               if new_salary is not None: update_salary(id,new_salary)
        except Exception as e:
                print(f"{e}")

    @staticmethod
    def display_employees_infos():
        
        employees_infos = display_users_infos()

        return employees_infos
    
    @staticmethod
    def display_employee_infos(first_name:str):
       try:
           
            user_infos = display_user_infos(first_name)
              
            if user_infos:

                return user_infos
            
            else:

                return "An error occured, Impossible to display user data !"

       except Exception as e:
           print(f"An error occured, Impossible to display user data: {e}")

   
        





    


