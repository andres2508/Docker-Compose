import cherrypy
import psycopg2
import pprint

class DatabaseConsult(object):
    @cherrypy.expose
    def index(self):
        host = "host="+'192.168.130.124'+" "
        port = "port="+str(5432)+" "
        db = "dbname="+'swn'+" "
        user = "user="+'pi'+" "
        passwd = "password="+'security++'+" "

        conn_string = host+port+db+user+passwd
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM devices")
        records = cursor.fetchall()
        #pprint.pprint(records)
        #print((records['device_name']))
        return "This are database values"+" id_divice: "+str(records[0][0]) + " name_device: "+str(records[0][1])

    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 5000})
if __name__ == '__main__':
    cherrypy.quickstart(DatabaseConsult())


