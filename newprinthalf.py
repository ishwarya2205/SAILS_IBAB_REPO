def print_half(text):
    if len(text)< 2:
        print(text)
        return text  
    else:
        mid = len(text) // 2
        print(mid)
        return text[:mid]
        
def mymain():
    text=("python language")
    print_half(text)
     
if __name__== "__main__":
	mymain()
