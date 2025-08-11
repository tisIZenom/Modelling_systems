import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class VisualizationPanel(QWidget):
    def __init__(self, title):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel(title)
        layout.addWidget(label)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiphysics Audio Visualization")
        self.setGeometry(100, 100, 1400, 500)

        main_layout = QHBoxLayout()

        self.lissajous_panel = VisualizationPanel("Lissajous Figure")
        self.chladni_panel = VisualizationPanel("Chladni Pattern")
        self.light_panel = VisualizationPanel("Light Reflection")

        main_layout.addWidget(self.lissajous_panel)
        main_layout.addWidget(self.chladni_panel)
        main_layout.addWidget(self.light_panel)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
