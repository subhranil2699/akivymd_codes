from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.list import MDList, OneLineListItem

from kivymd_extensions.akivymd.uix.behaviors.addwidget import AKAddWidgetAnimationBehavior

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 10
        padding: 10
        
        MDBoxLayout:
            adaptive_height: True
            spacing: 10
            
            MDRaisedButton:
                text: "Add Widgets"
                on_press: app.add_widget()
            
            MDRaisedButton:
                text: "Clear"
                on_press: app.clear_widget()
        
        ScrollView:
            AnimatedBox:
                id: list
                transition: 'fade_size'
'''


class AnimatedBox(MDList, AKAddWidgetAnimationBehavior):
    pass


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def add_widget(self):
        items = []
        for i in range(20):
            items.append(OneLineListItem(
                text=f"Item {i}"
            ))
        self.root.ids.list.items = items

    def clear_widget(self):
        self.root.ids.list.clear_widgets()


if __name__ == '__main__':
    MainApp().run()
