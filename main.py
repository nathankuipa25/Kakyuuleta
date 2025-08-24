from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivymd.uix.behaviors import CircularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem
from kivymd.toast import toast


class IconListItem(OneLineIconListItem):
	icon = StringProperty()


class CircularRippleButton(CircularRippleBehavior, ButtonBehavior,MDFloatLayout):
	text = StringProperty("btn")
	

class Calculator(MDApp):
	def build(self):
		self.input = StringProperty('')
		self.output = StringProperty('')
		
		self.screen = Builder.load_file('main.kv')
		
		buttons = ["9","8","7","*","6","5","4","/",	"3","2","1","+","0","=","-","CLR",]
		for item in buttons:
			
			self.screen.ids.keypad.add_widget(CircularRippleButton(text = item,size_hint_y = None,height ="190dp",on_press = self.do_something))
			
		return self.screen
		
	def menu_callback(self,text_item):
		toast(f'{text_item} page is under development!', True, 80, 200, 0)

		
	def open_menu(self):
		menu_items = [{
			"text":"Open source licenses",
			"icon": "license",
			"viewclass": "IconListItem",
			"on_release": lambda x=f"license": self.menu_callback(x)
		},
		{
			"text":"About",
			"icon": "information-outline",
			"viewclass": "IconListItem",
			"on_release": lambda x='about': self.menu_callback(x)
		}
		]
		
		menu = MDDropdownMenu(caller=self.screen.ids.button,items=menu_items,width_mult=4,)		
		menu.open()
			
	def do_something(self,instance):
		try:		
			if instance.text == 'CLR':
				self.input = ''
				self.output = ''
				self.screen.ids.display.text = self.output
							
			elif instance.text == '=':
				answer = str(eval(self.screen.ids.display.text)).strip()
				self.screen.ids.display.text = str(answer)
			else:
				self.screen.ids.display.text += instance.text
		except Exception as e:
			self.screen.ids.display.text = "Invalid Operation!"
		
		
Calculator().run()