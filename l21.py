import re
def match(text):

		# regex
		pattern = '[A-Z]+[a-z]+$'

		# searching pattern
		if re.search(pattern, text):
			print ("correct")
		else:
			print("error")
# Driver Function
print("please enter your first name")
firstname=input()
print("please enter your last name")
lastname=input()
print("please enter your city name")
city=input()
print(match(firstname))
print(match(lastname))
print(match(city))
def match1(number):
   pattern='^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$'
   if re.search(pattern, number):
       return ("correct")
   else:
       print("error")
print("please enter phone")
phone=input()
print(match1(phone))

def match2(code):
    regex= re.compile(r"(\b\d{2}-\d{3}\b|\b\d{3}\b\s)")
    if(re.search(regex,code)):
        return ("correct")
    else:
        return("error")
print("please enter your zip code")
zip=input()
print(match2(zip))
