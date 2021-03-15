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