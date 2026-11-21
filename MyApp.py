import kivy

kivy.require('2.3.1')

from kivymd.app import MDApp
from LoginScreen import LoginScreen
from kivy.uix.screenmanager import ScreenManager
from Screen_Main import MainScreen
from FunctionFromAmin.Calculator import Cumculator
from FunctionFromAmin.DnD import DnD
from FunctionFromAmin.DnD_Funci.New_pers_func import New_hero_forDnd
from FunctionFromAmin.TimeScreen import TimerScreen

class MyApps(MDApp):
    
    def build(self):
        mng = ScreenManager()

        mng.add_widget(LoginScreen(name = 'Login'))
        mng.add_widget(MainScreen(name = 'Main'))
        mng.add_widget(Cumculator(name = 'Calculator'))
        mng.add_widget(DnD(name = 'DnD'))
        mng.add_widget(New_hero_forDnd(name='createHero'))
        mng.add_widget(TimerScreen(name='Timer'))
        return mng