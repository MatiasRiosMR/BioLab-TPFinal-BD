import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QDialog, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt
import psycopg2
from PyQt5.QtWidgets import QVBoxLayout, QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import graficas  # Importa el archivo de gráficos

# Configuración de la base de datos
DB_CONFIG = {
    "dbname": "BioLab",
    "user": "postgres",
    "password": "123456",
    "host": "localhost",
    "port": "5432"
}

# Conexión a PostgreSQL
def conectar_bd():
    try:
        print("Intentando conectar con la base de datos...")
        conn = psycopg2.connect(**DB_CONFIG)
        print("Conexión a la base de datos establecida con éxito.")
        return conn
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        sys.exit(1)


class BuscarPacientes(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔍 Buscar Pacientes")
        self.setGeometry(200, 200, 1000, 500)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        # Campo de búsqueda por folio
        self.label_folio = QLabel("🆔 Buscar por folio:")
        self.label_folio.setFont(QFont("Arial", 14))
        self.input_folio = QLineEdit()
        self.input_folio.setPlaceholderText("Ingresa el folio del paciente")
        self.input_folio.setStyleSheet("padding: 10px; font-size: 14px; border: 2px solid #00BFFF;")

        # Campo de búsqueda por sexo
        self.label_sexo = QLabel("⚥ Buscar por sexo:")
        self.label_sexo.setFont(QFont("Arial", 14))
        self.input_sexo = QLineEdit()
        self.input_sexo.setPlaceholderText("Ingresa el sexo del paciente (M/F)")
        self.input_sexo.setStyleSheet("padding: 10px; font-size: 14px; border: 2px solid #FF69B4;")

        # Botón de búsqueda
        self.boton_buscar = QPushButton("🔍 Buscar")
        self.boton_buscar.setFont(QFont("Arial", 14))
        self.boton_buscar.setStyleSheet("background-color: #32CD32; color: white; padding: 10px;")
        self.boton_buscar.clicked.connect(self.buscar_pacientes)

        # Tabla para mostrar resultados
        self.tabla_resultados = QTableWidget()
        self.tabla_resultados.setColumnCount(4)
        self.tabla_resultados.setHorizontalHeaderLabels(["Folio", "Sexo", "Edad", "Detalles"])
        self.tabla_resultados.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla_resultados.setStyleSheet("font-size: 12px; background-color: #F5F5F5;")

        # Agregar widgets al layout
        layout.addWidget(self.label_folio)
        layout.addWidget(self.input_folio)
        layout.addWidget(self.label_sexo)
        layout.addWidget(self.input_sexo)
        layout.addWidget(self.boton_buscar)
        layout.addWidget(self.tabla_resultados)
        
        self.setLayout(layout)

    def buscar_pacientes(self):
        folio = self.input_folio.text()
        sexo = self.input_sexo.text()
        
        print(f"Iniciando búsqueda de pacientes. Folio: {folio}, Sexo: {sexo}")

        query = "SELECT folio_id, sexo, edad FROM Paciente WHERE 1=1"
        params = []

        if folio:
            query += " AND folio_id = %s"
            params.append(folio)
        if sexo:
            query += " AND sexo = %s"
            params.append(sexo)

        conn = conectar_bd()
        cursor = conn.cursor()

        try:
            print(f"Ejecutando consulta: {query} con parámetros {params}")
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            print(f"Resultados encontrados: {len(resultados)}")
            self.tabla_resultados.setRowCount(0)
            
            for fila, datos in enumerate(resultados):
                self.tabla_resultados.insertRow(fila)
                for columna, dato in enumerate(datos):
                    self.tabla_resultados.setItem(fila, columna, QTableWidgetItem(str(dato)))

                # Botón para ver detalles
                boton_detalles = QPushButton("📋 Ver Detalles")
                boton_detalles.setStyleSheet("background-color: #FFD700; color: black; padding: 5px;")
                boton_detalles.clicked.connect(lambda _, f=datos[0]: self.ver_detalles(f))
                self.tabla_resultados.setCellWidget(fila, 3, boton_detalles)
        
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            QMessageBox.critical(self, "Error", f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()
            conn.close()
            print("Conexión con la base de datos cerrada.")


    def ver_detalles(self, folio):
        print(f"Mostrando detalles para el paciente con folio: {folio}")
        detalles_dialog = DetallesPaciente(folio)
        detalles_dialog.exec_()

class DetallesPaciente(QDialog):
    def __init__(self, folio):
        super().__init__()
        self.folio = folio
        self.setWindowTitle(f"📋 Detalles del Paciente: {folio}")
        self.setGeometry(200, 200, 800, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel(f"Detalles del Paciente con Folio: {self.folio}")
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        self.label.setStyleSheet("color: #4682B4;")
        layout.addWidget(self.label)

        # Crear tabla para mostrar los detalles
        self.tabla_detalles = QTableWidget()
        self.tabla_detalles.setColumnCount(2)
        self.tabla_detalles.setHorizontalHeaderLabels(["Campo", "Valor"])
        self.tabla_detalles.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla_detalles.horizontalHeader().setStretchLastSection(True)
        self.tabla_detalles.setStyleSheet("font-size: 14px; background-color: #F5F5F5;")
        layout.addWidget(self.tabla_detalles)

        self.cargar_detalles()

        self.setLayout(layout)

    def cargar_detalles(self):
        print(f"Cargando detalles del paciente con folio: {self.folio}")
        conn = conectar_bd()
        cursor = conn.cursor()

        query = """
        SELECT * FROM Paciente WHERE folio_id = %s
        """
        try:
            print(f"Ejecutando consulta de detalles: {query} con folio {self.folio}")
            cursor.execute(query, (self.folio,))
            detalles = cursor.fetchone()

            if detalles:
                print(f"Detalles encontrados: {detalles}")
                columnas = [desc[0] for desc in cursor.description]
                self.tabla_detalles.setRowCount(len(columnas))

                for fila, (columna, valor) in enumerate(zip(columnas, detalles)):
                    self.tabla_detalles.setItem(fila, 0, QTableWidgetItem(columna))
                    self.tabla_detalles.setItem(fila, 1, QTableWidgetItem(str(valor)))
            else:
                print("No se encontraron detalles para el folio.")
                QMessageBox.warning(self, "Sin datos", "No se encontraron detalles para este folio.")
        
        except Exception as e:
            print(f"Error al cargar los detalles: {e}")
            QMessageBox.critical(self, "Error", f"Error al cargar los detalles: {e}")
        finally:
            cursor.close()
            conn.close()
            print("Conexión con la base de datos cerrada tras cargar detalles.")

class GraficasEstadisticas(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Seleccionar Gráfica")
        self.setGeometry(200, 200, 600, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Diccionario de gráficas disponibles
        self.graficas = {
            "Distribución de IMC": graficas.plot_bmi_distribution,
            "Horas de Sueño vs Riesgo de Hipertensión": graficas.plot_sleep_vs_hypertension,
            "Colesterol Promedio por Género": graficas.plot_avg_total_cholesterol_by_gender,
            "Distribucion de Trigliceridos": graficas.plot_triglyceride_distribution,
            "Riesgo de hipertensión y colesterol total por rango de edad": graficas.plot_hypertension_and_cholesterol_by_age
        }

        # Lista para seleccionar gráfica
        self.label_seleccion = QLabel("Seleccione una gráfica para visualizar:")
        self.label_seleccion.setFont(QFont("Arial", 14))
        self.label_seleccion.setAlignment(Qt.AlignCenter)

        self.lista_graficas = QTableWidget()
        self.lista_graficas.setRowCount(len(self.graficas))
        self.lista_graficas.setColumnCount(1)
        self.lista_graficas.setHorizontalHeaderLabels(["Gráficas"])
        self.lista_graficas.horizontalHeader().setStretchLastSection(True)
        self.lista_graficas.setEditTriggers(QTableWidget.NoEditTriggers)
        self.lista_graficas.setSelectionBehavior(QTableWidget.SelectRows)
        self.lista_graficas.setStyleSheet("font-size: 14px; background-color: #F5F5F5;")

        # Rellenar la lista con los nombres de las gráficas
        for i, nombre in enumerate(self.graficas.keys()):
            self.lista_graficas.setItem(i, 0, QTableWidgetItem(nombre))

        # Botón para ver la gráfica seleccionada
        self.boton_ver = QPushButton("👁️ Visualizar Gráfica")
        self.boton_ver.setFont(QFont("Arial", 14))
        self.boton_ver.setStyleSheet("background-color: #32CD32; color: white; padding: 10px;")
        self.boton_ver.clicked.connect(self.mostrar_grafica)

        # Agregar widgets al layout
        layout.addWidget(self.label_seleccion)
        layout.addWidget(self.lista_graficas)
        layout.addWidget(self.boton_ver)

        self.setLayout(layout)

    def mostrar_grafica(self):
        fila_seleccionada = self.lista_graficas.currentRow()
        if fila_seleccionada == -1:
            print("Advertencia: No se ha seleccionado ninguna gráfica.")
            QMessageBox.warning(self, "Advertencia", "Seleccione una gráfica antes de continuar.")
            return

        nombre_grafica = self.lista_graficas.item(fila_seleccionada, 0).text()
        print(f"Gráfica seleccionada: {nombre_grafica}")
        funcion_grafica = self.graficas.get(nombre_grafica)

        if funcion_grafica:
            print(f"Mostrando gráfica: {nombre_grafica}")
            dialogo_grafica = VentanaGrafica(nombre_grafica, funcion_grafica)
            dialogo_grafica.exec_()


class VentanaGrafica(QDialog):
    def __init__(self, titulo, funcion_grafica):
        super().__init__()
        self.setWindowTitle(f"📊 {titulo}")
        self.setGeometry(200, 200, 800, 600)
        self.init_ui(funcion_grafica)

    def init_ui(self, funcion_grafica):
        layout = QVBoxLayout()

        # Crear un canvas de matplotlib
        figura = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(figura)
        ax = figura.add_subplot(111)

        # Dibujar la gráfica
        funcion_grafica(ax)

        layout.addWidget(canvas)
        self.setLayout(layout)
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🏥 BioLAB")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #E6E6FA;")
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Mensaje de bienvenida
        label_bienvenida = QLabel("✨ Bienvenidos a BioLAB ✨\n¿En qué podemos ayudarte?")
        label_bienvenida.setFont(QFont("Arial", 18, QFont.Bold))
        label_bienvenida.setAlignment(Qt.AlignCenter)
        label_bienvenida.setStyleSheet("color: #4B0082;")
        layout.addWidget(label_bienvenida)

        # Botones principales con iconos
        boton_buscar = QPushButton("🔍 Buscar Pacientes")
        boton_buscar.setFont(QFont("Arial", 16))
        boton_buscar.setStyleSheet("background-color: #32CD32; color: white; padding: 15px;")
        boton_buscar.clicked.connect(self.abrir_buscar_pacientes)

        boton_estadisticos = QPushButton("📊 Ver Estadísticos")
        boton_estadisticos.setFont(QFont("Arial", 16))
        boton_estadisticos.setStyleSheet("background-color: #1E90FF; color: white; padding: 15px;")
        boton_estadisticos.clicked.connect(self.ver_estadisticos)

        boton_contacto = QPushButton("📞 Contacto")
        boton_contacto.setFont(QFont("Arial", 16))
        boton_contacto.setStyleSheet("background-color: #FF6347; color: white; padding: 15px;")
        boton_contacto.clicked.connect(self.ver_contacto)

        boton_salir = QPushButton("❌ Salir")
        boton_salir.setFont(QFont("Arial", 16))
        boton_salir.setStyleSheet("background-color: #8B0000; color: white; padding: 15px;")
        boton_salir.clicked.connect(self.close)

        # Añadir botones al layout
        layout.addWidget(boton_buscar)
        layout.addWidget(boton_estadisticos)
        layout.addWidget(boton_contacto)
        layout.addWidget(boton_salir)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def abrir_buscar_pacientes(self):
        print("Abriendo ventana de búsqueda de pacientes.")
        buscar_dialog = BuscarPacientes()
        buscar_dialog.exec_()

    def ver_estadisticos(self):
        print("Abriendo ventana de estadísticas.")
        estadisticos_dialog = GraficasEstadisticas()
        estadisticos_dialog.exec_()
        #QMessageBox.information(self, "Estadísticos", "Próximamente disponible.")

    def ver_contacto(self):
        print("Mostrando información de contacto.")
        QMessageBox.information(self, "Contacto", "Para soporte, contáctanos en sistemas.biolab@biocompany.com.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())
