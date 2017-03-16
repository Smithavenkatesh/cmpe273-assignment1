FROM python:2.7.13
MAINTAINER Your Name "smithav17@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
CMD ["https://github.com/Smithavenkatesh/cmpe273-assignment1-config"]
