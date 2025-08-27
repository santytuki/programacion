import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
    QRadioButton, QButtonGroup, QComboBox, QCheckBox, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #e0f7fa;")
        layout = QGridLayout()
        self.setLayout(layout)

        # Título
        titulo = QLabel("Formulario de Registro")
        titulo.setStyleSheet("font-size: 22px; font-weight: bold; color: #00796b;")
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo, 0, 0, 1, 2)

        # Nombre
        label_nombre = QLabel("Nombre:")
        self.input_nombre = QLineEdit()
        layout.addWidget(label_nombre, 1, 0)
        layout.addWidget(self.input_nombre, 1, 1)

        # Email
        label_email = QLabel("Email:")
        self.input_email = QLineEdit()
        layout.addWidget(label_email, 2, 0)
        layout.addWidget(self.input_email, 2, 1)

        # Contraseña
        label_pass = QLabel("Contraseña:")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        layout.addWidget(label_pass, 3, 0)
        layout.addWidget(self.input_pass, 3, 1)

        # Género
        label_genero = QLabel("Género:")
        self.radio_m = QRadioButton("Masculino")
        self.radio_f = QRadioButton("Femenino")
        grupo_genero = QButtonGroup(self)
        grupo_genero.addButton(self.radio_m)
        grupo_genero.addButton(self.radio_f)
        layout.addWidget(label_genero, 4, 0)
        layout.addWidget(self.radio_m, 4, 1)
        layout.addWidget(self.radio_f, 4, 2)

        # País
        label_pais = QLabel("País:")
        self.combo_pais = QComboBox()
        self.combo_pais.addItems(["Argentina", "Brasil", "Chile", "Uruguay", "Paraguay"])
        layout.addWidget(label_pais, 5, 0)
        layout.addWidget(self.combo_pais, 5, 1)

        # Términos
        self.checkbox = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.checkbox, 6, 0, 1, 2)

        # Botón
        boton = QPushButton("Registrarse")
        boton.setStyleSheet("background-color: #00796b; color: white; font-size: 15px;")
        layout.addWidget(boton, 7, 0, 1, 2)
        layout.setAlignment(Qt.AlignCenter)

        boton.clicked.connect(self.validar)

    def validar(self):
        if (not self.input_nombre.text().strip() or
            not self.input_email.text().strip() or
            not self.input_pass.text().strip() or
            not (self.radio_m.isChecked() or self.radio_f.isChecked()) or
            not self.checkbox.isChecked()):
            QMessageBox.warning(self, "Error", "Completa todos los campos y acepta los términos.")
        else:
            QMessageBox.information(self, "Éxito", "¡Registro exitoso!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())