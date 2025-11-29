import flet as ft

class OnboardingScreen:
    def __init__(self, page):
        self.page = page
        self.current_step = 0
        self.onboarding_screens = [
            {
                "title": "Predict Your DEWA Bills",
                "content": "AI-powered bill forecasting so you never face bill shock again",
                "icon": "📊",
                "color": "#0F4C81"
            },
            {
                "title": "Smart AC Optimization", 
                "content": "Reduce AC costs by 30% while maintaining perfect comfort",
                "icon": "🌡️",
                "color": "#22C55E"
            },
            {
                "title": "UAE Energy Intelligence",
                "content": "Cultural pattern recognition for Ramadan, summer, and family life", 
                "icon": "🇦🇪",
                "color": "#F59E0B"
            }
        ]
    
    def show(self):
        current = self.onboarding_screens[self.current_step]
        
        content = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#F8FAFC", "#FFFFFF"]
            ),
            content=ft.Column([
                # Progress indicator
                ft.Container(
                    content=ft.Row([
                        ft.Container(
                            width=30, height=4, 
                            bgcolor=current["color"] if i == self.current_step else "#E2E8F0",
                            border_radius=2
                        ) for i in range(len(self.onboarding_screens))
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    padding=ft.padding.only(top=40, bottom=20)
                ),
                
                # Main content
                ft.Container(
                    content=ft.Column([
                        ft.Container(height=60),
                        ft.Text(current["icon"], size=80),
                        ft.Container(height=20),
                        ft.Text(current["title"], size=28, weight=ft.FontWeight.BOLD, 
                               color="#1E293B", text_align=ft.TextAlign.CENTER),
                        ft.Container(height=15),
                        ft.Text(current["content"], size=16, color="#64748B", 
                               text_align=ft.TextAlign.CENTER),
                        ft.Container(height=60),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=40
                ),
                
                # Navigation - FIXED BUTTONS
                ft.Container(
                    content=ft.Row([
                        ft.TextButton(
                            "Skip", 
                            on_click=lambda e: self.go_to_dashboard(),
                            style=ft.ButtonStyle(color="#64748B")
                        ),
                        ft.Container(width=20),
                        ft.ElevatedButton(
                            "Next" if self.current_step < 2 else "Get Started",
                            on_click=lambda e: self.next_screen(),
                            style=ft.ButtonStyle(
                                bgcolor=current["color"],
                                padding=ft.padding.symmetric(horizontal=30, vertical=15)
                            )
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    padding=20
                )
            ]),
            width=self.page.width,
            height=self.page.height,
        )
        
        self.page.clean()
        self.page.add(content)
        self.page.update()
    
    def next_screen(self):
        if self.current_step < 2:
            self.current_step += 1
            self.show()
        else:
            self.go_to_dashboard()
    
    def go_to_dashboard(self):
        from screens.dashboard import DashboardScreen
        DashboardScreen(self.page).show()
