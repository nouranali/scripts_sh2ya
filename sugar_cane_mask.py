import numpy as np
import rasterio
from glob import glob
from osgeo import gdal

def clip_raster_file(input_file_name,clipping_file_name,output_file_name):
    options_list = [
                '-of GTiff',
            ]

    clipping_file=gdal.Open(clipping_file_name)
    xmin, xpixel, _, ymax, _, ypixel = clipping_file.GetGeoTransform()
    width, height = clipping_file.RasterXSize, clipping_file.RasterYSize
    xmax = xmin + width * xpixel
    ymin = ymax + height * ypixel
    output_file=gdal.Translate(output_file_name,input_file_name,projWin=[xmin, ymax, xmax, ymin])

 


winter_crops=glob("/home/nouran.ali/Desktop/winter_crops_res_nov_29/planet/*.tif")
summer_crops=glob("/home/nouran.ali/summer_summer_crops_results/planet_summer_results/25_august_0.95_threshold/*.tiff")
for c in summer_crops:
    new="/home/nouran.ali/Desktop/output_planet_masked/"+c.split("/")[-1].split(".tiff")[0] +"new.tiff"
    for a in winter_crops:
        tmp=a.split("/")[-1].split(".tif")[0] +"tmp.tiff"
        print(tmp)
        try:
            clip_raster_file(a,c,tmp)
            a2=rasterio.open(tmp)
            c=rasterio.open(c)
            if a2.shape==c.shape:
                meta_data=c.meta
                print(meta_data)
                with rasterio.open(new,"w",**meta_data) as dst:
                    a2=a2.read(1)
                    c=c.read(1)
                    print(c.shape,"***")
                    print(a2.shape)
                    print(new)
                    c[a2==4]=255
                    dst.nodسata = 255
                    print(dst.shape,"///")
                    dst.write(c.astype(np.uint16),indexes=1)
                print("done ")
        except:
            continue        
