#This is our base image we are going to use to run our Flask App. 22.04
# is the tags which identifies this specific image on the Docker hub.
FROM ubuntu:22.04

#this allows us to add some metadata to our Flask docker image.
#THis case is to specify the specific version of our Flask image
LABEL version="1.0.0"

#This one allows us to add metadata to our Flask image.
#This case is about specifying the description of our image.
LABEL description="This is a Dockerfile which creates a docker image which \
                    will run a docker container which contains a Flask app "

#This Docker instruction permits to specify the maintainer of this Flask image.
#This also can be done by using LABEL instruction
LABEL org.opencontainers.image.authors="Ben"

#This instructions allows us to install in the container all the required 
#packages that our Flask App needs to be run successfully.
RUN apt update && apt install python3 python3-pip python3-venv -y && \
    python3 -m venv flask && pip3 install Flask SQLAlchemy pymysql cryptography && \
    useradd -m -d /home/flask -s /usr/nologin flask && mkdir -p /home/flask/flask-app && \
    chown -R flask:flask /home/flask/flask-app


#This one allows us to specify the external port in which users should
#use to access on the Flask App.
EXPOSE 8081

#This command or instruction permits to specify
#the working directory of the Flask image.    
WORKDIR /home/flask/flask-app

#This command will assing the default user of the container to flask
USER flask

#As the source code of our Flask App is stored on Github,this command allows
# us to download it directly and copy it in the Flask container 
COPY . /home/flask/flask-app/

#This instruction allows us to specify the default command which docker will
#run once the Flask App container is in runnning mode
CMD [ "/bin/bash","-c","sleep 60 && python3 /home/flask/flask-app/database_and_table_creation.py && python3 /home/flask/flask-app/main.py" ]