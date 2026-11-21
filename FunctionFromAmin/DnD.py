from kivymd.uix.screen import MDScreen
from kivymd.uix.button.button import MDButton, MDButtonText
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.anchorlayout import AnchorLayout
from kivymd.uix.gridlayout import GridLayout
from kivy.utils import get_color_from_hex

class DnD(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.newPrsn = MDButton(
            MDButtonText(text='Создать нового персонажа')
        )
        self.newPrsn.bind(on_release = self.ToNewPers)
        
        self.own_layout = BoxLayout(
            orientation = 'vertical', size_hint = (1, 1)
        )
        
        self.space_toBtn = AnchorLayout(anchor_x = 'center', anchor_y = 'center', size_hint = (1, 1))
        self.To_Anchorbro = GridLayout(cols = 1, size_hint_y = 0, size_hint_x = 0.3, spacing = '3dp')
        
        self.add_widget(self.own_layout)#Кнопка для перехода в окно создания персонажа
        self.To_Anchorbro.add_widget(self.newPrsn)
        self.space_toBtn.add_widget(self.To_Anchorbro)
        self.own_layout.add_widget(self.space_toBtn)
        
        self.toYourHero = MDButton(
            MDButtonText( text='Мои Персонажи', pos_hint = {'center_x': 0.5, 'center_y': 0.5}),
            theme_width = 'Custom',
            theme_height = 'Custom',
            size_hint = (None, None),
            width = 230,
            height = 38,
            )
        self.toYourHero.bind(on_release = self.toYourPers)
        self.To_Anchorbro.add_widget(self.toYourHero)
        
        
        
        self.md_bg_color = get_color_from_hex("#E1A358")
    
    def ToNewPers(self, instance): #Окно для создания персонажа - нужен отдельный класс
        self.manager.current = 'createHero'
        
    def toYourPers(self, instnace): #Окно для работы с созданными персонажами
        self.manager.current()