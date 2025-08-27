import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout, 
                             QRadioButton, QButtonGroup, QComboBox, QCheckBox, 
                             QPushButton, QMessageBox)
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        # Crear QLabel grande y centrado ("Formulario de Registro")
        titulo = QLabel("Formulario de Registro")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(titulo, 0, 0, 1, 2)  # Fila 0, ocupa 2 columnas

        # Crear QLabel "Nombre:" y QLineEdit al lado
        self.label_nombre = QLabel("Nombre:")
        layout.addWidget(self.label_nombre, 1, 0)  # Fila 1, columna 0
        
        self.input_nombre = QLineEdit()
        layout.addWidget(self.input_nombre, 1, 1)  # Fila 1, columna 1

        # Campo Email
        self.label_email = QLabel("Email:")
        layout.addWidget(self.label_email, 2, 0)  # Fila 2, columna 0
        
        self.input_email = QLineEdit()
        layout.addWidget(self.input_email, 2, 1)  # Fila 2, columna 1

        # Campo Contraseña (ocultar texto)
        self.label_password = QLabel("Contraseña:")
        layout.addWidget(self.label_password, 3, 0)  # Fila 3, columna 0
        
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)  # Oculta el texto
        layout.addWidget(self.input_password, 3, 1)  # Fila 3, columna 1

        # Label para Género
        self.label_genero = QLabel("Género:")
        layout.addWidget(self.label_genero, 4, 0)  # Fila 4, columna 0

        # RadioButtons para Masculino y Femenino en la misma fila
        self.radio_masculino = QRadioButton("Masculino")
        self.radio_femenino = QRadioButton("Femenino")
        
        layout.addWidget(self.radio_masculino, 4, 1)  # Fila 4, columna 1
        layout.addWidget(self.radio_femenino, 4, 2)   # Fila 4, columna 2

        # Agrupar los RadioButtons para que solo uno pueda estar seleccionado
        self.grupo_genero = QButtonGroup(self)
        self.grupo_genero.addButton(self.radio_masculino)
        self.grupo_genero.addButton(self.radio_femenino)

        # Label para País
        self.label_pais = QLabel("País:")
        layout.addWidget(self.label_pais, 5, 0)  # Fila 5, columna 0

        # QComboBox con al menos 5 países
        self.combo_pais = QComboBox()
        self.combo_pais.addItem("Seleccione un país")  # Opción por defecto
        self.combo_pais.addItem("Argentina")
        self.combo_pais.addItem("Brasil")
        self.combo_pais.addItem("Chile")
        self.combo_pais.addItem("Colombia")
        self.combo_pais.addItem("México")
        self.combo_pais.addItem("España")
        layout.addWidget(self.combo_pais, 5, 1, 1, 2)  # Fila 5, columna 1, ocupa 2 columnas

        # Checkbox de términos y condiciones
        self.checkbox_terminos = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.checkbox_terminos, 6, 0, 1, 3)  # Fila 6, ocupa 3 columnas

        # EJERCICIO 6: Botón de registro
        self.boton_registrar = QPushButton("Registrarse")
        self.boton_registrar.clicked.connect(self.validar_formulario)
        layout.addWidget(self.boton_registrar, 7, 0, 1, 3)  # Fila 7, ocupa 3 columnas

    # EJERCICIO 6: Función de validación del formulario
    def validar_formulario(self):
        # Validar campo Nombre
        if not self.input_nombre.text().strip():
            QMessageBox.warning(self, "Error", "Por favor, ingrese su nombre.")
            return

        # Validar campo Email
        if not self.input_email.text().strip():
            QMessageBox.warning(self, "Error", "Por favor, ingrese su email.")
            return

        # Validar campo Contraseña
        if not self.input_password.text().strip():
            QMessageBox.warning(self, "Error", "Por favor, ingrese una contraseña.")
            return

        # Validar selección de Género
        if not self.radio_masculino.isChecked() and not self.radio_femenino.isChecked():
            QMessageBox.warning(self, "Error", "Por favor, seleccione su género.")
            return

        # Validar selección de País
        if self.combo_pais.currentText() == "Seleccione un país":
            QMessageBox.warning(self, "Error", "Por favor, seleccione un país.")
            return

        # Validar aceptación de términos
        if not self.checkbox_terminos.isChecked():
            QMessageBox.warning(self, "Error", "Debe aceptar los términos y condiciones.")
            return

        # Si todas las validaciones pasan, mostrar mensaje de éxito
        QMessageBox.information(self, "Éxito", "¡Registro completado con éxito!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())