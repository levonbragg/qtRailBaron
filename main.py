import sys
import numpy

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PySide6 import QtWidgets as qtw, QtCore
from paytables import rbPayTable, bcPayTableUS, bcPayTableUK, rbCityAr, bcCityAr, bcUKCityar
from destinations_us import (REGIONS_US_LIST, REGIONS_US, PLAINS, NORTHWEST, SOUTHWEST,
                             NORTH_CENTRAL, SOUTH_CENTRAL, SOUTHEAST, NORTHEAST, DESTINATIONS_US_DICT,
                             REGIONS_RBUS, DESTINATIONS_RBUS_DICT)
from destinations_uk import (REGIONS_UK_LIST, REGIONS_UK, SCOTTISH_LOWLANDS, RED_ROSE_COUNTRY, WALES,
                             WEST_COUNTRY, SCOTTISH_HIGHLANDS, WHITE_ROSE_COUNTRY, MIDLANDS, EAST_ANGLIA,
                             HOME_COUNTIES, DESTINATIONS_UK_DICT)
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.chk_rbUS.setChecked(True)
        self.fill_fare_and_destination_tables()

        self.lv_source.itemSelectionChanged.connect(self.source_selected)
        self.lv_source.itemClicked.connect(self.source_selected)
        self.lv_destination.itemSelectionChanged.connect(self.dest_selected)
        self.lv_destination.itemClicked.connect(self.dest_selected)
        self.chk_rbUS.toggled.connect(self.fill_fare_and_destination_tables)
        self.chk_bcUS.toggled.connect(self.fill_fare_and_destination_tables)
        self.chk_bcUK.toggled.connect(self.fill_fare_and_destination_tables)
        self.tbl_region.itemSelectionChanged.connect(self.load_region_items)
        self.lbl_payout.setText("0.00")

    def load_region_items(self):
        """
        Load region destinations into the destination table based on the selected item in region table.
        :return:
        """
        if self.chk_rbUS.isChecked():
            dataset = DESTINATIONS_RBUS_DICT
        elif self.chk_bcUS.isChecked():
            dataset = DESTINATIONS_US_DICT
        elif self.chk_bcUK.isChecked():
            dataset = DESTINATIONS_UK_DICT
        try:
            row = self.tbl_region.selectedIndexes()[0].row()
            column = self.tbl_region.selectedIndexes()[0].column()
            if row == 0 or column == 0:
                return None
            else:
                if column & 1:
                    # ODD Selection
                    region = str(row + 1) + 'ODD'
                    i = 1
                    for row in dataset[region]:
                        self.insert_destination_row(i, row)
                        i += 1
                else:
                    # EVEN selection
                    region = str(row + 1) + 'EVEN'
                    i = 1
                    for row in dataset[region]:
                        self.insert_destination_row(i, row)
                        i += 1
        except IndexError:
            pass
        self.tbl_destination.resizeColumnsToContents()
        self.tbl_destination.resizeRowsToContents()

    def fill_fare_and_destination_tables(self):
        """
        Fill fare lists (source, and destination) and load region data into the destination tables.
        Set ROW1, COL1 to selected, and call the function to load region destinations.
        :return:
        """
        self.lv_source.clear()
        self.lv_destination.clear()

        self.tbl_destination.clearContents()
        self.tbl_destination.setRowCount(12)
        self.tbl_destination.setColumnCount(3)
        self.insert_destination_row(0, ['', 'ODD', 'EVEN'])

        self.tbl_region.clearContents()
        self.tbl_region.setRowCount(12)
        self.tbl_region.setColumnCount(3)
        self.insert_region_row(0,['','ODD','EVEN'])

        if self.chk_rbUS.isChecked():
            for location in rbCityAr:
                self.lv_source.addItem(location)
                self.lv_destination.addItem(location)
            i=1
            for region in REGIONS_RBUS:
                self.insert_region_row(i, region)
                i += 1

        if self.chk_bcUS.isChecked():
            for location in bcCityAr:
                self.lv_source.addItem(location)
                self.lv_destination.addItem(location)
            i = 1
            for region in REGIONS_US:
                self.insert_region_row(i, region)
                i += 1

        if self.chk_bcUK.isChecked():
            for location in bcUKCityar:
                self.lv_source.addItem(location)
                self.lv_destination.addItem(location)
            i = 1
            for region in REGIONS_UK:
                self.insert_region_row(i, region)
                i+=1
        self.tbl_region.resizeColumnsToContents()
        self.tbl_region.resizeRowsToContents()
        self.tbl_region.item(1,1).setSelected(True)
        self.load_region_items()

    def insert_destination_row(self, row, data):
        self.tbl_destination.setItem(row, 0, QTableWidgetItem(str(data[0])))
        self.tbl_destination.setItem(row, 1, QTableWidgetItem(data[1]))
        self.tbl_destination.setItem(row, 2, QTableWidgetItem(data[2]))

    def insert_region_row(self, row, region):
        self.tbl_region.setItem(row, 0, qtw.QTableWidgetItem(str(region[0])))
        self.tbl_region.setItem(row, 1, qtw.QTableWidgetItem(region[1]))
        self.tbl_region.setItem(row, 2, qtw.QTableWidgetItem(region[2]))

    def source_selected(self):
        self.calculate_payout()

    def dest_selected(self):
        self.calculate_payout()

    def round_up(self, x):
        """
        Round up to nearest 100. Needed when using the payout multipliers
        :param x: value to round
        :return: rounded value
        """
        return x if x % 100 == 0 else x + 100 - x % 100

    def calculate_payout(self):
        if self.chk_rbUS.isChecked():
            payout = (rbPayTable[self.lv_source.currentIndex().row(), self.lv_destination.currentIndex().row()]) * self.doubleSpinBox.value()
            payout = self.round_up(payout)
            self.lbl_payout.setText(str(int(payout)))
        if self.chk_bcUS.isChecked():
            payout = (bcPayTableUS[self.lv_source.currentIndex().row(), self.lv_destination.currentIndex().row()] * 1000) * self.doubleSpinBox.value()
            payout = self.round_up(payout)
            self.lbl_payout.setText(str(int(payout)))
        if self.chk_bcUK.isChecked():
            payout = (bcPayTableUK[self.lv_source.currentIndex().row(), self.lv_destination.currentIndex().row()] * 1000) * self.doubleSpinBox.value()
            payout = self.round_up(payout)
            self.lbl_payout.setText(str(int(payout)))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.tbl_region.setAlternatingRowColors(True)
    form.tbl_destination.setAlternatingRowColors(True)
    form.show()
    return_code = app.exec()
    sys.exit(return_code)