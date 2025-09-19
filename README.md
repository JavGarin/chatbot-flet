# Chatbot Flet 🤖

![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)
![Flet](https://img.shields.io/badge/Flet-Framework-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Aplicación de chatbot de escritorio desarrollada con Python y el framework Flet. Este proyecto demuestra una arquitectura de software modular, escalable y mantenible, ideal para aplicaciones de escritorio modernas.

## ✨ Características

- **Interfaz de Usuario Moderna:** Construida con Flet, permitiendo una experiencia de usuario fluida y atractiva.
- **Arquitectura Modular:** El código está organizado en módulos cohesivos y de bajo acoplamiento, facilitando el mantenimiento y la extensibilidad.
- **Lógica de Chat Desacoplada:** La inteligencia del chatbot está separada de la interfaz de usuario, permitiendo futuras integraciones con diferentes modelos de IA.
- **Herramientas Extensibles:** El sistema de "herramientas" permite agregar nuevas funcionalidades al chatbot de manera sencilla.

## 📸 Screenshot

*Aquí puedes insertar una captura de pantalla de la aplicación en funcionamiento.*

![Screenshot de la App](/assets/chatbot-flet.png)

## 🏗️ Estructura del Proyecto

El proyecto sigue una estructura organizada para promover la escalabilidad y mantenibilidad.

```
chatbot-flet/
├── .venv/                   # Entorno virtual de Python
├── app/                     # Directorio principal de la aplicación
│   ├── __init__.py
│   ├── chatbot.py           # Lógica central y estado del chatbot
│   ├── ui.py                # Componentes y layout de la interfaz de usuario
│   └── tools/               # Módulos de herramientas para el chatbot
│       ├── __init__.py
│       ├── ai_chat.py       # Herramienta para interactuar con un modelo de IA
│       └── weather.py       # Herramienta para consultar el clima
├── .gitignore               # Archivos y carpetas ignorados por Git
├── main.py                  # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación del proyecto
```

### Módulos Clave

- **`main.py`**: Es el punto de entrada que inicializa y ejecuta la aplicación Flet.
- **`app/ui.py`**: Define todos los controles y el layout de la interfaz gráfica. Es responsable de la presentación visual, pero no contiene lógica de negocio.
- **`app/chatbot.py`**: Contiene la clase `Chatbot`, que gestiona el estado de la conversación, procesa los mensajes del usuario y utiliza las herramientas disponibles.
- **`app/tools/`**: Este paquete contiene "herramientas" que el chatbot puede usar. Cada herramienta es un módulo independiente (por ejemplo, `weather.py`), lo que permite agregar nuevas funcionalidades sin modificar el núcleo del chatbot.


## 🛠️ Arquitectura y Buenas Prácticas

Este proyecto fue diseñado pensando en la **escalabilidad** y el **mantenimiento** a largo plazo.

- **Separación de Responsabilidades (SoC):** La interfaz de usuario (`ui.py`), la lógica de negocio (`chatbot.py`) y las funcionalidades específicas (`tools/`) están completamente separadas. Esto permite que un desarrollador pueda modificar la apariencia visual sin tocar la lógica del chatbot, y viceversa.
- **Inyección de Dependencias (Conceptual):** El `Chatbot` recibe las herramientas que necesita, lo que facilita la realización de pruebas unitarias y la adición de nuevas herramientas sin alterar el código existente.
- **Escalabilidad:** Para agregar una nueva función al chatbot (por ejemplo, "buscar en la web"), simplemente se necesita crear un nuevo archivo en el directorio `app/tools/` e implementarla. El sistema está diseñado para descubrir y utilizar estas herramientas de forma dinámica.

## 📄 Licencia

Este proyecto JavGarin está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
