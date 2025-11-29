import flet as ft
from screens.splash import SplashScreen

def main(page: ft.Page):
    # Diagnostics-level professional setup
    page.title = "ETERNA • UAE Energy Intelligence Platform"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#0F4C81",
            secondary="#22C55E",
            tertiary="#F59E0B",
            surface=ft.colors.WHITE,
            on_primary=ft.colors.WHITE,
        ),
        font_family="Inter"
    )
    
    page.padding = 0
    page.spacing = 0
    
    # Start with premium splash
    SplashScreen(page).show()

if __name__ == "__main__":
    ft.app(target=main)
    
