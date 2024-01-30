import sys
import importlib
import pathlib
import pyseq
import re

from PySide2 import QtWidgets, QtGui, QtCore

# UI 생성하기 전에 경로를 지정해서 rc를 계속 불러오지 않아도 되도록 설정해준다!
# 무.조.건 UI 생성 전!!!!!!!
sys.path.append('/home/rapa/git_workspace/Sequence_manager/resource/rc')

from resource.ui import sequence_manager_ui

importlib.reload(sequence_manager_ui)

class SequenceManger(QtWidgets.QMainWindow, sequence_manager_ui.Ui_MainWindow_Sequence_manager):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.__dir = ''


        self.setupUi(self)
        self._signal()

        # 리스트에 넣는 방법
        self.listWidget__missing.addItems(['aaaaaaaa', 'bbbbb', 'ccccccccccc'])

        self.listWidget__missing.customContextMenuRequested.connect(self.custom_context)

        # 어떤 아이템을 클릭했는가.
        self.listWidget__missing.currentItemChanged.connect(self.changed_missing_item)


    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, val):
        # assert isinstance(val, pathlib.Path)
        self.__dir = val

    def _signal(self):
        self.toolButton__dirpath.clicked.connect(self.set_dir)

    def set_dir(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            'Get Path',
            '/data'
        )
        # print(type(self.dir))
        self.lineEdit__dirpath.setText(self.dir)
        self.set_listwidget_seq_info()

    def set_listwidget_seq_info(self):
        path = pathlib.Path(self.dir)
        seq_list = path.glob('*.exr')
        comp = re.compile(r'\.(?P<frange>[0-9]{4})\.', re.DOTALL)

        file_frame_lst = list()
        filename_lst = list()

        for seq in seq_list:
            srch = comp.search(seq.name)
            file_frame_lst.append(int(srch.group('frange')))
            filename_lst.append(seq.name)

        seq_name = pyseq.Sequence(filename_lst)
        self.listWidget__seq_info.addItem(str(seq_name))
        return str(seq_name)

    # def set_missing(self):
    #     lst = list(range(1001, 1151))
    #     frame_info = set(lst) ^ set(file_frame_lst)
        # print(list(frame_info))

        # test - file copy
        # shutil.copy2(
        #    '/home/rapa/aaa.py', '/home/rapa/qqq.py')









    def changed_missing_item(self, idx: QtWidgets.QListWidgetItem):
        print(idx.text())

    def custom_context(self, pos: QtCore.QPoint):
        '''

        :param pos: type을 정해줘야 어떤걸 사용할 수 있는지 뜸.
        :return:
        '''
        menu = QtWidgets.QMenu('ddd', self)
        menu.addAction('asdflkj')
        menu.exec_()
        # print(pos.x())
        pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    seq_mgr = SequenceManger()
    seq_mgr.show()
    sys.exit(app.exec_())

