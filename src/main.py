from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class KFCapitalApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        label = Label(text='Welcome to KF Capital Management')
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    KFCapitalApp().run()
