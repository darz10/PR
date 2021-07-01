FROM python:3.8.5

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install --upgrade pip

RUN python3 -m pip install -r /tmp/requirements.txt

COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]