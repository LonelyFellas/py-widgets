from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import QPushButton


class CustomButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text+'113399999', parent)
        self.setObjectName("dar_btn_default")
        self.adjustSize()
        self.setFixedWidth(self.sizeHint().width() + 5)
        self.setFixedHeight(self.sizeHint().height())
        self.setStyleSheet("""
            QPushButton#dar_btn_default {
                outline: none;
                border: 1px solid rgba(0,0,0,0.2);
                background: #ffffff;
                border-radius: 6px;
            }
            QPushButton#dar_btn_default:hover {
                border: 1px solid #1677ff;
            }
        """)
        self.setCursor(QCursor(Qt.PointingHandCursor))

