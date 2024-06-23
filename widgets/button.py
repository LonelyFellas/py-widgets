from typing import Optional, Literal
from PySide6.QtCore import QEvent, QPropertyAnimation, QEasingCurve, Property, QObject
from PySide6.QtGui import QCursor, Qt, QColor, QPainter, QPainterPath
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect


class DarButton(QPushButton):
    def __init__(self, text, parent=None, variant='outlined',
                 shape: Optional[Literal['default', 'circle', 'round']] = 'default'):
        super().__init__(text, parent)
        self.ripple_effects = []
        self.setObjectName("dar_btn")
        self.setProperty("dar_btn_default", True)
        self.setProperty("borderColor", Qt.transparent)
        self.computed_self_size(shape)
        self.setStyleSheet("border: 1px solid rgba(0,0,0,0.2)")

        self.border_radius = self.computed_border_radius(shape)
        self.setStyleSheet(f"""
            QPushButton[dar_btn_default="true"] {{
                outline: none;
                border: 1px solid rgba(0,0,0,0.2);
                background: #ffffff;
                border-radius: {self.border_radius}px;
            }}
            QPushButton[dar_btn_default="true"]:hover {{
                border: 1px solid rgb(22, 119, 255);
                color: rgb(22, 119, 255);
            }}
            QPushButton[dar_btn_default="true"]:pressed {{
                border: 1px solid rgb(0, 59, 255);
                color: rgb(0, 59, 255);
            }}
            QPushButton[dar_btn_active="true"] {{
                outline: none;
                border: 1px solid rgb(0, 59, 255);
                background: #ffffff;
                color: rgb(0, 59, 255);    
                border-radius: {self.border_radius}px;
            }}
        """)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.installEventFilter(self)

        self.switch_shadow_effect()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            self.hover_in()
        elif event.type() == QEvent.Leave:
            self.hover_out()
        elif event.type() == QEvent.MouseButtonPress:
            self.setProperty("dar_btn_active", True)
            self.setProperty("dar_btn_default", False)
            self.style().unpolish(self)
            self.style().polish(self)
            self.create_ripple(event.position())
        elif event.type() == QEvent.MouseButtonRelease:
            self.setProperty("dar_btn_active", False)
            self.setProperty("dar_btn_default", True)
            self.style().unpolish(self)
            self.style().polish(self)
        return super().eventFilter(obj, event)

    def hover_in(self):
        self.switch_shadow_effect(hover_type='event_in')

    def hover_out(self):
        self.switch_shadow_effect(hover_type='event_out')

    def switch_shadow_effect(self, hover_type: Optional[Literal['event_in', 'event_out']] = 'event_in'):
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(15)
        shadow_effect.setOffset(0, 4 if hover_type == 'event_in' else 2)
        shadow_effect.setColor(QColor(0, 0, 0, 60 if hover_type == 'event_in' else 30))
        self.setGraphicsEffect(shadow_effect)

    def computed_border_radius(self, shape: Literal['default', 'circle', 'round']) -> int:
        if shape == 'default':
            radius_size = 6
        elif shape == 'circle':
            radius_size = self.width() // 2

        else:
            radius_size = self.width() // 4

        return radius_size

    def computed_self_size(self, shape: Literal['default', 'circle', 'round']):
        size_hint = self.sizeHint()
        if shape == 'default' or shape == 'round':
            self.adjustSize()
            self.setFixedSize(size_hint.width() + 5, size_hint.height())
        else:
            self.adjustSize()
            self.setFixedSize(size_hint.width() + 5, size_hint.width() + 5)



    def create_ripple(self, pos):
        ripple = Ripple(self, pos)
        self.ripple_effects.append(ripple)
        ripple.animation.finished.connect(lambda: self.ripple_effects.remove(ripple))
        ripple.start_animation()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)
        painter.setClipPath(path)
        for ripple in self.ripple_effects:
            ripple.paint(painter)

class Ripple(QObject):
    def __init__(self, button, center):
        super().__init__()
        self.button = button
        self.center = center
        self._radius = 0
        self.opacity = 1.0
        self.animation = QPropertyAnimation(self, b"radius")
        self.animation.setDuration(600)
        self.animation.setStartValue(0)
        self.animation.setEndValue(max(button.width(), button.height()))
        self.animation.setEasingCurve(QEasingCurve.OutQuad)
        self.animation.valueChanged.connect(self.update_opacity)

    @Property(float)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.button.update()

    def start_animation(self):
        self.animation.start()

    def update_opacity(self):
        self.opacity = 1.0 - self.radius / max(self.button.width(), self.button.height())
        self.button.update()

    def paint(self, painter):
        if self.opacity > 0:
            brush = QColor(22, 119, 255, int(self.opacity * 255))
            painter.setBrush(brush)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(self.center, self.radius, self.radius)
