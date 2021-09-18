from kivymd.app import MDApp
from kivy.lang.builder import Builder

from kivymd_extensions.akivymd.uix.datepicker import AKDatePicker

KV = '''
MDScreen:
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDFloatLayout:
            
            MDRaisedButton: 
                text: 'Open'
                on_release: app.open()
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            MDLabel:
                id: date
                text: ''
                halign: 'center'
                pos_hint: {'center_x': .5, 'center_y': .2}
'''


class DatePickerApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date = AKDatePicker(callback=self.callback)

    def callback(self, date):
        self.root.ids.date.text = '' if not date else f"{date.day}/{date.month}/{date.year}"

    def build(self):
        return Builder.load_string(KV)

    def open(self):
        self.date.open()


if __name__ == '__main__':
    DatePickerApp().run()
