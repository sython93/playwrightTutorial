

class HomePage:

    def __init__(self, page):
        self.stock_dropdown = page.get_by_role("button", name="Stock >")
        self.dynamic_toggle = page.get_by_role("button", name="Dynamic")
        self.ctrlk_button = page.get_by_role("button", name="Ctrl+K")

