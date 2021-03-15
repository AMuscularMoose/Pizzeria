#################################################################################
#simple dictionary
#################################################################################
alien = {'color':'green','points':5}
print(alien['color'])
print(alien['points'])


#################################################################################
#Modifying values ina dictionary
#################################################################################

alien['color'] = 'yellow'
print(alien['color'])

#################################################################################
#Looping through a dictionary
#################################################################################

fav_langs = {
    'jen' : 'py',
    'sarah' : 'c',
    'ed' : 'ruby',
    'phil' : 'py'
    }

for k,v in fav_langs.items():
    print("key:",k)
    print("value:",v)
    #items() method returns a list of key-val pairs

for name in fav_langs.keys():
    print(name.title())
    #keys() method returns keys and the title() function tidies up the output

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

for key, value in phonebook.items():
    print('KEY:',key,'VALUE:', value)
for phonebook_tuple in phonebook.items():
    print(phonebook_tuple)
