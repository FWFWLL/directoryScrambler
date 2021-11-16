import os
import sys
import pathlib
import random
import string

# Generates a random string of uppercase ASCII and digits of specified length
def generate_random_filename(length):
	return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def main():
	if(len(sys.argv) < 3):
		print(f"usage: {sys.argv[0]} [DIRECTORY] [LENGTH]")
	else:
		srcDir = sys.argv[1]
		length = int(sys.argv[2])
		for filename in os.listdir(srcDir):
			file_extension = pathlib.Path(filename).suffix
			src = srcDir + "/" + filename
			newFilename = generate_random_filename(length) + file_extension
			dst = srcDir + "/" + newFilename
			os.rename(src, dst)
			print(f"Renamed {filename} to {newFilename}")

if __name__ == "__main__":
	main()
