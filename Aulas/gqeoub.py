import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout


class CharacterSheet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ficha de Personagem - D&D")
        self.initUI()

    def initUI(self):
        layout = QFormLayout()

        self.name_entry = QLineEdit()
        layout.addRow("Nome:", self.name_entry)

        self.class_entry = QLineEdit()
        layout.addRow("Classe:", self.class_entry)

        self.level_entry = QLineEdit()
        layout.addRow("Nível:", self.level_entry)

        self.str_entry = QLineEdit()
        layout.addRow("Força:", self.str_entry)

        self.save_button = QPushButton("Salvar")
        self.save_button.clicked.connect(self.salvar)
        layout.addRow(self.save_button)

        self.setLayout(layout)

    def salvar(self):
        nome = self.name_entry.text()
        classe = self.class_entry.text()
        nivel = self.level_entry.text()
        forca = self.str_entry.text()
        print(f"Nome: {nome}\nClasse: {classe}\nNível: {nivel}\nForça: {forca}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CharacterSheet()
    window.show()
    sys.exit(app.exec_())
