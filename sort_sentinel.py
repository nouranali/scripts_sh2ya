from datetime import datetime
from glob import glob
import shutil
from shutil import copy2
from distutils.dir_util import copy_tree

govs=glob("/mnt/storage/crops/winter_2022/All_winter/*")
for g in govs:
    marakez=glob(f"{g}/*")
    # for m in marakez:
    m=g
    t=m.split("/")[-1]
    
    all_folders_names=glob(f"{m}/*")
    print(all_folders_names)
    all_folders_names.sort(key=lambda name: datetime.strptime(name.split("/")[-1].split("_")[-1],
                                                    "%Y-%m-%d"), reverse=False)

    print(all_folders_names[len(all_folders_names)//2])
    d=all_folders_names[len(all_folders_names)//2].split("/")[-1]
    # print(all_folders_names[len(all_folders_names)//2],f"/home/nouran.ali/Desktop/sentinel_winter_tiles/{t}")
    shutil.copytree(all_folders_names[len(all_folders_names)//2],f"/home/nouran.ali/Desktop/sentinel_winter_tiles/{t}/{d}",dirs_exist_ok=True)


