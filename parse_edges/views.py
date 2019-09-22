from django.shortcuts import render
from django.http import HttpResponse
import os
import pickle

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
		

	