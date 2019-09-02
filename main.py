from PySide2 import QtWidgets, QtCore, QtGui


app = QtWidgets.QApplication([])

splitter = QtWidgets.QSplitter()

model = QtWidgets.QFileSystemModel()
model.setRootPath(QtCore.QDir.currentPath())

tree = QtWidgets.QTreeView(splitter)
tree.setModel(model)
tree.setRootIndex(model.index(QtCore.QDir.currentPath()))  # 获取当前路径的 Index 并作为视图的根路径

list_ = QtWidgets.QListView(splitter)
list_.setModel(model)
list_.setRootIndex(model.index(QtCore.QDir.currentPath()))

parentIndex = model.index(QtCore.QDir.currentPath())  # 获取当前路径的 Index
parentIndex = model.index(0, 0, QtCore.QModelIndex())  # 获取当前路径的 Index
numRows = model.rowCount(parentIndex)
print(numRows)

for row in range(numRows):
    index = model.index(row, 0, parentIndex)
    text = model.data(index, QtGui.Qt.DisplayRole)
    print(text)


splitter.setWindowTitle("Two Views")
splitter.show()

app.exec_()
