import re
import pyseq
import shutil
import pathlib

# dirpath = pathlib.Path('/data/workspace/python/copy_files/seqeunce_data')
dirpath = pathlib.Path('D:/netflix_ac/resource/render_seq')

print(dirpath)

res = dirpath.glob('*.exr')
print(res)

comp = re.compile(r'\.(?P<frange>[0-9]{4})\.', re.DOTALL)
file_frame_lst = list()
filename_lst = list()
for i in res:
    srch = comp.search(i.name)
    file_frame_lst.append(int(srch.group('frange')))
    filename_lst.append(i.name)

print(filename_lst)
lst = list(range(1001, 1151))


frame_info = set(lst) ^ set(file_frame_lst)
# print(list(frame_info))


# test - file copy
#shutil.copy2(
#    '/home/rapa/aaa.py', '/home/rapa/qqq.py')

s = pyseq.Sequence(filename_lst)
print(frame_info)