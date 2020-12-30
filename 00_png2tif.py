# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:19:20 2020

@author: janak
"""

import glob
import os
import pdb
import rasterio
import numpy as np
import sys

#Create empty dictionaries for storing transform and crs
transform_dict={}
crs_dict={}

in_folder='./data'

#store the transform and crs of all the tiles from image folder: FTiff_DEM
for image in glob.glob('E:\THESIS\FTiff_DEM/*.tif'):
# for image in glob.glob(in_folder+'/FTiff_DEM/*.tif'):
    img=rasterio.open(image)
    tile_name=image.split('_DEM\\')[1].split('_')[0][:6]
    transform_dict[tile_name]=img.transform
    crs_dict[tile_name]=img.crs
    print('The tile {} has transform\n {} \nand crs {}'.format(tile_name, transform_dict[tile_name], crs_dict[tile_name]))

#Access the folder
for folder in os.listdir('Outputs_4m_Server'):
    if not os.path.isdir(folder):
        for png in glob.glob('Outputs_4m_Server/'+folder+'/*.png'):
            if 'tst_conf_mat.png' not in png and 'tra_tst_Acc.png' not in png and 'tra_tst_Loss.png' not in png:
                tile_name=png.split('\\')[1].split('_')[0][:6]
                print(tile_name)
                #Read the PNG image
                png_image=rasterio.open(png).read().astype('uint8')
                #Separately operate whether the PNG is RGB, ground truth of Predicted map
                if '_rgb.png' in png:
                    # print('{}: RGB image'.format(png))
                        if not os.path.isfile('Outputs_4m_Server/'+folder+'/{}_rgb.tif'.format(tile_name)):
                            # os.remove('{}_gt_map.tif'.format(tile_name))
                            print('--Preparing the geotiff of RGB map: {}'.format(tile_name))
                            # png_image=np.moveaxis(png_image,-1,0)
                            png_image=png_image.squeeze()
                            with rasterio.open('Outputs_4m_Server/'+folder+'/{}_rgb.tif'.format(tile_name),'w',driver='GTiff',height=png_image.shape[1],width=png_image.shape[2],count=3,dtype=png_image.dtype,crs=crs_dict[tile_name],transform=transform_dict[tile_name],) as dst:
                                dst.write(png_image) 
                                print('Geotiff of RGB map {} is prepared'.format(tile_name))
                                print('***********--------------***********--------------')
                        else:
                            print('Geotiff of RGB map {} already exists'.format(tile_name))
                            print('***********--------------***********--------------')

                else:
                    if '_gt_map.png' in png:
                        if not os.path.isfile('Outputs_4m_Server/'+folder+'/{}_gt_map.tif'.format(tile_name)):
                            # os.remove('{}_gt_map.tif'.format(tile_name))
                            print('--Preparing the geotiff of ground truth map: {}'.format(tile_name))
                            # png_image=np.moveaxis(png_image,-1,0)
                            png_image=png_image.squeeze()
                            with rasterio.open('Outputs_4m_Server/'+folder+'/{}_gt_map.tif'.format(tile_name),'w',driver='GTiff',height=png_image.shape[1],width=png_image.shape[2],count=3,dtype=png_image.dtype,crs=crs_dict[tile_name],transform=transform_dict[tile_name],) as dst:
                                dst.write(png_image) 
                                print('Geotiff of Ground truth map {} is prepared'.format(tile_name))
                                print('***********--------------***********--------------')
                        else:
                            print('Geotiff of Ground truth map {} already exists'.format(tile_name))
                            print('***********--------------***********--------------')
                            
                    elif '_pred_map.png' in png:
                        if not os.path.isfile('Outputs_4m_Server/'+folder+'/{}_pred_map.tif'.format(tile_name)):
                            # os.remove('{}_gt_map.tif'.format(tile_name))
                            print('--Preparing the geotiff of predicted map: {}'.format(tile_name))
                            # png_image=np.moveaxis(png_image,-1,0)
                            png_image=png_image.squeeze()
                            with rasterio.open('Outputs_4m_Server/'+folder+'/{}_pred_map.tif'.format(tile_name),'w',driver='GTiff',height=png_image.shape[1],width=png_image.shape[2],count=3,dtype=png_image.dtype,crs=crs_dict[tile_name],transform=transform_dict[tile_name],) as dst:
                                dst.write(png_image) 
                                print('Geotiff of Predicted map {} is prepared'.format(tile_name))
                                print('***********--------------***********--------------')
                        else:
                            print('Geotiff of Predicted map {} already exists'.format(tile_name))
                            print('***********--------------***********--------------')
                        
                   





