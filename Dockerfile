FROM python:3.9
RUN apt-get update \
    && apt-get -y install git

COPY requirements.txt /tmp/pip-tmp/
RUN pip --no-cache-dir install -r /tmp/pip-tmp/requirements.txt
RUN rm -rf /tmp/pip-tmp
RUN pip install uwsgi

WORKDIR /app
COPY ./src .

EXPOSE 5000

ENV FLASK_APP controller
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]