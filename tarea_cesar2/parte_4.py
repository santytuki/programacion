import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QRadioButton, QButtonGroup, QComboBox
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
        label_nombre = QLabel("Nombre:")
        layout.addWidget(label_nombre, 1, 0)  # Fila 1, columna 0
        
        input_nombre = QLineEdit()
        layout.addWidget(input_nombre, 1, 1)  # Fila 1, columna 1

        # Campo Email
        label_email = QLabel("Email:")
        layout.addWidget(label_email, 2, 0)  # Fila 2, columna 0
        
        input_email = QLineEdit()
        layout.addWidget(input_email, 2, 1)  # Fila 2, columna 1

        # Campo Contraseña (ocultar texto)
        label_password = QLabel("Contraseña:")
        layout.addWidget(label_password, 3, 0)  # Fila 3, columna 0
        
        input_password = QLineEdit()
        input_password.setEchoMode(QLineEdit.Password)  # Oculta el texto
        layout.addWidget(input_password, 3, 1)  # Fila 3, columna 1

        # Label para Género
        label_genero = QLabel("Género:")
        layout.addWidget(label_genero, 4, 0)  # Fila 4, columna 0

        # RadioButtons para Masculino y Femenino en la misma fila
        radio_masculino = QRadioButton("Masculino")
        radio_femenino = QRadioButton("Femenino")
        
        layout.addWidget(radio_masculino, 4, 1)  # Fila 4, columna 1
        layout.addWidget(radio_femenino, 4, 2)   # Fila 4, columna 2

        # Agrupar los RadioButtons para que solo uno pueda estar seleccionado
        grupo_genero = QButtonGroup(self)
        grupo_genero.addButton(radio_masculino)
        grupo_genero.addButton(radio_femenino)

        # EJERCICIO 4: Label para País
        label_pais = QLabel("País:")
        layout.addWidget(label_pais, 5, 0)  # Fila 5, columna 0

        # EJERCICIO 4: QComboBox con al menos 5 países
        combo_pais = QComboBox()
        combo_pais.addItem("Seleccione un país")  # Opción por defecto
        combo_pais.addItem("Argentina")
        combo_pais.addItem("Brasil")
        combo_pais.addItem("Chile")
        combo_pais.addItem("Colombia")
        combo_pais.addItem("México")
        combo_pais.addItem("España")
        layout.addWidget(combo_pais, 5, 1, 1, 2)  # Fila 5, columna 1, ocupa 2 columnas

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())