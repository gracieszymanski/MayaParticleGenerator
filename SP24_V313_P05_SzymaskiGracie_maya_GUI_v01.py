#  SP24_V313_P05_SzymaskiGracie_maya_GUI_v01
# GUI on the Maya Particles Generator Code
# By Gracie Szymanski
# Created 5/3/24

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QSpinBox, QLabel
from PySide2.QtUiTools import QUiLoader
import SP24_V313_P01_SzymanskiGracie_maya_particles_v02 as mp

#global variables
UI_MWPATH = "SP24_V313_P05_SzymaskiGracie_maya_GUI_v01.ui"
loader = QUiLoader()


#Main Window Class
class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        gui = loader.load(UI_MWPATH, None) #loads in ui file with main window design

        #handles file name input widget
        self.file_name = gui.file_name_lineEdit.text() #sets default file name
        gui.file_name_lineEdit.textChanged.connect(self.update_file_name) #signals to update file name

        #handles folder path widget
        self.selected_folder_label = gui.selected_folder_label #defines folder label as a variable to be used later in a function
        self.path = 0 #sets default path variable
        gui.folder_button.clicked.connect(self.update_path) #signals to update path

        #handles file type widget
        self.file_type = "MEL" #sets default file type
        gui.file_type_comboBox.currentTextChanged.connect(self.update_file_type) #signals to update file name

        #handles particle count widget
        self.count = 2000 #sets default count
        gui.count_spinBox.valueChanged.connect(self.update_count) #signals to update count

        #handles center widgets
        #sets default center at 0,0,0
        self.cx = 0 
        self.cy = 0
        self.cz = 0
        #signals to update center
        gui.x_spinBox.valueChanged.connect(self.update_cx)
        gui.y_spinBox.valueChanged.connect(self.update_cy)
        gui.z_spinBox.valueChanged.connect(self.update_cz)

        #handles selected shape widget
        self.layout = gui.shape_option_layout #defines layout as a variable to be used in the later function
        self.shape_selection_comboBox = gui.shape_selection_comboBox #defines combo box as a variable to be used in later function
        gui.shape_selection_comboBox.currentIndexChanged.connect(self.adjust_shape_input_widgets) #signals to update the app widgtes based on chosen shape
        #defines default size variables for the shapes
        self.size = 10
        self.hollow_size = 5
        self.diameter = 10
        self.hollow_diameter = 5
        self.height = 15
        self.thickness = 2
        #creates the widgets that may pop up on the app depending on what shape the user chooses
        #these widgets are hidden until the user makes a choice of what shape they want
        self.size_spinBox = QSpinBox()
        self.size_spinBox.setRange(1,1000)
        self.size_spinBox.setValue(self.size)
        self.size_label = QLabel("Enter Size:")
        self.hollow_size_spinBox = QSpinBox()
        self.hollow_size_spinBox.setRange(1,1000)
        self.hollow_size_spinBox.setValue(self.hollow_size)
        self.hollow_size_label = QLabel("Enter Hollow Size:")
        self.diameter_spinBox = QSpinBox()
        self.diameter_spinBox.setRange(1,1000)
        self.diameter_spinBox.setValue(self.diameter)
        self.diameter_label = QLabel("Enter Diameter:")
        self.hollow_diameter_spinBox = QSpinBox()
        self.hollow_diameter_spinBox.setRange(1,1000)
        self.hollow_diameter_spinBox.setValue(self.diameter)
        self.hollow_diameter_label = QLabel("Enter Hollow Diameter:")
        self.height_spinBox = QSpinBox()
        self.height_spinBox.setRange(1,1000)
        self.height_spinBox.setValue(self.height)
        self.height_label = QLabel("Enter Height:")
        self.thickness_spinBox = QSpinBox()
        self.thickness_spinBox.setRange(1,1000)
        self.thickness_spinBox.setValue(self.thickness)
        self.thickness_label = QLabel("Enter Thickness:")
        #defines the signal for these shape size widgets
        self.size_spinBox.valueChanged.connect(self.update_size) #signals to update the size
        self.hollow_size_spinBox.valueChanged.connect(self.update_hollow_size) #signals to update the hollow size
        self.diameter_spinBox.valueChanged.connect(self.update_diameter) #signals to update the diameter
        self.hollow_diameter_spinBox.valueChanged.connect(self.update_hollow_diameter) #signals to update the hollow diameter
        self.height_spinBox.valueChanged.connect(self.update_height) #signals to update the height
        self.thickness_spinBox.valueChanged.connect(self.update_thickness) #signals to update the thickness

        #handles the go button
        self.go_button = gui.go_button #defines the go button as a variable so it can be used in later function
        gui.go_button.clicked.connect(self.run_maya_particles) #signals to run and write the maya particles file

        self.setCentralWidget(gui)

    def enable_run(self): # function to enable the go button once enough user input is available to run / reduces user error

        if self.path != 0 and self.shape_selection_comboBox.currentIndex() != 0 :
            self.go_button.setEnabled(True)


    def update_file_name(self, text): #updates the file name based on user input

        self.file_name = text


    def update_path(self): #updates the file path based on user input

        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.Directory)
        if file_dialog.exec():
            path = file_dialog.selectedFiles()
            if path:
                self.selected_folder_label.setText(path[0])
                self.path = path[0]
                
            self.enable_run() #runs the enable run function to check to see if the go button should be activated yet


    def update_file_type(self, text): #updates the file type based on user input

        self.file_type = text


    def update_count(self, cleanText): #updates particle count based on user input

        self.count = cleanText


    def update_cx(self, value): #updates x center based on user input

        self.cx = value


    def update_cy(self, value): #updates y center based on user input

        self.cy = value


    def update_cz(self, value): #updates z center based on user input

        self.cz = value


    def delete_past_widgets(self): #deletes any previous widgets in the grid layout so that user can switch between shape options without cluttering the app

        if self.layout.count() > 0:
            for i in reversed(range(self.layout.count())):
                widget = self.layout.itemAt(i).widget()
                self.layout.removeWidget(widget)
                widget.deleteLater()


    def adjust_shape_input_widgets(self): #adjust which widgets are present on the app based on user input of shape

        self.delete_past_widgets() #clear all previous widgets out if any were there
        self.enable_run() #runs the enable run function to check to see if the go button should be activated yet

        #if statements to check which widgets to add based on each shape's needs
        if self.shape_selection_comboBox.currentIndex() == 1 or self.shape_selection_comboBox.currentIndex() == 8:
            self.layout.addWidget(self.size_label, 0, 0)
            self.layout.addWidget(self.size_spinBox, 0, 1)

        if self.shape_selection_comboBox.currentIndex() == 2:
            self.layout.addWidget(self.size_label, 0, 0)
            self.layout.addWidget(self.size_spinBox, 0, 1)
            self.layout.addWidget(self.hollow_size_label, 1, 0)
            self.layout.addWidget(self.hollow_size_spinBox, 1, 1)  

        if self.shape_selection_comboBox.currentIndex() == 3 or self.shape_selection_comboBox.currentIndex() == 6:
            self.layout.addWidget(self.diameter_label, 0, 0)
            self.layout.addWidget(self.diameter_spinBox, 0, 1)

        if self.shape_selection_comboBox.currentIndex() == 4:
            self.layout.addWidget(self.diameter_label, 0, 0)
            self.layout.addWidget(self.diameter_spinBox, 0, 1)
            self.layout.addWidget(self.hollow_diameter_label, 1, 0)
            self.layout.addWidget(self.hollow_diameter_spinBox, 1, 1)

        if self.shape_selection_comboBox.currentIndex() == 5 or self.shape_selection_comboBox.currentIndex() == 7:
            self.layout.addWidget(self.diameter_label, 0, 0)
            self.layout.addWidget(self.diameter_spinBox, 0, 1)
            self.layout.addWidget(self.height_label, 1, 0)
            self.layout.addWidget(self.height_spinBox, 1, 1)

        if self.shape_selection_comboBox.currentIndex() == 9:
            self.layout.addWidget(self.size_label, 0, 0)
            self.layout.addWidget(self.size_spinBox, 0, 1) 
            self.layout.addWidget(self.thickness_label, 1, 0)
            self.layout.addWidget(self.thickness_spinBox, 1, 1)

        if self.shape_selection_comboBox.currentIndex() == 10:        
            self.layout.addWidget(self.size_label, 0, 0)
            self.layout.addWidget(self.size_spinBox, 0, 1) 
            self.layout.addWidget(self.height_label, 1, 0)
            self.layout.addWidget(self.height_spinBox, 1, 1)


    def update_size(self, value): #updates size based on user input

        self.size = value


    def update_hollow_size(self, value): #updates hollow size based on user input

        self.hollow_size = value


    def update_diameter(self, value): #updates diameter based on user input

        self.diameter = value


    def update_hollow_diameter(self,value): #updaes hollow diameter based on user input

        self.hollow_diameter = value


    def update_height(self, value): #updates height based on user input

        self.height = value


    def update_thickness(self, value): #updates thickness based on user input

        self.thickness = value


    def run_maya_particles(self): #calls the maya particles file to run and write a specific file

        #if statements to check what type of shape to write out
        if self.shape_selection_comboBox.currentIndex() == 1:
            mp.write_cube(self.file_name, self.count, self.size, self.file_type, self.path, self.cx, self.cy, self.cz)
        
        if self.shape_selection_comboBox.currentIndex() == 2:
            mp.write_hol_cube(self.file_name, self.count, self.size, self.hollow_size, self.file_type, self.path, self.cx, self.cy, self.cz)
        
        if self.shape_selection_comboBox.currentIndex() == 3:
            mp.write_sphere(self.file_name, self.count, self.diameter, self.file_type, self.path, self.cx, self.cy, self.cz)

        if self.shape_selection_comboBox.currentIndex() == 4:
            mp.write_hol_sphere(self.file_name, self.count, self.hollow_diameter, self.diameter, self.file_type, self.path, self.cx, self.cy, self.cz)

        if self.shape_selection_comboBox.currentIndex() == 5:
            mp.write_cylinder(self.file_name, self.count, self.diameter, self.height, self.file_type, self.path, self.cx, self.cy, self.cz)

        if self.shape_selection_comboBox.currentIndex() == 6:
            mp.write_disk(self.file_name, self.count, self.diameter, self.file_type, self.path, self.cx, self.cy, self.cz)

        if self.shape_selection_comboBox.currentIndex() == 7:
            mp.write_cone(self.file_name, self.count, self.diameter, self.height, self.file_type, self.path, self.cx, self.cy, self.cz)

        if self.shape_selection_comboBox.currentIndex() == 8:
            mp.write_diamond(self.file_name, self.count, self.size, self.file_type, self.path, self.cx, self.cy, self.cz)

        if self.shape_selection_comboBox.currentIndex() == 9:
            mp.write_heart(self.file_name, self.count, self.size, self.thickness, self.file_type, self.path, self.cx, self.cy, self.cz)

        if self.shape_selection_comboBox.currentIndex() == 10:
            mp.write_pyramid(self.file_name, self.count, self.size, self.height, self.file_type, self.path, self.cx, self.cy, self.cz)


if __name__ == "__main__":

    app = QApplication([])
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
