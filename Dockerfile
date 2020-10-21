FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip3 install -r requirements.txt