#library dependencies
from PyQt4 import QtGui
import mainFrame
import sys

def main():
    """The main function will instantiate the main QT Application
    that runs the whole application. The main function calls on the
    mainFrame class that we created which is run by the application.
    This function allows clean exiting of the overall application"""

    #creates the base Qt Application
    app = QtGui.QApplication(sys.argv)

    #calls the frame class to create the
    #GUI portions
    frame = mainFrame.MainFrame()

    #executes the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()