from PySide6.QtWidgets import QMainWindow, QToolBar, QVBoxLayout, QFrame, QPushButton, QStackedWidget, QLabel, QMessageBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from api import APIRequest
import random


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle('app')

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

        self.api_r = APIRequest()

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
        self.frame_b = None
        toolbar.addSeparator()

    def quit_app(self):
        self.app.quit()

    def get_a(self):
        self.random_headline.setText(random.choice(self.api_r.get_headlines()))

        self.stacked_widget.setCurrentIndex(0)

    def get_b(self):
        if self.frame_b:
            self.stacked_widget.removeWidget(self.frame_b)
        self.frame_b = QFrame()
        self.layout_b = QVBoxLayout()
        self.text_b = QLabel('option b!')
        self.headlines = self.api_r.get_headlines()
        for index, headline in enumerate(self.headlines):
            headline_btn = QPushButton(headline)
            headline_btn.setObjectName(str(index))
            headline_btn.clicked.connect(self.show_description)
            self.layout_b.addWidget(headline_btn)
        self.frame_b.setLayout(self.layout_b)
        self.stacked_widget.addWidget(self.frame_b)

        self.stacked_widget.setCurrentIndex(1)

    def show_description(self):
        the_btn = self.sender()
        message_box = QMessageBox()
        message_box.setMinimumSize(700, 200)
        message_box.setWindowTitle('Description')
        message_box.setInformativeText(
            self.api_r.get_description(int(the_btn.objectName())))
        message_box.setDefaultButton(QMessageBox.Ok)
        message_box.exec()
