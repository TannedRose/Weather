FROM python:3.11

RUN apt-get update && apt-get install -y telnet tcpdump iputils-ping dnsutils
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/WeatherApp

COPY . /opt/WeatherApp

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app
CMD ["python3", "/manage.py", "runserver", "0.0.0.0:8000"]