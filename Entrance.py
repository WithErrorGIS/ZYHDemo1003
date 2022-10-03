import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QPointF,QLineF
from PyQt5.QtGui import (QPainter, QBrush, QLinearGradient, QConicalGradient, QRadialGradient,
                         QPen, QColor, QBrush, QPainterPath, QPolygonF)

from PyQt5.QtWidgets import (QMainWindow, QGraphicsPolygonItem, QGraphicsLineItem,QGraphicsItem, QGraphicsEllipseItem,QGraphicsView,
                             QGraphicsScene, QFileDialog, QApplication, QMessageBox, QWidget, QGridLayout, QFrame,
                             QTreeWidgetItem)


#引入各个功能类
from Function import Layer

#读取主窗体UI
from MainUI_LXY import *


class MyWindow(QMainWindow, Ui_MainWindow, QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        # 存储用于展示的scene
        self.scene = QtWidgets.QGraphicsScene(self)

        # 所有图层
        self.editableLayers = []

        # 可开始编辑的图层，暂时没做
        self.editableLayers = []

        self.initUI()

        self.test()  # 用于测试，生成三个图层

    # 窗口初始化
    def initUI(self):
        # 设置画布背景为白色
        self.scene.setBackgroundBrush(Qt.white)
        # 设置画布内的图形可以被鼠标画框选择
        self.graphicsView.setDragMode(self.graphicsView.RubberBandDrag)

        #初始化图层树
        self.treeWidget_layer.setHeaderLabels(['Layers in WEGIS'])
        # 设置图层树的根节点
        self.root = QTreeWidgetItem(self.treeWidget_layer)
        self.root.setText(0, '示例地图')

    # 用于测试，生成三个图层
    def test(self):

        #定义三个图层
        layer1 = Layer.Layer(1,'layer1')
        layer2 = Layer.Layer(2,'layer2')
        layer3 = Layer.Layer(3,'layer3')

        # 定义一个画笔，设置画笔颜色和宽度
        pen = QPen()
        pen.setColor(QColor(0, 160, 230))
        pen.setWidth(1)

        #创建图形
        point = QPointF(-50.0, -90.0)
        line = QLineF(QPointF(-50.0, -15.0), QPointF(202.0, -140.0))
        polygon = QPolygonF([QtCore.QPointF(-100.0, -150.0), QtCore.QPointF(-120.0, 150.0), QtCore.QPointF(320.0, 160.0)])


        m_pointItem = QGraphicsEllipseItem()  # 定义一个点图元（实际上为一个实心圆）
        m_pointItem.setRect(point.x()-5,point.y()-5,10,10)
        m_pointItem.setPen(pen)
        m_pointItem.setBrush(QColor(0, 160, 230))#填充
        m_pointItem.setFlag(QGraphicsItem.ItemIsMovable)
        m_pointItem.setFlag(QGraphicsItem.ItemIsSelectable)

        m_lineItem = QGraphicsLineItem()  # 定义一个线图元
        m_lineItem.setLine(line)
        m_lineItem.setPen(pen)
        m_lineItem.setFlag(QGraphicsItem.ItemIsMovable)
        m_lineItem.setFlag(QGraphicsItem.ItemIsSelectable)

        m_polygonItem = QGraphicsPolygonItem()  # 定义一个多边形图元
        m_polygonItem.setPolygon(polygon)
        m_polygonItem.setPen(pen)
        m_polygonItem.setFlag(QGraphicsItem.ItemIsMovable)
        m_polygonItem.setFlag(QGraphicsItem.ItemIsSelectable)

        #将图元添加至图层
        layer1.geometries = [m_pointItem]
        layer2.geometries = [m_lineItem]
        layer3.geometries = [m_polygonItem]

        #把图层加到地图数据中
        self.editableLayers.append(layer1)
        self.editableLayers.append(layer2)
        self.editableLayers.append(layer3)

        # 把图元加到地图展示中
        self.scene.addItem(m_pointItem)
        self.scene.addItem(m_lineItem)
        self.scene.addItem(m_polygonItem)
        self.graphicsView.setScene(self.scene)

        #刷新图层树
        self.refreshLayers()

    def refreshLayers(self):
        for layer in self.editableLayers:
            # 将所有图层添加至子节点
            child = QTreeWidgetItem(self.root)
            child.setText(0, layer.name)
            self.root.addChild(child)
        self.treeWidget_layer.expandAll() #展开所有图层树节点


    #删除选择集,还没做好
    def DelAllItem(self):
        scene = self.graphicsView.scene()
        Items = scene.selectedItems()
        print(len(Items))
        for item in Items:
            scene.removeItem(item)

        # self.items(self.graphicsView.rubberBandRect())

        # Items=self.items(area)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
