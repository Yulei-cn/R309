import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QLabel, QLineEdit


SERVER_HOST = "localhost"
SERVER_PORT = 10000  


class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.running = False
        self.thread = None
        self.client_socket = None
        self.initUI()

    def initUI(self):
        # Set up the grid layout
        grid_layout = QGridLayout()

        # Create label and line edit for the counter
        self.label = QLabel('Compteur :')
        self.line_edit = QLineEdit(self)
        self.line_edit.setText(str(self.counter))
        
        # Create buttons
        self.button_start = QPushButton('Start', self)
        self.button_reset = QPushButton('Reset', self)
        self.button_stop = QPushButton('stop', self)
        self.button_connect = QPushButton('Connect', self)
        self.button_quit = QPushButton('Quitter', self)

        # Connect buttons to their functions
        self.button_start.clicked.connect(self.startCount)
        self.button_reset.clicked.connect(self.resetCount)
        self.button_stop.clicked.connect(self.stopCount)
        
        self.button_quit.clicked.connect(self.quitApp)
        self.button_connect.clicked.connect(self.connectAction)


        # Add widgets to the layout
        grid_layout.addWidget(self.label, 0, 0, 1, 2)
        grid_layout.addWidget(self.line_edit, 1, 0, 1, 2)
        grid_layout.addWidget(self.button_start, 2, 0, 1, 2)
        grid_layout.addWidget(self.button_reset, 3, 0)
        grid_layout.addWidget(self.button_stop, 3, 1)
        grid_layout.addWidget(self.button_connect, 4, 0)
        grid_layout.addWidget(self.button_quit, 4, 1)

        self.setLayout(grid_layout)
        self.setWindowTitle('Chronomètre')
        self.show()


    def __startCount(self):
        self.running = True
        while self.running:
            self.counter += 1
            self.line_edit.setText(str(self.counter))
            self.sendMessage(str(self.counter))  # send counter value
            threading.Event().wait(1)


    def startCount(self):
        if not self.thread or not self.thread.is_alive():
            self.thread = threading.Thread(target=self.__startCount)
            self.thread.start()
        self.sendMessage("START")

    def resetCount(self):
        self.counter = 0
        self.line_edit.setText(str(self.counter))
        self.sendMessage("RESET")

    def stopCount(self):
        self.running = False
        if self.thread:
            self.thread.join()
        self.sendMessage("STOP")

    def connectAction(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(('localhost', 10000))
            self.sendMessage("CONNECTED")
        except Exception as e:
            print("Connection Error: ", e)

    def quitApp(self):
        self.stopCount()
        self.sendMessage("BYE")
        QApplication.exit(0)

    def sendMessage(self, message):
        if self.client_socket:
            try:
                self.client_socket.send(message.encode())
            except Exception as e:
                print("Error sending message: ", e)

def main():
    app = QApplication(sys.argv)
    ex = CounterApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
