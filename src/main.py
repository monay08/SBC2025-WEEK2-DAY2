import flet as ft

def main(page: ft.Page):
    img = ft.Image(
        src=f"apple.jpg",
        width=45,
        height=45,
        fit=ft.ImageFit.CONTAIN,
    )
    
    page.title = "Apple Product"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME_ROUNDED, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.WECHAT_ROUNDED, label="Chat"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS_ROUNDED, label="Settings"),
        ]
    )
    page.add(
        ft.Row(
            controls=[
                img,
                ft.Text("Apple Product")
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )

ft.app(target=main)