from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def __init__(self, text: str, color: tuple(int, int, int)) -> None:
        self.color = color
        self.text = text
    
    def set_text(self, text: str):
        self.text = text
    def get_text(self) -> str:
        return self.text
    def set_color(self, color: tuple(int, int, int)):
        self.color = color
    def get_color(self) -> tuple(int, int, int):
        return self.color
        
    @abstractmethod
    def on_hover(self):
        pass
    
    @abstractmethod
    def on_click(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass
    