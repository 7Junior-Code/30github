""" Stopwatch app"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

""" Class Stopwatch"""
class Stopwatch(QWidget):
    """ Class starts from this function"""
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("START", self)
        self.stop_button = QPushButton("STOP", self)
        self.reset_button = QPushButton("RESET", self)
        self.timer = QTimer(self)
        """ We call the function initUI and
         we are prepared for the stopwatch at the end of the function"""
        self.initUI()

    def initUI(self):
        """ We set the window title and the position first of all"""
        self.setWindowTitle("🌏🌱 Earth Hour πStopwatch ⏱️🎄")
        self.setGeometry(300, 175, 600, 200)

        """ We create a vertical box layout for the time_label and add it to our window"""
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        """ We command to keep the time_label at center at all times"""
        self.time_label.setAlignment(Qt.AlignCenter)

        """ Now we create a horizontal box layout for the buttons (start, stop, reset) and
         locate the buttons horizontally"""
        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        """ We customize the label and the buttons to our likes"""
        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
            }
            QPushButton{
                font-size: 50px;
                background-color: #3895ff;
                color: #eb8f8f;
                font-family: Chalkduster;
            }
            QLabel{
                font-size: 120px;
                background-color: #76cf76;
                color: #e6eb8f;
                border-radius: 70px;
                font-family: Annai MN;
            }
        """)

        """ For buttons we put commands to recognize each of these actions done and
         enter the functions for them"""
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    """ Functions to start, stop and reset"""
    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    """ Function to format the time stopwatch text"""
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        """ For Milliseconds we put // 10 to remove the annoying 0 at the end doing nothing."""
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    """ Function to update the display of the stopwatch."""
    def update_display(self):
        """ Each 10 milliseconds the display updates"""
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

""" The entire code starts from here:"""
if __name__ == '__main__':
    """ We create a window here"""
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
