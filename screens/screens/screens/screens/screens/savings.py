import flet as ft

class SavingsScreen:
    def __init__(self, page):
        self.page = page
    
    def show(self):
        header = ft.Container(
            content=ft.Row([
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_color="#64748B",
                    on_click=lambda _: self.go_back()
                ),
                ft.Text("SAVINGS OPTIMIZER", size=16, weight=ft.FontWeight.BOLD, expand=True, color="#1E293B"),
                ft.IconButton(
                    icon=ft.icons.INFO_OUTLINED,
                    icon_color="#64748B",
                    on_click=lambda _: self.show_info()
                )
            ]),
            padding=20,
            bgcolor="white",
            border=ft.border.only(bottom=ft.border.BorderSide(1, "#E2E8F0"))
        )
        
        content = ft.Column([
            header,
            
            # Savings Impact
            ft.Container(
                content=ft.Column([
                    ft.Text("POTENTIAL MONTHLY SAVINGS", size=12, color="#64748B", weight=ft.FontWeight.BOLD),
                    ft.Container(height=10),
                    ft.Text("AED 245", size=42, weight=ft.FontWeight.BOLD, color="#22C55E"),
                    ft.Text("25% reduction from current usage", size=14, color="#64748B"),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.LinearProgressIndicator(
                            value=0.75,
                            color="#22C55E",
                            bgcolor="#E2E8F0"
                        ),
                        height=8,
                        border_radius=4
                    ),
                    ft.Container(height=8),
                    ft.Row([
                        ft.Text("Current", size=12, color="#64748B"),
                        ft.Text("Optimized", size=12, color="#22C55E", weight=ft.FontWeight.BOLD),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ]),
                padding=30,
                bgcolor="#F0FDF4",
                margin=ft.margin.symmetric(horizontal=24, vertical=16),
                border_radius=16,
                border=ft.border.all(1, "#22C55E20")
            ),
            
            # Optimization Options
            ft.Container(
                content=ft.Column([
                    ft.Text("OPTIMIZATION ACTIONS", size=12, color="#64748B", weight=ft.FontWeight.BOLD),
                    ft.Container(height=16),
                    self._build_optimization_option("AC Temperature Optimization", "Set to 24°C during peak hours", "AED 120", True),
                    ft.Divider(height=1, color="#F1F5F9"),
                    self._build_optimization_option("Peak Hour Management", "Shift heavy appliance usage", "AED 85", True),
                    ft.Divider(height=1, color="#F1F5F9"),
                    self._build_optimization_option("Standby Power Reduction", "Smart plug automation", "AED 40", False),
                ]),
                padding=24,
                bgcolor="white",
                margin=ft.margin.symmetric(horizontal=24),
                border_radius=16,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color=ft.colors.BLACK12,
                )
            ),
            
            # Activation Button
            ft.Container(
                content=ft.ElevatedButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.BOLT, color="white"),
                        ft.Text("ACTIVATE ALL OPTIMIZATIONS", size=16, weight=ft.FontWeight.BOLD, color="white"),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    on_click=lambda _: self.activate_all(),
                    style=ft.ButtonStyle(
                        bgcolor="#22C55E",
                        padding=20,
                        shape=ft.RoundedRectangleBorder(radius=12)
                    )
                ),
                padding=ft.padding.symmetric(horizontal=24, vertical=20)
            ),
            
        ], spacing=0)
        
        self.page.clean()
        self.page.add(content)
        self.page.update()
    
    def _build_optimization_option(self, title, description, savings, enabled):
        return ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Text(title, size=16, color="#1E293B", weight=ft.FontWeight.BOLD),
                    ft.Text(description, size=14, color="#64748B"),
                    ft.Container(height=4),
                    ft.Text(savings, size=14, color="#22C55E", weight=ft.FontWeight.BOLD),
                ], expand=True),
                ft.Switch(
                    value=enabled,
                    active_color="#22C55E",
                    on_change=lambda e: self.toggle_optimization(title, e.control.value)
                )
            ]),
            padding=ft.padding.symmetric(vertical=12)
        )
    
    def toggle_optimization(self, title, enabled):
        status = "enabled" if enabled else "disabled"
        self.show_snackbar(f"🔧 {title} {status}")
    
    def activate_all(self):
        self.show_snackbar("🚀 All optimizations activated! Saving AED 245/month")
        
        # Return to dashboard after delay
        import asyncio
        async def return_dashboard():
            await asyncio.sleep(2)
            self.go_back()
        
        asyncio.create_task(return_dashboard())
    
    def show_info(self):
        self.show_snackbar("💡 Savings are calculated based on your usage patterns")
    
    def go_back(self):
        from screens.dashboard import DashboardScreen
        DashboardScreen(self.page).show()
    
    def show_snackbar(self, message):
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(message),
            bgcolor="#0F4C81"
        )
        self.page.snack_bar.open = True
        self.page.update()
