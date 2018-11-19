#0
print('DESAFIO 0\n')
a = 2**38

print(a)
print ('\n')

#1 
print('DESAFIO 1\n')
from string import maketrans 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet2 ='cdefghijklmnopqrstuvwxyzab'

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text2 = "Aosg rckmq y kclqyeck tcpbybcgpy"
url = 'map'

def translator_messages(phrase):
	translator = maketrans(alphabet, alphabet2)
	translated_message = phrase.translate(translator)
	print(translated_message)

translator_messages(text)

translator_messages(url)

print ('\n')

#2
import re
print('DESAFIO 2\n')
from collections import Counter
with open("problem2.txt", "r+") as file2:   #This file has the content hidden in the page
	data2 = file2.read().replace('\n','')

chars = Counter(data2)
result = chars.most_common()

print(result)
result = str(result)
print(''.join(re.findall('[a-z]', result)))

print('\n')

#3

print("DESAFIO 3\n")

with open("problem3.txt", "r+") as file3:   #This file has the content hidden in the page
	data3 = file3.read().replace('\n', '')

print(''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', data3)))
print('\n')

#4

print("DESAFIO 4\n")

import urllib2
first_nothing = "12345"
link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?notihing="
raw_content = urllib2.urlopen(url + first_nothing)
content = raw_content.read()
next_nothing = re.findall("[0-9]", content)

print(next_nothing)

