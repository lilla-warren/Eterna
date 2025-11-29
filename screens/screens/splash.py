import flet as ft
import asyncio

class SplashScreen:
    def __init__(self, page):
        self.page = page
    
    def show(self):
        # Professional splash with UAE aesthetic
        splash_content = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#0F4C81", "#1E6BA1"]
            ),
            content=ft.Column([
                ft.Container(height=100),
                # Logo/Icon area
                ft.Container(
                    content=ft.Icon(ft.icons.ENERGY_SAVINGS_LEAF_OUTLINED, size=80, color="white"),
                    padding=20,
                    border_radius=50,
                    bgcolor="#22C55E"
                ),
                ft.Text("ETERNA", size=48, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text("UAE Energy Intelligence", size=18, color="white70"),
                ft.Container(height=30),
                ft.ProgressBar(width=200, color="white", bgcolor="#1E6BA1"),
                ft.Container(height=100),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            width=self.page.width,
            height=self.page.height,
        )
        
        self.page.clean()
        self.page.add(splash_content)
        self.page.update()
        
        # Navigate after delay
        async def navigate():
            await asyncio.sleep(2)
            from screens.onboarding import OnboardingScreen
            OnboardingScreen(self.page).show()
        
        asyncio.create_task(navigate())
