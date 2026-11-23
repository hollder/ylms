import sqlite3

import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.updatetable)
        self.db = sqlite3.connect('coffee.sqlite')
        self.db.execute("""CREATE TABLE IF NOT EXISTS coffee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sort TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER NOT NULL,
            volume INTEGER NOT NULL)""")

    def updatetable(self):
        cursor = self.db.cursor()
        res = cursor.fetchall()

        if cursor.description:
            column_names = [desc[0] for desc in cursor.description]
            self.tableWidget.setColumnCount(len(column_names))
            self.tableWidget.setHorizontalHeaderLabels(column_names)

        self.tableWidget.setRowCount(len(res))
        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
