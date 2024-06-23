import os

from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout
import sys

from widgets.button import DarButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        root_path = os.path.dirname(os.path.abspath(__file__))
        print(os.path.join(root_path, 'images', 'loading.svg'))
        self.setWindowTitle("Hot Reload Example")
        self.setGeometry(-1000, 500, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel("Initial Text")
        button1 = DarButton("Click me!2233344")
        button2 = DarButton("A", shape='circle')
        button3 = DarButton("Button", icon=os.path.join(root_path, 'images', 'loading2.png'))
        self.layout1 = QHBoxLayout()
        self.layout1.setAlignment(Qt.AlignLeft)
        self.img_label = QLabel()
        self.img_label.setPixmap(QPixmap(os.path.join(root_path, 'images', 'loading2.png')).scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.text_label = QLabel("111")
        self.layout1.addWidget(self.img_label)
        self.layout1.addWidget(self.text_label)


        self.layout.addLayout(self.layout1)

        self.layout.addWidget(button1)
        self.layout.addWidget(button2)
        self.layout.addWidget(button3)
        self.layout.addWidget(self.label)

        # 设置一个标签来显示是否热更新工作
        self.label.setText("Hot Reload is 889991!33")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
