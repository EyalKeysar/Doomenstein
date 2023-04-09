from Button import Button

class MenuButton(Button):
    def __init__(self, text: str, color: tuple[int, int, int]) -> None:
        super().__init__(text, color)
    
    def on_hover(self):
        pass
    
    def on_click(self):
        pass
    
    def draw(self):
        pass