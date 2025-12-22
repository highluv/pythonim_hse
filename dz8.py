from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import os
from requests import get, put
import urllib.parse
import json

# Input your Yandex.Disk OAuth token here
YA_TOKEN = input("Введите OAuth-токен Яндекс.Диска: ").strip()
YA_HEADERS = {"Authorization": f"OAuth {YA_TOKEN}"}

def get_uploaded_files():
    """
    Получает список всех файлов в папке Backup на Яндекс.Диске
    Возвращает set имён файлов.
    """
    uploaded = set()
    limit = 100
    offset = 0

    while True:
        resp = get(
            "https://cloud-api.yandex.net/v1/disk/resources",
            headers=YA_HEADERS,
            params={
                "path": "Backup",
                "limit": limit,
                "offset": offset
            }
        )

        data = resp.json()
        items = data.get("_embedded", {}).get("items", [])

        if not items:
            break

        for item in items:
            if item["type"] == "file":
                uploaded.add(item["name"])

        offset += limit

    return uploaded


class HttpGetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        uploaded_files = get_uploaded_files()
        local_files = os.listdir("pdfs")

        def fname2html(fname):
            style = ""
            if fname in uploaded_files:
                style = 'style="background-color: rgba(0, 200, 0, 0.25);"'

            return f"""
                <li {style}
                    onclick="fetch('/upload', {{method: 'POST', body: '{fname}'}})">
                    {fname}
                </li>
            """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = f"""
        <html>
            <head>
                <meta charset="utf-8">
                <title>Загрузка файлов</title>
            </head>
            <body>
                <h3>Файлы (зелёные уже загружены)</h3>
                <ul>
                    {''.join(map(fname2html, local_files))}
                </ul>
            </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        fname = self.rfile.read(content_len).decode("utf-8")

        local_path = f"pdfs/{fname}"
        ya_path = f"Backup/{urllib.parse.quote(fname)}"

        # Получаем URL для загрузки
        resp = get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            headers=YA_HEADERS,
            params={"path": ya_path}
        )

        upload_url = resp.json()["href"]

        # Загружаем файл
        with open(local_path, "rb") as f:
            put(upload_url, files={"file": (fname, f)})

        self.send_response(200)
        self.end_headers()

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HttpGetHandler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()



run()
