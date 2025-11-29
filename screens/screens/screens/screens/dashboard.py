import flet as ft
import random
from datetime import datetime, timedelta

class DashboardScreen:
    def __init__(self, page):
        self.page = page
        self.current_usage = random.randint(1200, 1800)
        self.bill_prediction = self.calculate_prediction()
        self.savings_data = self.generate_savings_data()
    
    def calculate_prediction(self):
        base = 420
        seasonal = 180
        return base + seasonal + random.randint(-60, 60)
    
    def generate_savings_data(self):
        return [random.randint(200, 500) for _ in range(6)]
    
    def show(self):
        header = ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Text("ENERGY DASHBOARD", size=12, color="#64748B", weight=ft.FontWeight.BOLD, letter_spacing=1),
                    ft.Text("Al Falasi Residence • Dubai Hills", size=16, weight=ft.FontWeight.BOLD, color="#1E293B"),
                ], expand=True),
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.icons.ACCOUNT_CIRCLE,
                        icon_size=32,
                        icon_color="#0F4C81",
                        on_click=lambda _: self.open_profile()
                    ),
                    padding=8,
                    bgcolor="#F1F5F9",
                    border_radius=20
                )
            ]),
            padding=ft.padding.symmetric(horizontal=24, vertical=20),
            bgcolor="white",
            border=ft.border.only(bottom=ft.border.BorderSide(1, "#E2E8F0"))
        )
        
        content = ft.Column([
            header,
            
            # Row 1: Key Metrics
            ft.Container(
                content=ft.Row([
                    self._build_metric_card("Current Load", f"{self.current_usage}W", "⚡", "#F59E0B", "12% ↑ from avg", self.show_usage_details),
                    self._build_metric_card("Bill Forecast", f"AED {self.bill_prediction}", "💰", "#EF4444", "Due Jun 15", self.show_bill_details),
                    self._build_metric_card("CO₂ Saved", "24.8 kg", "🌱", "#22C55E", "3.2 trees", self.show_sustainability),
                ], spacing=12),
                padding=ft.padding.symmetric(horizontal=24, vertical=16)
            ),
            
            # Row 2: Usage Visualization
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("ENERGY CONSUMPTION", size=12, color="#64748B", weight=ft.FontWeight.BOLD, expand=True),
                        ft.Container(
                            content=ft.TextButton(
                                "Last 6 Months",
                                on_click=lambda _: self.show_analytics()
                            ),
                            bgcolor="#F1F5F9",
                            padding=ft.padding.symmetric(horizontal=12, vertical=6),
                            border_radius=12
                        )
                    ]),
                    ft.Container(height=16),
                    self._build_usage_chart(),
                ]),
                padding=20,
                bgcolor="white",
                margin=ft.margin.symmetric(horizontal=24),
                border_radius=16,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color=ft.colors.BLACK12,
                )
            ),
            
            # Row 3: Quick Actions & AI Insights
            ft.Container(
                content=ft.Row([
                    self._build_quick_action("Optimize Now", ft.icons.BOLT, "#22C55E", "Save AED 85", self.activate_savings),
                    self._build_quick_action("AC Analysis", ft.icons.AC_UNIT, "#0F4C81", "70% of usage", self.show_ac_analysis),
                    self._build_quick_action("Peak Alert", ft.icons.WARNING, "#F59E0B", "2PM-8PM", self.show_peak_alerts),
                ], spacing=12),
                padding=ft.padding.symmetric(horizontal=24, vertical=16)
            ),
            
            # Row 4: AI Insights Card
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("AI ENERGY INSIGHTS", size=12, color="#64748B", weight=ft.FontWeight.BOLD, expand=True),
                        ft.Icon(ft.icons.AUTO_AWESOME, size=16, color="#0F4C81")
                    ]),
                    ft.Container(height=12),
                    self._build_insight_item("AC units running 4+ hours continuously", "Optimize cycling to save AED 120/mo", self.show_insight_details),
                    ft.Divider(height=1, color="#F1F5F9"),
                    self._build_insight_item("Peak hour usage increased 23%", "Shift laundry to morning for AED 65 savings", self.show_insight_details),
                    ft.Divider(height=1, color="#F1F5F9"),
                    self._build_insight_item("Standby power: AED 45 monthly", "Smart plugs can reduce by 80%", self.show_insight_details),
                ]),
                padding=20,
                bgcolor="white",
                margin=ft.margin.symmetric(horizontal=24),
                border_radius=16,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color=ft.colors.BLACK12,
                )
            ),
            
            # Navigation - Premium bottom bar
            ft.Container(
                content=ft.Row([
                    self._build_nav_item(ft.icons.DASHBOARD, "Dashboard", True, lambda _: print("Already on dashboard")),
                    self._build_nav_item(ft.icons.ANALYTICS, "Analytics", False, lambda _: self.show_analytics()),
                    ft.Container(
                        content=ft.IconButton(
                            icon=ft.icons.ADD,
                            icon_size=24,
                            icon_color="white",
                            on_click=lambda _: self.quick_action()
                        ),
                        padding=16,
                        bgcolor="#0F4C81",
                        border_radius=25,
                        shadow=ft.BoxShadow(
                            spread_radius=2,
                            blur_radius=15,
                            color=ft.colors.BLACK26,
                        )
                    ),
                    self._build_nav_item(ft.icons.SAVINGS, "Savings", False, lambda _: self.activate_savings()),
                    self._build_nav_item(ft.icons.SETTINGS, "Settings", False, lambda _: self.open_settings()),
                ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                padding=16,
                bgcolor="white",
                border=ft.border.only(top=ft.border.BorderSide(1, "#E2E8F0"))
            )
            
        ], spacing=0)
        
        self.page.clean()
        self.page.add(content)
        self.page.update()
    
    def _build_metric_card(self, title, value, icon, color, subtitle, on_click):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(icon, size=16),
                    ft.Container(expand=True),
                    ft.Container(
                        content=ft.Text("···", size=12, color=color),
                        padding=4,
                        bgcolor=f"{color}20",
                        border_radius=6
                    )
                ]),
                ft.Container(height=8),
                ft.Text(value, size=18, weight=ft.FontWeight.BOLD, color="#1E293B"),
                ft.Text(title, size=12, color="#64748B"),
                ft.Container(height=4),
                ft.Text(subtitle, size=10, color=color, weight=ft.FontWeight.BOLD),
            ]),
            padding=16,
            bgcolor="white",
            expand=True,
            border_radius=12,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.BLACK10,
            ),
            on_click=on_click
        )
    
    def _build_usage_chart(self):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        values = self.savings_data
        
        bars = []
        max_val = max(values)
        
        for i, (month, value) in enumerate(zip(months, values)):
            height = (value / max_val) * 60
            color = "#0F4C81" if i == len(months)-1 else "#CBD5E1"
            
            bars.append(
                ft.Column([
                    ft.Text(f"AED {value}", size=10, color="#64748B"),
                    ft.Container(height=4),
                    ft.Container(
                        width=20,
                        height=height,
                        bgcolor=color,
                        border_radius=4
                    ),
                    ft.Container(height=4),
                    ft.Text(month, size=10, color="#64748B"),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
            )
        
        return ft.Row(bars, alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    
    def _build_quick_action(self, text, icon, color, subtitle, on_click):
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Icon(icon, size=20, color=color),
                    padding=12,
                    bgcolor=f"{color}20",
                    border_radius=12
                ),
                ft.Container(height=8),
                ft.Text(text, size=12, weight=ft.FontWeight.BOLD, color="#1E293B", text_align=ft.TextAlign.CENTER),
                ft.Text(subtitle, size=10, color=color, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=12,
            bgcolor="white",
            expand=True,
            border_radius=12,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.colors.BLACK10,
            ),
            on_click=on_click
        )
    
    def _build_insight_item(self, title, description, on_click):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(ft.icons.TRENDING_UP, size=16, color="#0F4C81"),
                    padding=8,
                    bgcolor="#F1F5F9",
                    border_radius=8
                ),
                ft.Container(width=12),
                ft.Column([
                    ft.Text(title, size=14, color="#1E293B", weight=ft.FontWeight.BOLD),
                    ft.Text(description, size=12, color="#64748B"),
                ], expand=True),
                ft.Icon(ft.icons.CHEVRON_RIGHT, size=16, color="#CBD5E1")
            ]),
            padding=ft.padding.symmetric(vertical=8),
            on_click=on_click
        )
    
    def _build_nav_item(self, icon, label, active, on_click):
        color = "#0F4C81" if active else "#94A3B8"
        return ft.Container(
            content=ft.Column([
                ft.IconButton(
                    icon=icon,
                    icon_size=24,
                    icon_color=color,
                    on_click=on_click
                ),
                ft.Text(label, size=10, color=color)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2),
            on_click=on_click
        )

    # === CLICK HANDLERS ===
    
    def activate_savings(self, e=None):
        from screens.savings import SavingsScreen
        SavingsScreen(self.page).show()
    
    def show_analytics(self, e=None):
        self.show_snackbar("📊 Opening Analytics...")
    
    def show_ac_analysis(self, e=None):
        self.show_snackbar("🌡️ AC Analysis Loading...")
    
    def show_peak_alerts(self, e=None):
        self.show_snackbar("⚠️ Peak Alert Details...")
    
    def show_usage_details(self, e=None):
        self.show_snackbar("⚡ Usage Details...")
    
    def show_bill_details(self, e=None):
        self.show_snackbar("💰 Bill Forecast Details...")
    
    def show_sustainability(self, e=None):
        self.show_snackbar("🌱 Sustainability Report...")
    
    def show_insight_details(self, e=None):
        self.show_snackbar("🤖 AI Insight Details...")
    
    def open_profile(self, e=None):
        self.show_snackbar("👤 Profile Settings...")
    
    def open_settings(self, e=None):
        self.show_snackbar("⚙️ Opening Settings...")
    
    def quick_action(self, e=None):
        self.show_snackbar("🚀 Quick Action Menu...")
    
    def show_snackbar(self, message):
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(message),
            bgcolor="#0F4C81"
        )
        self.page.snack_bar.open = True
        self.page.update()
            # Row 3: Quick Actions & AI Insights
            ft.Container(
                content=ft.Row([
                    self._build_quick_action("Optimize Now", ft.icons.BOLT, "#22C55E", "Save AED 85"),
                    self._build_quick_action("AC Analysis", ft.icons.AC_UNIT, "#0F4C81", "70% of usage"),
                    self._build_quick_action("Peak Alert", ft.icons.WARNING, "#F59E0B", "2PM-8PM"),
                ], spacing=12),
                padding=ft.padding.symmetric(horizontal=24, vertical=16)
            ),
            
            # Row 4: AI Insights Card
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("AI ENERGY INSIGHTS", size=12, color="#64748B", weight=ft.FontWeight.BOLD, expand=True),
                        ft.Icon(ft.icons.AUTO_AWESOME, size=16, color="#0F4C81")
                    ]),
                    ft.Container(height=12),
                    self._build_insight_item("AC units running 4+ hours continuously", "Optimize cycling to save AED 120/mo"),
                    ft.Divider(height=1, color="#F1F5F9"),
                    self._build_insight_item("Peak hour usage increased 23%", "Shift laundry to morning for AED 65 savings"),
                    ft.Divider(height=1, color="#F1F5F9"),
                    self._build_insight_item("Standby power: AED 45 monthly", "Smart plugs can reduce by 80%"),
                ]),
                padding=20,
                bgcolor="white",
                margin=ft.margin.symmetric(horizontal=24),
                border_radius=16,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color=ft.colors.BLACK12,
                )
            ),
            
            # Navigation - Premium bottom bar
            ft.Container(
                content=ft.Row([
                    self._build_nav_item(ft.icons.DASHBOARD, "Dashboard", True),
                    self._build_nav_item(ft.icons.ANALYTICS, "Analytics", False),
                    ft.Container(
                        content=ft.Icon(ft.icons.ADD, size=24, color="white"),
                        padding=16,
                        bgcolor="#0F4C81",
                        border_radius=25,
                        shadow=ft.BoxShadow(
                            spread_radius=2,
                            blur_radius=15,
                            color=ft.colors.BLACK26,
                        )
                    ),
                    self._build_nav_item(ft.icons.SAVINGS, "Savings", False),
                    self._build_nav_item(ft.icons.SETTINGS, "Settings", False),
                ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                padding=16,
                bgcolor="white",
                border=ft.border.only(top=ft.border.BorderSide(1, "#E2E8F0"))
            )
            
        ], spacing=0)
        
        self.page.clean()
        self.page.add(content)
        self.page.update()
    
    def _build_metric_card(self, title, value, icon, color, subtitle):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(icon, size=16),
                    ft.Container(expand=True),
                    ft.Container(
                        content=ft.Text("···", size=12, color=color),
                        padding=4,
                        bgcolor=f"{color}20",
                        border_radius=6
                    )
                ]),
                ft.Container(height=8),
                ft.Text(value, size=18, weight=ft.FontWeight.BOLD, color="#1E293B"),
                ft.Text(title, size=12, color="#64748B"),
                ft.Container(height=4),
                ft.Text(subtitle, size=10, color=color, weight=ft.FontWeight.BOLD),
            ]),
            padding=16,
            bgcolor="white",
            expand=True,
            border_radius=12,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.BLACK10,
            )
        )
    
    def _build_usage_chart(self):
        # Simple bar chart simulation
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        values = self.savings_data
        
        bars = []
        max_val = max(values)
        
        for i, (month, value) in enumerate(zip(months, values)):
            height = (value / max_val) * 60
            color = "#0F4C81" if i == len(months)-1 else "#CBD5E1"
            
            bars.append(
                ft.Column([
                    ft.Text(f"AED {value}", size=10, color="#64748B"),
                    ft.Container(height=4),
                    ft.Container(
                        width=20,
                        height=height,
                        bgcolor=color,
                        border_radius=4
                    ),
                    ft.Container(height=4),
                    ft.Text(month, size=10, color="#64748B"),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
            )
        
        return ft.Row(bars, alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    
    def _build_quick_action(self, text, icon, color, subtitle):
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Icon(icon, size=20, color=color),
                    padding=12,
                    bgcolor=f"{color}20",
                    border_radius=12
                ),
                ft.Container(height=8),
                ft.Text(text, size=12, weight=ft.FontWeight.BOLD, color="#1E293B", text_align=ft.TextAlign.CENTER),
                ft.Text(subtitle, size=10, color=color, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=12,
            bgcolor="white",
            expand=True,
            border_radius=12,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.colors.BLACK10,
            )
        )
    
    def _build_insight_item(self, title, description):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(ft.icons.TRENDING_UP, size=16, color="#0F4C81"),
                    padding=8,
                    bgcolor="#F1F5F9",
                    border_radius=8
                ),
                ft.Container(width=12),
                ft.Column([
                    ft.Text(title, size=14, color="#1E293B", weight=ft.FontWeight.BOLD),
                    ft.Text(description, size=12, color="#64748B"),
                ], expand=True),
                ft.Icon(ft.icons.CHEVRON_RIGHT, size=16, color="#CBD5E1")
            ]),
            padding=ft.padding.symmetric(vertical=8)
        )
    
    def _build_nav_item(self, icon, label, active):
        color = "#0F4C81" if active else "#94A3B8"
        return ft.Column([
            ft.Icon(icon, size=24, color=color),
            ft.Text(label, size=10, color=color)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
