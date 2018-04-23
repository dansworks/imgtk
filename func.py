"""
currently call file in terminal to get thumb nail and websize
resize of high-res images in img_in folder.
Handels multiple images.

python func.py 

s
PIL.ImageOps.grayscale(image) 

"""
import os, sys
from PIL import Image, ImageEnhance,ImageOps
import numpy as np
import matplotlib.pyplot as plt


def verify_img(img_filename):
	#make sure the file is a valid image. 	
	result = 0
	try:
		im=Image.open(img_filename)
		im.verify()
		# print("valid image")
		result = 1
	except Exception as e:
		print(e)
		print("exception was raised. Invalid image file.")
		result = 0

	return result


def resize(img_thumb = 200, web_img = 550):
	"""
	Takes all images from a folder or imgs in list
	crops them down to websize and thumbnail size.
	"""
	basewidth_thumb_nail = img_thumb
	basewidth_website_ = web_img
	#grab all file names in img_out folder
	path_out = 'img_out/'
	path_in = 'img_in/' 
	files = os.listdir(path_in)
	#right now only grabs .jpg files. All other files ignored.
	imgs = [i for i in files if i.endswith('.jpg')]
	# print(imgs)

	for i in imgs:
		#first call veryify_img to make sure the the file is valid image.
		if verify_img(path_in+i) == 1:
			img = Image.open(path_in+i)
			wpercent_th = (basewidth_thumb_nail/float(img.size[0]))
			hsize_th = int((float(img.size[1])*float(wpercent_th)))
			img = img.resize((basewidth_thumb_nail,hsize_th), Image.ANTIALIAS)
			img.save(path_out+'th-'+i)
			wpercent_web = (basewidth_thumb_nail/float(img.size[0]))
			hsize_web = int((float(img.size[1])*float(wpercent_web)))
			img_web = img.resize((basewidth_thumb_nail,hsize_web), Image.ANTIALIAS)
			img_web.save(path_out+'web-'+i)

		else:
			print("Invalid image skipped.")
			

print(resize(350, 700))




