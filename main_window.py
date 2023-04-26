from PySide6.QtWidgets import QMainWindow, QToolBar, QVBoxLayout, QFrame, QLabel, QStackedWidget
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
import random
import api


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("app")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction('Copy')
        edit_menu.addAction('Cut')
        edit_menu.addAction('Paste')
        edit_menu.addAction('Undo')
        edit_menu.addAction('Redo')

        menu_bar.addMenu('Window')
        menu_bar.addMenu('Settings')
        menu_bar.addMenu('Help')

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        #  ------------------------------  stacked_widget "page a"  ------------------------------
        action_a = QAction('one random headline', self)
        action_a.triggered.connect(self.get_a)
        toolbar.addAction(action_a)

        toolbar.addSeparator()

        self.frame_a = QFrame()

        self.layout_a = QVBoxLayout()

        self.random_headline = QLabel(
            'Random headline', alignment=Qt.AlignCenter)

        self.layout_a.addWidget(self.random_headline)

        self.frame_a.setLayout(self.layout_a)

        self.stacked_widget.addWidget(self.frame_a)

        #  ------------------------------  stacked_widget "page b"  ------------------------------
        action2 = QAction('top ten headlines', self)
        action2.triggered.connect(self.get_b)
        toolbar.addAction(action2)

        toolbar.addSeparator()

        self.frame_b = QFrame()

        self.layout_b = QVBoxLayout()

        self.text_b = QLabel('option b!')

        self.headlines = api.get_headlines()

        self.headline0 = QLabel(self.headlines[0], alignment=Qt.AlignCenter)
        self.headline1 = QLabel(self.headlines[1], alignment=Qt.AlignCenter)
        self.headline2 = QLabel(self.headlines[2], alignment=Qt.AlignCenter)
        self.headline3 = QLabel(self.headlines[3], alignment=Qt.AlignCenter)
        self.headline4 = QLabel(self.headlines[4], alignment=Qt.AlignCenter)
        self.headline5 = QLabel(self.headlines[5], alignment=Qt.AlignCenter)
        self.headline6 = QLabel(self.headlines[6], alignment=Qt.AlignCenter)
        self.headline7 = QLabel(self.headlines[7], alignment=Qt.AlignCenter)
        self.headline8 = QLabel(self.headlines[8], alignment=Qt.AlignCenter)
        self.headline9 = QLabel(self.headlines[9], alignment=Qt.AlignCenter)

        self.layout_b.addWidget(self.headline0)
        self.layout_b.addWidget(self.headline1)
        self.layout_b.addWidget(self.headline2)
        self.layout_b.addWidget(self.headline3)
        self.layout_b.addWidget(self.headline4)
        self.layout_b.addWidget(self.headline5)
        self.layout_b.addWidget(self.headline6)
        self.layout_b.addWidget(self.headline7)
        self.layout_b.addWidget(self.headline8)
        self.layout_b.addWidget(self.headline9)

        self.frame_b.setLayout(self.layout_b)

        self.stacked_widget.addWidget(self.frame_b)

    def quit_app(self):
        self.app.quit()

    def get_a(self):
        #  use setCurrentWidget() - ?
        self.stacked_widget.setCurrentIndex(0)

        self.random_headline.setText(random.choice(api.get_headlines()))

    def get_b(self):
        #  use setCurrentWidget() - ?
        self.stacked_widget.setCurrentIndex(1)

        self.headlines = api.get_headlines()

        self.headline0.setText(self.headlines[0])
        self.headline1.setText(self.headlines[1])
        self.headline2.setText(self.headlines[2])
        self.headline3.setText(self.headlines[3])
        self.headline4.setText(self.headlines[4])
        self.headline5.setText(self.headlines[5])
        self.headline6.setText(self.headlines[6])
        self.headline7.setText(self.headlines[7])
        self.headline8.setText(self.headlines[8])
        self.headline9.setText(self.headlines[9])
