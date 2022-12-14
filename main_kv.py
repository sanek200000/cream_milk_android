from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.title = "Разбавлятель для сливок"
#Window.size = (324, 720)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')


class Container(BoxLayout):
    def change_text(self):
        try:
            fat_cont_cream = int(self.fat_cont_cream.text)
            amount_of_cream = int(self.amount_of_cream.text)
            fat_cont_milk = float(self.fat_cont_milk.text)
            fat_cont_mix = int(self.fat_cont_mix.text)
        except:
            self.amount_of_milk.text = 'Введено неверное значение, повторите ввод.'
        else:
            if fat_cont_milk >= fat_cont_mix:
                fat_cont_milk = 1
                self.fat_cont_milk.text = str(fat_cont_milk)
                
            amount_of_milk = ((fat_cont_cream - fat_cont_mix) * amount_of_cream) / (fat_cont_mix - fat_cont_milk)
            amount_of_milk = str(int(amount_of_milk))
            
            self.amount_of_milk.text = f'Количество молока для разведения {amount_of_milk}, мл'

class CreamFatApp(App):
    def build(self):
        return Container()
    
    
if __name__ == "__main__":
	CreamFatApp().run()