FROM python:3.7
ENV http_proxy="http://66690:D4v1d313Alejandro@10.50.8.20:8080"
ENV https_proxy="http://66690:D4v1d313Alejandro@10.50.8.20:8080"
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD["python","config.py"]
