from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        #widgets
        self.btn = Button(text="Soy un boton") #Definimos Widgets
        self.txt = Label(text="Soy una etiqueta")
        self.txt2 = Label(text="Hola Mundo")
        self.txt3 = Label(text="Ola K ase")
        
        #conexiones
        self.btn.bind(on_press=self.saludar) #Con bind (unir) realizamos conexiones entre eventos de un widget a metodos
        
        #layouts
        layout = BoxLayout(padding=10, spacing=10)
        lv = BoxLayout(orientation='vertical')
        lv.add_widget(self.txt2)
        lv.add_widget(self.txt3)
        layout.add_widget(self.btn)
        layout.add_widget(self.txt)
        layout.add_widget(lv)
        return layout
    
    def saludar(self, instance): #instance es el widget que llamo al metodo
        print("HOLA MUDNOOOOO|")
        
app = MyApp()
app.run() # Tambien es valido MyApp().run()
