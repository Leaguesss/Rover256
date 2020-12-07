from terrain import Tile

class Planet:
	def __init__(self, name, width, height):
		"""
		Initialise the planet object
		"""
		self.name = name
		self.width = width
		self.height = height
		self.tiles = [['temp'] * self.width for i in range(self.height)] #get a width * height list
		self.n_tiles = 0

	def add_tile(self, terrain_type, high_elevation, low_elevation=None):
		self.tiles[self.n_tiles // self.width][self.n_tiles % self.width] = Tile(terrain_type, high_elevation, low_elevation)
		self.n_tiles += 1

	def get_tile(self, x, y):
		"""
		Returns tile on the coordinates
		"""
		return self.tiles[x][y]

	def tiles_number(self):
		return self.n_tiles

	def get_name(self):
		return self.name
	
	
	
	
	
