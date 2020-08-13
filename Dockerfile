FROM pypy

WORKDIR /srv/tower2
COPY . .

RUN pip3 install -r requirements.txt

ENV FLASK_APP=/srv/tower2/app.py

CMD ["pypy3", "-m", "flask", "run", "--host=0.0.0.0"]