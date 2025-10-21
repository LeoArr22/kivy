from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from util.widgets_personalizados import ScrButton
from util.intrucciones import instruccion_pantalla_esfuerzo

# -------- Pantalla 4: Pulso luego de esfuerzo --------
class VentanaPulsoEsfuerzo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #layouts
        layout = BoxLayout(orientation='vertical', padding=20)
        layout_superior = BoxLayout(orientation='vertical')
        layout_inferior = BoxLayout(orientation='vertical', size_hint_y=None)
        formulario = BoxLayout(orientation='vertical', size_hint=(None, None), width=250, spacing=10)
        contenedor = AnchorLayout(anchor_x='center')
        
        #widgets
        txt = Label(text=instruccion_pantalla_esfuerzo)
        self.input_p1 = TextInput(hint_text="Pulsos en P1", multiline=False, size_hint_y=None, height=40)
        self.input_p2 = TextInput(hint_text="Pulsos en P2", multiline=False, size_hint_y=None, height=40)
        btn_sig = ScrButton(self, 'left', 'ventana_final', text="Siguiente", size_hint_y=None, height=50)
        btn_sig.bind(on_press=self.guardar_datos)
        btn_atras = ScrButton(self, 'right', 'ventana_sentadillas', text="Regresar", size_hint_y=None, height=50)
        
        #add widget
        layout_superior.add_widget(txt)
        formulario.add_widget(Label(text="Ingrese la cantidad de pulsos luego del esfuerzo:", size_hint_y=None, height=30))
        formulario.add_widget(self.input_p1)
        formulario.add_widget(Label(text="Ingrese la cantidad de pulsos luego del descanso:", size_hint_y=None, height=30))
        formulario.add_widget(self.input_p2)
        formulario.add_widget(btn_sig)
        formulario.add_widget(btn_atras)
        
        #add layout
        contenedor.add_widget(formulario)
        layout_inferior.add_widget(contenedor)
        
        layout.add_widget(layout_superior)
        layout.add_widget(layout_inferior)
        self.add_widget(layout)
        
    def guardar_datos(self, instance):
        app = App.get_running_app() #Obtenemos la instancia actual
        app.p1 = self.input_p1.text #A esa instancia, le agregamos un nuevo atributo
        app.p2 = self.input_p2.text
        