# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 400, 100)
helloMsg = QLabel("<h1>Hello, World!<h1>", parent=window)
helloMsg.move(60, 15)
window.show()
sys.exit(app.exec())