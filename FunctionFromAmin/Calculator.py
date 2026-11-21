from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.label.label import MDLabel
from kivymd.uix.textfield.textfield import MDTextField
from kivymd.uix.boxlayout import BoxLayout #Перенеси всё это пожалуйста на kivyMD для работы уведомлений, не дай бог не перенесешь уебище ебаное
from kivymd.uix.button.button import MDButton, MDButtonText
from kivymd.uix.snackbar.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.label import MDLabel
from kivymd.uix.anchorlayout import AnchorLayout
from kivy.utils import get_color_from_hex

class Cumculator(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = BoxLayout(orientation = 'vertical') #Специальный контейнер для ввода
        self.top_layout = BoxLayout(orientation = 'vertical', size_hint_y = 0.5)
        self.bottom_layout = GridLayout(size_hint_x = 0.7, size_hint_y = 1, spacing = 10, padding = 10)
        self.bottom_layout.cols = 4
        self.input = MDTextField(fill_color_normal = [246,240,249, 1], mode = 'filled') #Окно ввода для калкулатора
        self.top_layout.add_widget(self.input)
        self.mech_symbol = ['-', '+', '*', '/', '=', 'C']
        self.numb_lsts = [str(i) for i in range(10)]
        self.numb_lsts += self.mech_symbol
        self.visual = MDLabel(text='', size_hint_y = 0.1, md_bg_color = ['246','240','249', '.9'], size_hint=(1, 0.6))
        self.top_layout.add_widget(self.visual)
        self.advance_space = BoxLayout(orientation = 'vertical')
        self.backToMain = MDButton(MDButtonText(text='Назад'), pos_hint = {'top': 1})
        self.backToMain.bind(on_release = self.back_to_main)
        self.advance_space.add_widget(self.backToMain)
        self.top_layout.add_widget(self.advance_space)
        
        self.md_bg_color = get_color_from_hex('#E1A358')
        
        #Для калькулятора
        self.first_numb = ''
        
        self.second_numb = ''
        
        self.is_second = False
        self.is_result_get = False
        
        self.operator = ''
        
        for i in self.numb_lsts:
            self.numb_btn = MDButton(MDButtonText(text = i), theme_width = "Custom", size_hint_x = 0.1, size_hint_y = 0.1)
            self.numb_btn.bind(on_release = self.mechanics_numb)
            self.bottom_layout.add_widget(self.numb_btn)
            self.numb_btn.value = i
        
        
        self.layout.add_widget(self.top_layout)
        self.layout.add_widget(self.bottom_layout)
        #вконце добавление на камкулятор
        self.add_widget(self.layout)
    
    #Функционал калькулятор ниже    
    def mechanics_numb(self, instance):
        symbol = instance.value
        if self.is_second is False:
            if symbol not in ('+', '-', '/', '*', '=', 'C'):
                if self.is_result_get:
                    self.first_numb = symbol
                    self.is_result_get = False
                    self.visual.text = self.first_numb
                else:
                    self.input.text = symbol
                    self.first_numb += symbol
                    self.visual.text += symbol
            
            elif symbol in ('+', '-', '/', '*'): # Долго объяснять - последовательность, визуал берет при продолжения выражения число результат, которое записано в 1-ое число и сразу же берет себе оператор - я крутой
                self.visual.text = self.first_numb
                self.operator = symbol
                self.is_second = True
                self.visual.text += ' ' + self.operator + ' '
        else:
            if symbol not in ('+', '-', '/', '*', '=', 'C'): # Виузал, 2-ое число и всё
                self.input.text = symbol
                self.second_numb += symbol
                self.visual.text += symbol
                
        if symbol == '=': # по сути тут будут реализованы все операторы и решение - вроде ничего не сломал
            if self.operator == '+': 
                self.input.text = str(int(self.first_numb) + int(self.second_numb))
                self.first_numb = str(int(self.first_numb) + int(self.second_numb))
                self.visual.text += ' ' + '=' + ' ' + self.first_numb
            elif self.operator == '-': 
                self.input.text = str(int(self.first_numb) - int(self.second_numb))
                self.first_numb = str(int(self.first_numb) - int(self.second_numb))
                self.visual.text += ' ' + '=' + ' ' + self.first_numb
            elif self.operator == '/':
                if self.second_numb != '0':
                    self.input.text = str(int(self.first_numb) / int(self.second_numb))
                    self.first_numb = str(int(self.first_numb) / int(self.second_numb))
                    self.visual.text += ' ' + '=' + ' ' + self.first_numb    
                elif self.second_numb == '0':
                        MDSnackbar(
                            MDSnackbarText(text="Деление на ноль запрещено"),
                            pos_hint={"center_x": 0.5}
                        ).open()
                        
            self.is_second = False
            self.is_result_get = True
            self.second_numb = ''
        if symbol == 'C':
            self.input.text = ''
            self.is_second = False
            self.first_numb = ''
            self.second_numb = ''
            self.visual.text = ''
            
    def back_to_main(self, instance):
        self.manager.current = 'Main'