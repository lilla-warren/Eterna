import flet as ft
import asyncio

class SplashScreen:
    def __init__(self, page):
        self.page = page
    
    def show(self):
        # Splash screen content
        splash_content = ft.Container(
            content=ft.Column([
                ft.Text("ETERNA", size=40, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text("Smarter Energy. Lower Bills. Happier Homes.", size=16, color="white"),
                ft.ProgressBar(width=200, color="white")
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            width=self.page.width,
            height=self.page.height,
            bgcolor="#0F4C81"
        )
        
        self.page.clean()
        self.page.add(splash_content)
        self.page.update()
        
        # Use async timer instead of time.sleep
        async def navigate_to_onboarding():
            await asyncio.sleep(2)
            from screens.onboarding import OnboardingScreen
            OnboardingScreen(self.page).show()
        
        # Start the async task
        asyncio.create_task(navigate_to_onboarding())
