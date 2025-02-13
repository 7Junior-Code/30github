# PyQt5 key
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🪄🎉My Journey Starter!🧑🏻‍💻🏆")
        self.setGeometry(950, 350, 550, 700)

        label = QLabel(self)
        label.setGeometry(0, 0, 550, 700)

        pixmap = QPixmap("Aktan's_Starter.jpeg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()