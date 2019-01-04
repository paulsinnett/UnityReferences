# make a database of all Unity meta files and find files that aren't used

import os, yaml

def list_meta_files(directory):
	files = []
	for name in os.listdir(directory):
		path = os.path.join(directory, name)
		if (os.path.isdir(path)):
			files.extend(list_meta_files(path))
		else:
			base, ext = os.path.splitext(path)
			if (ext == '.meta' and not os.path.isdir(base)):
				files.append(path)
	return files

metas = list_meta_files('Assets')
for meta in metas:
	guid = yaml.load(open(meta, 'r'))['guid']
	print('{} {}'.format(guid, meta))
