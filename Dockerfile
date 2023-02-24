FROM --platform=linux/amd64 python:3.10-slim-bullseye
RUN apt update && apt install curl/stable-security -y
WORKDIR /app
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
