# DevSecOps: How to identify and fix security problems in code with SAST tools

<h1>1- Introduction</h1><br/>
<p>The creation of a secure Software is primordial in a world dominated by cyberattacks. In this project we're going to show how we can create a secure software by introducing security best practice in the CI/CD.<br/></p>
<h2>2- Project Diagram</h2><br/>
<img src="/assets/project_diagram.png" alt="DevSecOps diagram" width="100%">
<h2>3- Our Flask App</h2>
<p>To demonstrate how to fix security problems in the code with SAST tools, we created a simple Flask App which manages Employees by doing CRUD (Create, Read, Update, Delete). We contenerise the App inside a docker container to facilitate the app to be run without the need of making configuration.
Before running the App, we need to change the MYSQL IP address in the database.py file in line 5 and 18 and if your database is listening in another port than the default 3306, so you can specify the port in those lines like this: <b>engine = create_engine("mysql+pymysql://mysql_username:mysql_password@mysql_ip:mysql_port/mysql_database_name")</b>.<br/>
To run easily the Flask App without having to do any configuration, you can install <b>docker</b> and <b>docker compose</b> by following the instructions <a href="https://docs.docker.com/engine/install/">here</a> depending from your OS system and then runs the following command to launch directly the Flask App and the MYSQL database: <b>docker compose up</b><br/>
Once those Apps are in running mode, you can use a tool like <b><a href="https://curl.se/download.html">curl</a></b> or <b><a href="https://www.postman.com/downloads/">Postman</a></b> to do your CRUD. In this tutorial, we will use <b><a href="https://curl.se/download.html">curl</a></b>.<br/>
<h3>3.1 Create or Add an Employee in the database</h3>
To add an Employee in the database, we need to send a <b>POST</b> request from the Flask App to the MYSQL database in the URI <b>http://192.168.1.2:8081/add_employee</b> like this: <b> curl -X POST -H 'Content-Type: application/json' -d '{"first_name":"White","last_name":"HACKER","gender":"MALE","salary":5000.0}' 'http://192.168.1.2:8081/add_employee'</b> An Employee with the following entries will be added in the database: First name: White Last name: HACKER Gender: MALE Salary: 5000.0€ . Note that the IP address of the Flask App is <b>192.168.1.2</b> and Flask is listening in the port <b>8080</b> and also the MYSQL database is using the IP address 192.168.1.3 and is listening in the default port 3306.<br/>
<h3>3.2- Read or Display an Employee from the database</h3>
To display an Employee from the database, we need to send a <b>GET</b> request from the Flask App to the MYSQL database like this: <b> curl -X GET http://192.168.1.2:8081/employee?first_name=White</b><br/>

<h3>3.3 Update an Employee from the database</h3>
To update an Employee in the database, we need to know first his/her ID. For example, the Employee White Hacker has the ID=1. So to update his information in the MYSQL database, we need to send a <b>PUT</b> request as follows: curl -X PUT -H 'Content-Type: application/json' -d '{"id":1,"first_name":"Pierre","last_name":"Cardin","salary":10000.0}' 'http://192.168.1.2:8081/update_employee' . We can now send a <b>GET</b> request to display the updated informations: <b>curl -X GET http://192.168.1.2:8081/employee?first_name=Pierre
</b> . We can also update only the First name by running the command:  <b>curl -X PUT -H 'Content-Type: application/json' -d '{"id":1,"first_name":"Jean"}' 'http://192.168.1.2:8081/update_employee' </b> or you also can update only the last name or the salary as follows: last name: <b>curl -X PUT -H 'Content-Type: application/json' -d '{"id":1,"last_name":"Batista"}' 'http://192.168.1.2:8081/update_employee'</b> salary: <b>curl -X PUT -H 'Content-Type: application/json' -d '{"id":1,"salary": 2000.0}' 'http://192.168.1.2:8081/update_employee'</b> . You can now send a <b>GET</b> request to display the new informations updated.<br/>
<h3>3.4 Delete an Employee from the database</h3><br/>
To delete an Employee in the database, we need to send a <b>DELETE</b> request from the Flask App to the MYSQL database as follows: <b>curl -X DELETE http://192.168.1.2:8081/delete_employee?id=1</b>


</p><br/>
<h2>4- Watch the video to learn how to fix security problems in CI/CD</h2><br/>
<a href="https://www.linkedin.com/posts/e-ben-sidi-87b51a242_devsecops-jenkins-sast-activity-7318976270577373184-Oz1F?utm_source=share&utm_medium=member_desktop&rcm=ACoAADw7tV8BqIg_cwvMuPaiSHCfVjgxeNX_TUI">Please click here to watch the video</a>
