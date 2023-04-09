from abc import ABC, abstractmethod
from Button import Button

class ButtonGroup(ABC):
    @abstractmethod
    def __init__(self, buttons: list[Button] = []) -> None:
        self.buttons = buttons

    def add_button(self, button: Button) -> None:
        self.buttons.append(button)
    
    def pop_button(self, index: int) -> None:
        self.buttons.pop(index)
        
    def get_buttons(self) -> list[Button]:
        return self.buttons
    
    @abstractmethod
    def draw(self):
        pass
