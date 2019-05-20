# b64finder - Base64 pattern finder
By RemsFlems.

More RemsFlems work at https://talk2me.freeboxos.fr
###### DESCRIPTION #######
	This program will let you find any bas64 pattern into any files.

	This repository contains 2 files: b64finder.py & b64finder1L.py

	b64finder1L.py is similar to b64finder.py but condensated into one statment (one line).
###### HOW TO RUN ########
##### Search base64 patterns into superfile.txt
	python b64finder.py superfile.txt
##### Search base64 patterns into superfile.txt and show the 5 most probable results.
	python b64finder.py superfile.txt 5
##### Search base64 patterns with minimum length 3,max length 80 into superfile.txt and show the 5 most probable results.
	python b64finder.py superfile.txt 5 3 80
##### Usage for b64finder1L.py is exactly the same:
	python b64finder1L.py superfile.txt

	python b64finder1L.py superfile.txt 5

	python b64finder1L.py superfile.txt 5 3 80



