#library dependencies
import sys
from PyQt4 import QtGui

#created classes
import mainFrame

def main():
    #creates the base Qt Application
    app = QtGui.QApplication(sys.argv)

    #calls the frame class to create the
    #GUI portions
    frame = mainFrame.MainFrame()

    #executes the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()