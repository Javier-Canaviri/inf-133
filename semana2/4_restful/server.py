from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "carrera": "Ingenieria de Sistemas",
    },
]


class RESTRequestHandler(BaseHTTPRequestHandler):

    def response_handler(self,statusCode, data):
        self.send_response(statusCode)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def data_reader(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        post_data = json.loads(post_data.decode("utf-8"))
        post_data["id"] = len(estudiantes) + 1
        estudiantes.append(post_data)
        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(estudiantes).encode("utf-8"))

    def find_estudent_by_id(self,id,estudiantes):
        return next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
        )


    def do_GET(self):
        if self.path == "/estudiantes":
            self.response_handler(self,200,estudiantes)
            """self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))"""
             
        elif self.path == "/estudiantes/carreras/":
            estEconomia = next((estudiante["carrera":"Economia"] for estudiante in estudiantes),None,)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(list(estEconomia)).encode("utf-8"))
        
        elif self.path == "/carreras":
            carreras = set(estudiante["carrera"] for estudiante in estudiantes)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(list(carreras)).encode("utf-8"))
        
        elif self.path == "/economistas":  
            estEconomia = [estudiante for estudiante in estudiantes if estudiante["carrera"] == "Economia"]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estEconomia).encode("utf-8"))
               
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_estudent_by_id(self,id,estudiantes)
            if estudiante:
                self.response_handler(self,200,estudiante)
                """self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))"""
        
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

   
    def do_POST(self):
        if self.path == "/estudiantes":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_PUT(self):
        if self.path.startswith("/estudiantes"):
            data = self.read_data()            
            id = data["id"]
            estudiante = self.find_estudent_by_id(id)
            
            if estudiante:
                estudiante.update(data)
                self.response_handler(200,[estudiantes])
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_DELETE(self):
        if self.path == "/estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()