# Create a Tool for Calculating the Amount of Paint and Primer Needed to Paint a Wall.
# Requirements:
# 1. The number of walls must be entered by the user.
# 2. The number of layers must be entered separately by the user for both paint and primer.
# 3. The width and height of each wall must be entered separately by the user.
# 4. For the second and subsequent walls, if the user hits enter, the height must default to the height of the previous wall.
# 5. The result must be printed in liters.
# 6. The paint spreading rate is 13 square meters per 1 liter.
# 7. The primer spreading rate is 5 square meters per 1 liter.

total_wall_area = 0
wall_height = 0
wall_amount = int(input('How many walls do you want to paint? '))
primer_layers_amount = int(input('How many layers of primer do you want to paint? '))
paint_layers_amount = int(input('How many layers of paint do you want to paint? '))
for i in range(1, wall_amount+1):
    if wall_height == 0:
        print(f'What is height [in meters] of {i} wall? ')
        wall_height = float(input())
    elif wall_height > 0:
        print(f'What is height [in meters] of {i} wall? Hit enter if you want to use previous height.')
        wall_height_new = input()
        if wall_height_new == '':
            wall_height_new = wall_height
        wall_height = float(wall_height_new)
    print(f'What is width [in meters] of the {i} wall?')
    wall_width = float(input())
    wall_area = wall_height * wall_width
    total_wall_area += wall_area

primer_amount_need_l = (total_wall_area / 5) * primer_layers_amount
paint_amount_need_l = (total_wall_area / 13) * paint_layers_amount
print(f'You need {primer_amount_need_l:.2f} litres of primer\n'
      f'You need {paint_amount_need_l:.2f} litres of paint')
