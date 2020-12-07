import os
from planet import Planet
from rover import Rover

def load_level(filename):
	# check the path whether exites
	if not os.path.exists(filename):
		return False,"Level file could not be found"
	with open(filename,'r') as f:
		
		planet = f.readline().strip()
		if planet != '[planet]':
			return False,"Unable to load level file"
		# separate the list in different variables
		name = f.readline().strip().split(',')
		widthline = f.readline().strip().split(',')
		heightline = f.readline().strip().split(',')
		roverline = f.readline().strip().split(',')
		planet_information =[name,widthline,heightline,roverline]
		# check planet structure 
		for i in planet_information[:3]:
			if len(i) != 2:
				return False,"Unable to load level file"
		if len(planet_information[-1]) != 3:
			return False,"Unable to load level file"
		# str to int 
		name = name[-1]
		width = int(widthline[-1])
		height = int(heightline[-1])
		# print(roverline)
		rover_x,rover_y = int(roverline[-2]),int(roverline[-1])
		# check x and y is legit
		if (rover_x < 0) or (rover_y < 0):
			return False,"Unable to load level file"
		if (width < 5) or (height < 5):
			return False,"Unable to load level file"
		planet = Planet(name, width, height)
		rover = Rover(rover_x, rover_y)
		# skip line 6
		skipline6 = f.readline()
		tileline = f.readline().strip()
		if tileline != "[tiles]":
			return False,"Unable to load level file"
		# add tile to planet
		for i in range(width*height):
			line = f.readline().strip()
			try:
				terrain_type, *right = line.split(",")
				high_elevation = int(right[0])
				low_elevation = None
				if len(right) > 2:
					return False,"Unable to load level file"
				elif len(right) == 2:
					low_elevation = int(right[1])
			except:
				return False,"Unable to load level file"
			if (low_elevation != None) and (high_elevation <= low_elevation):
				return False,"Unable to load level file"
			planet.add_tile(terrain_type, high_elevation, low_elevation)
		# set planet
		rover.set_planet(planet)
	return True,rover
