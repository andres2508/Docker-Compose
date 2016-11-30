FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python python-pip postgresql postgresql-contrib wget 
RUN useradd -ms /bin/bash admin
COPY ./files/create_schema.sql /tmp/create_schema.sql
USER postgres
RUN service postgresql start && \
	sleep 40 &&\
	cat /tmp/create_schema.sql | psql
COPY ./files/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
COPY ./files/postgresql.conf /etc/postgresql/9.3/main/postgresql.conf
EXPOSE 80
EXPOSE 5432
USER postgres
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]
