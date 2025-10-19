from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from util.intrucciones import *


# -------- Clase de botón genérico --------
class ScrButton(Button):
    def __init__(self, pantalla_actual, direccion, destino, **kwargs):
        super().__init__(**kwargs)
        self.pantalla_actual = pantalla_actual
        self.direccion = direccion
        self.destino = destino

    def on_press(self):
        self.pantalla_actual.manager.transition.direction = self.direccion
        self.pantalla_actual.manager.current = self.destino


# -------- Pantalla 1: nombre y edad --------
class VentanaPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #layouts
        layout = BoxLayout(orientation='vertical', padding=20)
        layout_superior = BoxLayout(orientation='vertical')
        layout_inferior = BoxLayout(orientation='vertical', size_hint_y=None)
        
        #widgets
        txt = Label(text=explicacion_pantalla_inicial)
        
        self.input_nombre = TextInput(hint_text="Nombre", multiline=False, size_hint_y=None, height=40)
        self.input_edad = TextInput(hint_text="Edad", multiline=False, size_hint_y=None, height=40)
        
        btn = ScrButton(self, 'left', 'ventana2', text="Siguiente", size_hint_y=None, height=50)
        btn.bind(on_press=self.guardar_datos)
        
        #add widget
        layout_superior.add_widget(txt)
        layout_inferior.add_widget(Label(text="Ingrese su nombre:", size_hint_y=None, height=30))
        layout_inferior.add_widget(self.input_nombre)
        layout_inferior.add_widget(Label(text="Ingrese su edad:", size_hint_y=None, height=30))
        layout_inferior.add_widget(self.input_edad)
        layout_inferior.add_widget(btn)
        
        #add layout
        layout.add_widget(layout_superior)
        layout.add_widget(layout_inferior)        
        self.add_widget(layout)
    
    def guardar_datos(self, instance):
        app = App.get_running_app() #Obtenemos la instancia actual
        app.nombre = self.input_nombre.text #A esa instancia, le agregamos un nuevo atributo
        app.edad = self.input_edad.text


# -------- Pantalla 2: un número --------
class Ventana2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        self.input_num = TextInput(hint_text="Número favorito", multiline=False, size_hint_y=None, height=40)
        
        btn = ScrButton(self, 'left', 'ventana3', text="Siguiente", size_hint_y=None, height=50)
        btn.bind(on_press=self.guardar_dato)
        
        layout.add_widget(Label(text="Ingrese un número favorito:", size_hint_y=None, height=30))
        layout.add_widget(self.input_num)
        layout.add_widget(btn)
        
        self.add_widget(layout)
    
    def guardar_dato(self, instance):
        app = App.get_running_app()
        app.numero = self.input_num.text


# -------- Pantalla 3: mostrar todos los datos --------
class Ventana3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        self.lbl = Label(text="", size_hint_y=None, height=150)
        
        btn = ScrButton(self, 'right', 'ventana_principal', text="Volver al inicio", size_hint_y=None, height=50)
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def on_pre_enter(self): # on_pre_enter ->Se va a ejecutar antes de que la pantalla aparezca en pantalla
        app = App.get_running_app()
        nombre = getattr(app, "nombre", "") #getattr ->Esto averigua si existe el atributo "nombre" en el objeto  app
        edad = getattr(app, "edad", "") #En caso de no existir, le asigna ""
        numero = getattr(app, "numero", "")
        self.lbl.text = f"Nombre: {nombre}\nEdad: {edad}\nNúmero favorito: {numero}"


# -------- Clase principal de la app --------
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(VentanaPrincipal(name='ventana_principal'))
        sm.add_widget(Ventana2(name='ventana2'))
        sm.add_widget(Ventana3(name='ventana3'))
        return sm


# -------- Ejecutar app --------
MyApp().run()
