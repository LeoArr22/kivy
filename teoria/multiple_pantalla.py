from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # **kwargs permite pasar una cantidad indefinidad de valores nombrados (nombre='pepe', edad=11), se convierte en diccionario
        layout = BoxLayout()
        btn = Button(text="Ir a la otra pantalla") 
        btn.bind(on_press=self.cambiar_pantalla)
        layout.add_widget(btn)
        self.add_widget(layout)

    def cambiar_pantalla(self, instance):
        # Cambia a la pantalla llamada "otra"
        self.manager.current = "otra" # Cambia la pantalla actual


class OtraScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = Button(text="Volver")
        btn.bind(on_press=self.volver)
        layout = BoxLayout()
        layout.add_widget(btn)
        self.add_widget(layout)

    def volver(self, instance):
        self.manager.current = "inicio"


class MyApp(App):
    def build(self):
        sm = ScreenManager() #Ahora la clase App se va a encargar de las pantallas. Creamos un objeto llamada "sm" que sera el Gestor de Pantallas
        sm.add_widget(MyScreen(name="inicio")) # Añadimos las pantallas al gestor. Ademas colocamos el nombre para identificarlas
        sm.add_widget(OtraScreen(name="otra"))
        return sm #Retornamos el gestor de pantallas


MyApp().run()
