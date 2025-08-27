import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        # EJERCICIO 1: QLabel grande y centrado
        titulo = QLabel("Formulario de Registro")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(titulo, 0, 0, 1, 2)

        # EJERCICIO 1: QLabel "Nombre:" y QLineEdit
        label_nombre = QLabel("Nombre:")
        layout.addWidget(label_nombre, 1, 0)
        self.input_nombre = QLineEdit()
        layout.addWidget(self.input_nombre, 1, 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())