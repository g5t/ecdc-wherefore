# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WhereforeGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 662)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.consumerBarLayout = QtWidgets.QHBoxLayout()
        self.consumerBarLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.consumerBarLayout.setObjectName("consumerBarLayout")
        self.brokerAddressLayout = QtWidgets.QHBoxLayout()
        self.brokerAddressLayout.setObjectName("brokerAddressLayout")
        self.brokerAddressLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brokerAddressLabel.sizePolicy().hasHeightForWidth())
        self.brokerAddressLabel.setSizePolicy(sizePolicy)
        self.brokerAddressLabel.setObjectName("brokerAddressLabel")
        self.brokerAddressLayout.addWidget(self.brokerAddressLabel)
        self.brokerAddressEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.brokerAddressEdit.setObjectName("brokerAddressEdit")
        self.brokerAddressLayout.addWidget(self.brokerAddressEdit)
        self.consumerBarLayout.addLayout(self.brokerAddressLayout)
        self.line1_1 = QtWidgets.QFrame(self.centralwidget)
        self.line1_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1_1.setObjectName("line1_1")
        self.consumerBarLayout.addWidget(self.line1_1)
        self.startAtLabel = QtWidgets.QLabel(self.centralwidget)
        self.startAtLabel.setObjectName("startAtLabel")
        self.consumerBarLayout.addWidget(self.startAtLabel)
        self.startAtSelector = QtWidgets.QComboBox(self.centralwidget)
        self.startAtSelector.setObjectName("startAtSelector")
        self.consumerBarLayout.addWidget(self.startAtSelector)
        self.startOffsetEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.startOffsetEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.startOffsetEdit.setObjectName("startOffsetEdit")
        self.consumerBarLayout.addWidget(self.startOffsetEdit)
        self.startTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.consumerBarLayout.addWidget(self.startTimeEdit)
        self.line1_2 = QtWidgets.QFrame(self.centralwidget)
        self.line1_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1_2.setObjectName("line1_2")
        self.consumerBarLayout.addWidget(self.line1_2)
        self.endAtLabel = QtWidgets.QLabel(self.centralwidget)
        self.endAtLabel.setObjectName("endAtLabel")
        self.consumerBarLayout.addWidget(self.endAtLabel)
        self.endAtSelector = QtWidgets.QComboBox(self.centralwidget)
        self.endAtSelector.setObjectName("endAtSelector")
        self.consumerBarLayout.addWidget(self.endAtSelector)
        self.endOffsetEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.endOffsetEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.endOffsetEdit.setObjectName("endOffsetEdit")
        self.consumerBarLayout.addWidget(self.endOffsetEdit)
        self.endTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.endTimeEdit.setObjectName("endTimeEdit")
        self.consumerBarLayout.addWidget(self.endTimeEdit)
        self.verticalLayout_8.addLayout(self.consumerBarLayout)
        self.kafkaConfigFileLayout = QtWidgets.QHBoxLayout()
        self.kafkaConfigFileLayout.setObjectName("kafkaConfigFileLayout")
        self.kafkaConfigFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.kafkaConfigFileLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kafkaConfigFileLabel.sizePolicy().hasHeightForWidth())
        self.kafkaConfigFileLabel.setSizePolicy(sizePolicy)
        self.kafkaConfigFileLabel.setObjectName("kafkaConfigFileLabel")
        self.kafkaConfigFileLayout.addWidget(self.kafkaConfigFileLabel)
        self.kafkaConfigFileValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.kafkaConfigFileValueLabel.setEnabled(False)
        self.kafkaConfigFileValueLabel.setObjectName("kafkaConfigFileValueLabel")
        self.kafkaConfigFileLayout.addWidget(self.kafkaConfigFileValueLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.kafkaConfigFileLayout.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.kafkaConfigFileLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_8)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topicPartitionSourceTree = QtWidgets.QTreeView(self.centralwidget)
        self.topicPartitionSourceTree.setObjectName("topicPartitionSourceTree")
        self.verticalLayout_2.addWidget(self.topicPartitionSourceTree)
        self.enableDisableLayout = QtWidgets.QHBoxLayout()
        self.enableDisableLayout.setObjectName("enableDisableLayout")
        self.enableAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.enableAllButton.setObjectName("enableAllButton")
        self.enableDisableLayout.addWidget(self.enableAllButton)
        self.disableAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.disableAllButton.setObjectName("disableAllButton")
        self.enableDisableLayout.addWidget(self.disableAllButton)
        self.enableDefaultComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.enableDefaultComboBox.setProperty("placeholderText", "")
        self.enableDefaultComboBox.setObjectName("enableDefaultComboBox")
        self.enableDisableLayout.addWidget(self.enableDefaultComboBox)
        self.verticalLayout_2.addLayout(self.enableDisableLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.line_2_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_2_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2_1.setObjectName("line_2_1")
        self.horizontalLayout_2.addWidget(self.line_2_1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.partitionInfoBox = QtWidgets.QGroupBox(self.centralwidget)
        self.partitionInfoBox.setMinimumSize(QtCore.QSize(500, 0))
        self.partitionInfoBox.setObjectName("partitionInfoBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.partitionInfoBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.partitionInfoLayout = QtWidgets.QHBoxLayout()
        self.partitionInfoLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.partitionInfoLayout.setObjectName("partitionInfoLayout")
        self.lowLayout = QtWidgets.QFormLayout()
        self.lowLayout.setObjectName("lowLayout")
        self.lowOffsetLabel = QtWidgets.QLabel(self.partitionInfoBox)
        self.lowOffsetLabel.setObjectName("lowOffsetLabel")
        self.lowLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lowOffsetLabel)
        self.lowOffsetValue = QtWidgets.QLabel(self.partitionInfoBox)
        self.lowOffsetValue.setObjectName("lowOffsetValue")
        self.lowLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lowOffsetValue)
        self.partitionInfoLayout.addLayout(self.lowLayout)
        self.line3_1 = QtWidgets.QFrame(self.partitionInfoBox)
        self.line3_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line3_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3_1.setObjectName("line3_1")
        self.partitionInfoLayout.addWidget(self.line3_1)
        self.highLayout = QtWidgets.QFormLayout()
        self.highLayout.setObjectName("highLayout")
        self.highOffsetLabel = QtWidgets.QLabel(self.partitionInfoBox)
        self.highOffsetLabel.setObjectName("highOffsetLabel")
        self.highLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.highOffsetLabel)
        self.highOffsetValue = QtWidgets.QLabel(self.partitionInfoBox)
        self.highOffsetValue.setObjectName("highOffsetValue")
        self.highLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.highOffsetValue)
        self.partitionInfoLayout.addLayout(self.highLayout)
        self.line3_2 = QtWidgets.QFrame(self.partitionInfoBox)
        self.line3_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line3_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3_2.setObjectName("line3_2")
        self.partitionInfoLayout.addWidget(self.line3_2)
        self.lagLayout = QtWidgets.QFormLayout()
        self.lagLayout.setObjectName("lagLayout")
        self.lagLabel = QtWidgets.QLabel(self.partitionInfoBox)
        self.lagLabel.setObjectName("lagLabel")
        self.lagLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lagLabel)
        self.lagValue = QtWidgets.QLabel(self.partitionInfoBox)
        self.lagValue.setObjectName("lagValue")
        self.lagLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lagValue)
        self.partitionInfoLayout.addLayout(self.lagLayout)
        self.verticalLayout_5.addLayout(self.partitionInfoLayout)
        self.verticalLayout_4.addWidget(self.partitionInfoBox)
        self.sourceInfoBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sourceInfoBox.sizePolicy().hasHeightForWidth())
        self.sourceInfoBox.setSizePolicy(sizePolicy)
        self.sourceInfoBox.setObjectName("sourceInfoBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.sourceInfoBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sourceNameLabel = QtWidgets.QLabel(self.sourceInfoBox)
        self.sourceNameLabel.setObjectName("sourceNameLabel")
        self.horizontalLayout.addWidget(self.sourceNameLabel)
        self.sourceNameValue = QtWidgets.QLabel(self.sourceInfoBox)
        self.sourceNameValue.setObjectName("sourceNameValue")
        self.horizontalLayout.addWidget(self.sourceNameValue)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sourceTypeLabel = QtWidgets.QLabel(self.sourceInfoBox)
        self.sourceTypeLabel.setObjectName("sourceTypeLabel")
        self.horizontalLayout_3.addWidget(self.sourceTypeLabel)
        self.sourceTypeValue = QtWidgets.QLabel(self.sourceInfoBox)
        self.sourceTypeValue.setObjectName("sourceTypeValue")
        self.horizontalLayout_3.addWidget(self.sourceTypeValue)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(self.sourceInfoBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.otherLayout = QtWidgets.QFormLayout()
        self.otherLayout.setObjectName("otherLayout")
        self.firstOffsetLabel = QtWidgets.QLabel(self.sourceInfoBox)
        self.firstOffsetLabel.setObjectName("firstOffsetLabel")
        self.otherLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstOffsetLabel)
        self.firstOffsetValue = QtWidgets.QLabel(self.sourceInfoBox)
        self.firstOffsetValue.setObjectName("firstOffsetValue")
        self.otherLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstOffsetValue)
        self.currentOffsetLabel = QtWidgets.QLabel(self.sourceInfoBox)
        self.currentOffsetLabel.setObjectName("currentOffsetLabel")
        self.otherLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.currentOffsetLabel)
        self.currentOffsetValue = QtWidgets.QLabel(self.sourceInfoBox)
        self.currentOffsetValue.setObjectName("currentOffsetValue")
        self.otherLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.currentOffsetValue)
        self.currentMsgSizeLabel = QtWidgets.QLabel(self.sourceInfoBox)
        self.currentMsgSizeLabel.setObjectName("currentMsgSizeLabel")
        self.otherLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.currentMsgSizeLabel)
        self.currentMsgSizeValue = QtWidgets.QLabel(self.sourceInfoBox)
        self.currentMsgSizeValue.setObjectName("currentMsgSizeValue")
        self.otherLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currentMsgSizeValue)
        self.receivedMessagesLabel = QtWidgets.QLabel(self.sourceInfoBox)
        self.receivedMessagesLabel.setObjectName("receivedMessagesLabel")
        self.otherLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.receivedMessagesLabel)
        self.receivedMessagesValue = QtWidgets.QLabel(self.sourceInfoBox)
        self.receivedMessagesValue.setObjectName("receivedMessagesValue")
        self.otherLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.receivedMessagesValue)
        self.consumptionRateLabel = QtWidgets.QLabel(self.sourceInfoBox)
        self.consumptionRateLabel.setObjectName("consumptionRateLabel")
        self.otherLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.consumptionRateLabel)
        self.consumptionRateValue = QtWidgets.QLabel(self.sourceInfoBox)
        self.consumptionRateValue.setObjectName("consumptionRateValue")
        self.otherLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.consumptionRateValue)
        self.messageRateLabel = QtWidgets.QLabel(self.sourceInfoBox)
        self.messageRateLabel.setObjectName("messageRateLabel")
        self.otherLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.messageRateLabel)
        self.messageRateValue = QtWidgets.QLabel(self.sourceInfoBox)
        self.messageRateValue.setObjectName("messageRateValue")
        self.otherLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.messageRateValue)
        self.dataRateLabel = QtWidgets.QLabel(self.sourceInfoBox)
        self.dataRateLabel.setObjectName("dataRateLabel")
        self.otherLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.dataRateLabel)
        self.dataRateValue = QtWidgets.QLabel(self.sourceInfoBox)
        self.dataRateValue.setObjectName("dataRateValue")
        self.otherLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.dataRateValue)
        self.verticalLayout_6.addLayout(self.otherLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.dataLabel = QtWidgets.QLabel(self.sourceInfoBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataLabel.sizePolicy().hasHeightForWidth())
        self.dataLabel.setSizePolicy(sizePolicy)
        self.dataLabel.setObjectName("dataLabel")
        self.horizontalLayout_6.addWidget(self.dataLabel)
        self.dataValue = QtWidgets.QLabel(self.sourceInfoBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataValue.sizePolicy().hasHeightForWidth())
        self.dataValue.setSizePolicy(sizePolicy)
        self.dataValue.setObjectName("dataValue")
        self.horizontalLayout_6.addWidget(self.dataValue)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.timestampsBox = QtWidgets.QGroupBox(self.sourceInfoBox)
        self.timestampsBox.setObjectName("timestampsBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.timestampsBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.firstMsgTimLabel = QtWidgets.QLabel(self.timestampsBox)
        self.firstMsgTimLabel.setObjectName("firstMsgTimLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstMsgTimLabel)
        self.firstMsgTimeValue = QtWidgets.QLabel(self.timestampsBox)
        self.firstMsgTimeValue.setObjectName("firstMsgTimeValue")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstMsgTimeValue)
        self.lastMsgReceiveTimeLabel = QtWidgets.QLabel(self.timestampsBox)
        self.lastMsgReceiveTimeLabel.setObjectName("lastMsgReceiveTimeLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastMsgReceiveTimeLabel)
        self.lastMsgReceiveTimeValue = QtWidgets.QLabel(self.timestampsBox)
        self.lastMsgReceiveTimeValue.setObjectName("lastMsgReceiveTimeValue")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastMsgReceiveTimeValue)
        self.lastMsgTimeLabel = QtWidgets.QLabel(self.timestampsBox)
        self.lastMsgTimeLabel.setObjectName("lastMsgTimeLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastMsgTimeLabel)
        self.lastMsgTimeValue = QtWidgets.QLabel(self.timestampsBox)
        self.lastMsgTimeValue.setObjectName("lastMsgTimeValue")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lastMsgTimeValue)
        self.lastMsgKafkaTimeLabel = QtWidgets.QLabel(self.timestampsBox)
        self.lastMsgKafkaTimeLabel.setObjectName("lastMsgKafkaTimeLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lastMsgKafkaTimeLabel)
        self.lastMsgKafkaTimeValue = QtWidgets.QLabel(self.timestampsBox)
        self.lastMsgKafkaTimeValue.setObjectName("lastMsgKafkaTimeValue")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lastMsgKafkaTimeValue)
        self.verticalLayout_6.addWidget(self.timestampsBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.sourceInfoBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wherefore"))
        self.brokerAddressLabel.setText(_translate("MainWindow", "Broker address"))
        self.startAtLabel.setText(_translate("MainWindow", "Start at"))
        self.endAtLabel.setText(_translate("MainWindow", "Stop at"))
        self.kafkaConfigFileLabel.setText(_translate("MainWindow", "Configuration file:"))
        self.kafkaConfigFileValueLabel.setText(_translate("MainWindow", "(unset)"))
        self.enableAllButton.setText(_translate("MainWindow", "Enable all"))
        self.disableAllButton.setText(_translate("MainWindow", "Disable all"))
        self.partitionInfoBox.setTitle(_translate("MainWindow", "Partition info"))
        self.lowOffsetLabel.setText(_translate("MainWindow", "Low offset:"))
        self.lowOffsetValue.setText(_translate("MainWindow", "n/a"))
        self.highOffsetLabel.setText(_translate("MainWindow", "High offset:"))
        self.highOffsetValue.setText(_translate("MainWindow", "n/a"))
        self.lagLabel.setText(_translate("MainWindow", "Current lag:"))
        self.lagValue.setText(_translate("MainWindow", "n/a"))
        self.sourceInfoBox.setTitle(_translate("MainWindow", "Source info"))
        self.sourceNameLabel.setText(_translate("MainWindow", "Source name:"))
        self.sourceNameValue.setText(_translate("MainWindow", "n/a"))
        self.sourceTypeLabel.setText(_translate("MainWindow", "Source type:"))
        self.sourceTypeValue.setText(_translate("MainWindow", "n/a"))
        self.firstOffsetLabel.setText(_translate("MainWindow", "First offset"))
        self.firstOffsetValue.setText(_translate("MainWindow", "n/a"))
        self.currentOffsetLabel.setText(_translate("MainWindow", "Current offset"))
        self.currentOffsetValue.setText(_translate("MainWindow", "n/a"))
        self.currentMsgSizeLabel.setText(_translate("MainWindow", "Current msg. size"))
        self.currentMsgSizeValue.setText(_translate("MainWindow", "n/a"))
        self.receivedMessagesLabel.setText(_translate("MainWindow", "Received messages"))
        self.receivedMessagesValue.setText(_translate("MainWindow", "n/a"))
        self.consumptionRateLabel.setText(_translate("MainWindow", "Consumption rate"))
        self.consumptionRateValue.setText(_translate("MainWindow", "n/a"))
        self.messageRateLabel.setText(_translate("MainWindow", "Message rate"))
        self.messageRateValue.setText(_translate("MainWindow", "n/a"))
        self.dataRateLabel.setText(_translate("MainWindow", "Data rate"))
        self.dataRateValue.setText(_translate("MainWindow", "n/a"))
        self.dataLabel.setText(_translate("MainWindow", "Data:"))
        self.dataValue.setText(_translate("MainWindow", "n/a"))
        self.timestampsBox.setTitle(_translate("MainWindow", "Timestamps"))
        self.firstMsgTimLabel.setText(_translate("MainWindow", "First message time"))
        self.firstMsgTimeValue.setText(_translate("MainWindow", "n/a"))
        self.lastMsgReceiveTimeLabel.setText(_translate("MainWindow", "Last received time"))
        self.lastMsgReceiveTimeValue.setText(_translate("MainWindow", "n/a"))
        self.lastMsgTimeLabel.setText(_translate("MainWindow", "Last message time"))
        self.lastMsgTimeValue.setText(_translate("MainWindow", "n/a"))
        self.lastMsgKafkaTimeLabel.setText(_translate("MainWindow", "Last Kafka time"))
        self.lastMsgKafkaTimeValue.setText(_translate("MainWindow", "n/a"))
