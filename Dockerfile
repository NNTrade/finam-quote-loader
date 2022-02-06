ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

COPY requirements.txt /tmp/pip-tmp/
RUN pip --no-cache-dir install -r /tmp/pip-tmp/requirements.txt
RUN rm -rf /tmp/pip-tmp

WORKDIR /app
COPY ./src .

EXPOSE 5000

ENV FLASK_APP web_app
ENV FLASK_ENV production
ENV FLASK_DEBUG 0
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]