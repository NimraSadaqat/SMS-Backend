# setting up base image
FROM python:3.9.9-bullseye

# prevents python buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# prevents python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# sets up the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions
WORKDIR /SMS/backend/

# copies files and directories from current directory to WORKDIR
COPY . /SMS/backend/

# install system dependencies
RUN apt-get update 
RUN apt-get -y install libpq-dev gcc 
        # && apt-get install libpq-dev
# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /SMS/backend/
RUN pip install -r requirements.txt

# Build psycopg2-binary from source -- add required required dependencies
# RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
        # pip install --no-cache-dir -r requirements.txt && \
        # apk --purge del .build-deps &&\
        # pip install psycopg2

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]