from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, \
    QDialog, QDialogButtonBox, QVBoxLayout

from cliente import Cliente


class Ventana4(QMainWindow):
    def __init__(self, anterior, cedula):
        super(Ventana4, self).__init__(None)
        self.ventanaAnterior = anterior
        self.cedulaUsuario = cedula
        # Poner el título
        self.setWindowTitle("Editar Usuarios")
        # Poner el ícono
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

        self.fondo.setStyleSheet("background-color:#9693C9;")

        self.setCentralWidget(self.fondo)
        # Establecemos la distribución de los elementos con Layout horizontal
        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # --------- CREAR LAYOUT IZQUIERDO ------------
        self.ladoIzquierdo = QFormLayout()
        # Hacemos el letrero
        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Les escribimos el texto
        self.letrero1.setText("Editar Cliente")

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
        self.letrero2.setStyleSheet("color: #000000; margin-bottom: 40px;"
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
        self.nombreCompleto.setStyleSheet("margin-bottom: 30px;")

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Nombre completo*", self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)
        self.usuario.setStyleSheet("margin-bottom: 30px;")
        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password
        self.clave = QLineEdit()
        self.clave.setFixedWidth(250)
        self.clave.setStyleSheet("margin-bottom: 30px;")
        self.clave.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Contraseña*", self.clave)

        # Hacemos el campo para ingresar el password
        self.clave2 = QLineEdit()
        self.clave2.setFixedWidth(250)
        self.clave2.setStyleSheet("margin-bottom: 30px;")
        self.clave2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Verificación Contraseña*", self.clave2)

        # Hacemos el campo para ingresar el documento
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.documento.setStyleSheet("margin-bottom: 30px;")
        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.correo.setStyleSheet("margin-bottom: 30px;")
        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Correo electrónico*", self.correo)

        # ---------- BOTÓN EDITAR ----------------
        self.btnEditar = QPushButton("Editar")

        # Establecemos el ancho del botón
        self.btnEditar.setFixedWidth(90)

        # Le ponemos los estilos
        self.btnEditar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.btnEditar.clicked.connect(self.accionBtnEditar)

        # ---------- BOTÓN LIMPIAR ----------------
        self.btnLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del botón
        self.btnLimpiar.setFixedWidth(90)

        # Le ponemos los estilos
        self.btnLimpiar.setStyleSheet("background-color: #008B45;"
                                     "color: #FFFFFF;"
                                     "padding: 10px;"
                                     "margin-top: 40px;")

        self.btnLimpiar.clicked.connect(self.accionBtnlimpiar)
        self.ladoIzquierdo.addRow(self.btnEditar,self.btnLimpiar)

        self.horizontal.addLayout(self.ladoIzquierdo)


        # --------- CREAR LAYOUT DERECHO ------------

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
        self.letrero3.setStyleSheet("color: #000000;")

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
        self.letrero4.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
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
        self.respuesta3.setStyleSheet("margin-bottom: 30px;")
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


        # ---------- BOTÓN ELIMINAR ----------------
        self.btnEliminar = QPushButton("Eliminar")

        # Establecemos el ancho del botón
        self.btnEliminar.setFixedWidth(90)

        # Le ponemos los estilos
        self.btnEliminar.setStyleSheet("background-color: #008B45;"
                                     "color: #FFFFFF;"
                                     "padding: 10px;"
                                     "margin-top: 40px;")

        self.btnEliminar.clicked.connect(self.accionBtnEliminar)

        # ---------- BOTÓN VOLVER ----------------
        self.btnVolver = QPushButton("Volver")

        # Establecemos el ancho del botón
        self.btnVolver.setFixedWidth(90)

        # Le ponemos los estilos
        self.btnVolver.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")

        self.btnVolver.clicked.connect(self.accionBtnVolver)

        self.ladoDerecho.addRow(self.btnEliminar, self.btnVolver)


        self.horizontal.addLayout(self.ladoDerecho)

        # --------- PONER SIEMPRE AL FINAL ------------
        self.fondo.setLayout(self.horizontal)

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

        # Llenamos los campos con los datos del usuario
        self.cargarDatos()


    def accionBtnEditar(self):
        self.datosCorrectos = True
        self.ventanaDialogo.setWindowTitle("Formulario de edición")
        # Validamos que las claves sean iguales
        if self.clave.text() != self.clave2.text():
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
            or self.respuesta3.text() == ''):
            self.datosCorrectos = False
            self.mensaje.setText("Debe seleccionar un usuario con documento válido")
            # Hacemos que se vea la ventana
            self.ventanaDialogo.exec_()
            self.accionBtnVolver()

        if self.datosCorrectos:
            self.file = open('datos/clientes.txt', 'rb')
            usuarios = []
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")

                # paramos el bucle si ya no encuentra más registros en el archivo
                if linea == '':
                    break

                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10])
                # Agregar los datos a la lista
                usuarios.append(u)
            # cerramos ael archivo txt
            self.file.close()
            existeDocumento = False

            for u in usuarios:
                if int(u.documento) == self.cedulaUsuario:
                    u.usuario = self.usuario.text()
                    u.clave = self.clave.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.respuesta3 = self.respuesta3.text()
                    existeDocumento = True
                    break

            if not existeDocumento:
                self.mensaje.setText(f"No existe usuario registrado con el documento {self.cedulaUsuario}")
                self.ventanaDialogo.exec_()
                self.accionBtnVolver()
            self.file = open('datos/clientes.txt', 'wb')
            for u in usuarios:
                self.file.write(bytes(
                    u.nombreCompleto + ";"
                    + u.usuario + ";"
                    + u.clave + ";"
                    + u.documento + ";"
                    + u.correo + ";"
                    + u.pregunta1 + ";"
                    + u.pregunta2 + ";"
                    + u.pregunta3 + ";"
                    + u.respuesta1 + ";"
                    + u.respuesta2 + ";"
                    + u.respuesta3, encoding='UTF-8'))

            self.file.close()
            if existeDocumento:
                self.mensaje.setText("Usuario actualizado correctamente")
                self.ventanaDialogo.exec_()
                self.accionBtnlimpiar()
                self.accionBtnVolver()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                #print(linea)
                if linea == '':
                    break
            self.file.close()

    def accionBtnlimpiar(self):
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

    def accionBtnEliminar(self):
        self.datosCorrectos = True
        self.eliminar = False

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
                or self.respuesta3.text() == ''):

            self.datosCorrectos = False

            self.mensaje.setText("Debe seleccionar un usuario con documento válido")
            self.ventanaDialogo.exec_()
            self.accionBtnVolver()

        if self.datosCorrectos:
            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            self.ventanaDialogoEliminar.resize(300, 150)

            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            self.verticalEliminar = QVBoxLayout()

            self.mensajeEliminar = QLabel("¿Estas seguro que desea eliminar este registro de usuario?")
            self.mensajeEliminar.setStyleSheet('background-color: #008B45; color: #FFFFFF; padding: 10 px;')

            self.verticalEliminar.addWidget(self.mensajeEliminar)

            # Se agregaron los botones aceptar y cancelar

            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            # agergamos opcionBox
            self.verticalEliminar.addWidget(self.opcionesBox)

            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            self.file = open('datos/clientes.txt', 'rb')
            usuarios = []
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")

                # paramos el bucle si ya no encuentra más registros en el archivo
                if linea == '':
                    break

                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10])
                # Agregar los datos a la lista
                usuarios.append(u)
            # cerramos ael archivo txt
            self.file.close()

            existeDocumento = False
            for u in usuarios:
                if int(u.documento) == self.cedulaUsuario:
                    usuarios.remove(u)
                    existeDocumento = True
                    break

            self.file = open('datos/clientes.txt', 'wb')

            # Ingresar los datos con el registro eliminado

            for u in usuarios:
                self.file.write(bytes(
                    u.nombreCompleto + ";"
                    + u.usuario + ";"
                    + u.clave + ";"
                    + u.documento + ";"
                    + u.correo + ";"
                    + u.pregunta1 + ";"
                    + u.pregunta2 + ";"
                    + u.pregunta3 + ";"
                    + u.respuesta1 + ";"
                    + u.respuesta2 + ";"
                    + u.respuesta3, encoding='UTF-8'))
            self.file.close()

            if existeDocumento:
                self.mensaje.setText("Usuario eliminado correctamente.")
                self.ventanaDialogo.exec_()
                self.accionBtnlimpiar()
                self.accionBtnVolver()

    def accionBtnVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cargarDatos(self):
        self.file = open('datos/clientes.txt', 'rb')
        usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")

            # paramos el bucle si ya no encuentra más registros en el archivo
            if linea == '':
                break

            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10])
            # Agregar los datos a la lista
            usuarios.append(u)
        # cerramos ael archivo txt
        self.file.close()

        # Variable para controlar si existe documento
        existeDocumento = False
        #Buscamos que exista la cédula

        for u in usuarios:
            if int(u.documento) == self.cedulaUsuario:
                # Procedemos a mostrar los datos en el formulario
                self.nombreCompleto.setText(u.nombreCompleto)
                # Hacemos que no se pueda editar el campo
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.clave.setText(u.clave)
                self.clave2.setText(u.clave)
                self.documento.setText(u.documento)
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.pregunta2.setText(u.pregunta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta1.setText(u.respuesta1)
                self.respuesta2.setText(u.respuesta2)
                self.respuesta3.setText(u.respuesta3)
                existeDocumento = True
                # Salimos del for
                break

        if not existeDocumento:
            self.mensaje.setText(f"No existe usuario registrado con el documento {self.cedulaUsuario}")
            self.ventanaDialogo.exec_()
            self.accionBtnVolver()

    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()