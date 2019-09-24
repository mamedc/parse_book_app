from django.shortcuts import render
from django.http import HttpResponse
import os
import pickle
import cv2
import numpy as np

from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import re

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
static_path = SITE_ROOT + '\\static\\parse_edges\\'

img_disp_width = 1000
img_disp_height = 1333.333333


def get_img_list(img_files_path):
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	return img_list


def open_update_save_dict(static_path, img_list, img_index, trim_dict_):
	# If existing dict
	if os.path.isfile(static_path + 'trim_dict.pkl'):
		
		# Open
		with open(static_path + 'trim_dict.pkl', 'rb') as f: 
			trim_dict = pickle.load(f)
		
		# Update
		if img_list[img_index] in trim_dict.keys():
			trim_dict[img_list[img_index]].update(trim_dict_)
		else:
			trim_dict[img_list[img_index]] = trim_dict_
		
		# Save
		with open(static_path + 'trim_dict.pkl', 'wb') as f:
			pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)

	# If not existing dict
	else:
		# Create dict
		trim_dict = {img_list[img_index]: trim_dict_}
		# Save
		with open(static_path + 'trim_dict.pkl', 'wb') as f:
			pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)



def parse_ctrl(request):

	# Load list of files to trim
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	total_images_len = len(img_list)

	# Load 'trim_dict'
	static_path = SITE_ROOT + '\\static\\parse_edges\\'
	# If existing dict
	if os.path.isfile(static_path + 'trim_dict.pkl'):
		# Open
		with open(static_path + 'trim_dict.pkl', 'rb') as f: 
			trim_dict = pickle.load(f)
	else:
		# Dict does not exist
		trim_dict = {}

	##### Check what is missing #####

	# Left edge
	if True:
		left_edge_imgs = []
		if len(trim_dict.keys()) > 0:
			for img in trim_dict.keys():
				if 'left_edge' in trim_dict[img].keys():
					left_edge_imgs.append(img)
			left_edge_missing = list(set(img_list) - set(left_edge_imgs))
		else:
			left_edge_missing = img_list
		left_edge_missing_len = len(left_edge_missing)
		left_edge_done_len = total_images_len - left_edge_missing_len

	# Right edge
	if True:
		right_edge_imgs = []
		if len(trim_dict.keys()) > 0:
			for img in trim_dict.keys():
				if 'right_edge' in trim_dict[img].keys():
					right_edge_imgs.append(img)
			right_edge_missing = list(set(img_list) - set(right_edge_imgs))
		else:
			right_edge_missing = img_list
		right_edge_missing_len = len(right_edge_missing)
		right_edge_done_len = total_images_len - right_edge_missing_len

	# Top edge
	if True:
		top_edge_imgs = []
		if len(trim_dict.keys()) > 0:
			for img in trim_dict.keys():
				if 'top_edge' in trim_dict[img].keys():
					top_edge_imgs.append(img)
			top_edge_missing = list(set(img_list) - set(top_edge_imgs))
		else:
			top_edge_missing = img_list
		top_edge_missing_len = len(top_edge_missing)
		top_edge_done_len = total_images_len - top_edge_missing_len

	# Bottom edge
	if True:
		bottom_edge_imgs = []
		if len(trim_dict.keys()) > 0:
			for img in trim_dict.keys():
				if 'bottom_edge' in trim_dict[img].keys():
					bottom_edge_imgs.append(img)
			bottom_edge_missing = list(set(img_list) - set(bottom_edge_imgs))
		else:
			bottom_edge_missing = img_list
		bottom_edge_missing_len = len(bottom_edge_missing)
		bottom_edge_done_len = total_images_len - bottom_edge_missing_len

	# Header edge
	if True:
		header_imgs = []
		if len(trim_dict.keys()) > 0:
			for img in trim_dict.keys():
				if 'header' in trim_dict[img].keys():
					header_imgs.append(img)
			header_missing = list(set(img_list) - set(header_imgs))
		else:
			header_missing = img_list
		header_missing_len = len(header_missing)
		header_done_len = total_images_len - header_missing_len

	# Footer edge
	if True:
		footer_imgs = []
		if len(trim_dict.keys()) > 0:
			for img in trim_dict.keys():
				if 'footer' in trim_dict[img].keys():
					footer_imgs.append(img)
			footer_missing = list(set(img_list) - set(footer_imgs))
		else:
			footer_missing = img_list
		footer_missing_len = len(footer_missing)
		footer_done_len = total_images_len - footer_missing_len

	# Vertical split
	if True:
		splt_vert_imgs = []
		if len(trim_dict.keys()) > 0:
			for img in trim_dict.keys():
				if 'split_vertical' in trim_dict[img].keys():
					splt_vert_imgs.append(img)
			splt_vert_missing = list(set(img_list) - set(splt_vert_imgs))
		else:
			splt_vert_missing = img_list
		splt_vert_missing_len = len(splt_vert_missing)
		splt_vert_done_len = total_images_len - splt_vert_missing_len

	# Trim recipes
	if True:
		trim_recipes_imgs = []
		if len(trim_dict.keys()) > 0:
			for img in trim_dict.keys():
				if 'trim_recipes' in trim_dict[img].keys():
					trim_recipes_imgs.append(img)
			trim_recipes_missing = list(set(img_list) - set(trim_recipes_imgs))
		else:
			trim_recipes_missing = img_list
		trim_recipes_missing_len = len(trim_recipes_missing)
		trim_recipes_done_len = total_images_len - trim_recipes_missing_len


	context = {
		'total_images_len': total_images_len,
		
		'left_edge_missing': left_edge_missing,
		'left_edge_missing_len': left_edge_missing_len,
		'left_edge_done_len': left_edge_done_len,

		'right_edge_missing': right_edge_missing,
		'right_edge_missing_len': right_edge_missing_len,
		'right_edge_done_len': right_edge_done_len,

		'top_edge_missing': top_edge_missing,
		'top_edge_missing_len': top_edge_missing_len,
		'top_edge_done_len': top_edge_done_len,

		'bottom_edge_missing': bottom_edge_missing,
		'bottom_edge_missing_len': bottom_edge_missing_len,
		'bottom_edge_done_len': bottom_edge_done_len,

		'header_missing': header_missing,
		'header_missing_len': header_missing_len,
		'header_done_len': header_done_len,

		'footer_missing': footer_missing,
		'footer_missing_len': footer_missing_len,
		'footer_done_len': footer_done_len,

		'splt_vert_missing': splt_vert_missing,
		'splt_vert_missing_len': splt_vert_missing_len,
		'splt_vert_done_len': splt_vert_done_len,

		'trim_recipes_missing': trim_recipes_missing,
		'trim_recipes_missing_len': trim_recipes_missing_len,
		'trim_recipes_done_len': trim_recipes_done_len,

	}
	
	return render(request, 'parse_edges/parse_ctrl.html', context)


def trim_left(request, img_index):

	# List of files to trim
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	
	# POST
	if request.method == 'POST':

		static_path = SITE_ROOT + '\\static\\parse_edges\\'
		trim_dict_ = {'left_edge': int(request.POST.get('x_trim_coord'))}

		# If existing dict
		if os.path.isfile(static_path + 'trim_dict.pkl'):
			# Open
			with open(static_path + 'trim_dict.pkl', 'rb') as f: 
				trim_dict = pickle.load(f)
			# Update
			if img_list[img_index] in trim_dict.keys():
				trim_dict[img_list[img_index]].update(trim_dict_)
			else:
				trim_dict[img_list[img_index]] = trim_dict_
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)

		# If not existing dict
		else:
			# Create dict
			trim_dict = {img_list[img_index]: trim_dict_}
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)


		# Go to next image
		img_index += 1
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_left.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
	
	# GET
	else:
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_left.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
	

def trim_right(request, img_index):

	# List of files to trim
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	
	# POST
	if request.method == 'POST':

		static_path = SITE_ROOT + '\\static\\parse_edges\\'
		trim_dict_ = {'right_edge': int(request.POST.get('x_trim_coord'))}

		# If existing dict
		if os.path.isfile(static_path + 'trim_dict.pkl'):
			# Open
			with open(static_path + 'trim_dict.pkl', 'rb') as f: 
				trim_dict = pickle.load(f)
			# Update
			if img_list[img_index] in trim_dict.keys():
				trim_dict[img_list[img_index]].update(trim_dict_)
			else:
				trim_dict[img_list[img_index]] = trim_dict_
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)

		# If not existing dict
		else:
			# Create dict
			trim_dict = {img_list[img_index]: trim_dict_}
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)


		# Go to next image
		img_index += 1
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_right.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
	
	# GET
	else:
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_right.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)


def trim_top(request, img_index):

	# List of files to trim
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	
	# POST
	if request.method == 'POST':

		static_path = SITE_ROOT + '\\static\\parse_edges\\'
		trim_dict_ = {'top_edge': int(request.POST.get('y_trim_coord'))}

		# If existing dict
		if os.path.isfile(static_path + 'trim_dict.pkl'):
			# Open
			with open(static_path + 'trim_dict.pkl', 'rb') as f: 
				trim_dict = pickle.load(f)
			# Update
			if img_list[img_index] in trim_dict.keys():
				trim_dict[img_list[img_index]].update(trim_dict_)
			else:
				trim_dict[img_list[img_index]] = trim_dict_
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)

		# If not existing dict
		else:
			# Create dict
			trim_dict = {img_list[img_index]: trim_dict_}
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)


		# Go to next image
		img_index += 1
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_top.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
	
	# GET
	else:
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_top.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
		

def trim_bottom(request, img_index):

	# List of files to trim
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	
	# POST
	if request.method == 'POST':

		static_path = SITE_ROOT + '\\static\\parse_edges\\'
		trim_dict_ = {'bottom_edge': int(request.POST.get('y_trim_coord'))}

		# If existing dict
		if os.path.isfile(static_path + 'trim_dict.pkl'):
			# Open
			with open(static_path + 'trim_dict.pkl', 'rb') as f: 
				trim_dict = pickle.load(f)
			# Update
			if img_list[img_index] in trim_dict.keys():
				trim_dict[img_list[img_index]].update(trim_dict_)
			else:
				trim_dict[img_list[img_index]] = trim_dict_
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)

		# If not existing dict
		else:
			# Create dict
			trim_dict = {img_list[img_index]: trim_dict_}
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)


		# Go to next image
		img_index += 1
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_bottom.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
	
	# GET
	else:
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_bottom.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
		

def trim_header(request, img_index):

	# List of files to trim
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	
	# POST
	if request.method == 'POST':

		static_path = SITE_ROOT + '\\static\\parse_edges\\'
		trim_dict_ = {'header': int(request.POST.get('y_trim_coord'))}

		# If existing dict
		if os.path.isfile(static_path + 'trim_dict.pkl'):
			# Open
			with open(static_path + 'trim_dict.pkl', 'rb') as f: 
				trim_dict = pickle.load(f)
			# Update
			if img_list[img_index] in trim_dict.keys():
				trim_dict[img_list[img_index]].update(trim_dict_)
			else:
				trim_dict[img_list[img_index]] = trim_dict_
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)

		# If not existing dict
		else:
			# Create dict
			trim_dict = {img_list[img_index]: trim_dict_}
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)


		# Go to next image
		img_index += 1
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_header.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
	
	# GET
	else:
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_header.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)


def trim_footer(request, img_index):

	# List of files to trim
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	
	# POST
	if request.method == 'POST':

		static_path = SITE_ROOT + '\\static\\parse_edges\\'
		trim_dict_ = {'footer': int(request.POST.get('y_trim_coord'))}

		# If existing dict
		if os.path.isfile(static_path + 'trim_dict.pkl'):
			# Open
			with open(static_path + 'trim_dict.pkl', 'rb') as f: 
				trim_dict = pickle.load(f)
			# Update
			if img_list[img_index] in trim_dict.keys():
				trim_dict[img_list[img_index]].update(trim_dict_)
			else:
				trim_dict[img_list[img_index]] = trim_dict_
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)

		# If not existing dict
		else:
			# Create dict
			trim_dict = {img_list[img_index]: trim_dict_}
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)


		# Go to next image
		img_index += 1
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_footer.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
	
	# GET
	else:
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/parse_footer.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)


def split_recipe_vertical(request, img_index):

	# List of files to trim
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	
	# POST
	if request.method == 'POST':

		static_path = SITE_ROOT + '\\static\\parse_edges\\'
		trim_dict_ = {'split_vertical': [
			int(request.POST.get('x_split_coord_1')), 
			int(request.POST.get('x_split_coord_2')), 
			request.POST.get('rec_side'), 
		]}

		# If existing dict
		if os.path.isfile(static_path + 'trim_dict.pkl'):
			# Open
			with open(static_path + 'trim_dict.pkl', 'rb') as f: 
				trim_dict = pickle.load(f)
			# Update
			if img_list[img_index] in trim_dict.keys():
				trim_dict[img_list[img_index]].update(trim_dict_)
			else:
				trim_dict[img_list[img_index]] = trim_dict_
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)

		# If not existing dict
		else:
			# Create dict
			trim_dict = {img_list[img_index]: trim_dict_}
			# Save
			with open(static_path + 'trim_dict.pkl', 'wb') as f:
				pickle.dump(trim_dict, f, pickle.HIGHEST_PROTOCOL)


		# Go to next image
		img_index += 1
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/split_vertical.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)
	
	# GET
	else:
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, 'parse_edges/split_vertical.html', context)
		
		else:
			html = "<html><body>End of images.</body></html>"
			return HttpResponse(html)


def trim_recipes(request, img_index):

	dict_key_name = 'trim_recipes'
	html_to_render = 'parse_edges/trim_recipes.html'

	# List of files to trim
	img_list = get_img_list(img_files_path)
	
	# POST
	if request.method == 'POST':

		# Extract form fields with y coords (we need the loop because we
		# dont know how many recipes we will have)
		y_coords = []
		for y_key in [k for k in request.POST.keys() if k[:6] == 'y_trim']:
			y_coords.append(int(request.POST.get(y_key)))

		trim_dict_ = {dict_key_name: y_coords}
		open_update_save_dict(static_path, img_list, img_index, trim_dict_)

		# Go to next image
		img_index += 1
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, html_to_render, context)
		
		else:
			return HttpResponse('<html><body>End of images.</body></html>')
	
	# GET
	else:
		if img_index < len(img_list):
			context = {
				'img_list_len': len(img_list),
				'img_index': img_index,
				'current_img_file': img_list[img_index],
				'current_img_path': '\\\\' + img_files_path + '\\\\' + img_list[img_index],
				'img_number': img_index + 1,
			}
			return render(request, html_to_render, context)
		
		else:
			return HttpResponse('<html><body>End of images.</body></html>')


def read_procedures(request, img_index):

	# List of files to trim
	img_list = get_img_list(img_files_path)
	
	if img_index < len(img_list):
		
		# Open img
		raw_img = cv2.imread(SITE_ROOT + '\\' + img_files_path + '\\' + img_list[img_index])
		img = raw_img.copy()

		# Load dict with trim infos
		with open(static_path + 'trim_dict.pkl', 'rb') as f: 
			trim_dict = pickle.load(f)
		dict_ = trim_dict[img_list[img_index]]

		# Correct for different dimentions
		x_prop = img.shape[1] / img_disp_width
		y_prop = img.shape[0] / img_disp_height

		# Get cuts
		left_edge = int(dict_['left_edge'] * x_prop)
		right_edge = int(dict_['right_edge'] * x_prop)
		top_edge = int(dict_['top_edge'] * y_prop)
		bottom_edge = int(dict_['bottom_edge'] * y_prop)
		header = int(dict_['header'] * y_prop)
		footer = int(dict_['footer'] * y_prop)
		split_vert_left = int(min(dict_['split_vertical'][:2]) * x_prop)
		split_vert_right = int(max(dict_['split_vertical'][:2]) * x_prop)
		procedure_side = dict_['split_vertical'][2]
		recipe_cuts = [int(x) for x in np.array(sorted(dict_['trim_recipes'])) * y_prop]
		recipe_cuts = recipe_cuts + [footer]

		header_img = img[top_edge : header, left_edge : right_edge]
		footer_img = img[footer : bottom_edge, left_edge : right_edge]

		# For each recipe
		for i in range(len(recipe_cuts)-1):
			if procedure_side == 'left':
				proc_img = img[recipe_cuts[i]:recipe_cuts[i+1], left_edge:split_vert_left]
				ingr_img = img[recipe_cuts[i]:recipe_cuts[i+1], split_vert_right:right_edge]
			else:
				proc_img = img[recipe_cuts[i]:recipe_cuts[i+1], split_vert_right:right_edge]
				ingr_img = img[recipe_cuts[i]:recipe_cuts[i+1], left_edge:split_vert_left]

		# Apply OCR
		gray = cv2.cvtColor(proc_img, cv2.COLOR_BGR2GRAY)
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		gray = cv2.medianBlur(gray, 3)
		temp_img = project_fld + input_fld + '\\' + 'temp_img.jpg'
		cv2.imwrite(temp_img, gray)
		text = pytesseract.image_to_string(Image.open(temp_img))
	    
		with open(temp_img, 'rb') as f: procedure_img = f.read()   
		os.remove(temp_img)




		temp_path = SITE_ROOT + '\\' + img_files_path + '\\'
		temp_proc_img = temp_path + 'temp_proc_img.jpg'
		temp_ingr_img = temp_path + 'temp_ingr_img.jpg'
		cv2.imwrite(temp_proc_img, proc_img)
		cv2.imwrite(temp_ingr_img, ingr_img)


		assert False, dict_

		

		html = "<html><body>End of images.</body></html>"
		return HttpResponse(html)

	else:

		html = "<html><body>End of images.</body></html>"
		return HttpResponse(html)


