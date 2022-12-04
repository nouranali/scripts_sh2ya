from glob import glob
import shutil

tmps=glob("/home/nouran.ali/im/home/nouran.ali/tmp/*")
i=0
for tmp in tmps:
    try:
        tif=glob(tmp+"/temp/agri_mask/*pred*.tif")[0]
        print(i)
        # print(tif.split("/")[-1].split(".tif")[0])
        tif2="/home/nouran.ali/Desktop/output_planet_masked/test/"+tif.split("/")[-1].split(".tif")[0]+str(i)+".tif"
        print(tif2)
        shutil.copy(tif,tif2)
        i+=1
    except:
        continue