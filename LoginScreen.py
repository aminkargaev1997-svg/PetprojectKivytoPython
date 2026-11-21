from kivymd.uix.anchorlayout import AnchorLayout
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.button.button import MDButton, MDButtonText
from kivy.utils import get_color_from_hex

class LoginScreen(MDScreen):
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout_poryadok = BoxLayout(orientation = 'vertical', size_hint = (0.8, 0.4))
        self.layout_pos = AnchorLayout(anchor_x='center', anchor_y='center') #Ниже окно авторизации - изначальная позиция(может быть временно)
        self.username = MDTextField(MDTextFieldHintText(text = 'Логин'), mode = 'filled' )
        self.password = MDTextField(MDTextFieldHintText(text = 'Пароль'), password = True, mode = 'filled')
        self.button_enter = MDButton(MDButtonText(text = "Войти"), pos_hint={'center_x': 0.5})
        self.button_enter.bind(on_release = self.callback)
        self.layout_poryadok.add_widget(self.username)
        self.layout_poryadok.add_widget(self.password)
        self.layout_poryadok.add_widget(self.button_enter)
        self.layout_pos.add_widget(self.layout_poryadok)
        self.add_widget(self.layout_pos)
        self.md_bg_color = get_color_from_hex("#E1A358")
        
    def callback(self, instance):
        
        #Конечный правильный итог
        self.manager.current = 'Main'