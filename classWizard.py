import os
from typing import List
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtWidgets import *

PATH = ""


class Ui_dialog(object):
    def setupUi(self, dialog)->None:

        self.variaveis = []

        if dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(800, 400)
        dialog.setMinimumSize(QSize(800, 400))
        dialog.setMaximumSize(QSize(800, 400))
        self.gridLayout_7 = QGridLayout(dialog)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(dialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.labelName = QLabel(self.widget)
        self.labelName.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.labelName, 0, 0, 1, 1)

        self.lineNome = QLineEdit(self.widget)
        self.lineNome.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineNome, 0, 1, 1, 1)

        self.labelArguments = QLabel(self.widget)
        self.labelArguments.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.labelArguments, 1, 0, 1, 1)

        self.lineArgumentos = QLineEdit(self.widget)
        self.lineArgumentos.setObjectName(u"lineEdit_2")
        self.lineArgumentos.setDragEnabled(False)

        self.gridLayout_3.addWidget(self.lineArgumentos, 1, 1, 1, 1)

        self.checkHasDestructor = QCheckBox(self.widget)
        self.checkHasDestructor.setObjectName(u"checkBox")
        self.checkHasDestructor.setChecked(True)

        self.gridLayout_3.addWidget(self.checkHasDestructor, 2, 0, 1, 1)

        self.checkVirtualDestructor = QCheckBox(self.widget)
        self.checkVirtualDestructor.setObjectName(u"checkBox_2")

        self.gridLayout_3.addWidget(self.checkVirtualDestructor, 2, 1, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.checkSubClass = QCheckBox(self.widget_2)
        self.checkSubClass.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkSubClass, 1, 0, 1, 2)

        self.labelInclude = QLabel(self.widget_2)
        self.labelInclude.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.labelInclude, 3, 0, 1, 1)

        self.lineInclude = QLineEdit(self.widget_2)
        self.lineInclude.setObjectName(u"lineEdit_4")
        self.lineInclude.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineInclude, 3, 1, 1, 1)

        self.labelScope = QLabel(self.widget_2)
        self.labelScope.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.labelScope, 4, 0, 1, 1)

        self.comboBoxScope = QComboBox(self.widget_2)
        self.comboBoxScope.setObjectName(u"comboBox")
        self.comboBoxScope.setEnabled(False)
        self.comboBoxScope.addItem("Public")
        self.comboBoxScope.addItem("Protected")
        self.comboBoxScope.addItem("Private")

        self.gridLayout_2.addWidget(self.comboBoxScope, 4, 1, 1, 1)

        self.labelSuperClassName = QLabel(self.widget_2)
        self.labelSuperClassName.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.labelSuperClassName, 2, 0, 1, 1)

        self.comboBoxSuperClass = QComboBox(self.widget_2)
        self.comboBoxSuperClass.setObjectName(u"comboBox_3")
        self.comboBoxSuperClass.setEnabled(False)
        self.fillAncestors()

        self.gridLayout_2.addWidget(self.comboBoxSuperClass, 2, 1, 1, 1)

        self.gridLayout_3.addWidget(self.widget_2, 3, 0, 1, 2)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.buttonRemove = QPushButton(self.widget_3)
        self.buttonRemove.setObjectName(u"pushButton")

        self.gridLayout_5.addWidget(self.buttonRemove, 2, 0, 1, 1)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_8 = QGridLayout(self.widget_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.labelAddNew = QLabel(self.widget_4)
        self.labelAddNew.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.labelAddNew, 0, 0, 1, 1)

        self.variableName = QLineEdit(self.widget_4)
        self.variableName.setObjectName(u"lineEdit_5")

        self.gridLayout_8.addWidget(self.variableName, 1, 0, 1, 2)

        self.labelScope_2 = QLabel(self.widget_4)
        self.labelScope_2.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.labelScope_2, 2, 0, 1, 1)

        self.comboBoxScope_2 = QComboBox(self.widget_4)
        self.comboBoxScope_2.setObjectName(u"comboBox_2")
        self.comboBoxScope_2.addItem("Public")
        self.comboBoxScope_2.addItem("Protected")
        self.comboBoxScope_2.addItem("Private")

        self.gridLayout_8.addWidget(self.comboBoxScope_2, 2, 1, 1, 1)

        self.checkHasGetter = QCheckBox(self.widget_4)
        self.checkHasGetter.setObjectName(u"checkBox_4")

        self.gridLayout_8.addWidget(self.checkHasGetter, 3, 0, 1, 2)

        self.checkHasSetter = QCheckBox(self.widget_4)
        self.checkHasSetter.setObjectName(u"checkBox_5")

        self.gridLayout_8.addWidget(self.checkHasSetter, 4, 0, 1, 2)

        self.checkHasPrefix = QCheckBox(self.widget_4)
        self.checkHasPrefix.setObjectName(u"checkBox_6")

        self.gridLayout_8.addWidget(self.checkHasPrefix, 5, 0, 1, 2)

        self.linePrefix = QLineEdit(self.widget_4)
        self.linePrefix.setObjectName(u"lineEdit_6")
        self.linePrefix.setEnabled(False)

        self.gridLayout_8.addWidget(self.linePrefix, 6, 0, 1, 2)

        self.buttonAddVariable = QPushButton(self.widget_4)
        self.buttonAddVariable.setObjectName(u"pushButton_2")
        self.buttonAddVariable.setEnabled(False)

        self.gridLayout_8.addWidget(self.buttonAddVariable, 7, 0, 1, 2)

        self.gridLayout_5.addWidget(self.widget_4, 0, 1, 3, 1)

        self.listVariable = QListWidget(self.widget_3)
        self.listVariable.setObjectName(u"listWidget")

        self.gridLayout_5.addWidget(self.listVariable, 1, 0, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.widget_3, 0, 1, 1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_6.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.retranslateUi(dialog)

        self.buttonBox.accepted.connect(self.createClass)
        self.buttonBox.rejected.connect(self.cancel)
        self.checkHasPrefix.stateChanged.connect(self.disablePreffix)
        self.checkSubClass.stateChanged.connect(self.toggleInheritance)

        self.comboBoxSuperClass.currentIndexChanged.connect(self.updateInclude)

        self.buttonAddVariable.clicked.connect(self.addVariable)
        self.variableName.textChanged.connect(self.variableNameNotEmpty)
        self.buttonRemove.clicked.connect(self.removeList)
        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog)->None:
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"C++ class wizard", None))
        self.labelName.setText(QCoreApplication.translate("dialog", u"Class name:", None))
        self.labelArguments.setText(QCoreApplication.translate("dialog", u"Arguments:", None))
        self.checkHasDestructor.setText(QCoreApplication.translate("dialog", u"Has destructor", None))
        self.checkVirtualDestructor.setText(QCoreApplication.translate("dialog", u"Virtual destructor", None))
        self.checkSubClass.setText(QCoreApplication.translate("dialog", u"Inherits another class", None))
        self.labelInclude.setText(QCoreApplication.translate("dialog", u"Ancestor's include name:", None))
        self.labelSuperClassName.setText(QCoreApplication.translate("dialog", u"Ancestor:", None))
        self.labelScope.setText(QCoreApplication.translate("dialog", u"Scope:", None))
        self.buttonRemove.setText(QCoreApplication.translate("dialog", u"Remove", None))
        self.label_7.setText(QCoreApplication.translate("dialog", u"Member Variables", None))
        self.labelAddNew.setText(QCoreApplication.translate("dialog", u"Add New:", None))
        self.labelScope_2.setText(QCoreApplication.translate("dialog", u"Scope:", None))
        self.checkHasGetter.setText(QCoreApplication.translate("dialog", u"Add \"getter\" method", None))
        self.checkHasSetter.setText(QCoreApplication.translate("dialog", u"Add \"setter\" method", None))
        self.checkHasPrefix.setText(QCoreApplication.translate("dialog", u"Add prefix:", None))
        self.buttonAddVariable.setText(QCoreApplication.translate("dialog", u"Add", None))
    # retranslateUi


    def fillAncestors(self)->None:
        dir = filter(lambda name: name.endswith(".h"),os.listdir(PATH))
        for i in dir:
            self.comboBoxSuperClass.addItem(i)
        self.lineInclude.setText(f"#include \"{self.comboBoxSuperClass.currentText()}\"")


    def removeList(self)->None:
        selected = self.listVariable.selectedItems()[0]
        nomeItem = selected.text()

        for i in range(self.listVariable.count()):
            if self.listVariable.item(i).text() == nomeItem:
                self.listVariable.takeItem(i)
                self.variaveis.pop(i)
                break


    def variableNameNotEmpty(self)->None:
        self.buttonAddVariable.setEnabled(self.variableName.text() != "")


    def disablePreffix(self)->None:
        self.linePrefix.setEnabled(self.checkHasPrefix.isChecked())


    def addVariable(self)->None:
        nameType = self.variableName.text()
        scope = self.comboBoxScope_2.currentText()
        hasGetter = self.checkHasGetter.isChecked()
        hasSetter = self.checkHasSetter.isChecked()
        hasPrefix = self.checkHasPrefix.isChecked()
        prefix = self.linePrefix.text()

        var = Variable(nameType,scope,hasGetter,hasSetter,prefix*hasPrefix)

        self.variaveis.append(var)
        self.listVariable.addItem(var.nameType)
        
        var = None

        self.variableName.setText("")
        return


    def updateInclude(self)->None:
        self.lineInclude.setText(f"#include \"{self.comboBoxSuperClass.currentText()}\"")


    def toggleInheritance(self)->None:
        self.comboBoxScope.setEnabled(self.checkSubClass.isChecked())
        self.comboBoxSuperClass.setEnabled(self.checkSubClass.isChecked())
        self.lineInclude.setEnabled(self.checkSubClass.isChecked())


    def createClass(self)->None:
        nome = self.lineNome.text()
        args = self.lineArgumentos.text() 
        hasDestructor = self.checkHasDestructor.isChecked()
        virtualDestructor = self.checkVirtualDestructor.isChecked()
       
        if self.checkSubClass.isChecked():
            ancestorName = self.comboBoxSuperClass.currentText()
            ancestorInclude = self.lineInclude.text()
            ancestorScope = self.comboBoxScope.currentText()   
            creator = SubClassCreator(nome,self.variaveis,args,hasDestructor,virtualDestructor,ancestorName,ancestorScope,ancestorInclude)   
        else:
            creator = ClassCreator(nome,self.variaveis,args,hasDestructor,virtualDestructor)
        creator.makeHeader()
        creator.makeImplementation()


    def cancel(self)->None:
        print("Saindo")
        exit()


class Variable():
    def __init__(self,nameType: str, scope: str, getter: bool, setter : bool, preffix : str) -> None:
        if nameType[-1] == ";":nameType=nameType[:-1]
        lista = nameType.split()
        self.type = lista[0]
        self.name = lista[1]
        if preffix: self.name = preffix+inicialMaiuscula(self.name)
        if ("=" in nameType):
            self.value = lista[3]
        else:
            self.value = ""
        self.scope = scope
        self.getter = getter
        self.setter = setter
        self.nameType = f"{self.type} {self.name}"
        if self.value:
            self.nameType += f" = {self.value}"

    
    def writeVariableLine(self)->str:
        if self.value:
            return f"\t{self.type} {self.name} = {self.value};\n"
        else:
            return f"\t{self.type} {self.name};\n"


    def writeGetterSetterLineHeader(self)->str:
        outText = ""
        if self.getter:
            outText+=f"\t{self.type} get{inicialMaiuscula(self.name)}();\n"
        if self.setter:
            outText+=f"\tvoid set{inicialMaiuscula(self.name)}({self.type} {self.name});\n"
        if outText:
            outText+="\n"
        return outText


    def writeGetterSetterImplementation(self,className:str)->str:
        outText = ""
        if self.getter:
            outText += f"{self.type} {className}::get{inicialMaiuscula(self.name)}()"+"{\n"
            outText += f"\treturn this->{self.name};\n"
            outText += "}\n\n\n"
        if self.setter:
            outText += f"void {className}::set{inicialMaiuscula(self.name)}({self.type} {self.name})"+"{\n"
            outText += f"\tthis->{self.name} = {self.name};\n"
            outText += "}\n\n\n"
        return outText


class ClassCreator():
    def __init__(self, name: str, variables:List[Variable],args: str , destructor: bool, virtualDestructor:bool) -> None:
        self.name = name
        self.variables = variables
        self.args = args
        self.destructor = destructor
        self.virtualDestructor = virtualDestructor
        

    def makeHeader(self)->None:
        outText = f"using namespace std;\n\n#ifndef {self.name}_H\n#define {self.name}_H\n\n"
        outText += self.createConstructorHeader()
        outText += self.createDestructorHeader()
        outText += self.attributeLineCreatorHeader()
        outText += "};\n\n#endif"
        return salvaTexto(outText,f"{self.name}.h")


    def attributeLineCreatorHeader(self)->str:
        publics = [i for i in self.variables if i.scope == "Public"]
        protecteds = [i for i in self.variables if i.scope == "Protected"]
        privates = [i for i in self.variables if i.scope == "Private"]
        outText = ""
        if publics:
            for variable in publics:
                outText+=variable.writeVariableLine()
        for variable in self.variables:
            outText+=variable.writeGetterSetterLineHeader()
        if protecteds:
            outText+="protected:\n"
            for variable in protecteds:
                outText+=variable.writeVariableLine()
        if privates:
            outText+="private:\n"
            for variable in privates:
                outText+=variable.writeVariableLine()
        return outText


    def createConstructorHeader(self)->str:
        outText = f"class {self.name}" + "{\n"
        outText += f"public:\n"
        outText += "\t\t//Constructor\n"
        if self.args:
            self.linConstructor = f"\t{self.name}({self.args});\n"
        else:
            self.linConstructor = f"\t{self.nome}();\n"
        outText += self.linConstructor
        return outText


    def createDestructorHeader(self)->str:
        outText = ""
        if self.destructor:
            outText += "\n\t//Destructor\n"
            if self.virtualDestructor:
                outText += f"\tvirtual ~{self.name}();\n\n"
            else:
                outText += f"\t~{self.name}();\n\n"
        return outText


    def makeImplementation(self)->None:
        outText = f'using namespace std;\n\n#include <iostream>\n#include "{self.name}.h"\n\n'
        outText += self.createConstructorImplementation()
        outText += self.createDestructorImplementation()
        outText += self.createAttributeImplementation()
        return salvaTexto(outText,f"{self.name}.cpp")


    def createConstructorImplementation(self)->str:
        outText = f"{self.name}::{self.linConstructor[1:-2]}"+"{\n"
        outText += "}\n\n\n"
        return outText


    def createDestructorImplementation(self)->str:
        return f"{self.name}::~{self.name}()"+"{\n}\n\n\n"


    def createAttributeImplementation(self)->str:
        outText = ""
        for variable in self.variables:
            outText += variable.writeGetterSetterImplementation(self.name)
        return outText


class SubClassCreator(ClassCreator):
    def __init__(self, name: str, variables:List[Variable],args: str , destructor: bool, virtualDestructor:bool, superClassName: str,scope: str, superClassInclude: str) -> None:
        super().__init__(name, variables, args, destructor, virtualDestructor)
        self.superClassName = superClassName[:-2]
        self.scope = scope
        self.superClassInclude = superClassInclude


    def createConstructorHeader(self)->str:
        outText = f"{self.superClassInclude}\n\n"
        outText += f"class {self.name} : {self.scope.lower()} {self.superClassName}" + "{\n"
        outText += f"public:\n"
        self.linConstructorAncestor = ""
        with open(f"./{PATH}/{self.superClassName}.h","r") as arq:
            for lin in arq:
                if lin.startswith(f"\t{self.superClassName}("):
                    self.linConstructorAncestor = lin
        outText += "\t//Constructor\n"
        if self.args:
            self.linConstructor = f"\t{self.name}{self.linConstructorAncestor.replace(self.superClassName,'')[1:-3]}, {self.args});\n"
        else:
            self.linConstructor = f"\t{self.name}{self.linConstructorAncestor.replace(self.superClassName,'')[1:-2]};\n"
        outText += self.linConstructor
        return outText

    def createConstructorImplementation(self)->str:
        outText = f"{self.name}::{self.linConstructor[1:-2]}:\n"
        outText += f"\t{self.superClassName}("

        linConstrutorInterno = self.linConstructorAncestor[1:-2].replace(self.superClassName,"")[1:-1].split(",")
        for lin in linConstrutorInterno:
            print(lin)
            outText += f"{lin.split()[1]},"
        outText = outText[:-1]+"){\n"
        outText += "}\n\n\n"
        return outText


def inicialMaiuscula(string: str)->str:
    return string[0].upper() + string[1:]


def salvaTexto(outText: str,nome: str)->None:
    global PATH
    with open(f"./{PATH}/{nome}","w") as arq:
        arq.write(outText)


if __name__ == "__main__":
    import sys
    PATH = sys.argv[1]
    app = QApplication()
    dialog = QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
