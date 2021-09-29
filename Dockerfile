#Base python docker image
FROM python:3.9.7-buster

#Import Code
ADD . /code

# Changing dir
WORKDIR /code

#Installing lib
RUN pip install flask

#Exposing the port
EXPOSE 5001

#Run python file
CMD python main.py