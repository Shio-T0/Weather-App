import sys

from PyQt5.QtWidgets import QApplication, \
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon

from city_manager import City

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city = City()

        self.welcoming_label = QLabel(self)
        self.input_city_name = QLineEdit(self)
        self.enter_city_button = QPushButton('Enter', self)

        self.city_name_label = QLabel('Preset:', self)
        self.emoji_label = QLabel('💠', self)
        self.temperature_label = QLabel('00°C', self)
        self.description_label = QLabel('description', self)
        self.humidity_label = QLabel('humidity', self)
        self.pressure_label = QLabel('pressure', self)

        self.vbox = QVBoxLayout()
        self.input_hbox = QHBoxLayout()
        self.important_details_hbox = QHBoxLayout()
        self.minor_details_hbox = QHBoxLayout()

        self.timer = QTimer()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather API")
        self.setWindowIcon(QIcon("weather_icon.png"))
        self.setGeometry(300, 300, 250, 150)

        self.welcoming_label.setText("Welcome to Weather API")

        self.welcoming_label.setObjectName('welcoming_label')

        self.input_city_name.setPlaceholderText("Enter City Name")


        self.vbox.addWidget(self.welcoming_label)


        self.input_hbox.addWidget(self.input_city_name)
        self.input_hbox.addWidget(self.enter_city_button)
        self.vbox.addLayout(self.input_hbox)

        self.vbox.addWidget(self.city_name_label)
        self.vbox.addWidget(self.emoji_label)

        self.important_details_hbox.addWidget(self.description_label)
        self.important_details_hbox.addWidget(self.temperature_label)
        self.vbox.addLayout(self.important_details_hbox)

        self.minor_details_hbox.addWidget(self.humidity_label)
        self.minor_details_hbox.addWidget(self.pressure_label)
        self.vbox.addLayout(self.minor_details_hbox)

        self.setLayout(self.vbox)


        self.enter_city_button.clicked.connect(self.enterCity)


        self.city_name_label.setObjectName("city_name")
        self.city_name_label.setAlignment(Qt.AlignCenter)

        self.emoji_label.setObjectName('emoji')
        self.emoji_label.setAlignment(Qt.AlignCenter)

        self.description_label.setObjectName("description")
        self.description_label.setAlignment(Qt.AlignCenter)

        self.temperature_label.setObjectName('temperature')
        self.temperature_label.setAlignment(Qt.AlignCenter)


        self.humidity_label.setObjectName("humidity")
        self.humidity_label.setAlignment(Qt.AlignCenter)

        self.pressure_label.setObjectName("pressure")
        self.pressure_label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet('''
            QWidget {
                background-color: rgb(255, 255, 255);
            }
            
            QLabel#welcoming_label {
                font-size: 40px;
                font-weight: bold;
            }
            QLineEdit {
                font-size: 20px;
            }
            
            QPushButton {
                font-size: 20px;
                background-color: rgb(230, 230, 230);
                border: 1px solid black;
                padding: 2px 10px;
            }
            QPushButton:hover {
                background-color: rgb(240, 240, 240);
            }
            QPushButton:pressed {
                background-color: rgb(250, 250, 250);
                border: 1px solid rgb(10, 10, 10);
            }
            
            QLabel {
                font-family: Arial;
            }
            QLabel#city_name {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#emoji {
                font-size: 100px;
            }
            QLabel#temperature {
                font-size: 30px;
                font-weight: bold;
                font-family: Times New Roman;
                margin: 0px 100px 10px 0px;
            }
            QLabel#description {
                font-size: 25px;
                font-style: italic;
                font-weight: bold;
                font-family: Times New Roman;
                margin: 0px 0px 10px 100px;
            }
            QLabel#humidity {
                background-color: rgb(230, 230, 230);
                font-size: 15px;
                margin: 20px 0px 0px 0px;
                padding: 5px;
            }
            QLabel#pressure {
                background-color: rgb(230, 230, 230);
                font-size: 15px;
                margin: 20px 0px 0px 0px;
                padding: 5px;
            }
        ''')



    def updateCityDetails(self):
        self.city_name_label.setText(self.city.name)
        self.emoji_label.setText(self.city.weather_emoji)
        self.description_label.setText(self.city.weather_description)
        self.temperature_label.setText(self.city.temperature)

        self.humidity_label.setText(self.city.humidity)
        self.pressure_label.setText(self.city.pressure)

    def defaultInputBox(self):
        self.input_city_name.setPlaceholderText("Enter City Name")
        self.input_city_name.setStyleSheet('color: black;')
        self.timer.stop()

    def changeInputBox(self):
        self.input_city_name.clear()
        self.input_city_name.setPlaceholderText(self.city.errorOccurred())
        self.input_city_name.setStyleSheet('color: red;')

        self.timer.timeout.connect(self.defaultInputBox)
        self.timer.start(1000)


    def enterCity(self):
        name = self.input_city_name.text()
        self.city = City(name)


        if self.city.errorOccurred() == '':
            self.updateCityDetails()
            self.input_city_name.clear()

        else:
            self.changeInputBox()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())