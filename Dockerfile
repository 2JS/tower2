FROM python:3.8

WORKDIR /usr/local/src
COPY . .

RUN pip3 install -r requirements.txt

# ENV FLASK_APP=/usr/local/src/app.py

CMD ["python", "/usr/local/src/app.py"]
