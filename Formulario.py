import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLineEdit,
    QRadioButton, QPushButton, QLabel, QMessageBox
)
from PyQt5.QtCore import Qt


class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario")
        self.setGeometry(300, 200, 420, 280)

        # Layout
        layout = QGridLayout()

        # Entradas
        self.num1 = QLineEdit(self)
        self.num1.setPlaceholderText("Ingrese primer número")
        self.num2 = QLineEdit(self)
        self.num2.setPlaceholderText("Ingrese segundo número")

        layout.addWidget(QLabel("Número 1:"), 0, 0)
        layout.addWidget(self.num1, 0, 1)
        layout.addWidget(QLabel("Número 2:"), 1, 0)
        layout.addWidget(self.num2, 1, 1)

        # RadioButtons
        self.suma = QRadioButton("Suma (+)")
        self.resta = QRadioButton("Resta (-)")
        self.multi = QRadioButton("Multiplicación (×)")
        self.divi = QRadioButton("División (÷)")

        layout.addWidget(QLabel("Operación:"), 2, 0, Qt.AlignTop)
        layout.addWidget(self.suma, 2, 1)
        layout.addWidget(self.resta, 3, 1)
        layout.addWidget(self.multi, 4, 1)
        layout.addWidget(self.divi, 5, 1)

        # Botones
        self.btn_ejecutar = QPushButton("Ejecutar")
        self.btn_ejecutar.clicked.connect(self.operar)
        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.close)

        layout.addWidget(self.btn_ejecutar, 6, 0)
        layout.addWidget(self.btn_salir, 6, 1)

        # Resultado
        self.resultado = QLabel("Resultado: ---")
        self.resultado.setStyleSheet("font-weight: bold; color: blue;")
        layout.addWidget(self.resultado, 7, 0, 1, 2)

        self.setLayout(layout)

    def operar(self):
        try:
            n1 = float(self.num1.text())
            n2 = float(self.num2.text())

            if self.suma.isChecked():
                res = n1 + n2
            elif self.resta.isChecked():
                res = n1 - n2
            elif self.multi.isChecked():
                res = n1 * n2
            elif self.divi.isChecked():
                if n2 != 0:
                    res = n1 / n2
                else:
                    QMessageBox.warning(self, "Error", "No se puede dividir entre cero")
                    return
            else:
                QMessageBox.warning(self, "Error", "Seleccione una operación")
                return

            self.resultado.setText(f"Resultado: {res}")
            self.num1.clear()
            self.num2.clear()

        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec_())
