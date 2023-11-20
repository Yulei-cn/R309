from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Ma première fenêtre")

        # Create a QLabel widget to display the message
        self.label = QLabel("")

        # Create a QLineEdit widget for name input
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Entrez votre nom")

        # Create a QPushButton widget to trigger the message
        self.button_ok = QPushButton("OK")
        self.button_ok.clicked.connect(self.display_message)

        # Create a QPushButton widget to quit the application
        self.button_quit = QPushButton("Quitter")
        self.button_quit.clicked.connect(self.close)

        # Create a QVBoxLayout to arrange the widgets vertically
        layout = QVBoxLayout()
        layout.addWidget(self.name_input)
        layout.addWidget(self.button_ok)
        layout.addWidget(self.label)
        layout.addWidget(self.button_quit)

        self.setLayout(layout)

    def display_message(self):
        # Get the name from the QLineEdit widget
        name = self.name_input.text()

        # Display the personalized message
        self.label.setText(f"Bonjour {name}!")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.resize(300, 200)
    window.show()
    app.exec()