from django.shortcuts import render
from django.http import HttpResponse
import os
import pickle

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