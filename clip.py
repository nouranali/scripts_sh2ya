import glob
import rasterio
import os
from tqdm import tqdm
from osgeo import gdal
input_folder = "/mnt/storage/crops/summer_crops/original_data_summer/Quena"
output_folder = "/home/nouran.ali/Desktop/clipped_summer/quena/"

# folders = glob.glob(input_folder + "/*.tif*")



# for folder in tqdm(folders):
#     folde_name = os.path.basename(folder)
#     files = glob.glob(folder + "/*.jp2")

#     os.makedirs(output_folder+ folde_name,exist_ok=True)

# for _file in tqdm(folders):
#     file_name = os.path.basename(_file)
#     with rasterio.open(_file) as s2_data:
#         img = s2_data.read()
#         meta = s2_data.meta
#     print(img.shape,"++++")
#     img = img[:,0:500,0:500]
#     print(img.shape)
#     meta.update({
#     "width":img.shape[1],
#     "height":img.shape[2],
#     })

#     out_file_path = output_folder + "/"+file_name
#     with rasterio.open(out_file_path,'w',**meta) as dst:
#         dst.write(img)

# folders = glob.glob(input_folder + "/*L2A*")

# options_list = [
#             '-of JPEG2000',
#         ]

# options_string = " ".join(options_list)

input_file_name="/home/nouran.ali/Desktop/quena/quena.tif"


clipping_file=gdal.Open(input_file_name)

# input_tif=gdal.Open(input_file_name)
# xmin, xpixel, _, ymax, _, ypixel = clipping_file.GetGeoTransform()
# width, height = clipping_file.RasterXSize, clipping_file.RasterYSize
# xmax = xmin + width * xpixel
# ymin = ymax + height * ypixel
# print("xmin, ymin, xmax, ymax ",xmin, ymin, xmax, ymax)
# output_file=gdal.Translate(output_file_name,input_file_name,projWin=[xmin, ymax, xmax, ymin])



#################################

folders = glob.glob(input_folder + "/*L2A*")

for folder in tqdm(folders):
    tiff = os.path.basename(folder)
    files = glob.glob(folder + "/*.jp2")
    print(files)
    out_folder_path=output_folder+ folder.split("/")[-1]
    os.makedirs(out_folder_path,exist_ok=True)
    
    for _file in tqdm(files):
        file_name = os.path.basename(_file)
        input_tif=gdal.Open(_file)
        xmin, xpixel, _, ymax, _, ypixel = clipping_file.GetGeoTransform()
        width, height = clipping_file.RasterXSize, clipping_file.RasterYSize
        xmax = xmin + width * xpixel
        ymin = ymax + height * ypixel
        print("xmin, ymin, xmax, ymax ",xmin, ymin, xmax, ymax)
        out_file_path = out_folder_path +"/" +file_name 
        output_file=gdal.Translate(out_file_path,input_tif,projWin=[xmin, ymax, xmax, ymin])

        
 
