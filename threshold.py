import numpy as np
import rasterio
import glob



marakez=glob.glob("/data/result_november/all_summer/result_with_shift/*")
print(marakez)
for m in marakez:
    tifs=sorted(glob.glob("{}/*.tiff".format(m)))
    heatmap=rasterio.open(tifs[0])
    pred=rasterio.open(tifs[1])
    threshold=tifs[2]
    meta_data=pred.meta
    print(meta_data)
    with rasterio.open(threshold,"w",**meta_data) as dst:
        heatmap=heatmap.read(1)
        pred=pred.read(1)
        print(pred.shape,"***")
        pred[heatmap<0.90]=255
        dst.nodata = 255
        print(dst.shape,"///")
        dst.write(pred.astype(np.uint16),indexes=1)
    print("done for :",m)    
    
    
