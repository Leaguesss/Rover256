class Rover:
	Directions = {
		'N': (-1, 0),
		'E': (0, 1),
		'S': (1, 0),
		'W': (0, -1),
	}

	def __init__(self, x, y):
		"""
		Initialises the rover
		"""
		self.x = x
		self.y = y
		self.battery = 100
		self.explored_tiles = set()
	def set_planet(self, planet):
		"""
		Set the planet, And add current tile to the explored tiles.
		"""
		self.planet = planet
		# get the current tile
		cur_tile = self.planet.get_tile(self.x, self.y)
		# add current tile to expored
		self.explored_tiles.add(cur_tile)
		self.elevation = cur_tile.elevation()[0]
		# print(self.x,self.y)
		# print(self.elevation)
	def slope(self):
		cur_tile = self.planet.get_tile(self.x, self.y)
		high_elevation, low_elevation = cur_tile.elevation()
		# check whether is a slope
		if low_elevation is None:
			return high_elevation
		if self.elevation == high_elevation:
			return high_elevation,low_elevation
		else:
			return high_elevation

	def move(self, direction, cycles):
		"""
		Moves the rover on the planet
		"""
		for i in range(cycles):
			# check battery
			if self.battery < 0:
				break
			# Directions = {'N': (-1, 0),'E': (0, 1),'S': (1, 0),'W': (0, -1),}
			next_x = (self.x + Rover.Directions[direction][0]) % self.planet.height
			next_y = (self.y + Rover.Directions[direction][1]) % self.planet.width
			
			# print(next_x,next_y)
			next_tile = self.planet.get_tile(next_x, next_y)
			if self.elevation not in next_tile.elevation():
				elevation = self.slope()
				if elevation not in next_tile.elevation():
					continue
				self.elevation = elevation
			#check whethere is shade
			if next_tile.is_shaded():
				self.battery -= 1
			self.x, self.y = next_x, next_y
			# add expored tile
			self.explored_tiles.add(self.planet.get_tile(self.x, self.y))

	def wait(self, cycles):
		"""
		The rover will wait for the specified cycles
		"""
		cur_tile = self.planet.get_tile(self.x, self.y)
		# recharge if it's not shaded
		if not cur_tile.is_shaded():
			self.battery += cycles
			if self.battery > 100:
				self.battery = 100

	def scan(self, type):
		print('')
		if type == 'shade':
			for i in range(-2, 3): # -2, -1, 0, 1, 2
				line = ['']
				for j in range(-2, 3):  # -2, -1, 0, 1, 2
					x = (self.x + i) % self.planet.height # if i = 0, x = self.x % height= can't overrange
					y = (self.y + j) % self.planet.width # if j = 0, y = self.y % =  width can't overrange
					tile = self.planet.get_tile(x, y)
					self.explored_tiles.add(tile) # scan also = expored 
					if x == self.x and y == self.y:
						line.append('H')
					elif tile.is_shaded():
						line.append('#')
					else:
						line.append(' ')
				line.append('')
				print("|".join(line))
		elif type == 'elevation':
			cur_high, cur_low = self.planet.get_tile(self.x, self.y).elevation()
			# print(cur_high,cur_low)
			for i in range(-2, 3):
				line = ['']
				for j in range(-2, 3):
					x = (self.x + i) % self.planet.height # same reason above
					y = (self.y + j) % self.planet.width
					tile = self.planet.get_tile(x, y)
					high_elevation, low_elevation = tile.elevation()
					self.explored_tiles.add(tile)
					if x == self.x and y == self.y:
						line.append('H')
						continue 
					if cur_low is None:
						if cur_high > high_elevation: # check the elevation
							line.append('-')
						else:
							if low_elevation is None:
								if cur_high == high_elevation:
									line.append(' ')
								else:
									line.append('+')
							else:
								if cur_high < low_elevation:
									line.append('+')
								elif self.elevation == low_elevation:
									line.append('/')
								else:
									line.append('\\')
					else:
						if cur_low > high_elevation:
							line.append('-')
						else:
							if low_elevation is None:
								if cur_low == high_elevation or cur_high == high_elevation:
									line.append(' ')
								else:
									line.append('+')
							else:
								if cur_low == high_elevation:
									line.append('\\')
								elif cur_low == low_elevation:
									line.append(' ')
								elif cur_high == high_elevation:
									line.append('/')
								else:
									line.append('+')
							
				line.append('') # in order to get two | in two sides
				print("|".join(line))
		print('')
	def stats(self):
		print('')
		print("Explored: {}%".format(len(self.explored_tiles) * 100 // self.planet.tiles_number()))
		print("Battery: {}/100".format(self.battery))
		print('')
	def finish(self):
		print('')
		print("You explored {}% of {}".format(
			len(self.explored_tiles) * 100 // self.planet.tiles_number(),
			self.planet.get_name()))
		print('')
	
