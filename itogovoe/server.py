from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from storage import TaskStorage
from validators import validate_task_data


storage = TaskStorage()


class TaskHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/tasks":
            tasks = [task.to_dict() for task in storage.get_all()]

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(tasks).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        # 1. POST /tasks — создание задачи
        if self.path == "/tasks":
            try:
                content_length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_length)
                data = json.loads(body)
    
                validate_task_data(data)
    
                task = storage.add_task(
                    title=data["title"],
                    priority=data["priority"]
                )
    
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(task.to_dict()).encode("utf-8"))
    
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
    
            except ValueError as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
    
            return
    
        # 2. POST /tasks/{id}/complete — отметка выполнения
        if self.path.startswith("/tasks/") and self.path.endswith("/complete"):
            try:
                parts = self.path.split("/")
                task_id = int(parts[2])
            except (IndexError, ValueError):
                self.send_response(404)
                self.end_headers()
                return
    
            success = storage.complete_task(task_id)
    
            if success:
                self.send_response(200)
            else:
                self.send_response(404)
    
            self.end_headers()
            return
    
        # 3. Любой другой POST — 404
        self.send_response(404)
        self.end_headers()



def run():
    server = HTTPServer(("", 8000), TaskHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()


if __name__ == "__main__":
    run()
