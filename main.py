from flask import Flask, request, jsonify, render_template
from Employee import Employee
from Gender import Gender

app = Flask(__name__)

@app.route("/employee", methods=['GET'])
def employee_infos():
    
    f_name = request.args.get('first_name')

    user_infos = Employee.display_employee_infos(f_name)
    
    if f_name and user_infos:
        
       return jsonify(user_infos)
    elif not f_name or user_infos:

        return jsonify({"message":" No user input provided !"}), 400
    else:

        return jsonify({"message":"An error, occured impossible to display the Employee"}), 400
    

@app.route("/add_employee", methods=['POST'])
def addEmployee():

    employee=None

    employee_infos = request.get_json()
   
    if not employee_infos:

        return jsonify({"message":"No data are provided"}),400

    first_name = employee_infos.get('first_name')

    last_name = employee_infos.get('last_name')

    gender = employee_infos.get('gender')

    salary = employee_infos.get('salary')

    if employee_infos and first_name and last_name and gender and salary:

       employee = Employee(first_name,last_name,gender.upper(),salary)
    
    else:

        return jsonify({"message":"All users input are mandatory !"}),400
    
    try:

        Employee.add_employee(employee)

        return jsonify({"message":"Employee added successfully !"})
    
    except Exception as e:
        
        print(f"{e}")
        return jsonify({"message":"An error occured, Employee has not been added successfully !"})
        

@app.route("/delete_employee", methods=['DELETE'])   
def deleteEmployee():
    
    id = int(request.args.get('id'))

    if id and type(id) is int:

        try:
            Employee.delete_employee(id)

            return jsonify({"message":"Employee deleted successfully !"})
            
        except Exception as e:
            print(f"An error occured, Impossible to delete the Employee:{e}")
    
    elif not id or id is None:

        return jsonify({"message":"No ID provided !"})

    else:

        return jsonify({"message":"An error occured, Impossible to delete the Employee !"})    


@app.route("/update_employee", methods=['PUT'])
def updateEmployee():

    user_infos = request.get_json()
    id = user_infos.get('id')
    first_name = user_infos.get('first_name')
    last_name = user_infos.get('last_name')
    salary = user_infos.get('salary')

    try:

        if id and type(id) is int:

            if first_name:
                Employee.update_employee(id=id,new_f_name=first_name)
            if last_name:
                Employee.update_employee(id=id,new_l_name=last_name)
            if salary:
                Employee.update_employee(id=id,new_salary=salary)

            return jsonify({"message":"Employee updated successfully !"}), 201
            
        elif not id or id is None:
            return jsonify({"message":"No ID is provided !"}), 400
        
        else:

            return jsonify({"message":"An error occured, Impossible to update Employee !"}), 400
              

    except Exception as e:

        print(f"An error occured, Impossible to update Employee: {e}")

        return jsonify({"message":"An error occured, Impossible to update Employee !"}), 400
    

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=8080,debug=True)
