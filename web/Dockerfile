# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat \
    && apt-get install -y --no-install-recommends gcc build-essential libffi-dev 

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# CMD [ "python", "/usr/src/app/manage.py", "create_db" ]
# CMD [ "python", "/usr/src/app/manage.py", "db","init" ]
# CMD [ "python", "/usr/src/app/manage.py", "db", "migrate" ]
# CMD [ "python", "/usr/src/app/manage.py", "db", "upgrade" ]
