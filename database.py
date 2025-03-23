from Gender import Gender
from sqlalchemy import create_engine, text

# Modify the below IP to add the IP of your database and add a port number if necessary
engine = create_engine("mysql+pymysql://root:@192.168.1.3")

def create_database():
  try:  
      with engine.connect() as connection:

          connection.execute(text("CREATE DATABASE IF NOT EXISTS users_database"))
          connection.commit()
  except Exception as e :
      print(f"Problem of creating the database:{e}")


# Modify the below IP to add the IP of your database and add a port number if necessary
new_engine = create_engine("mysql+pymysql://root:@192.168.1.3/users_database")
table = "users"

def create_users_table():

  try:

     with new_engine.connect() as connection:
        
        connection.execute(text(f"CREATE TABLE IF NOT EXISTS {table} (first_name varchar(20), last_name varchar(20), id int AUTO_INCREMENT, gender varchar(6),salary decimal(10,2), CONSTRAINT pr_key PRIMARY KEY (id) )"))
        connection.commit()

  except Exception as e:
    
     print(f"Problem of creating the table :{e}")

def add_users(f_name:str,l_name:str,gender:Gender,salary:float):
    
    gender = gender.upper()
    
    try:
       
        with new_engine.connect() as connection:
       
             connection.execute(text("INSERT INTO users (first_name, last_name, gender,salary) VALUES (:first_name,:last_name,:gender,:salary)"),[{"first_name":f_name,"last_name":l_name,"gender":gender,"salary":salary}])
            
             connection.commit()

    except Exception as e:
       
       print(f"Problem of adding data in the table {table}: {e}")

def delete_user(id:int):

   if id:

      with new_engine.connect() as connection:
       
           try:
          
               connection.execute(text("DELETE FROM users WHERE (id=:id)"),[{"id":id}])

               connection.commit()

               print(f"User deleted successfully !")

           except Exception as e:
          
               print(f"An error occured, Impossible to delete user: {e}") 

   else:
      print("ID is required !")
           

def update_user_f_name(id:int, new_f_name:str):
   try: 
        with new_engine.connect() as connection:
       
           if id and new_f_name:
          
              connection.execute(text("UPDATE users SET first_name=:new_f_name WHERE (id=:id)"),[{"id":id,"new_f_name":new_f_name}])           
              
              connection.commit()

              print("First name updated successfully !")

   except Exception as e:
        
        print(f"Error to update the first name: {e}")

def update_user_l_name(id:int,new_l_name:str):
   
   try:
      
      with new_engine.connect() as connection:

         if id and new_l_name:
          
            connection.execute(text("UPDATE users SET last_name=:new_l_name WHERE (id=:id)"),[{"id":id,"new_l_name":new_l_name}])

            connection.commit()

            print(f"Last name updated successfully !")

   except Exception as e:

      print(f"Error to update the last name: {e}")

def update_salary(id:int,new_salary:float):

    try:
       
       with new_engine.connect() as connection:

         if id and new_salary:
           
            connection.execute(text("UPDATE users SET salary=:new_salary WHERE (id=:id)"),[{"id":id,"new_salary":new_salary}])
         
            connection.commit()
         
            print("Your salary has been updated successfully !")

    except Exception as e:
       
       print(f"Error to update the salary: {e}")

def display_users_infos():
   
   users_infos={}

   try:
       with new_engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM users"))

            for row in result:
                
                users_infos[row.id] = [row.first_name, row.last_name, row.gender, row.salary]
                
   
       return users_infos
   
   except Exception as e:
      
      print(f"An error occured, Impossible to display users infos : {e}")
          
def display_user_infos(f_name:str):
   user = {}
  
   try:

      with new_engine.connect() as connection:
           result = connection.execute(text("SELECT first_name,last_name,id,gender,salary FROM users WHERE (first_name=:f_name)"),[{"f_name":f_name}])
      
           if result: 

              for row in result:

                  user[row.id] = [row.first_name,row.last_name,row.gender,row.salary]
   
              return user
      
           else:

              return "An error occured, Impossible to display user data !"



   except Exception as e:

      print(f"An error occured, Impossible to display user data: {e}")   
          

def display_user_infos_by_id(id:int):
   
   user = []
    
   with new_engine.connect() as connection:
      result = connection.execute(text("SELECT first_name,last_name,gender,salary FROM users WHERE (id=:id)"),[{"id":id}])

      for row in result:
         user.append(row.first_name)
         user.append(row.last_name)
         user.append(row.gender)
         user.append(row.salary)
   
   return user
