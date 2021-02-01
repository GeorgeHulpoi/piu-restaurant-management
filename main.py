import sys

from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

# MAIN APP
app = QApplication(sys.argv)

# MAIN WINDOW
window = MainWindow(title="Management Restaurant")

# RUN APP
if __name__ == "__main__":
    sys.exit(app.exec_())
