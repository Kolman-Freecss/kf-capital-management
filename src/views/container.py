from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class Container(BoxLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = 10
        self.size_hint = (0.8, 0.5)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.background_color = (1, 1, 1, 1)  # White background
        self.bind(size=self._update_rect, pos=self._update_rect)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
