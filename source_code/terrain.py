class Tile:
	def __init__(self, terrain_type, high_elevation, low_elevation=None):
		"""
		Initialises the terrain tile and attributes
		"""
		self.terrain_type = terrain_type
		self.high_elevation = high_elevation
		self.low_elevation = low_elevation
		self.rover = None


	def elevation(self):
		"""
		Returns an integer value of the elevation number
		of the terrain object
		"""
		return (self.high_elevation, self.low_elevation)

	def is_shaded(self):
		"""
		Returns True if the terrain tile is shaded, otherwise False
		"""
		return self.terrain_type == 'shaded'

	def set_occupant(self, obj):
		"""
		Sets the occupant on the terrain tile
		"""
		self.rover = obj
		return self.rover

	def get_occupant(self):
		"""
		Gets the entity on the terrain tile
		If nothing is on this tile, it should return None
		"""
		return self.rover
	
	
