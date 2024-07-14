import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from project import convert_data  # Ensure project.py is in the same directory or adjust the import path


class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.input_label = QLabel('Select Input File', self)
        layout.addWidget(self.input_label)

        self.input_btn = QPushButton('Browse', self)
        self.input_btn.clicked.connect(self.select_input_file)
        layout.addWidget(self.input_btn)

        self.output_label = QLabel('Select Output File', self)
        layout.addWidget(self.output_label)

        self.output_btn = QPushButton('Browse', self)
        self.output_btn.clicked.connect(self.select_output_file)
        layout.addWidget(self.output_btn)

        self.convert_btn = QPushButton('Convert', self)
        self.convert_btn.clicked.connect(self.convert_files)
        layout.addWidget(self.convert_btn)

        self.setLayout(layout)

        self.setWindowTitle('Data Converter')
        self.show()

    def select_input_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select Input File", "",
                                              "All Files (*);;JSON Files (*.json);;XML Files (*.xml);;YAML Files (*.yml *.yaml)",
                                              options=options)
        if file:
            self.input_label.setText(file)
            self.input_file = file

    def select_output_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getSaveFileName(self, "Select Output File", "",
                                              "All Files (*);;JSON Files (*.json);;XML Files (*.xml);;YAML Files (*.yml *.yaml)",
                                              options=options)
        if file:
            self.output_label.setText(file)
            self.output_file = file

    def convert_files(self):
        convert_data(self.input_file, self.output_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConverterApp()
    sys.exit(app.exec_())
