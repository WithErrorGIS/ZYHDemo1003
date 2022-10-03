import pandas as pd

class Layer(object):

    def __init__(self, _type, name='new_layer', srid=3857):
        '''
        :param _type: 图层中几何体的类别，用type类型
        :param name: 图层名字
        '''
        self.type = _type  # 图层中几何体类别，暂时为1点，2线，3面
        self.name = name  # 图层名字
        self.geometries = []  # 几何体列表

        #以下为未做部分
        self.visible = True  # 图层可见状态
        self.selectedItems = []  # 被选中的几何体ID（为了使选中几何体和属性表结合）
        self.srid = srid
        self.attr_desp_dict = {'id': 'int'}  # 属性表描述，k为属性名称，v为属性类型，k,v均为str类型
        self.table = pd.DataFrame(columns=['id'])  # 属性表