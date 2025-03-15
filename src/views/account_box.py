from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class AccountBox(Label):
    def __init__(self, color, amount, **kwargs):
        super(AccountBox, self).__init__(**kwargs)
        self.text = f'BANK\n${amount}'
        self.color = (1, 1, 1, 1)  # White text
        self.size_hint = (1, 1)
        self.halign = 'center'
        self.valign = 'middle'
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
