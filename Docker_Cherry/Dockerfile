FROM ubuntu:14.04
RUN apt-get update && apt-get install -y python python-pip python-cherrypy python-psycopg2 
RUN apt-get install python3-pip -y
RUN useradd -ms /bin/bash cherry
RUN apt-get remove python-cherrypy -y
RUN pip install cherrypy
USER cherry
WORKDIR /home/cherry
ADD ./files/server.py /home/cherry
EXPOSE 5000
EXPOSE 5432
USER root
CMD ["python", "server.py"]
