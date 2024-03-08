#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2


hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        conn = psycopg2.connect(database="postgres",
                        host="postgres",
                        user="postgres",
                        password="example",
                        port="5432")
        cursor = conn.cursor()
        cursor.execute("select F.name, F.img from flats F")

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>sreality.cz scrapped</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        
        for name, img in cursor.fetchall():
            self.wfile.write(bytes(f'<p>{name} <img src="{img}"/></p>', "utf-8"))
            pass

        self.wfile.write(bytes("</body></html>", "utf-8"))



if __name__ == "__main__":        
    print("Server starting")
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
