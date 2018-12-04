#!/usr/bin/python
#_*_coding:UTF-8 _*_

import os
import fnmatch

def is_file_match(filename,patterns):
	for pattern in patterns:
		if fnmatch.fnmatch(filename,pattern):
			return True
		return False
def find_specific_files(root,patterns=['*'],exclude_dirs=[]):
	for root,dirnames,filenames in os.walk(root):
		for filename in filenames:
			if is_file_match(filename,patterns):
				yield os.path.join(root,filename)
	for d in exclude_dirs:
		if d in dirnames:
			dirnames.remove(d)
if __name__ =='__main__':
#search the dir all file
	'''for item in find_specific_files('.'):
		print(item)'''
#search the dir all picture
'''patterns =['*.jpg','*.jpeg','*.png','*.tif']
for item in find_specific_files('.',patterns):
	print(item)'''
#search the dir all file except dir2
'''patterns =['*.jpg','*.jpeg','*.png','*.tif']
exclude_dirs =['dir2']
for item in find_specific_files('.',patterns,exclude_dirs):
        print(item)'''
#search  The 10 largest files in the directory
for name in find_specific_files('.'):
	files={name: os.path.getsize(name)}
	#print(files.items())
result =sorted(files.items(),key=lambda d:d[1],reverse=True)[:10]
#print(result) 
for i,t in enumerate(result,1):
	print(i,t[0],t[1])
