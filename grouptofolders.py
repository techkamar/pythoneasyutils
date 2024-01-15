#! /usr/bin/python3
import os
import sys


def mkfolder(foldername):
	command = f"mkdir {foldername}"
	print(f"Running {command}")
	os.system(command)

def movefile(filename,foldername):
	# command = f"mv \"{os.getcwd()}/{filename}\" \"{os.getcwd()}/{foldername}/\""
	command = f"mv {filename} {foldername}/"
	print(f"Running {command}")
	os.system(command)

def main(file_group_count):
	all_files = os.listdir(os.getcwd())
	print(all_files)
	all_files.sort()
	index = 0
	folder_number = 0
	while index < len(all_files):
		mkfolder(folder_number)
		for counter in range(0,file_group_count):
			print(f"[+] Moving file {index}/{len(all_files)}")
			if index < len(all_files):
				movefile(all_files[index],folder_number)
				index+=1
		# Change folder
		folder_number+=1
if __name__ == "__main__":
	file_group_count = int(sys.argv[1])
	main(file_group_count)