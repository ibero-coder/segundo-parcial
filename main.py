from PyQt5 import QtWidgets, uic
import sys
import load_menu_principal
from clases.integral.load_ventana_integracion import VentanaIntegracion
from clases.RL.load_ventana_regresion import VentanaRegresion
from PyQt5.QtWidgets import QApplication, QDialog


def main():
    app=QtWidgets.QApplication(sys.argv)
    ventana=load_menu_principal.MenuPrincipal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()