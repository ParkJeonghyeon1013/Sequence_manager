import sys
import importlib
import pathlib
import pyseq
import re
import os
import shutil

from PySide2 import QtWidgets, QtGui, QtCore

# UI 생성하기 전에 경로를 지정해서 rc를 계속 불러오지 않아도 되도록 설정해준다!
# 무.조.건 UI 생성 전!!!!!!!
# sys.path.append('/home/rapa/git_workspace/Sequence_manager/resource/rc')
sys.path.append('C:/Users/USER/Desktop/git_workspace/Sequence_manager/resource')
from resource.ui2 import sequence_manager_custom_ui

importlib.reload(sequence_manager_custom_ui)

class SequenceManger(QtWidgets.QMainWindow, sequence_manager_custom_ui.Ui_MainWindow_Sequence_manager):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        # self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        # 나온 시퀀스 파일에서 우클릭했을 때 그부분에서만 연관 탭이 뜨도록 policy 를 내가 만든 Custom으로 설정해야 함.
        self.listWidget__missing.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.listWidget__error_frame.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.listWidget__seq_info.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)

        self.__file_lst = list()
        self.select_seq_name = ''
        self.__dir = ''
        self.open_file_key = False



        self._signal()


        # 리스트에 넣는 방법
        # self.listWidget__missing.addItems(['aaaaaaaa', 'bbbbb', 'ccccccccccc'])


        # 어떤 아이템을 클릭했는가.
        self.listWidget__seq_info.currentItemChanged.connect(self.changed_info_item)
        self.listWidget__missing.currentItemChanged.connect(self.changed_missing_item)
        self.listWidget__error_frame.currentItemChanged.connect(self.changed_err_item)
        self.listWidget__sequence.currentItemChanged.connect(self.changed_seq_item)

        # seq info listwidget 에서 우클릭했을 때
        self.listWidget__seq_info.customContextMenuRequested.connect(self.custom_context_seq_info)
        self.listWidget__missing.customContextMenuRequested.connect(self.custom_context_missing)
        self.listWidget__error_frame.customContextMenuRequested.connect(self.custom_context_err)


        self.set_preview()
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, val):
        # assert isinstance(val, pathlib.Path)
        self.__dir = val

    @property
    def file_lst(self):
        return self.__file_lst
    @file_lst.setter
    def file_lst(self, val):
        # assert isinstance(val, list)
        self.__file_lst = val

    def _signal(self):
        self.label__seq_info.setText('')
        self.toolButton__dirpath.clicked.connect(self.set_dir)
        self.toolButton__work_filepath.clicked.connect(self.set_open_file)
        # self.label__preview.setPixmap(self.set_preview)

    def custom_context_seq_info(self, pos: QtCore.QPoint):
        '''

        :param pos: type을 정해줘야 어떤걸 사용할 수 있는지 뜸.
        :return:
        '''
        index = self.listWidget__seq_info.indexAt(pos)
        if not index.isValid():
            return
        context = QtWidgets.QMenu(self)
        test_menu = QtWidgets.QMenu('Info', self)
        context.addMenu(test_menu)

        action_text_menu_seq_info = QtWidgets.QAction('Detail', self)
        test_menu.addAction(action_text_menu_seq_info)

        actions = context.exec_(self.listWidget__seq_info.mapToGlobal(pos))

        # 클릭했을 때
        if actions == action_text_menu_seq_info:
            self.listWidget__missing.addItems(self.set_missing())
            self.listWidget__error_frame.addItems(self.set_err())
            self.listWidget__sequence.addItems(self.set_sequcene())
            print()
            print('click info > detail')

    def custom_context_missing(self, pos: QtCore.QPoint):
        index = self.listWidget__missing.indexAt(pos)
        if not index.isValid():
            return
        context = QtWidgets.QMenu(self)
        menu1 = QtWidgets.QAction('Send to Render Farm')
        context.addAction(menu1)

        actions = context.exec_(self.listWidget__missing.mapToGlobal(pos))
        if actions == menu1:
            print('클릭했다')

    def custom_context_err(self, pos: QtCore.QPoint):
        index = self.listWidget__missing.indexAt(pos)
        if not index.isValid():
            return
        context = QtWidgets.QMenu(self)
        menu1 = QtWidgets.QAction('Send to Render Farm')
        context.addAction(menu1)

        actions = context.exec_(self.listWidget__missing.mapToGlobal(pos))
        if actions == menu1:
            print('클릭했다')

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

    def set_dir(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            'Get Path',
            # '/data'
            'D:/netflix_ac/resource/render_seq'
        )
        # print(type(self.dir))
        self.lineEdit__dirpath.setText(self.dir)
        self.set_listwidget_seq_info()

    def set_sequcene(self):
        path = pathlib.Path(self.dir)
        exr_list = path.glob('*.exr')
        seq_lst = [str(file.name) for file in exr_list]
        return seq_lst


    def set_label_seq_info(self):
        self.label__seq_info.setText(self.select_seq_name)

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

        self.file_lst = filename_lst
        seq_name = pyseq.Sequence(filename_lst)
        self.select_seq_name = str(seq_name)
        self.listWidget__seq_info.clear() # 시퀀스가 여러개면 문제가 있을 텐디..
        self.listWidget__seq_info.addItem(self.select_seq_name)




    # missing frame 찾아주는 모듈
    def set_missing(self) -> list:
        path = pathlib.Path(self.dir)
        seq_list = path.glob('*.exr')
        comp = re.compile(r'\.(?P<frange>[0-9]{4})\.', re.DOTALL)

        file_frame_lst = list()
        filename_lst = list()

        for seq in seq_list:
            srch = comp.search(seq.name)
            file_frame_lst.append(int(srch.group('frange')))
            filename_lst.append(seq.name)

        seq_name = self.select_seq_name
        tmp = re.search(r'(\d+)-(\d+)', seq_name)
        f_num = int(tmp[1])
        l_num = int(tmp[2]) + 1

        norm_lst = list(range(f_num, l_num))

        mis_frame = set(norm_lst) ^ set(file_frame_lst)
        mis_frame_lst = [f'render.{frame}.exr' for frame in mis_frame]

        self.listWidget__missing.clear()
        return mis_frame_lst

    # 0byte 파일 찾아서 return
    def set_err(self) -> list:
        hpath = pathlib.Path(self.dir)
        files = hpath.glob('*.exr')
        err_lst = list()

        for file in files:
            file_size = os.stat(file.as_posix()).st_size
            if file_size == 0:
                err_lst.append(file.name)

        if len(err_lst) == 0:
            return ['0 Byte 파일이 없습니다.']
        else:
            return err_lst

    # 파일 오픈할 수 있도록
    def set_open_file(self):
        if self.open_file_key == True:
            path = QtWidgets.QFileDialog.getOpenFileName(
                self,
                'Open File',
                # '/data'
                self.lineEdit__work_filepath.text()
            )
        self.open_file_key = False


    def changed_info_item(self, idx: QtWidgets.QListWidgetItem):
        print(idx.text())
        self.label__seq_info.setText(f'선택 시퀀스 : {idx.text()}')

    def changed_missing_item(self, idx: QtWidgets.QListWidgetItem):
        print(idx.text())

    def changed_err_item(self, idx: QtWidgets.QListWidgetItem):
        print(idx.text())
        open_file = f'{self.dir}/{idx.text()}'
        self.lineEdit__work_filepath.setText(open_file)
        self.open_file_key = True

    def changed_seq_item(self, idx: QtWidgets.QListWidgetItem):
        print(idx.text())

    def set_preview(self):
        self.label__preview.setPixmap(QtGui.QPixmap('D:/netflix_ac/resource/gif_seq/musicTone_0000.png'))

        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    seq_mgr = SequenceManger()
    seq_mgr.show()
    sys.exit(app.exec_())
