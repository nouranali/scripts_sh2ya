from datetime import datetime
from glob import glob
import shutil
from shutil import copy2
from distutils.dir_util import copy_tree

govs=glob("/home/nouran.ali/im/scratch/agri/crops_planet/data_summer_2022/*")
for g in govs:
    marakez=glob(f"{g}/*")
    for m in marakez:
        t=m.split("/")[-1]
        
        all_folders_names=glob(f"{m}/files/*")
        print(all_folders_names)
        all_folders_names.sort(key=lambda name: datetime.strptime(name.split("/")[-1],
                                                      "%Y%m%d"), reverse=False)

        print(all_folders_names[len(all_folders_names)//2])
        d=all_folders_names[len(all_folders_names)//2].split("/")[-1]
        shutil.copytree(all_folders_names[len(all_folders_names)//2],f"/data/planet_tiles/{t}/files/{d}")


