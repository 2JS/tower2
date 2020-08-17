FROM python:3.8

WORKDIR /srv/tower2
COPY . .

RUN pip3 install -r requirements.txt

# ENV FLASK_APP=/srv/tower2/app.py

CMD ["python", "/srv/tower2/app.py"]