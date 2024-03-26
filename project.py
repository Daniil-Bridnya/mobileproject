import json

import requests
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout


class LayWidget(MDBoxLayout):
    title_widget = ObjectProperty()
    container_widget = ObjectProperty()
    tag_widget = ObjectProperty()
    min_price_widget = ObjectProperty()
    max_price_widget = ObjectProperty()

    def search_goods(self):

        if self.title_widget.text:
            self.search_by_name()

        if self.tag_widget.text:
            self.search_by_tag()

        if self.min_price_widget.text and self.max_price_widget.text:
            self.search_by_price()

        else:
            print('Ничего не выбрано')

    def search_by_name(self):
        req_param = self.title_widget.text
        url = 'http://127.0.0.1:5000/goods/title?title=' + req_param
        response = requests.get(url)
        data_list = json.loads(response.text)
        self.show_goods(data_list)

    def search_by_tag(self):
        req_param = self.tag_widget.text
        url = 'http://127.0.0.1:5000/goods/' + req_param
        response = requests.get(url)
        data_list = json.loads(response.text)
        self.show_goods(data_list)

    def search_by_price(self):
        req_param_min = self.min_price_widget.text
        req_param_max = self.max_price_widget.text
        url = 'http://127.0.0.1:5000/goods/price?min=' + req_param_min + '&max=' + req_param_max
        response = requests.get(url)
        data_list = json.loads(response.text)
        self.show_goods(data_list)

    def show_goods(self, goods):
        for good in goods:
            print(good['title'])
            self.ids.container.add_widget(
                MDCard(
                    MDRelativeLayout(
                        MDIconButton(
                            icon="dots-vertical",
                            pos_hint={"top": 1, "right": 1}
                        ),
                        MDLabel(
                            text='Наименование - ' + good['title'],
                            adaptive_size=True,
                            pos=("12dp", "142dp"),
                        ),
                        MDLabel(
                            text='Описание - ' + good['description'],
                            adaptive_size=True,
                            pos=("12dp", "115dp"),
                        ),
                        MDLabel(
                            text='Тэг - ' + good['tags'],
                            adaptive_size=True,
                            pos=("12dp", "88dp"),
                        ),
                        MDLabel(
                            text='Оценка - ' + str(good['user_evaluation']),
                            adaptive_size=True,
                            pos=("12dp", "61dp"),
                        ),
                        MDLabel(
                            text='Цена - ' + str(good['price']),
                            adaptive_size=True,
                            pos=("12dp", "34dp"),
                        ),
                        MDLabel(
                            text='Остаток - ' + str(good['stock_balance']),
                            adaptive_size=True,
                            pos=("12dp", "7dp"),
                        ),
                    ),
                    style='elevated',
                    padding="4dp",
                    size_hint=(None, None),
                    size=("480dp", "200dp"),
                    ripple_behavior=True,
                )
            )

    def clear_list(self):

        self.ids.container.clear_widgets()


class ProjectApp(MDApp):
    title = 'Бридня Д.В.'

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"  # "Red", ,"Purple"


if __name__ == '__main__':
    ProjectApp().run()
