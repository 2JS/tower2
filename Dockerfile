FROM arm64v8/python:3.8

WORKDIR /app
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python", "/app/app.py"]
