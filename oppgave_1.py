with open('test2.txt', 'w') as wfile:
    condition = 99

    while condition > 0:
	    wfile.write(f"{condition} bottles of beer on the wall, {condition} bottles of beer, take one down pass it around, {condition -1} bottles of beer on the wall\n")
	    condition -= 1
	    if condition == 0:
		    wfile.write("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall...\n")
