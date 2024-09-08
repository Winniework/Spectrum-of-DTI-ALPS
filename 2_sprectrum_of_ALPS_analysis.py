import os
import nibabel as nib
import numpy as np
import csv
from PIL import Image, ImageDraw
import sys

def load_and_pad(in_file):
    nifti_img = nib.load(in_file)
    data = nifti_img.get_data()
    return data


def find_max_mean(matrix,xa_list,xp_list,y_list,z_list):
    top_means=[]
    for z in z_list:
        for y in y_list:
            max_meang = 0
            max_meanb = 0
            for xa in xa_list:
                positions = []
                for i in range(xa-3, xa+4):
                    for j in range(y-3, y+4):
                        if (i-xa)**2 + (j-y)**2 <= 2.5**2:
                            positions.append((i,j,z))
                valuesg = [matrix[i][j][z][1] for i,j,z in positions]
                valuesra = [matrix[i][j][z][0] for i,j,z in positions]
                valuesba = [matrix[i][j][z][2] for i,j,z in positions]
                meang = np.mean(valuesg)-np.mean(valuesra)  
                for xp in xp_list:
                    positions = []
                    for i in range(xp-3, xp+4):
                        for j in range(y-3, y+4):
                            if (i-xp)**2 + (j-y)**2 <= 2.5**2:
                                positions.append((i,j,z))
                    valuesb = [matrix[i][j][z][2] for i,j,z in positions]
                    valuesrp = [matrix[i][j][z][0] for i,j,z in positions]
                    valuesgp = [matrix[i][j][z][1] for i,j,z in positions]
                    meanb = np.mean(valuesb)-np.mean(valuesrp)
                    top_means.append((meang+meanb, (xa,y,z),(xp,y,z)))
    top_means = sorted(top_means, key=lambda x: x[0], reverse=True)[:1000]
    return top_means

def calculate_circle_mean(a_position,img):
    positions = []
    data = nib.load(img).get_data()
    for i in range(a_position[0]-3, a_position[0]+4):
        for j in range(a_position[1]-3, a_position[1]+4):
            if (i-a_position[0])**2 + (j-a_position[1])**2 <= 5**2:
                positions.append((i,j))
    values = [data[i][j][a_position[2]] for i,j in positions]
    circle_mean = np.mean(values)          
    return circle_mean

xa_l_list = range(120, 136)
xp_l_list = range(108, 124)
xa_r_list = range(42, 58)
xp_r_list = range(54, 70)
y_list = range(99,114)
z_list = range(95,105)

dir_name = './ALPS/'
l_max_mean=0
r_max_mean=0
path_colormap = dir_name + 'DTI_reoriented_ColorMap.nii.gz'

data = load_and_pad(path_colormap)
top_means_l = find_max_mean(data,xa_l_list,xp_l_list,y_list,z_list)
top_means_r = find_max_mean(data,xa_r_list,xp_r_list,y_list,z_list)

path_Dxx = dir_name + 'dti_reoriented_Dxx.nii.gz'
path_Dyy = dir_name + 'dti_reoriented_Dyy.nii.gz'
path_Dzz = dir_name + 'dti_reoriented_Dzz.nii.gz'

for idx, (mean,a_position,p_position) in enumerate(top_means_l):
    dxx_a=calculate_circle_mean(a_position,path_Dxx)
    dxx_p=calculate_circle_mean(p_position,path_Dxx)
    dyy_a=calculate_circle_mean(a_position,path_Dyy)
    dyy_p=calculate_circle_mean(p_position,path_Dyy)            
    dzz_a=calculate_circle_mean(a_position,path_Dzz)
    dzz_p=calculate_circle_mean(p_position,path_Dzz)
    alps=(dxx_a+dxx_p)/(dyy_p+dzz_a)
    with open(dir_name + 'alps_l.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([idx,a_position,p_position,dxx_a,dxx_p,dyy_a,dyy_p,dzz_a,dzz_p,alps])  

for idx, (mean,a_position,p_position) in enumerate(top_means_r):
    dxx_a=calculate_circle_mean(a_position,path_Dxx)
    dxx_p=calculate_circle_mean(p_position,path_Dxx)
    dyy_a=calculate_circle_mean(a_position,path_Dyy)
    dyy_p=calculate_circle_mean(p_position,path_Dyy)            
    dzz_a=calculate_circle_mean(a_position,path_Dzz)
    dzz_p=calculate_circle_mean(p_position,path_Dzz)
    alps=(dxx_a+dxx_p)/(dyy_p+dzz_a)
    with open(dir_name + 'alps_r.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([idx,a_position,p_position,dxx_a,dxx_p,dyy_a,dyy_p,dzz_a,dzz_p,alps])                  