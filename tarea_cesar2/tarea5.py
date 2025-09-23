import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTextEdit, QComboBox, QMessageBox

class SistemaDocentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión de Docentes")
        self.setGeometry(100, 100, 800, 600)
        self.archivo_datos = "docentes.txt"
        self.initUI()
        self.cargar_datos()

    def initUI(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout()
        central.setLayout(layout)

        # Panel izquierdo: formulario
        form_group = QWidget()
        form_layout = QGridLayout()
        form_group.setLayout(form_layout)

        self.legajo_edit = QLineEdit()
        self.nombre_edit = QLineEdit()
        self.apellido_edit = QLineEdit()
        self.dni_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.telefono_edit = QLineEdit()
        self.materia_edit = QLineEdit()
        self.categoria_combo = QComboBox()
        self.categoria_combo.addItems(["Titular", "Asociado", "Adjunto", "Auxiliar", "Interino"])

        form_layout.addWidget(QLabel("Legajo:"), 0, 0)
        form_layout.addWidget(self.legajo_edit, 0, 1)
        form_layout.addWidget(QLabel("Nombre:"), 1, 0)
        form_layout.addWidget(self.nombre_edit, 1, 1)
        form_layout.addWidget(QLabel("Apellido:"), 2, 0)
        form_layout.addWidget(self.apellido_edit, 2, 1)
        form_layout.addWidget(QLabel("DNI:"), 3, 0)
        form_layout.addWidget(self.dni_edit, 3, 1)
        form_layout.addWidget(QLabel("Email:"), 4, 0)
        form_layout.addWidget(self.email_edit, 4, 1)
        form_layout.addWidget(QLabel("Teléfono:"), 5, 0)
        form_layout.addWidget(self.telefono_edit, 5, 1)
        form_layout.addWidget(QLabel("Materia:"), 6, 0)
        form_layout.addWidget(self.materia_edit, 6, 1)
        form_layout.addWidget(QLabel("Categoría:"), 7, 0)
        form_layout.addWidget(self.categoria_combo, 7, 1)

        # Botones
        self.btn_agregar = QPushButton("Agregar")
        self.btn_buscar = QPushButton("Buscar")
        self.btn_modificar = QPushButton("Modificar")
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_limpiar = QPushButton("Limpiar")

        self.btn_agregar.clicked.connect(self.agregar_docente)
        self.btn_buscar.clicked.connect(self.buscar_docente)
        self.btn_modificar.clicked.connect(self.modificar_docente)
        self.btn_eliminar.clicked.connect(self.eliminar_docente)
        self.btn_limpiar.clicked.connect(self.limpiar_formulario)

        form_layout.addWidget(self.btn_agregar, 8, 0)
        form_layout.addWidget(self.btn_buscar, 8, 1)
        form_layout.addWidget(self.btn_modificar, 9, 0)
        form_layout.addWidget(self.btn_eliminar, 9, 1)
        form_layout.addWidget(self.btn_limpiar, 10, 0, 1, 2)

        layout.addWidget(form_group)

        # Panel derecho: lista y detalles
        right_group = QVBoxLayout()
        self.lista_docentes = QListWidget()
        self.lista_docentes.itemClicked.connect(self.mostrar_detalles)
        right_group.addWidget(self.lista_docentes)
        self.detalles_text = QTextEdit()
        self.detalles_text.setReadOnly(True)
        right_group.addWidget(self.detalles_text)

        right_widget = QWidget()
        right_widget.setLayout(right_group)
        layout.addWidget(right_widget)

    # Ejercicio 2: Funciones de archivo
    def cargar_datos(self):
        self.lista_docentes.clear()
        if not os.path.exists(self.archivo_datos):
            return
        with open(self.archivo_datos, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split("|")
                if len(datos) == 8:
                    self.agregar_a_lista(datos)

    def guardar_datos(self):
        with open(self.archivo_datos, "w", encoding="utf-8") as f:
            for i in range(self.lista_docentes.count()):
                item = self.lista_docentes.item(i)
                datos = item.data(100)
                f.write("|".join(datos) + "\n")

    def agregar_docente(self):
        legajo = self.legajo_edit.text().strip()
        if not legajo:
            QMessageBox.warning(self, "Error", "El legajo es obligatorio")
            return
        if self.buscar_por_legajo(legajo):
            QMessageBox.warning(self, "Error", "Ya existe ese legajo")
            return
        datos = [
            legajo,
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            self.email_edit.text().strip(),
            self.telefono_edit.text().strip(),
            self.materia_edit.text().strip(),
            self.categoria_combo.currentText()
        ]
        self.agregar_a_lista(datos)
        self.guardar_datos()
        self.limpiar_formulario()
        QMessageBox.information(self, "OK", "Docente agregado")

    # Ejercicio 3: Búsqueda y visualización
    def agregar_a_lista(self, datos):
        texto = f"{datos[2]}, {datos[1]} ({datos[0]})"
        from PyQt5.QtWidgets import QListWidgetItem
        item = QListWidgetItem(texto)
        item.setData(100, datos)
        self.lista_docentes.addItem(item)

    def mostrar_detalles(self, item):
        datos = item.data(100)
        detalles = f"""Legajo: {datos[0]}
Nombre: {datos[1]}
Apellido: {datos[2]}
DNI: {datos[3]}
Email: {datos[4]}
Teléfono: {datos[5]}
Materia: {datos[6]}
Categoría: {datos[7]}"""
        self.detalles_text.setPlainText(detalles)

    def buscar_por_legajo(self, legajo):
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(100)
            if datos[0].lower() == legajo.lower():
                return item
        return None

    def buscar_docente(self):
        legajo = self.legajo_edit.text().strip()
        if not legajo:
            QMessageBox.warning(self, "Error", "Ingrese legajo")
            return
        item = self.buscar_por_legajo(legajo)
        if item:
            self.lista_docentes.setCurrentItem(item)
            self.mostrar_detalles(item)
        else:
            QMessageBox.information(self, "No encontrado", "No existe ese legajo")

    # Ejercicio 4: Modificar y eliminar
    def modificar_docente(self):
        item = self.lista_docentes.currentItem()
        if not item:
            QMessageBox.warning(self, "Error", "Seleccione un docente")
            return
        datos = item.data(100)
        self.legajo_edit.setText(datos[0])
        self.nombre_edit.setText(datos[1])
        self.apellido_edit.setText(datos[2])
        self.dni_edit.setText(datos[3])
        self.email_edit.setText(datos[4])
        self.telefono_edit.setText(datos[5])
        self.materia_edit.setText(datos[6])
        self.categoria_combo.setCurrentText(datos[7])
        # Al modificar, el botón agregar actualiza el item
        self.btn_agregar.setText("Actualizar")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(lambda: self.actualizar_docente(item))

    def actualizar_docente(self, item):
        datos = [
            self.legajo_edit.text().strip(),
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            self.email_edit.text().strip(),
            self.telefono_edit.text().strip(),
            self.materia_edit.text().strip(),
            self.categoria_combo.currentText()
        ]
        item.setText(f"{datos[2]}, {datos[1]} ({datos[0]})")
        item.setData(100, datos)
        self.guardar_datos()
        self.limpiar_formulario()
        self.btn_agregar.setText("Agregar")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)
        QMessageBox.information(self, "OK", "Docente modificado")

    def eliminar_docente(self):
        item = self.lista_docentes.currentItem()
        if not item:
            QMessageBox.warning(self, "Error", "Seleccione un docente")
            return
        datos = item.data(100)
        r = QMessageBox.question(self, "Confirmar", f"¿Eliminar a {datos[1]} {datos[2]}?", QMessageBox.Yes | QMessageBox.No)
        if r == QMessageBox.Yes:
            self.lista_docentes.takeItem(self.lista_docentes.row(item))
            self.guardar_datos()
            QMessageBox.information(self, "OK", "Docente eliminado")

    def limpiar_formulario(self):
        self.legajo_edit.clear()
        self.nombre_edit.clear()
        self.apellido_edit.clear()
        self.dni_edit.clear()
        self.email_edit.clear()
        self.telefono_edit.clear()
        self.materia_edit.clear()
        self.categoria_combo.setCurrentIndex(0)
        self.btn_agregar.setText("Agregar")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SistemaDocentes()
    win.show()
    sys.exit(app.exec_())