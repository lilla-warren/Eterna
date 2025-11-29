import flet as ft

class DashboardScreen:
    def __init__(self, page):
        self.page = page
    
    def show(self):
        # Bill Prediction Card
        bill_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Your next bill is estimated at", color="grey", size=14),
                    ft.Text("AED 425", size=32, weight=ft.FontWeight.BOLD),
                    ft.Row([
                        ft.Icon(ft.icons.ARROW_DOWNWARD, color="green", size=16),
                        ft.Text("12% lower than last month", color="green"),
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20
            ),
            width=300
        )
        
        # Real-time Usage
        usage_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Current Usage", size=16),
                    ft.Row([
                        ft.Icon(ft.icons.BOLT, color="orange"),
                        ft.Text("1.2 kW", size=20, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ]),
                padding=15
            )
        )
        
        # Quick Save Button
        save_button = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.ENERGY_SAVINGS_LEAF),
                ft.Text("Activate Quick Save Mode", size=16)
            ], alignment=ft.MainAxisAlignment.CENTER),
            on_click=lambda _: self.activate_savings(),
            style=ft.ButtonStyle(padding=20, bgcolor="#22C55E")
        )
        
        # Savings Counter
        savings_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Column([
                            ft.Text("CO₂ Saved", size=12),
                            ft.Text("12.4 kg", size=16, weight=ft.FontWeight.BOLD),
                        ]),
                        ft.VerticalDivider(),
                        ft.Column([
                            ft.Text("Money Saved", size=12),
                            ft.Text("AED 67", size=16, weight=ft.FontWeight.BOLD),
                        ]),
                    ])
                ]),
                padding=15
            )
        )
        
        # Navigation
        nav_bar = ft.Row([
            ft.IconButton(ft.icons.HOME, on_click=lambda _: print("Dashboard")),
            ft.IconButton(ft.icons.INSIGHTS, on_click=lambda _: print("Insights")),
            ft.IconButton(ft.icons.NOTIFICATIONS, on_click=lambda _: print("Alerts")),
            ft.IconButton(ft.icons.PERSON, on_click=lambda _: print("Profile")),
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
        
        # Main layout
        content = ft.Column([
            ft.Text("ETERNA Dashboard", size=24, weight=ft.FontWeight.BOLD),
            bill_card,
            ft.Row([usage_card, savings_card], alignment=ft.MainAxisAlignment.SPACE_AROUND),
            save_button,
            ft.Container(height=20),
            nav_bar
        ])
        
        self.page.clean()
        self.page.add(content)
        self.page.update()
    
    def activate_savings(self):
        from screens.savings import SavingsScreen
        SavingsScreen(self.page).show()
