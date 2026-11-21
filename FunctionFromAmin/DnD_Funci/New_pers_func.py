from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.textfield.textfield import MDTextField, MDTextFieldHintText, MDTextFieldHelperText
from kivymd.uix.anchorlayout import AnchorLayout
from kivy.utils import get_color_from_hex

class New_hero_forDnd(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.own_layout = BoxLayout(orientation='vertical', size_hint_y = 1)
        
        self.inputName = MDTextField(
            MDTextFieldHintText(text = 'Название персонажа', font_size = 1),
            MDTextFieldHelperText(text = 'Имя персонажа(Мухаммад лох)'),
            fill_color_normal=(0, 0, 0, 1),
            mode='filled',
            theme_height = 'Custom',
            size_hint = (1, None),
            height = '40dp'
        )
        
        self.space_forAll = AnchorLayout(anchor_y = 'top')
        
        self.space_forAll.add_widget(self.inputName)
        
        self.own_layout.add_widget(self.space_forAll)
        
        self.add_widget(self.own_layout)
        
        self.md_bg_color = get_color_from_hex("#E1A358")