import random
import os

x_size = 5
y_size = 5

x_coord_list = list(range(x_size))
y_coord_list = list(range(y_size))

choice_list = [0,1,1] # This list is to be modified to effectively change the probability of being a black cell

grid = [{'x': x, 'y': y, 'color':random.choice(choice_list)} for x in x_coord_list for y in y_coord_list]

print(grid)

def pathfinder(cell):
	x = cell.get('x')
	y = cell.get('y')
	print(x,y)
	traversed(y)
	up = y+1
	left = x-1
	centre = x
	right = x+1
	while up < y_size:
		try: 
			# print('Trying upper left')
			check(left,up)
		except:
			pass
		try: 
			# print('Trying upper middle')
			check(centre, up)
		except:
			pass
		try: 
			# print('Trying upper right')
			check(right, up)
		except:
			pass
		print('Failed to percolate')
		break
	return

def traversed(y):
	if y == y_size-1:
		print('Percolated!!!')
		os._exit(0)

def check(x,y):
	check_item = {'x': x, 'y': y, 'color': 1}
	for next_cell in grid:
		if next_cell == check_item:
			pathfinder(next_cell)

for cell in grid:
	if cell.get('y') == 0 and cell.get('color') == 1:
		pathfinder(cell)