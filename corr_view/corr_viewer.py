import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
)
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtGui import QPainter

class LocationMap(QGraphicsView):
    def __init__(self, data, on_point_clicked_callback):
        super().__init__()
        self.data = data
        self.on_point_clicked_callback = on_point_clicked_callback
        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.Antialiasing)
        self.draw_points()

    def draw_points(self):
        radius = 4
        for i, row in self.data.iterrows():
            x, y = row["x"], row["y"]
            item = QGraphicsEllipseItem(QRectF(x - radius, -y - radius, 2 * radius, 2 * radius))
            item.setBrush(QBrush(Qt.red))
            item.setPen(QPen(Qt.black))
            item.setData(0, (x, y))  # сохраняем координаты в item
            item.setFlag(QGraphicsEllipseItem.ItemIsSelectable)
            self.scene().addItem(item)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        pos = self.mapToScene(event.pos())
        items = self.scene().items(pos)

        for item in items:
            data = item.data(0)
            if data:
                self.on_point_clicked_callback(data)
                break


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Location Viewer")

        # Загружаем данные
        self.data = pd.read_csv("input.csv", sep="\t")
        self.data.rename(columns={"XCoord": "x", "YCoord": "y"}, inplace=True)

        # Основной layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Левая часть — карта
        self.map_view = LocationMap(self.data, self.update_coordinates)
        main_layout.addWidget(self.map_view)

        # Правая часть — информация
        self.info_panel = QWidget()
        info_layout = QVBoxLayout()
        self.info_panel.setLayout(info_layout)
        self.coord_label = QLabel("Координаты: (не выбрано)")
        info_layout.addWidget(self.coord_label)
        info_layout.addStretch()
        main_layout.addWidget(self.info_panel)

    def update_coordinates(self, point):
        x, y = point
        self.coord_label.setText(f"Координаты: X={x:.2f}, Y={y:.2f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
