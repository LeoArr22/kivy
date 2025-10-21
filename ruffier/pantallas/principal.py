from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from util.widgets_personalizados import ScrButton
from util.intrucciones import titulo, explicacion_pantalla_inicial

# -------- Pantalla 1: nombre y edad --------
class VentanaPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #layouts
        layout = BoxLayout(orientation='vertical', padding=20)
        layout_superior = BoxLayout(orientation='vertical')
        layout_inferior = BoxLayout(orientation='vertical', size_hint_y=None)
        formulario = BoxLayout(orientation='vertical', size_hint=(None, None), width=250, spacing=10)
        contenedor = AnchorLayout(anchor_x='center')

        
        #widgets
        txt = Label(text=explicacion_pantalla_inicial)
        
        self.input_nombre = TextInput(hint_text="Nombre", multiline=False, size_hint_y=None, height=40)
        self.input_edad = TextInput(hint_text="Edad", multiline=False, size_hint_y=None, height=40)
        
        btn = ScrButton(self, 'left', 'ventana_pulso_reposo', text="Siguiente", size_hint_y=None, height=50)
        btn.bind(on_press=self.guardar_datos)
        
        #add widget
        layout_superior.add_widget(txt)
        formulario.add_widget(Label(text="Ingrese su nombre:", size_hint_y=None, height=30))
        formulario.add_widget(self.input_nombre)
        formulario.add_widget(Label(text="Ingrese su edad:", size_hint_y=None, height=30))
        formulario.add_widget(self.input_edad)
        formulario.add_widget(btn)
        
        #add layout
        contenedor.add_widget(formulario)
        layout_inferior.add_widget(contenedor)
        
        layout.add_widget(layout_superior)
        layout.add_widget(layout_inferior)        
        self.add_widget(layout)
    
    def guardar_datos(self, instance):
        app = App.get_running_app() #Obtenemos la instancia actual
        app.nombre = self.input_nombre.text #A esa instancia, le agregamos un nuevo atributo
        app.edad = self.input_edad.text