import flet as ft
from screens.splash import SplashScreen

def main(page: ft.Page):
    # Professional page setup
    page.title = "ETERNA - UAE Energy Intelligence"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#0F4C81",
            secondary="#22C55E", 
            on_primary=ft.colors.WHITE,
        )
    )
    page.padding = 0
    page.fonts = {
        "Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap"
    }
    page.theme = ft.Theme(font_family="Poppins")
    
    # Start with splash screen
    SplashScreen(page).show()

if __name__ == "__main__":
    ft.app(target=main)
