from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ScrButton(Button):
    def __init__(self, pantalla_actual, direccion, destino, **kwargs):
        super().__init__(**kwargs)
        self.pantalla_actual = pantalla_actual
        self.direccion = direccion
        self.destino = destino

    def on_press(self):
        self.pantalla_actual.manager.transition.direction = self.direccion
        self.pantalla_actual.manager.current = self.destino        

class VentanaPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn1 = ScrButton(self, 'left', 'ventana1', text='Ir a ventana 1')
        btn2 = ScrButton(self, 'up', 'ventana2', text='Ir a ventana 2')
        btn3 = ScrButton(self, 'right', 'ventana3', text='Ir a ventana 3')
        btn4 = ScrButton(self, 'down', 'ventana4', text='Ir a ventana 4')
        txt = Label(text='Seleccione una opcion')
        layout_principal = BoxLayout()
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout_principal.add_widget(txt)
        layout_principal.add_widget(layout)
        self.add_widget(layout_principal)
        
class Ventana1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = ScrButton(self, 'right', 'ventana_principal', text="Volver a principal")
        layout = BoxLayout()
        layout.add_widget(btn)
        self.add_widget(layout)
        
class Ventana2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = ScrButton(self, 'down', 'ventana_principal', text='Volver a Principal')
        layout = BoxLayout()
        layout.add_widget(btn)
        self.add_widget(layout)
        
class Ventana3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = ScrButton(self, 'left', 'ventana_principal', text='Volver a Principal')
        layout = BoxLayout()
        layout.add_widget(btn)
        self.add_widget(layout)
        
class Ventana4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = ScrButton(self, 'up', 'ventana_principal', text='Volver a Principal')
        layout = BoxLayout()
        layout.add_widget(btn)
        self.add_widget(layout)        

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(VentanaPrincipal(name='ventana_principal'))
        sm.add_widget(Ventana1(name='ventana1'))
        sm.add_widget(Ventana2(name='ventana2'))
        sm.add_widget(Ventana3(name='ventana3'))
        sm.add_widget(Ventana4(name='ventana4'))
        return sm
    
MyApp().run()
               