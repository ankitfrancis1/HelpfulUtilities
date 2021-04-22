#Utility to convert csv files from UCS-2 (utf_16_le) to UTF-8 ಥ_ಥ
#Also an example of :
#		how to read file path of current directory, be it script file or converted frozen exe
#		How to delete a directory, using shutil.rmtree
#		How to loop through all files in a directory, and read/write each file
import os
import sys
import shutil
import codecs

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    parent_dir = os.path.dirname(sys.executable)
elif __file__:
    parent_dir = os.path.dirname(__file__)
	
dest_path = os.path.join(parent_dir,"converted")
try:
	# creating directory for files
	if os.path.exists(dest_path):
		shutil.rmtree(dest_path)
	desired_permission = 0o777
	try:
		original_umask = os.umask(0)
		os.makedirs(dest_path, desired_permission)
	finally:
		os.umask(original_umask)
	print ('Creating files in: '+dest_path)
	BLOCKSIZE = 1048576 # or some other, desired size in bytes
	#conversion
	for filename in os.listdir(parent_dir):
		if filename.endswith(".csv"):
			targetFile = dest_path +"\\" + filename
			with codecs.open(os.path.join(parent_dir,filename), "r","utf_16_le") as sourceFile:
				with codecs.open(targetFile, "w", "utf-8") as targetFile:
					while True:
						contents = sourceFile.read(BLOCKSIZE)
						if not contents:
							break
						targetFile.write(contents)
	print('Successful!');
except:
	print('Unable to create all files! please close any open csv files in {'+ dest_path +'} and try again')
					
os.system('pause')					