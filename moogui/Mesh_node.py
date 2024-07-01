from re import S
from PySide6 import QtWidgets

from node_editor.node import Node
from Example_Project.common_widgets import FloatLineEdit, StringLineEdit

class FileMeshGenerator_node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Mesh"
        self.type_text = "FileMeshGenerator"
        self.set_color(title_color=(0, 128, 0))

        self.add_pin(name="FileName", is_output=False)      
        self.add_pin(name="output", is_output=True)
        self.build()

    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        self.widget.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.dialog = QtWidgets.QFileDialog()
       # self.dialog.setFileMode(None)
        self.dialog.setWindowTitle('Open folder...')

        layout.addWidget(self.dialog)
        self.widget.setLayout(layout)


        #self.scaler_line = StringLineEdit()
        #layout.addWidget(self.scaler_line)
        #self.widget.setLayout(layout)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()       

class TransformGenerator_node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Mesh"
        self.type_text = "TransformGenerator"
        self.set_color(title_color=(0, 128, 0))
        self.add_pin(name="input", is_output=False)
        self.add_pin(name="output", is_output=True)
        self.build()

    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        self.widget.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
    

        label = QtWidgets.QLabel("transform:")
        layout.addWidget(label)
        self.transform = QtWidgets.QComboBox()
        self.transform.addItem('TRANSLATE')
        self.transform.addItem('TRANSLATE_CENTER_ORIGIN')
        self.transform.addItem('TRANSLATE_MIN_ORIGIN')
        self.transform.addItem('ROTATE')
        self.transform.addItem('SCALE')
        layout.addWidget(self.transform)

        label = QtWidgets.QLabel("vector_value:")
        layout.addWidget(label)

        self.vector_value = StringLineEdit()
        layout.addWidget(self.vector_value)
 
        self.widget.setLayout(layout)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()      

class SideSetsBetweenSubdomainsGenerator_node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Mesh"
        self.type_text = "SideSetsBetweenSubdomainsGenerator"
        self.set_color(title_color=(0, 128, 0))
        self.add_pin(name="input", is_output=False)
        self.add_pin(name="output", is_output=True)
        self.build()

    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        self.widget.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
    
        label = QtWidgets.QLabel("new_boundary:")
        layout.addWidget(label)
        self.new_boundary = StringLineEdit()
        layout.addWidget(self.new_boundary)

        label = QtWidgets.QLabel("pared_block")
        layout.addWidget(label)
        self.paired_block = StringLineEdit()
        layout.addWidget(self.paired_block)

        self.widget.setLayout(layout)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget() 