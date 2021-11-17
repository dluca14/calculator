FROM python:3.9-alpine

# set env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /calculator

# install psycopg2 deps
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install systems deps
RUN pip install pipenv

# install project deps
COPY Pipfile /calculator/
COPY Pipfile.lock /calculator/
RUN test -f Pipfile.lock || (echo 'Please run "pipenv lock" to generate the Pipfile.lock file'; false)
RUN pipenv install --system --deploy

## Install pipenv and compilation dependencies
#RUN pip install pipenv
#RUN apt-get update && apt-get install -y --no-install-recommends gcc
#
## Install python dependencies in /.venv
#COPY Pipfile .
#COPY Pipfile.lock .
#RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

# copy project
COPY . .