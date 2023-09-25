FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 8082
CMD ["waitress-serve", "--listen=*:8082", "app:app"]