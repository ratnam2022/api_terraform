FROM python:slim-bullseye
//Needs to add user
WORKDIR /app
COPY /src/requirements.txt .
RUN pip3 install -r requirements.txt
COPY /src/. .
EXPOSE 5001
ENTRYPOINT [ "python", "app.py" ]
