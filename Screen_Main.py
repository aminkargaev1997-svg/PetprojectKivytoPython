from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button.button import MDButton, MDButtonText
from kivymd.uix.screen import MDScreen
from kivymd.uix.anchorlayout import AnchorLayout
from kivy.utils import get_color_from_hex

class MainScreen(MDScreen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = BoxLayout(orientation = 'vertical', size_hint = (0.5, 0))
        self.layout_centr = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
        self.btnCalculate = MDButton(MDButtonText(text = "Калкулатор"), pos_hint = {'center_x': 0.5})
        self.btnCalculate.bind(on_release = self.ToCalculator)
        self.layout.add_widget(self.btnCalculate)
        self.layout_centr.add_widget(self.layout)
        
        self.btnToDnd = MDButton(MDButtonText(
            text='DnD(aun)'),
            pos_hint = {'center_x': 0.5}
        )
        self.btnToDnd.bind(on_release = self.ToDND)
        self.layout.add_widget(self.btnToDnd)
        
        
        self.ToTimeoutscrn = MDButton(MDButtonText(text = 'Таймер'), pos_hint={'center_x': 0.5})
        self.ToTimeoutscrn.bind(on_release=self.toTimerScreen)
        
        self.layout.add_widget(self.ToTimeoutscrn)
        self.add_widget(self.layout_centr)
        self.md_bg_color = get_color_from_hex("#E1A358")
        
        
    
    def ToCalculator(self, instance):
        self.manager.current = 'Calculator'
        
    def ToDND(self, instance):
        self.manager.current = 'DnD'
        
    def toTimerScreen(self, instance):
        self.manager.current = 'Timer'