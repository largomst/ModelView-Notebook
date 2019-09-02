from PySide2 import QtWidgets, QtCore, QtGui


class StringListModel(QtCore.QAbstractListModel):
    def __init__(self, strings, parent=None):
        super().__init__()
        self._stringList = strings or []

    def rowCount(self, index):
        return len(self._stringList)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._stringList[index.row()]

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return ""
        else:
            if orientation == QtCore.Qt.Horizontal:
                return f"Column {section}"
            else:
                return f"Row {section}"

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnable
        else:
            return super().flags(index) | QtCore.Qt.ItemIsEditable

    def setData(self, index, value, role):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self._stringList[index.row()] = str(value)
            self.dataChanged.emit(index, index)
            print(self._stringList)
            return True
        else:
            return False

    # def insertRows(self, position, rows, parent):
    #     self.beginInsertRows(QtCore.QModelIndex(), position, position + rows - 1)
    #     for row in range(rows):
    #         self._stringList.insert(0, "")
    #     self.endInsertRows()
    #     return True

    # def remove(self, position, rows, parents):
    #     self.beginInsertRows(QtCore.QModelIndex(), position, position + rows - 1)
    #     for row in range(rows):
    #         self._stringList.remove(position)
    #     self.endInsertRows()
    #     return True


class SpinBoxDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self):
        super().__init__()

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QSpinBox()
        editor.setFrame(False)
        editor.setMinimum(0)
        editor.setMaximum(0)

        return editor

    def setEditor(self, editor, index):
        psss

    def setModelData(self, editor, model, index):
        pass

    def updateEidtorGemetry(self, editor, option, index):
        pass


app = QtWidgets.QApplication([])
numbers = "One Two Three Four Five".split(" ")
model = StringListModel(numbers)
view = QtWidgets.QListView()
view.setModel(model)
view.show()
app.exec_()
