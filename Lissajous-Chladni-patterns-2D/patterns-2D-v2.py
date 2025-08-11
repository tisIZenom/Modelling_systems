from collections import deque
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import QTime, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sounddevice as sd 

from PyQt5.QtCore import QTimer
import numpy as np

class VisualizationPanel(QWidget):
    def __init__(self, title):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel(title)
        layout.addWidget(label)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        
        # inserting the timer 
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_lissajous)
        self.timer.start(20)

        
        # the audio stuff goes here 
        # audio buffer goes here 
        self.audio_buffer = deque(maxlen=1024)
        
        # starting the audio input
        sd.InputStream(callback=self.audio_buffer,channels=1,samplerate=44099).start()


        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def update_plot(self, data=None):
        self.ax.clear()
        t = np.linspace(0, 2 * np.pi, 1000)
        if data == "lissajous":
            x = np.sin(3 * t)
            y = np.sin(4 * t)
            self.ax.plot(x, y)
        elif data == "chladni":
            self.ax.imshow(np.random.rand(50, 50), cmap='inferno')
        elif data == "light":
            self.ax.plot(np.sin(t) * np.cos(3 * t))
        self.canvas.draw()

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

        # Update loop
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_all_panels)
        self.timer.start(1)  # Update every 1 second

    def update_all_panels(self):
        self.lissajous_panel.update_plot(data="lissajous")
        self.chladni_panel.update_plot(data="chladni")
        self.light_panel.update_plot(data="light")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
