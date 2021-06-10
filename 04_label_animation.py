from kivymd.uix.label import MDIcon, MDLabel
from kivymd.app import MDApp
from kivy.lang.builder import Builder

from kivymd_extensions.akivymd.uix.behaviors.labelanimation import (
    AKAnimationIconBehavior,
    AKAnimationTextBehavior,
)

kv = """
MDScreen:

    MDFloatLayout:

        MyMDLabel:
            id: label
            text: "account on"
            pos_hint: {"center_x": .5, "center_y": .6}
            halign: "center"
            font_size: dp(20)
            theme_text_color: "Primary"

        MyMDIcon:
            id: icon
            icon: "account"
            pos_hint: {"center_x": .5, "center_y": .4}
            halign: "center"
            font_size: dp(100)
            theme_text_color: "Primary"

        MDRaisedButton:
            text: "Press"
            pos_hint: {"center_x": .5, "center_y": .1}
            on_release:
                label.text= "account on" if label.text=="account off" else "account off"
                icon.icon= "account" if icon.icon=="account-off" else "account-off"
"""

class MyMDIcon(MDIcon, AKAnimationIconBehavior):
    pass


class MyMDLabel(MDLabel, AKAnimationTextBehavior):
    pass



class LabelAnimation(MDApp):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    LabelAnimation().run()


