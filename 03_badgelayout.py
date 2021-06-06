from kivymd.app import MDApp
from kivy.lang.builder import Builder

from kivymd_extensions.akivymd.uix.badgelayout import AKBadgeLayout

KV = '''
<MyAKBadgeLayout@AKBadgeLayout>:
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    badgeitem_padding: '5dp'

MDScreen:
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: 'BadgeLayout'
            
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '10dp'
            padding: '10dp'
            
            # badgelayout with a raised button
            MyAKBadgeLayout:
                text: '101'
                offset: 0.5
                
                MDRaisedButton:
                    text: "Press"            
            
            # badgelayout with a MDLabel
            MyAKBadgeLayout:
                text: '41'
                badgeitem_color: 0, 1, 0, 1
                
                MDLabel:
                    size_hint: None, None
                    size: 100, 20
                    valign: 'center'
                    halign: 'center'
                    text: 'Press'
                    
'''


class BadgeLayoutApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    BadgeLayoutApp().run()
