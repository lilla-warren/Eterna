import flet as ft

class SavingsScreen:
    def __init__(self, page):
        self.page = page
    
    def show(self):
        content = ft.Column([
            ft.Text("Savings Mode", size=24, weight=ft.FontWeight.BOLD),
            
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Recommended Actions", size=18, weight=ft.FontWeight.BOLD),
                        ft.Divider(),
                        ft.Row([ft.Icon(ft.icons.AC_UNIT), ft.Text("Set AC to 24°C")]),
                        ft.Row([ft.Icon(ft.icons.DISHWASHER), ft.Text("Delay dishwasher until 8 PM")]),
                        ft.Row([ft.Icon(ft.icons.TV), ft.Text("Turn off idle electronics")]),
                    ]),
                    padding=20
                )
            ),
            
            ft.Text("Activate for:", size=16),
            ft.Row([
                ft.ElevatedButton("2 Hours", on_click=lambda _: self.activate_savings(2)),
                ft.ElevatedButton("Until Midnight", on_click=lambda _: self.activate_savings(6)),
                ft.ElevatedButton("Custom", on_click=lambda _: self.activate_savings(0)),
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
            
            ft.TextButton("Back to Dashboard", on_click=lambda _: self.back_to_dashboard())
        ])
        
        self.page.clean()
        self.page.add(content)
        self.page.update()
    
    def activate_savings(self, hours):
        # Show success message
        self.page.snack_bar = ft.SnackBar(content=ft.Text(f"Savings mode activated for {hours} hours!"))
        self.page.snack_bar.open = True
        self.page.update()
    
    def back_to_dashboard(self):
        from screens.dashboard import DashboardScreen
        DashboardScreen(self.page).show()
