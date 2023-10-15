# Password Generator App
from random import choice
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (800,700)

# Designate the .kv design file 
Builder.load_file('pass.kv')

class PassLayout(Widget):
	def gen(self):
		char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','@' ]
		len_ofword = self.ids.pass_len.text 
		password = ''

		for _ in range(int(len_ofword)):
			character = choice(char)
			password = password + character
		self.ids.pass_len.text = password


class PasswordApp(App):
	def build(self):
		Window.clearcolor = (65/255,71/255,103/255)
		return PassLayout()

if __name__ == '__main__':
	PasswordApp().run()