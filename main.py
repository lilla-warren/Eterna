import flet as ft
from screens.splash import SplashScreen

async def main(page: ft.Page):
    # Configure the page
    page.title = "ETERNA - UAE Energy Companion"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Start with splash screen
    SplashScreen(page).show()

# Run the app
if __name__ == "__main__":
    ft.app(target=main)
