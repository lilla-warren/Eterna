import flet as ft

class SavingsScreen:
    def __init__(self, page):
        self.page = page
    
    def show(self):
        header = ft.Container(
            content=ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: self.go_back()),
                ft.Text("Savings Mode", size=20, weight=ft.FontWeight.BOLD, expand=True),
                ft.IconButton(ft.icons.INFO_OUTLINED, icon_color="#64748B")
            ]),
            padding=20
        )
        
        # Savings Impact Card
        impact_card = ft.Container(
            content=ft.Column([
                ft.Text("Potential Monthly Savings", size=16, weight=ft.FontWeight.BOLD, color="#1E293B"),
                ft.Container(height=10),
                ft.Text("AED 245", size=32, weight=ft.FontWeight.BOLD, color="#22C55E"),
                ft.Text("25% reduction from current usage", size=14, color="#64748B"),
            ]),
            padding=20,
            bgcolor="#F0FDF4",
            border_radius=16,
            border=ft.border.all(1, "#22C55E20")
        )
        
        # Recommendations
        recommendations = ft.Container(
            content=ft.Column([
                ft.Text("Recommended Actions", size=18, weight=ft.FontWeight.BOLD, color="#1E293B"),
                ft.Container(height=15),
                self._build_recommendation("Set AC to 24°C", "Save AED 120/month", ft.icons.AC_UNIT),
                self._build_recommendation("Optimize peak hours", "Save AED 85/month", ft.icons.SCHEDULE),
                self._build_recommendation("Reduce standby power", "Save AED 40/month", ft.icons.POWER),
            ]),
            padding=20,
            bgcolor="white",
            border_radius=16,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.BLACK12,
            )
        )
        
        # Activation Options
        activation_title = ft.Container(
            content=ft.Text("Activate For:", size=16, weight=ft.FontWeight.BOLD, color="#1E293B"),
            padding=ft.padding.only(left=20, top=20, bottom=10)
        )
        
        activation_options = ft.Row([
            self._build_activation_option("2 Hours", "Quick save"),
            self._build_activation_option("Until 8 PM", "Evening optimization"),
            self._build_activation_option("24 Hours", "Full day savings"),
        ], spacing=10)
        
        content = ft.Column([
            header,
            ft.Container(height=10),
            impact_card,
            ft.Container(height=20),
            recommendations,
            ft.Container(height=20),
            activation_title,
            activation_options,
        ], spacing=0)
        
        self.page.clean()
        self.page.add(content)
        self.page.update()
    
    def _build_recommendation(self, title, savings, icon):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color="#0F4C81"),
                ft.Column([
                    ft.Text(title, size=16, color="#1E293B"),
                    ft.Text(savings, size=14, color="#22C55E"),
                ], expand=True),
                ft.Switch(value=False, active_color="#22C55E")
            ]),
            padding=ft.padding.symmetric(vertical=12)
        )
    
    def _build_activation_option(self, duration, description):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Column([
                    ft.Text(duration, size=16, weight=ft.FontWeight.BOLD, color="#0F4C81"),
                    ft.Text(description, size=12, color="#64748B"),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                on_click=lambda _: self.activate_savings(duration),
                style=ft.ButtonStyle(
                    bgcolor="#F8FAFC",
                    color="#0F4C81",
                    padding=15,
                    shape=ft.RoundedRectangleBorder(radius=12)
                )
            ),
            expand=True
        )
    
    def activate_savings(self, duration):
        # Show success
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"💰 Savings mode activated for {duration}!"),
            bgcolor="#22C55E"
        )
        self.page.snack_bar.open = True
        self.page.update()
        
        # Return to dashboard after delay
        import asyncio
        async def return_to_dashboard():
            await asyncio.sleep(2)
            self.go_back()
        
        asyncio.create_task(return_to_dashboard())
    
    def go_back(self):
        from screens.dashboard import DashboardScreen
        DashboardScreen(self.page).show()
