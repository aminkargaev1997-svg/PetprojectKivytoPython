from kivy.uix.treeview import TreeView
from kivymd.uix.screen import MDScreen
from kivymd.uix.anchorlayout import AnchorLayout
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label.label import MDLabel
from kivymd.uix.button.button import MDButton, MDButtonText
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

class TimerScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.BoxLayoutMain = BoxLayout(orientation='vertical', size_hint=(1, 1))
        self.BoxLayoutTop = BoxLayout(orientation='vertical')
        self.BoxLayoutBottom = BoxLayout(orientation='horizontal', size_hint = (None, None), size = (250, 60))
        self.AnchorPosition = AnchorLayout(anchor_x='center')
        
        self.own_timer = 0.0
        
        #Отображение времени
        self.VisualTimer_label = MDLabel(text=f'{int(self.own_timer // 3600):02d}:{int(self.own_timer // 60):02d}:{int(self.own_timer % 60):02d}:{int((self.own_timer % 1) * 100):02d}', halign='center')
        self.BoxLayoutTop.add_widget(self.VisualTimer_label)
        #кнопки активации
        self.btnStart = MDButton(MDButtonText(text = "Старт"))
        self.btnStart.bind(on_release = self.start)
        self.BoxLayoutBottom.add_widget(self.btnStart)
        
        #Кнопка стопа
        self.btnStop = MDButton(MDButtonText(text='Стоп'), disabled = True)
        self.btnStop.bind(on_release=self.stop)
        self.BoxLayoutBottom.add_widget(self.btnStop)
        
        #Кнопка очистки
        self.btnClear = MDButton(MDButtonText(text='Сбросить'), disabled = True)
        self.btnClear.bind(on_release=self.clear)
        self.BoxLayoutBottom.add_widget(self.btnClear)
        
        self.md_bg_color = get_color_from_hex("#E1A358")
        
        self.BoxLayoutMain.add_widget(self.BoxLayoutTop)
        self.AnchorPosition.add_widget(self.BoxLayoutBottom)
        self.BoxLayoutMain.add_widget(self.AnchorPosition)
        self.add_widget(self.BoxLayoutMain)
    
    # Ниже код функции секундромера, чет я перепутал и сделал не таймер
    def start(self, instance):
        self.timer_event = Clock.schedule_interval(self.timerUpdate, 0.01)
        self.btnClear.disabled, self.btnStop.disabled = False, False
            
    def timerUpdate(self, dt):
        self.btnStart.disabled = True
        self.own_timer += dt
        self.VisualTimer_label.text = f'{int(self.own_timer // 3600):02d}:{int(self.own_timer // 60):02d}:{int(self.own_timer % 60):02d}:{int((self.own_timer % 1) * 100):02d}'
            
    def stop(self, instance):
        self.timer_event.cancel()
        self.btnStart.disabled = False
        self.btnStop.disabled = True
    def clear(self, instance):
        self.own_timer = 0.0
        self.timer_event.cancel()
        self.btnClear.disabled, self.btnStop.disabled = True, True
        self.btnStart.disabled = False
        self.VisualTimer_label.text = f'{int(self.own_timer // 3600):02d}:{int(self.own_timer // 60):02d}:{int(self.own_timer % 60):02d}:{int((self.own_timer % 1) * 100):02d}'