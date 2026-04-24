def skip_characters(text):
	return text[::2]

def mymain():
	s = "india pakistan"
	result = skip_characters(s)
	print(result)

if __name__ == "__main__":
    mymain()
