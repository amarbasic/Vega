FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

RUN set -ex && pipenv install --deploy --system

COPY . .

RUN python manage.py compilemessages
RUN python manage.py collectstatic

EXPOSE 8000

CMD [ "gunicorn", "-c", "python:config.gunicorn", "vega.wsgi" ]
