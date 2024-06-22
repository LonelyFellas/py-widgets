from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
import sys

from widgets.button import CustomButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hot Reload Example")
        self.setGeometry(-1000, 500, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel("Initial Text")
        button = CustomButton("Click me!")
        self.layout.addWidget(button)
        self.layout.addWidget(self.label)

        # 设置一个标签来显示是否热更新工作
        self.label.setText("Hot Reload is 889991!33")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
