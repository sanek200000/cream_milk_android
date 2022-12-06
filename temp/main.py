from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.title = "Разбавлятель для сливок"

class CreamFatApp(App):
	
    # Создание всех виджетов (объектов)
    def __init__(self):
        super().__init__()
        self.label = Label(text='Количество молока для разведения, мл')
        
        self.fat_cont_cream = Label(text='жирность сливок, %')
        self.input_fat_cont_cream = TextInput(text='35', multiline=False, size_hint_x=None, width=100)
        self.amount_of_cream = Label(text='количество сливок, мг')
        self.input_amount_of_cream = TextInput(text='500', multiline=False, size_hint_x=None, width=100)
        
        self.fat_cont_milk = Label(text='жирность молока, %')
        self.input_fat_cont_milk = TextInput(text='2.5', multiline=False, size_hint_x=None, width=100)
        self.fat_cont_mix = Label(text='нужная жирность смеси, %')
        self.input_fat_cont_mix = TextInput(text='20', multiline=False, size_hint_x=None, width=100)
        

    def onpress(self, *args):
        try:
            fat_cont_cream = int(self.input_fat_cont_cream.text)
            amount_of_cream = int(self.input_amount_of_cream.text)
            fat_cont_milk = float(self.input_fat_cont_milk.text)
            fat_cont_mix = int(self.input_fat_cont_mix.text)
        except:
            self.label.text = 'Введено неверное значение, повторите ввод.'
        else:
            amount_of_milk = ((fat_cont_cream - fat_cont_mix) * amount_of_cream) / (fat_cont_mix - fat_cont_milk)
            amount_of_milk = str(int(amount_of_milk))
            
            self.label.text = f'Количество молока для разведения {amount_of_milk}, мл'
        pass
        
        
    # Основной метод для построения программы
    def build(self):
        # Все объекты будем помещать в один общий слой
        bl = BoxLayout(orientation='vertical', padding=[10,], spacing=5)
        
        bl.add_widget(self.label)
        
        gl = GridLayout(cols=2, spacing=3, row_force_default=True, row_default_height=40)
        
        gl.add_widget(self.fat_cont_cream)
        gl.add_widget(self.input_fat_cont_cream)
        gl.add_widget(self.amount_of_cream)
        gl.add_widget(self.input_amount_of_cream)
        gl.add_widget(self.fat_cont_milk)
        gl.add_widget(self.input_fat_cont_milk)
        gl.add_widget(self.fat_cont_mix)
        gl.add_widget(self.input_fat_cont_mix)

        bl.add_widget(gl)
        
        bl.add_widget(Button(text='Рассчитать', size_hint=(1, .2), on_press = self.onpress))
        return bl


if __name__ == "__main__":
	CreamFatApp().run()