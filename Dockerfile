# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.5.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
# RUN git clone https://github.com/gothinkster/django-realworld-example-app.git /drf_src

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.

WORKDIR /home/eldos/Projects/DjangoRestAPIStackOverflowProject


RUN ls /home/eldos/Projects/DjangoRestAPIStackOverflowProject .

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

VOLUME /DjangoRestAPIStackOverflowProject

EXPOSE 8000


CMD ./manage.py runserver
# CMD ["%%CMD%%"]