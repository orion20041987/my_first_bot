FROM python:3.9

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install -r requirements.txt

ENV TZ Europe/Moscow

CMD ["python3", "app.py"]
