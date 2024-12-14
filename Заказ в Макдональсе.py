import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit, QPushButton


class Something(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tr1 = QCheckBox('Чизбургер', self)
        self.tr1.move(50, 60)

        self.tr2 = QCheckBox('Гамбургер', self)
        self.tr2.move(50, 100)

        self.tr3 = QCheckBox('Кока-Кола', self)
        self.tr3.move(50, 140)

        self.tr4 = QCheckBox('Нагетсы', self)
        self.tr4.move(50, 180)

        self.positions = [self.tr1, self.tr2, self.tr3, self.tr4]

        self.res = QPlainTextEdit(self)
        self.res.setEnabled(False)
        self.res.move(50, 270)
        self.res.resize(400, 250)

        self.btn = QPushButton('Заказать', self)
        self.btn.resize(70, 30)
        self.btn.move(50, 230)
        self.btn.clicked.connect(self.order)

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Заказ в Макдональдсе')

    def order(self):
        self.res.clear()
        self.res.appendPlainText('Ваш заказ:')
        self.res.appendPlainText('')
        for i in self.positions:
            if i.isChecked():
                self.res.appendPlainText(i.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Something()
    ex.show()
    sys.exit(app.exec())