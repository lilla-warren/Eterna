import flet as ft

class OnboardingScreen:
    def __init__(self, page):
        self.page = page
        self.current_step = 0
        self.onboarding_screens = [
            {
                "title": "Your UAE Energy Companion",
                "content": "Smart AC advice, bill predictions, and real-time alerts for your home",
                "icon": "🏠"
            },
            {
                "title": "Predict Bills Before They Arrive", 
                "content": "No more bill shock. Know your costs in advance",
                "icon": "📊"
            },
            {
                "title": "Save Money Without Reducing Comfort",
                "content": "Optimize your energy usage while keeping your family comfortable", 
                "icon": "💸"
            }
        ]
    
    def show(self):
        current_screen = self.onboarding_screens[self.current_step]
        
        content = ft.Container(
            content=ft.Column([
                # Progress dots
                ft.Row([
                    ft.Container(width=20, height=5, bgcolor="blue" if i <= self.current_step else "grey", border_radius=5)
                    for i in range(len(self.onboarding_screens))
                ], alignment=ft.MainAxisAlignment.CENTER),
                
                # Main content
                ft.Container(height=100),
                ft.Text(current_screen["icon"], size=60),
                ft.Text(current_screen["title"], size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text(current_screen["content"], size=16, text_align=ft.TextAlign.CENTER),
                ft.Container(height=50),
                
                # Navigation buttons
                ft.Row([
                    ft.TextButton("Skip", on_click=lambda _: self.go_to_dashboard()),
                    ft.Container(width=20),
                    ft.ElevatedButton(
                        "Next" if self.current_step < len(self.onboarding_screens)-1 else "Get Started",
                        on_click=lambda _: self.next_screen()
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            padding=40
        )
        
        self.page.clean()
        self.page.add(content)
        self.page.update()
    
    def next_screen(self):
        if self.current_step < len(self.onboarding_screens) - 1:
            self.current_step += 1
            self.show()
        else:
            self.go_to_dashboard()
    
    def go_to_dashboard(self):
        from screens.dashboard import DashboardScreen
        DashboardScreen(self.page).show()
