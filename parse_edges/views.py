from django.shortcuts import render
import os

def trim_left(request, img_index):

	
	SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
	img_files_path = 'static\\\\parse_edges\\\\00_original_book_pics'
	img_list = next(os.walk(os.path.join(SITE_ROOT, img_files_path)))[2][:5]
	img_list = ['\\\\' + img_files_path + '\\\\' + x for x in img_list]

	# Current image file name
	current_img = img_list[img_index]
	
	# Next image url
	if img_index < len(img_list):
		next_img_index = img_index + 1
	else:
		next_img_index = None


	context = {
		'img_list': img_list,
		'current_img': current_img,
		'next_img_n': next_img_index,
	}

	return render(request, 'parse_edges/parse_left.html', context)

	