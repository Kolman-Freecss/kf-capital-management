from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex('#f0f0f0')  # Light gray background

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

class MainApp(App):
    def build(self):
        container = Container(orientation='horizontal')
        container.padding = [10, 10, 10, 10]
        container.size_hint = (0.8, 0.5)
        container.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Account data (color, amount)
        accounts = [
            (get_color_from_hex('#f44336'), 960.60),  # Red
            (get_color_from_hex('#ff9800'), 9570.20), # Orange
            (get_color_from_hex('#ffc107'), 290.10),  # Yellow
            (get_color_from_hex('#2196f3'), 1230.00), # Blue
            (get_color_from_hex('#4caf50'), 990.10),  # Green
            (get_color_from_hex('#9c27b0'), 2030.60), # Purple
        ]

        # Use a GridLayout to arrange the boxes in a grid
        grid_layout = GridLayout(cols=3, size_hint=(1, 1))

        accounts = [
            (get_color_from_hex('#f44336'), 960.60),  # Red
            (get_color_from_hex('#ff9800'), 9570.20), # Orange
            (get_color_from_hex('#ffc107'), 290.10),  # Yellow
            (get_color_from_hex('#2196f3'), 1230.00), # Blue
            (get_color_from_hex('#4caf50'), 990.10),  # Green
            (get_color_from_hex('#9c27b0'), 2030.60), # Purple
        ]

        # Use a GridLayout to arrange the boxes in a grid
        grid_layout = GridLayout(cols=3, size_hint=(1, 1))

        accounts = [
            (get_color_from_hex('#f44336'), 960.60),  # Red
            (get_color_from_hex('#ff9800'), 9570.20), # Orange
            (get_color_from_hex('#ffc107'), 290.10),  # Yellow
            (get_color_from_hex('#2196f3'), 1230.00), # Blue
            (get_color_from_hex('#4caf50'), 990.10),  # Green
            (get_color_from_hex('#9c27b0'), 2030.60), # Purple
        ]

        for color, amount in accounts:
            box = AccountBox(color=color, amount=amount)
            grid_layout.add_widget(box)

        mother_box = BoxLayout(orientation='vertical', size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5}, padding=20)
        with mother_box.canvas.before:
            Color(1, 1, 1, 1)  # White color
            mother_box.rect = Rectangle(size=mother_box.size, pos=mother_box.pos)
        def _update_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size

        mother_box.bind(size=_update_rect, pos=_update_rect)

        mother_box.add_widget(grid_layout)

        # Navbar Mother Box
        navbar_mother_box = BoxLayout(orientation='vertical', size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.9}, padding=10)
        with navbar_mother_box.canvas.before:
            Color(1, 1, 1, 1)  # White color
            navbar_mother_box.rect = Rectangle(size=navbar_mother_box.size, pos=navbar_mother_box.pos)
        def _update_rect_navbar(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size

        navbar_mother_box.bind(size=_update_rect_navbar, pos=_update_rect_navbar)

        # Navbar
        navbar = BoxLayout(orientation='horizontal', size_hint=(1, 1))
        menu_label = Label(text='☰', size_hint=(0.2, 1), color=(0, 0, 0, 1))
        home_label = Label(text='Home', size_hint=(0.6, 1), color=(0, 0, 0, 1))
        wallet_label = Label(text='Wallet Now', size_hint=(0.2, 1), color=(0, 0, 0, 1))
        navbar.add_widget(menu_label)
        navbar.add_widget(home_label)
        navbar.add_widget(wallet_label)

        navbar_mother_box.add_widget(navbar)

        root = BoxLayout(orientation='vertical')
        root.add_widget(navbar_mother_box)
        root.add_widget(mother_box)
        return root

if __name__ == '__main__':
    MainApp().run()
