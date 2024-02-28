from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFabButton

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    MDTopAppBar:
        type: "small"
        size_hint_x: 1
        pos_hint: {"center_x": .5, "center_y": .95}
    
        MDTopAppBarLeadingButtonContainer:
    
            MDActionTopAppBarButton:
                icon: "menu"
                on_release: nav_drawer.set_state("toggle")
    
        MDTopAppBarTitle:
            text: "Бридня Даниил Вадимович"
            pos_hint: {"center_x": .5}

    MDNavigationLayout:
        MDNavigationDrawer:
            id: nav_drawer
            radius: 0, dp(16), dp(16), 0

            MDNavigationDrawerMenu:

                MDNavigationDrawerLabel:
                    text: ""

                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "account"
                        

                    MDNavigationDrawerItemText:
                        text: "Какой то текст"

                    MDNavigationDrawerItemTrailingText:
                        text: "Какой то текст"
    
    MDBoxLayout:
        id: box
        adaptive_size: True
        spacing: "32dp"
        pos_hint: {"center_x": 0.93, "center_y": .2}
    
    MDBottomAppBar:
        md_bg_color: self.theme_cls.backgroundColor
        MDFabBottomAppBarButton:
            icon: "plus"
               
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        super().on_start()
        styles = {
            "standard": "surface",
        }
        for style in styles.keys():
            self.root.ids.box.add_widget(
                MDFabButton(
                    style=style, icon="pencil-outline", color_map=styles[style]
                )
            )


if __name__ == '__main__':
    Example().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
