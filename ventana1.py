import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QPushButton, \
    QLineEdit, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore


class Ventana1(QMainWindow):

    # Hacer el método de construcción de la ventana
    def __init__(self, parent=None):
        super().__init__(parent)

        # Poner el título
        self.setWindowTitle("Formulario de registro")

        # Poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))

        # Establecer las propiedades de ancho y alto
        self.ancho = 1000
        self.alto = 700

        # Establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/fondo.png')

        # Definimos la imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos con Layout horizontal
        self.horizontal = QHBoxLayout()
        # Le ponemos las márgenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ---------- LAYOUT IZQUIERDO -----------

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Les escribimos el texto
        self.letrero1.setText("Información del cliente")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # ---------- Layout izquierdo -----------

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Les escribimos el texto
        self.letrero1.setText("Información del cliente")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le ponemos el color de texto
        self.letrero1.setStyleSheet("color: #000000;")

        # Agregamos el letrero de la primera fila
        self.ladoIzquierdo.addRow(self.letrero1)

        # Hacemos el letrero
        self.letrero2 = QLabel()

        # Establecemos el ancho del label
        self.letrero2.setFixedWidth(340)

        # Le escribimos el texto
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos"
                              "\nmarcados con asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de texto y márgenes
        self.letrero2.setStyleSheet("color: #FFFFFF; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la línea siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Nombre completo*", self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password
        self.clave = QLineEdit()
        self.clave.setFixedWidth(250)
        self.clave.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Contraseña*", self.clave)

        # Hacemos el campo para ingresar el password
        self.clave2 = QLineEdit()
        self.clave2.setFixedWidth(250)
        self.clave2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Verificación Contraseña*", self.clave2)

        # Hacemos el campo para ingresar el documento
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Correo electrónico*", self.correo)

        # Hacemos el botón para registrar los datos
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del botón
        self.botonRegistrar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Hacemos el botón para limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del botón
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al Layout ladoIzquierdo
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # Agregamos el Layout ladoIzquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        # ---------- Layout derecho -----------

        # Creamos el layout del lado derecho
        self.ladoDerecho = QFormLayout()
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrero
        self.letrero3 = QLabel()
        # Les escribimos el texto
        self.letrero3.setText("Recuperar contraseña")

        # Le asignamos el tipo de letra
        self.letrero3.setFont(QFont("Andale Mono", 20))

        # Le ponemos el color de texto
        self.letrero3.setStyleSheet("color: #000080;")

        # Agregamos letrero a la primera fila
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero
        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(400)
        # Les escribimos el texto
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asteriscos son obligatorios")
        # Le asignamos el tipo de letra
        self.letrero4.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de texto y márgenes
        self.letrero4.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.letrero4)

        # Hacemos los letreros de preguntas
        self.lblPregunta1 = QLabel("Pregunta de verificación 1*")
        self.lblPregunta2 = QLabel("Pregunta de verificación 2*")
        self.lblPregunta3 = QLabel("Pregunta de verificación 3*")
        self.lblRespuesta1 = QLabel("Respuesta de verificación 1*")
        self.lblRespuesta2 = QLabel("Respuesta de verificación 2*")
        self.lblRespuesta3 = QLabel("Respuesta de verificación 3*")
        # Hacemos los campos de respuestas
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # Agregamos los campos al formulario en el orden que se desea ver
        self.ladoDerecho.addRow(self.lblPregunta1)
        self.ladoDerecho.addRow(self.pregunta1)
        self.ladoDerecho.addRow(self.lblRespuesta1)
        self.ladoDerecho.addRow(self.respuesta1)
        self.ladoDerecho.addRow(self.lblPregunta2)
        self.ladoDerecho.addRow(self.pregunta2)
        self.ladoDerecho.addRow(self.lblRespuesta2)
        self.ladoDerecho.addRow(self.respuesta2)
        self.ladoDerecho.addRow(self.lblPregunta3)
        self.ladoDerecho.addRow(self.pregunta3)
        self.ladoDerecho.addRow(self.lblRespuesta3)
        self.ladoDerecho.addRow(self.respuesta3)

        # Hacemos el botón para buscar
        self.btnBuscar = QPushButton("Buscar")
        self.btnBuscar.setFixedWidth(90)
        self.btnBuscar.setStyleSheet("background-color: #008B45;"
                                     "color: #FFFFFF;"
                                     "padding: 10px;"
                                     "margin-top: 40px;")

        # Hacemos el botón para recuperar
        self.btnRecuperar = QPushButton("Recuperar")
        self.btnRecuperar.setFixedWidth(90)
        self.btnRecuperar.setStyleSheet("background-color: #008B45;"
                                     "color: #FFFFFF;"
                                     "padding: 10px;"
                                     "margin-top: 40px;")

        self.ladoDerecho.addRow(self.btnBuscar, self.btnRecuperar)

        # Agregamos el layout derecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)


        # --------- OJO IMPORTANTE PONER AL FINAL --------------

        # Indicamos que el Layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

    # Metodo del botón limpiar
    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.clave.setText('')
        self.clave2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.pregunta2.setText('')
        self.pregunta3.setText('')
        self.respuesta1.setText('')
        self.respuesta2.setText('')
        self.respuesta3.setText('')

    # Metodo del botón Registrar
    def accion_botonRegistrar(self):
        # Creamos una ventana de diálogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)
        # Creamos el botón aceptar
        self.btnAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.btnAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)
        # Establecemos el título de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario de registro")
        # Configuramos la ventana para que sea modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)
        # Creamos un layout vertical
        self.vertical = QVBoxLayout()
        # Creamos un label para los mensajes
        self.mensaje = QLabel("")
        # Le ponemos estilos al mensaje
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")
        # Agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)
        # Agregamos las opciones de los botones
        self.vertical.addWidget(self.opciones)
        # Establecemos el layout de la ventana
        self.ventanaDialogo.setLayout(self.vertical)

        # Variables de datos correctos
        self.datosCorrectos = True
        # Validamos que las claves sean iguales
        if (self.clave.text() != self.clave2.text()):
            self.datosCorrectos = False
            self.mensaje.setText("Las contraseñas ingresadas no son iguales")
            # Hacemos que se vea la ventana
            self.ventanaDialogo.exec_()

        if (self.nombreCompleto.text() == ''
            or self.usuario.text() == ''
            or self.clave.text() == ''
            or self.clave2.text() == ''
            or self.documento.text() == ''
            or self.correo.text() == ''
            or self.pregunta1.text() == ''
            or self.pregunta2.text() == ''
            or self.pregunta3.text() == ''
            or self.respuesta1.text() == ''
            or self.respuesta2.text() == ''
            or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Debe ingresar todos los campos")
            # Hacemos que se vea la ventana
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:
            # Abrimos el archivo y registramos los datos
            self.file = open('datos/clientes.txt','ab')
            self.file.write(bytes(
                self.nombreCompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.clave.text() + ";"
                + self.clave2.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pregunta1.text() + ";"
                + self.pregunta2.text() + ";"
                + self.pregunta3.text() + ";"
                + self.respuesta1.text() + ";"
                + self.respuesta2.text() + ";"
                + self.respuesta3.text() + "\n", encoding='UTF-8'
                ))
            self.file.close()
            self.accion_botonLimpiar()
            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()
if __name__ == '__main__':

    app= QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())

