from PySide6.QtCore import QEvent, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QCursor, Qt, QColor
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect


class DarButton(QPushButton):
    def __init__(self, text, parent=None, variant='outlined'):
        super().__init__(text, parent)
        self.setObjectName("dar_btn")
        self.setProperty("dar_btn_default", True)
        self.setProperty("borderColor", Qt.transparent)
        self.adjustSize()
        self.setFixedWidth(self.sizeHint().width() + 5)
        self.setFixedHeight(self.sizeHint().height())
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

        # Add shadow effect
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(15)
        shadow_effect.setOffset(0, 2)
        shadow_effect.setColor(QColor(0, 0, 0, 30))
        self.setGraphicsEffect(shadow_effect)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
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