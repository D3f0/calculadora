#! /usr/bin/python
# *-* encoding: utf-8 *-*

#
# Autor: Nahuel DeofossÃ© (c) 2007
# Licencia: GPL
#

# Todo PyQt4 :)
from PyQt4.Qt import *

# Generado a travez del editor de designar
# cuando se actualiza el GUI, se debe correr Make para que
# se transformen en código
from interfase import Ui_MainWindow
# Para los argumentos de linea de entrada
import sys
# Todas las definiciones del automata que hemos separado en otro modulo (py)
from automata import ejecutar_automata

# Algunas funciones utiles


class Calculadora(QApplication):
    '''Aplicacion calculadora simple'''
    def __init__(self, *argumentos):
        QApplication.__init__(self, *argumentos)
        splash_pxmap = QPixmap("./resources/splash.png")
        splash = QSplashScreen(splash_pxmap)
        splash.show()
        ventana = VentanaCalculadora()
        ventana.show()
        splash.finish(ventana)
        self.exec_()

class VentanaCalculadora(QMainWindow, Ui_MainWindow):
    '''GUI de la calculadora.'''
    estado = "en_cero"  # De acuerdo a los estados del automata
    valor = 0
    operacion = ""
    def __init__(self, padre = None):
        '''Constructor de la ventana'''
        QMainWindow.__init__(self, padre)
        self.setupUi(self)
        self.connect(self.actionSalir, SIGNAL("triggered()"), qApp.exit )
        # Conectamos los digitos
        for i in [  self.btn_digit_1, self.btn_digit_2,
                    self.btn_digit_3, self.btn_digit_4,
                    self.btn_digit_5, self.btn_digit_6,
                    self.btn_digit_7, self.btn_digit_8,
                    self.btn_digit_9, self.btn_digit_0,
                    ]:
            self.connect(i, SIGNAL("clicked()"), self.in_digito)
        # Ahora conectamos las operaciones

    def in_digito(self):
        '''Pulsado de un digito'''
        num = self.sender().objectName()[-1:]
        ejecutar_automata(num, self)

    def on_btn_op_add_pressed(self):
        ejecutar_automata("+", self)

    def on_btn_op_sub_pressed(self):
        ejecutar_automata("-", self)

    def on_btn_op_mul_pressed(self):
        ejecutar_automata("*", self)

    def on_btn_op_div_pressed(self):
        ejecutar_automata("/", self)

    def on_btn_op_res_pressed(self):
        ejecutar_automata("=", self)

    def on_btn_clear_pressed(self):
        ejecutar_automata("c", self)



    # Funciones que llama el automata
    def actualizar(self, c):
        '''Agrega un caracter al display '''
        self.lineResultado.setText( self.lineResultado.text() + c )

    def establecer(self, c):
        '''Establece el valor del display'''
        self.lineResultado.setText(c)
    def operar(self, c):
        pass

    def almacenar(self, c):
        self.valor = float(self.lineResultado.text())

    def guardar_op(self,c):
        self.operacion = c

    def operar(self, c):
        result = 0
        self.valor2 = float(self.lineResultado.text())
        if self.operacion == "+":
            result = self.valor + self.valor2
        elif self.operacion == "-":
            result = self.valor - self.valor2
        elif self.operacion == "/":
            result = self.valor / self.valor2
        elif self.operacion == "*":
            result = self.valor * self.valor2
        else:
            print "Nada"
        self.lineResultado.setText(str(result))

    def limpiar(self, c):
        self.lineResultado.setText("0")
        self.valor = 0


if __name__ == "__main__":
    app = Calculadora(sys.argv)

