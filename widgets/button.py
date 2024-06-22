from PySide6.QtCore import QEvent
from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import QPushButton


class DarButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("border: 1px solid transparent;")
        self.setObjectName("dar_btn")
        self.setProperty("dar_btn_default", True)
        self.setProperty("borderColor", Qt.transparent)
        self.adjustSize()
        self.setFixedWidth(self.sizeHint().width() + 25)
        self.setFixedHeight(self.sizeHint().height() + 10)
        self.setStyleSheet("border: 1px solid rgba(0,0,0,0.2)")
        self.setStyleSheet("""
            QPushButton[dar_btn_default="true"] {
                outline: none;
                border: 1px solid rgba(0,0,0,0.2);
                background: #ffffff;
                border-radius: 6px;
            }
            QPushButton[dar_btn_default="true"]:hover {
                border: 1px solid rgb(22, 119, 255);
                color: rgb(22, 119, 255);
            }
            QPushButton[dar_btn_default="true"]:pressed {
                border: 1px solid rgb(0, 59, 255);
                color: rgb(0, 59, 255);
            }
            QPushButton[dar_btn_active="true"] {
                outline: none;
                border: 1px solid rgb(0, 59, 255);
                background: #ffffff;
                color: rgb(0, 59, 255);    
                border-radius: 6px;
            }
        """)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            self.hover_in_animation()
        elif event.type() == QEvent.Leave:
            self.hover_out_animation()
        elif event.type() == QEvent.MouseButtonPress:
            self.setProperty("dar_btn_active", True)
            self.setProperty("dar_btn_default", False)
            self.style().unpolish(self)
            self.style().polish(self)
        elif event.type() == QEvent.MouseButtonRelease:
            self.setProperty("dar_btn_active", False)
            self.setProperty("dar_btn_default", True)
            self.style().unpolish(self)
            self.style().polish(self)
        return super().eventFilter(obj, event)

    def hover_in_animation(self):
        pass

    def hover_out_animation(self):
        pass

    #
    # def eventFilter(self, obj, event):
    #     if event.type() == QEvent.Enter:
    #         self.hover_in_animation()
    #     elif event.type() == QEvent.Leave:
    #         self.hover_out_animation()
    #     return False
    #
    # def hover_in_animation(self):
    #     animation = QPropertyAnimation(self, b"borderColor")
    #     animation.setDuration(200)
    #     # animation.setStartValue(BORDER_COLOR_OUT)
    #     # animation.setEndValue(BORDER_COLOR_IN)
    #     animation.setEasingCurve(QEasingCurve.InOutQuad)
    #     animation.start()
    #     self.setStyleSheet("border: 1px solid rgb(22, 119, 255);")
    #
    # def hover_out_animation(self):
    #     animation = QPropertyAnimation(self, b"borderColor")
    #     animation.setDuration(200)
    #     # animation.setStartValue(BORDER_COLOR_IN)
    #     # animation.setEndValue(BORDER_COLOR_OUT)
    #     animation.setEasingCurve(QEasingCurve.InOutQuad)
    #     animation.start()
    #     self.setStyleSheet("border: 1px solid rgba(0, 0, 0, 0.2);")
