import sys
from PyQt4 import QtGui, QtCore

class DropDownMenu(QtGui.QWidget):
    """
    An basic example combo box application
    """

    def __init__(self):
        # create GUI
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Network Tools')
        # Set the window dimensions
        self.resize(250,50)
        
        # vertical layout for widgets
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)

        # Create a combo box and add it to our layout
        self.combo = QtGui.QComboBox()
        self.vbox.addWidget(self.combo)

        self.combo2 = QtGui.QComboBox()
        self.vbox.addWidget(self.combo2)

        # A label to display our selection
        self.lbl = QtGui.QLabel('Links')

        # Center align text
        #self.lbl.setAlignment(QtCore.Qt.AlignHCenter)
        #self.vbox.addWidget(self.lbl)

        # You can add items individually:
        self.combo.addItem('SATCOM')
        self.combo.addItem('Courier')
        self.combo.addItem('Ethernet')
        self.combo.addItem('Plain Text')
        self.combo.addItem('Cypher Text')

        self.combo.view().setDragDropMode(QtGui.QAbstractItemView.DragOnly)

        self.combo2.addItem('Unknown Host')
        self.combo2.addItem('Router')
        self.combo2.addItem('Radio')

        self.combo2.view().setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        
        # Connect the activated signal on the combo box to our handler.
        # This is an overloaded signal, meaning there are variants of it, for
        # example the activated(int) variant emits the index of the chosen
        # option, rather than it's text
        self.connect(self.combo, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)

    def combo_chosen(self, text):
        """
        Handler called when a distro is chosen from the combo box
        """
        self.lbl.setText(text)
