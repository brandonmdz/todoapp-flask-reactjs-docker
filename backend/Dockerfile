FROM python:slim

WORKDIR /app

COPY . /app

RUN python -m venv flask && \
    . flask/bin/activate && \
    pip install flask

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP application.py

ENV FLASK_RUN_HOST 0.0.0.0

CMD ["flask", "run"]