box_of_eggs = int(input('How many boxes of eggs do you have? '))
eggs_per_box = 6
eggs_per_omelette = 4

omelettes = int(float(box_of_eggs * eggs_per_box) / int(eggs_per_omelette))
print(f'You can make {omelettes} omelettes with {box_of_eggs} boxes of eggs!')
