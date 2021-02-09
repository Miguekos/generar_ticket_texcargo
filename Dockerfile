FROM python:3.6
WORKDIR /app

COPY ["./requeriment.txt" , "/app"]
RUN apt-get update
RUN apt-get install wkhtmltopdf -y
RUN pip install -r requeriments.txt

COPY ["." , "/app"]

EXPOSE 4545

CMD [ "python" , "app.py" ]