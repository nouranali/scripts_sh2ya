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

# agri="/home/nouran.ali/Desktop/agri_res_nov_29/T36RVV_A036912_20220717T083855_urban_pred.tif"
# crops="/data/result_november/all_summer/all_summer_fix_shift_30_aug/L2A_T36RVV_A026931_20220915T084040_threshold4037.tiff"
# new="/home/nouran.ali/Desktop/agri_res_nov_29/masked_crops/"+crops.split("/")[-1].split(".tiff")[0] +"new.tiff"
# tmp=agri.split("/")[-1].split(".tif")[0] +"tmp.tiff"
# clip_raster_file(agri,crops,tmp)

# agri=rasterio.open(tmp)
# crops=rasterio.open(crops)

# meta_data=crops.meta
# print(meta_data)
# with rasterio.open(new,"w",**meta_data) as dst:
#     agri=agri.read(1)
#     crops=crops.read(1)
#     print(crops.shape,"***")
#     print(agri.shape)
#     print(new)
#     crops[agri==3]=255
#     dst.nodata = 255
#     print(dst.shape,"///")
#     dst.write(crops.astype(np.uint16),indexes=1)
# print("done ")    


agri=glob("/home/nouran.ali/Desktop/agri_res_nov_29/planet/*.tif")
crops=glob("/home/nouran.ali/summer_crops_results/planet_summer_results/25_august_0.95_threshold/*.tiff")
for c in crops:
    new="/home/nouran.ali/Desktop/output_planet_masked/"+c.split("/")[-1].split(".tiff")[0] +"new.tiff"
    for a in agri:
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
                    c[a2==3]=255
                    dst.nodata = 255
                    print(dst.shape,"///")
                    dst.write(c.astype(np.uint16),indexes=1)
                print("done ")
        except:
            continue        
