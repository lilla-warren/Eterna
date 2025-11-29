import flet as ft
import asyncio

class SplashScreen:
    def __init__(self, page):
        self.page = page
    
    def show(self):
        # Premium gradient background like diagnostics app
        splash_content = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#0F4C81", "#1a237e", "#283593"]
            ),
            content=ft.Stack([
                # Background pattern
                ft.Container(
                    content=ft.Text("⚡", size=120, opacity=0.1),
                    alignment=ft.alignment.center
                ),
                
                # Main content
                ft.Column([
                    ft.Container(height=120),
                    
                    # Premium logo area
                    ft.Container(
                        content=ft.Column([
                            ft.Container(
                                content=ft.Icon(ft.icons.BAR_CHART, size=48, color="white"),
                                padding=20,
                                bgcolor="#22C55E",
                                border_radius=25,
                                shadow=ft.BoxShadow(
                                    spread_radius=2,
                                    blur_radius=15,
                                    color=ft.colors.BLACK38,
                                )
                            ),
                            ft.Container(height=20),
                            ft.Text("ETERNA", size=42, weight=ft.FontWeight.BOLD, color="white"),
                            ft.Text("ENERGY INTELLIGENCE PLATFORM", size=16, color="white70", letter_spacing=2),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        alignment=ft.alignment.center
                    ),
                    
                    ft.Container(height=80),
                    
                    # Loading with stats preview
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Initializing AI Analysis...", size=14, color="white70"),
                            ft.Container(height=10),
                            ft.ProgressBar(width=280, color="#22C55E", bgcolor="#1E6BA1"),
                            ft.Container(height=20),
                            ft.Row([
                                ft.Column([
                                    ft.Text("87%", size=18, weight=ft.FontWeight.BOLD, color="white"),
                                    ft.Text("Accuracy", size=12, color="white70"),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                ft.VerticalDivider(color="white30", height=30),
                                ft.Column([
                                    ft.Text("2.1k", size=18, weight=ft.FontWeight.BOLD, color="white"),
                                    ft.Text("Homes", size=12, color="white70"),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                ft.VerticalDivider(color="white30", height=30),
                                ft.Column([
                                    ft.Text("AED 427", size=18, weight=ft.FontWeight.BOLD, color="white"),
                                    ft.Text("Avg Savings", size=12, color="white70"),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        alignment=ft.alignment.center
                    ),
                    
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ]),
            width=self.page.width,
            height=self.page.height,
            padding=30
        )
        
        self.page.clean()
        self.page.add(splash_content)
        self.page.update()
        
        # Smooth transition
        async def navigate():
            await asyncio.sleep(3)
            from screens.dashboard import DashboardScreen
            DashboardScreen(self.page).show()
        
        asyncio.create_task(navigate())
