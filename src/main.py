#library dependencies
import sys
from PyQt4 import QtGui
import mainFrame

def main():
    """ Run the main Application within a MainFrame"""

    #creates the base Qt Application
    app = QtGui.QApplication(sys.argv)

    #calls the frame class to create the
    #GUI portions
    frame = mainFrame.MainFrame()

    #executes the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()