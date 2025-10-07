import mysql.connector
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QTableWidget, 
                             QTableWidgetItem, QMessageBox)
from mysql.connector import Error

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pagina_actual = 0
        self.registros_por_pagina = 10
        self.total_registros = 0
        
        self.initUI()
        self.calcular_total_registros()
        self.mostrar_registros()
        
    def initUI(self):
        # Configuración inicial de la ventana
        self.setWindowTitle("Sistema de Gestión Escolar")
        self.setGeometry(800, 300, 800, 500)  # Aumenté el tamaño para mejor visualización

        # Widget central y layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout_principal = QVBoxLayout(central_widget)

        # Título
        titulo = QLabel("LISTA DE ALUMNOS")
        titulo.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout_principal.addWidget(titulo)

        # Tabla para mostrar los registros
        self.tabla = QTableWidget()
        layout_principal.addWidget(self.tabla)

        # Layout para controles de paginación
        layout_controles = QHBoxLayout()
        
        # Botón Anterior
        self.btn_anterior = QPushButton("← Anterior")
        self.btn_anterior.clicked.connect(self.pagina_anterior)
        layout_controles.addWidget(self.btn_anterior)

        # Espacio flexible
        layout_controles.addStretch()

        # Etiqueta para mostrar página actual
        self.lbl_pagina = QLabel("Página 0 de 0")
        layout_controles.addWidget(self.lbl_pagina)

        # Espacio flexible
        layout_controles.addStretch()

        # Botón Siguiente
        self.btn_siguiente = QPushButton("Siguiente →")
        self.btn_siguiente.clicked.connect(self.pagina_siguiente)
        layout_controles.addWidget(self.btn_siguiente)

        layout_principal.addLayout(layout_controles)
        self.actualizar_botones()

    def conectar_db(self):
        """Establece conexión con la base de datos"""
        try:
            return mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='sharktopus12',
                database='colegio'
            )
        except Error as e:
            QMessageBox.critical(self, "Error", f"Error de conexión: {str(e)}")
            return None

    def calcular_total_registros(self):
        """Calcula el total de registros en la tabla alumno"""
        conexion = self.conectar_db()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT COUNT(*) FROM alumno")
                self.total_registros = cursor.fetchone()[0]
                print(f"Total de registros encontrados: {self.total_registros}")
            except Error as e:
                QMessageBox.critical(self, "Error", f"Error al contar registros: {str(e)}")
            finally:
                conexion.close()

    def mostrar_registros(self):
        """Muestra los registros de la página actual en la tabla"""
        conexion = self.conectar_db()
        if not conexion:
            return

        try:
            cursor = conexion.cursor()
            # Consulta con límite y offset para paginación
            offset = self.pagina_actual * self.registros_por_pagina
            print(f"Consultando registros: LIMIT {self.registros_por_pagina} OFFSET {offset}")
            
            cursor.execute("SELECT id, nombre, apellido FROM alumno ORDER BY id LIMIT %s OFFSET %s", 
                          (self.registros_por_pagina, offset))
            
            registros = cursor.fetchall()
            print(f"Registros obtenidos: {len(registros)}")
            
            # Configurar tabla
            self.tabla.setRowCount(len(registros))
            self.tabla.setColumnCount(3)
            self.tabla.setHorizontalHeaderLabels(['ID', 'Nombre', 'Apellido'])
            
            # Ajustar el ancho de las columnas
            self.tabla.setColumnWidth(0, 50)   # ID
            self.tabla.setColumnWidth(1, 200)  # Nombre
            self.tabla.setColumnWidth(2, 200)  # Apellido

            # Llenar tabla con datos
            for fila, registro in enumerate(registros):
                for columna, valor in enumerate(registro):
                    self.tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))
            
        except Error as e:
            QMessageBox.critical(self, "Error", f"Error al cargar registros: {str(e)}")
        finally:
            conexion.close()
            self.actualizar_etiqueta_pagina()
            self.actualizar_botones()

    def actualizar_etiqueta_pagina(self):
        """Actualiza la etiqueta con la información de paginación"""
        total_paginas = max(1, (self.total_registros + self.registros_por_pagina - 1) // self.registros_por_pagina)
        self.lbl_pagina.setText(f"Página {self.pagina_actual + 1} de {total_paginas}")

    def actualizar_botones(self):
        """Habilita/deshabilita botones según la página actual"""
        total_paginas = max(1, (self.total_registros + self.registros_por_pagina - 1) // self.registros_por_pagina)
        self.btn_anterior.setEnabled(self.pagina_actual > 0)
        self.btn_siguiente.setEnabled(self.pagina_actual < total_paginas - 1)

    def pagina_anterior(self):
        """Retrocede a la página anterior"""
        self.pagina_actual -= 1
        self.mostrar_registros()

    def pagina_siguiente(self):
        """Avanza a la página siguiente"""
        self.pagina_actual += 1
        self.mostrar_registros()

def insertar_datos_ejemplo():
    """Inserta datos de ejemplo en la base de datos"""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='sharktopus12',
            database='colegio'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Verificar si ya existen datos
            cursor.execute("SELECT COUNT(*) FROM alumno")
            count = cursor.fetchone()[0]
            
            if count == 0:
                print("Insertando datos de ejemplo...")
                
                # Datos de ejemplo
                alumnos = [
                    ('Juan', 'Pérez'),
                    ('María', 'Gómez'),
                    ('Carlos', 'López'),
                    ('Ana', 'Martínez'),
                    ('Luis', 'Rodríguez'),
                    ('Elena', 'Silva'),
                    ('Diego', 'Fernández'),
                    ('Marta', 'Hernández'),
                    ('Jorge', 'Díaz'),
                    ('Sofía', 'Torres'),
                    ('Pedro', 'Ramírez'),
                    ('Laura', 'Castro'),
                    ('Andrés', 'Vargas'),
                    ('Isabel', 'Rojas'),
                    ('Fernando', 'Mendoza'),
                    ('Carlos', 'López'),
                    ('Ana', 'Martínez'),
                    ('Luis', 'Rodríguez'),
                    ('Elena', 'Silva'),
                    ('Diego', 'Fernández'),
                    ('Marta', 'Hernández'),
                    ('Jorge', 'Díaz'),
                    ('Sofía', 'Torres'),
                    ('Pedro', 'Ramírez'),
                    ('Laura', 'Castro'),
                    ('Andrés', 'Vargas'),
                    ('Isabel', 'Rojas'),
                    ('Fernando', 'Mendoza'),
                    ('Roberto', 'García'),
                    ('Lucía', 'Moreno'),
                    ('Miguel', 'Álvarez'),
                    ('Cristina', 'Romero'),
                    ('Antonio', 'Navarro'),
                    ('Patricia', 'Torres'),
                    ('Francisco', 'Domínguez'),
                    ('Silvia', 'Vázquez'),
                    ('Joaquín', 'Ramos'),
                    ('Nuria', 'Gil'),
                    ('Alberto', 'Serrano'),
                    ('Rosa', 'Blanco')
                ]
                
                # Insertar alumnos
                sql = "INSERT INTO alumno (nombre, apellido) VALUES (%s, %s)"
                cursor.executemany(sql, alumnos)
                
                connection.commit()
                print(f"{len(alumnos)} alumnos insertados correctamente")
            else:
                print(f"Ya existen {count} registros en la tabla alumno")
                
    except Error as e:
        print(f"Error al insertar datos de ejemplo: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Configuración inicial de la base de datos
try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='sharktopus12'
    )
    if connection.is_connected():
        print('Conexión a MySQL establecida')
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS colegio;")
        print("Base de datos 'colegio' creada/existe")
        cursor.execute("USE colegio;")
        print("Usando base de datos 'colegio'")
        
        # Crear tablas si no existen
        tablas = {
            'alumno': """
                CREATE TABLE IF NOT EXISTS alumno (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL,
                    apellido VARCHAR(50) NOT NULL
                );
            """,
            'materia': """
                CREATE TABLE IF NOT EXISTS materia (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL
                );
            """,
            'cursado': """
                CREATE TABLE IF NOT EXISTS cursado (
                    id_alumno INT,
                    id_materia INT,
                    PRIMARY KEY (id_alumno, id_materia),
                    FOREIGN KEY (id_alumno) REFERENCES alumno(id),
                    FOREIGN KEY (id_materia) REFERENCES materia(id)
                );
            """
        }
        
        for nombre_tabla, consulta in tablas.items():
            cursor.execute(consulta)
            print(f"Tabla '{nombre_tabla}' creada/existe")
        
        print("Todas las tablas fueron verificadas/creadas")
        
        # Insertar datos de ejemplo
        insertar_datos_ejemplo()
        
except Error as e:
    print(f"Error de MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a MySQL cerrada")

# Ejecución de la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
        