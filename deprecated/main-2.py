import socket
import threading
import os
import json

class SimpleHTTPServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.static_dir = '.'  # Текущая директория

    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(1024).decode('utf-8')
            print(f"Получен запрос:\n{request}")

            # Парсим первую строку запроса
            request_line = request.split('\n')[0]
            method, path, _ = request_line.split()

            if method == 'GET':
                # API endpoint для получения списка изображений
                if path == '/api/images':
                    self.handle_api_images(client_socket)
                    return
                
                if path == '/':
                    path = '/main.html'
                elif path == '/panorams':
                    path = '/panorams.html'
                elif path == '/games':
                    path = '/gameMenu.html'
                elif path == '/documentation':
                    path = '/documentation.html'
                elif path == '/games/guesspanoram':
                    path == '/guessPanorams.html'
                
                file_path = self.static_dir + path

                if os.path.exists(file_path) and os.path.isfile(file_path):
                    # Определяем Content-Type
                    if file_path.endswith('.html'):
                        content_type = 'text/html; charset=utf-8'
                    elif file_path.endswith('.js'):
                        content_type = 'application/javascript'
                    elif file_path.endswith('.css'):
                        content_type = 'text/css'
                    elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
                        content_type = 'image/jpeg'
                    elif file_path.endswith('.png'):
                        content_type = 'image/png'
                    elif file_path.endswith('.json'):
                        content_type = 'application/json'
                    else:
                        content_type = 'text/plain'

                    # Читаем файл и отправляем ответ
                    with open(file_path, 'rb') as file:
                        content = file.read()

                    response = (
                        "HTTP/1.1 200 OK\r\n"
                        f"Content-Type: {content_type}\r\n"
                        f"Content-Length: {len(content)}\r\n"
                        "Connection: close\r\n"
                        "\r\n"
                    ).encode('utf-8') + content

                else:
                    # Файл не найден - отправляем 404.html
                    with open('404.html', 'rb') as file:
                        content = file.read()
                    
                    response = (
                        "HTTP/1.1 404 Not Found\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n"
                        f"Content-Length: {len(content)}\r\n"
                        "Connection: close\r\n"
                        "\r\n"
                    ).encode('utf-8') + content

            else:
                # Метод не поддерживается
                response = (
                    "HTTP/1.1 405 Method Not Allowed\r\n"
                    "Content-Type: text/html; charset=utf-8\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                    "<h1>405 - Method Not Allowed</h1>"
                ).encode('utf-8')

            client_socket.send(response)

        except Exception as e:
            print(f"Ошибка при обработке запроса: {e}")
            error_response = (
                "HTTP/1.1 500 Internal Server Error\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "Connection: close\r\n"
                "\r\n"
                "<h1>500 - Internal Server Error</h1>"
            ).encode('utf-8')
            client_socket.send(error_response)
        finally:
            client_socket.close()

    def handle_api_images(self, client_socket):
        """Обработка API запроса для получения списка изображений"""
        try:
            img_dir = os.path.join(self.static_dir, 'img')
            images = []
            
            if os.path.exists(img_dir):
                # Получаем список всех jpg/jpeg/png файлов в папке img
                for file in os.listdir(img_dir):
                    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                        images.append(f'/img/{file}')
            
            # Сортируем изображения по имени
            images.sort()
            
            response_data = json.dumps(images)
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: application/json\r\n"
                f"Content-Length: {len(response_data)}\r\n"
                "Access-Control-Allow-Origin: *\r\n"
                "Connection: close\r\n"
                "\r\n"
                + response_data
            ).encode('utf-8')
            
            client_socket.send(response)
            
        except Exception as e:
            print(f"Ошибка в API images: {e}")
            error_response = json.dumps({"error": "Internal server error"})
            response = (
                "HTTP/1.1 500 Internal Server Error\r\n"
                "Content-Type: application/json\r\n"
                f"Content-Length: {len(error_response)}\r\n"
                "Connection: close\r\n"
                "\r\n"
                + error_response
            ).encode('utf-8')
            client_socket.send(response)

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            server_socket.bind((self.host, self.port))
            server_socket.listen(20)
           

            while True:
                client_socket, addr = server_socket.accept()
                print(f"Подключение от {addr}")
                client_thread = threading.Thread(
                    target=self.handle_client, 
                    args=(client_socket,)
                )
                client_thread.daemon = True
                client_thread.start()

        except KeyboardInterrupt:
            print("\nОстановка сервера...")
        except Exception as e:
            print(f"Ошибка сервера: {e}")
        finally:
            server_socket.close()

if __name__ == "__main__":
    server = SimpleHTTPServer('localhost', 8080)
    server.start()