from deep_translator import (GoogleTranslator,MyMemoryTranslator)

choice = input('1. Convert from Text File\n2. Convert from a word [Type 1 / 2]\n')

if choice == '1':
 
	path = input('Enter full path to .txt file : ')
	from_lang = input('From which language ? ')
	to_lang = input ('To which language ? ')
	translated = MyMemoryTranslator(source=from_lang, target=to_lang).translate_file(path)
	print(translated)

elif choice == '2':

	word = input("Enter word ")
	from_lang = input('From which language ? ')
	to_lang = input ('To which language ? ')
	translated = MyMemoryTranslator(source=from_lang, target=to_lang).translate(word)
	print(translated)

else :

	print('Try Again | Error')	
