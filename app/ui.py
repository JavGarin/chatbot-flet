import flet
from flet import Page, TextField, ElevatedButton, Column, Text, Container, Colors, Dropdown, dropdown
from app.chatbot import get_response

def main(page: Page):
    page.title = "Chatbot con flet y OpenAI"
    page.bgcolor = Colors.BLUE_GREY_900
    page.theme_mode = "dark"

    input_box = TextField(
        label="Escribe tu mensaje",
        border_color=Colors.BLUE_200,
        focused_border_color=Colors.BLUE_400,
        text_style=flet.TextStyle(color=Colors.WHITE),
        expand=True
    )

    mode_dropdown = Dropdown(
        options=[
            dropdown.Option("chat", "Chat con IA"),
            dropdown.Option("weather", "Consultar Clima")
        ],
        value="chat",
        label="Modo",
        border_color=Colors.BLUE_200,
        color=Colors.WHITE
    )

    chat_area = Column(scroll='auto', expand=True)

    def send_message(e):
        user_message = input_box.value
        if not user_message:
            return
        
        # Mostrar mensaje del usuario
        chat_area.controls.append(Text(f"Usuario: {user_message}", color=Colors.WHITE))

        # Procesar según el modo seleccionado
        response = get_response(mode_dropdown.value, user_message)

        # Mostrar respuesta
        chat_area.controls.append(Text(f"Chatbot: {response}", color=Colors.BLUE_200))
        
        # Limpiar el input y actualizar UI
        input_box.value = ""
        page.update()

    send_button = ElevatedButton(
        text="Enviar",
        on_click=send_message,
        bgcolor=Colors.BLUE_700,
        color=Colors.WHITE
    )

    chat_container = Container(
        content=chat_area,
        bgcolor=Colors.BLUE_GREY_800,
        padding=10,
        border_radius=10,
        expand=True
    )

    input_container = Container(
        content=flet.Row(
            controls=[
                mode_dropdown,
                input_box,
                send_button
            ],
            spacing=10
        )
    )

    page.add(
        chat_container,
        input_container
    )

    page.window.width = 800
    page.window.height = 600
    page.update()
