# Parent image of python3
FROM python:3

# Sets an environment variable for the container
ENV PYTHONUNBUFFERED 1

# Makes the code directory and makes it the working directory
RUN mkdir /code
WORKDIR /code

# Copy from local to container
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
