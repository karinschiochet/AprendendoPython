import flet as ft

def main(page: ft.Page):
    page.title = 'Contador'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_number = ft.TextField(value='0', text_align=ft.TextAlign.CENTER, width=100)

    def minus_click(e):
        text_number.value = str(int(text_number.value) - 1)
        text_number.update()

    def plus_click(e):
        text_number.value = str(int(text_number.value) + 1)
        text_number.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.REMOVE, on_click=minus_click),
                text_number,
                ft.IconButton(icon=ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,

        )
    )
    page.update()


ft.app(target=main)