<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VR Панорамы - Документация</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
            padding: 40px 0;
        }

        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }

        .badges {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
            flex-wrap: wrap;
        }

        .badge {
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.3);
        }

        .content {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }

        .section {
            margin-bottom: 40px;
        }

        .section h2 {
            color: #4a5568;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 2em;
        }

        .section h3 {
            color: #2d3748;
            margin: 25px 0 15px 0;
            font-size: 1.4em;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }

        .feature-card {
            background: #f7fafc;
            padding: 25px;
            border-radius: 15px;
            border-left: 5px solid #667eea;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }

        .feature-icon {
            font-size: 2em;
            margin-bottom: 15px;
            color: #667eea;
        }

        .architecture {
            background: #edf2f7;
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
        }

        .code-block {
            background: #2d3748;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
        }

        .file-structure {
            background: #f7fafc;
            border: 2px dashed #cbd5e0;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
        }

        .file-item {
            margin: 5px 0;
            padding-left: 20px;
        }

        .file-icon {
            margin-right: 10px;
            color: #667eea;
        }

        .api-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .api-table th {
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
        }

        .api-table td {
            padding: 15px;
            border-bottom: 1px solid #e2e8f0;
        }

        .api-table tr:hover {
            background: #f7fafc;
        }

        .controls-list {
            list-style: none;
            padding: 0;
        }

        .controls-list li {
            background: #f7fafc;
            margin: 10px 0;
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }

        .key {
            background: #4a5568;
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            margin: 0 5px;
        }

        .footer {
            text-align: center;
            color: white;
            padding: 30px 0;
            margin-top: 40px;
        }

        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .header h1 {
                font-size: 2em;
            }
            
            .content {
                padding: 20px;
            }
            
            .features-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎮 VR Панорамы</h1>
            <p>Веб-сервер с Three.js для просмотра 360° панорам</p>
            <div class="badges">
                <span class="badge">Three.js</span>
                <span class="badge">WebXR</span>
                <span class="badge">Python</span>
                <span class="badge">WebGL</span>
                <span class="badge">VR</span>
            </div>
        </div>

        <div class="content">
            <div class="section">
                <h2>📖 О проекте</h2>
                <p>Простой HTTP-сервер для просмотра панорамных изображений в виртуальной реальности с использованием Three.js и WebXR. Проект позволяет автоматически сканировать папку с изображениями и просматривать их в интерактивном 360° режиме.</p>
            </div>

            <div class="section">
                <h2>✨ Возможности</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🎯</div>
                        <h3>Просмотр панорам</h3>
                        <p>Просматривайте 360° изображения в интерактивном режиме</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🕶️</div>
                        <h3>Поддержка VR</h3>
                        <p>Совместимость с Oculus Quest, HTC Vive через WebXR</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔄</div>
                        <h3>Автосканирование</h3>
                        <p>Автоматическое обнаружение изображений в папке</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">⌨️</div>
                        <h3>Управление с клавиатуры</h3>
                        <p>Навигация между изображениями с помощью стрелок</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">📱</div>
                        <h3>Адаптивный интерфейс</h3>
                        <p>Оптимальное отображение на всех устройствах</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🎨</div>
                        <h3>Современный дизайн</h3>
                        <p>Стильное главное меню с градиентами и анимациями</p>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2>🔧 Принцип работы</h2>
                
                <div class="architecture">
                    <h3>Архитектура системы</h3>
                    <p><strong>Веб-браузер (клиент)</strong> ↔ <strong>Python сервер</strong> ↔ <strong>Папка с изображениями</strong></p>
                    <p><strong>Three.js сцена</strong> → <strong>VR окружение</strong></p>
                </div>

                <h3>Ключевые компоненты</h3>
                
                <div class="feature-card">
                    <h4>🔧 Серверная часть (Python)</h4>
                    <ul>
                        <li>HTTP сервер на сокетах</li>
                        <li>Статическая раздача файлов</li>
                        <li>API для сканирования изображений</li>
                        <li>Маршрутизация запросов</li>
                    </ul>
                </div>

                <div class="feature-card">
                    <h4>🎨 Клиентская часть (Three.js)</h4>
                    <ul>
                        <li>3D сцена со сферой для панорам</li>
                        <li>WebXR интеграция для VR</li>
                        <li>Загрузчик текстур</li>
                        <li>Система навигации между изображениями</li>
                    </ul>
                </div>

                <h3>Процесс отображения панорамы</h3>
                <ol>
                    <li><strong>Загрузка изображения</strong> → Текстура накладывается на внутреннюю поверхность сферы</li>
                    <li><strong>Камера в центре</strong> → Пользователь находится внутри сферы</li>
                    <li><strong>Вращение камеры</strong> → Осмотр панорамы на 360°</li>
                    <li><strong>VR режим</strong> → Передача управления головному трекеру</li>
                </ol>
            </div>

            <div class="section">
                <h2>🚀 Как использовать</h2>
                
                <h3>Быстрый старт</h3>
                
                <div class="code-block">
# 1. Запустите сервер<br>
python main.py<br><br>
# 2. Добавьте изображения в папку img/ (JPG, PNG)<br>
# 3. Откройте в браузере<br>
http://localhost:8080
                </div>

                <h3>Управление</h3>
                
                <div class="feature-card">
                    <h4>🎮 В режиме панорам:</h4>
                    <ul class="controls-list">
                        <li><span class="key">←</span> <span class="key">→</span> или кнопки - переключение изображений</li>
                        <li>Мышь + перемещение - осмотр панорамы</li>
                        <li>VR кнопка - вход в виртуальную реальность</li>
                        <li><span class="key">Escape</span> - возврат в меню</li>
                    </ul>
                </div>

                <div class="feature-card">
                    <h4>🕶️ В VR режиме:</h4>
                    <ul class="controls-list">
                        <li>Поворот головы - осмотр окружения</li>
                        <li>VR контроллеры - навигация</li>
                    </ul>
                </div>
            </div>

            <div class="section">
                <h2>📁 Структура проекта</h2>
                
                <div class="file-structure">
                    <div class="file-item"><span class="file-icon">📄</span> main.py                 # Python HTTP сервер</div>
                    <div class="file-item"><span class="file-icon">📄</span> main.html              # Главное меню</div>
                    <div class="file-item"><span class="file-icon">📄</span> panorams.html          # Просмотр панорам (Three.js)</div>
                    <div class="file-item"><span class="file-icon">📄</span> 404.html               # Страница ошибки</div>
                    <div class="file-item"><span class="file-icon">📁</span> img/                   # Папка для изображений</div>
                    <div class="file-item" style="padding-left: 40px;"><span class="file-icon">🖼️</span> panorama1.jpg</div>
                    <div class="file-item" style="padding-left: 40px;"><span class="file-icon">🖼️</span> panorama2.jpg</div>
                    <div class="file-item" style="padding-left: 40px;"><span class="file-icon">🖼️</span> ...</div>
                </div>
            </div>

            <div class="section">
                <h2>🌐 API endpoints</h2>
                
                <table class="api-table">
                    <thead>
                        <tr>
                            <th>Endpoint</th>
                            <th>Метод</th>
                            <th>Описание</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><code>/</code></td>
                            <td>GET</td>
                            <td>Главное меню</td>
                        </tr>
                        <tr>
                            <td><code>/panorams</code></td>
                            <td>GET</td>
                            <td>Страница просмотра панорам</td>
                        </tr>
                        <tr>
                            <td><code>/games</code></td>
                            <td>GET</td>
                            <td>Заглушка (в разработке)</td>
                        </tr>
                        <tr>
                            <td><code>/api/images</code></td>
                            <td>GET</td>
                            <td>JSON список изображений из папки <code>img/</code></td>
                        </tr>
                    </tbody>
                </table>

                <h3>Пример ответа <code>/api/images</code></h3>
                <div class="code-block">
[<br>
  "/img/panorama1.jpg",<br>
  "/img/panorama2.jpg", <br>
  "/img/panorama3.png"<br>
]
                </div>
            </div>

            <div class="section">
                <h2>🛠️ Технические детали</h2>
                
                <div class="features-grid">
                    <div class="feature-card">
                        <h4>⚙️ Требования:</h4>
                        <ul>
                            <li>Python 3.6+</li>
                            <li>Браузер с WebGL поддержкой</li>
                            <li>Для VR: WebXR-совместимый браузер</li>
                        </ul>
                    </div>
                    <div class="feature-card">
                        <h4>📊 Поддерживаемые форматы:</h4>
                        <ul>
                            <li>Изображения: JPG, JPEG, PNG</li>
                            <li>3D графика: Three.js (WebGL)</li>
                            <li>VR: WebXR API</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <div class="footer">
            <p><strong>Сделано с ❤️ и Three.js</strong></p>
        </div>
    </div>
</body>
</html>