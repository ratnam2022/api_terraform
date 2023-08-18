FROM python:slim-bullseye
WORKDIR /app
COPY /src/requirements.txt .
RUN pip3 install -r requirements.txt
COPY /src/. .
EXPOSE 5001
ENTRYPOINT [ "python", "app.py" ]