import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
from core.swmm.hydrology.aquifer import Aquifer
from core.swmm.hydraulics.node import DirectInflow, DryWeatherInflow, RDIInflow, Treatment
from ui.frmGenericPropertyEditor import frmGenericPropertyEditor
from ui.property_editor_backend import PropertyEditorBackend


class frmAquifers(frmGenericPropertyEditor):

    SECTION_NAME = "[AQUIFERS]"
    SECTION_TYPE = Aquifer

    def __init__(self, main_form, edit_these=[]):
        self.help_topic = "swmm/src/src/aquifereditordialog.htm"
        self._main_form = main_form
        self.new_item = None
        self.project = main_form.project
        self.project_section = self.project.aquifers
        if self.project_section and isinstance(self.project_section.value, list) and \
            len(self.project_section.value) > 0 and \
            isinstance(self.project_section.value[0], self.SECTION_TYPE):

            if edit_these:  # Edit only specified item(s) in section
                if isinstance(edit_these[0], basestring):  # Translate list from names to objects
                    edit_names = edit_these
                    edit_objects = [item for item in self.project_section.value if item.name in edit_these]
                    edit_these = edit_objects

            else:  # Edit all items in section
                edit_these = []
                edit_these.extend(self.project_section.value)

        if len(edit_these) == 0:
            self.new_item = self.SECTION_TYPE()
            # self.new_item.name = "1"
            edit_these.append(self.new_item)
        else:
            self.new_item = False

        frmGenericPropertyEditor.__init__(self, self._main_form, edit_these,
                                          "SWMM " + self.SECTION_TYPE.__name__ + " Editor")

        for column in range(0, self.tblGeneric.columnCount()):
            # for patterns, show available patterns
            pattern_section = self.project.find_section("PATTERNS")
            pattern_list = pattern_section.value[0:]
            combobox = QtGui.QComboBox()
            combobox.addItem('')
            selected_index = 0
            for value in pattern_list:
                combobox.addItem(value.name)
                if edit_these[column].upper_evaporation_pattern == value.name:
                    selected_index = int(combobox.count()) - 1
            combobox.setCurrentIndex(selected_index)
            self.tblGeneric.setCellWidget(13, column, combobox)

    def cmdOK_Clicked(self):
        if self.new_item:  # We are editing a newly created item and it needs to be added to the project
            if self.project_section and isinstance(self.project_section.value, list):
                self.project_section.value.append(self.new_item)
            else:
                print("Unable to add new item to project: section is not a list: " + self.SECTION_NAME)
        self.backend.apply_edits()
        self.close()

    def cmdCancel_Clicked(self):
        self.close()
