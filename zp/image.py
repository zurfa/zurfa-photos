import logger
import config
import math

from PIL import Image, ImageDraw as PIL
import imagehash


class Image(object):
	"""handles image related functions"""
	def __init__(self):
		super(Image, self).__init__()
		self.lg	= logger.Logger()
		self.lg.setup(self.__class__.__name__)

	def open_image(self,File):
		try:
			Image	= PIL.Image.open(File)
		except IOError:
			self.lg.logger.error("Error opening file, does it exist? %s" % File)
			return False
		else:
			return Image

	def close_image(self,Handle):
		try:
			PIL.Image.close(Handle)
		except:
			return False
		else:
			return True

	def save_image(self,Image,Dest,Options=None):
		try:
			if Options:
				Image.save(Dest,**Options)
			else:
				Image.save(Dest)
		except IOError:
			self.lg.logger.error("Error saving file %s" % Dest)
			return False
		else:
			# self.lg.logger.info("Saved image %s" % Dest)
			return True
			Image.close()

	def thumb(self,File,Max,Dest=None,Options=None):
		Image	= self.open_image(File)

		# Set additional options
		if not Options:
			Options['quality']	= 95
			Options['optimize']	= True
			Options['qtables']	= 'web_high'

		if Image:
			Size	= math.image_constraints(Image.size,Max)
			Image	= Image.resize(Size,resample=PIL.Image.BILINEAR)
			self.lg.logger.info("Generated new thumbnail object for %s" % File)
			if Dest:
				return	(Image,Dest,Options)
			else:
				return	(Image,Options)

	def large_thumb(self,File,Dest=False,Obj=False):
		if Obj:
			Image	= File
		else:
			Image	= self.open_image(File)

		# Set additional options
		Options	= {}
		Options['quality']	= config.LARGE_THUMB_QUALITY
		Options['optimize']	= True
		Options['qtables']	= 'web_high'

		if Image:
			Size	= math.image_constraints(Image.size,config.LARGE_THUMB_SIZE)
			Image	= Image.resize(Size,resample=PIL.Image.BILINEAR)
			# self.lg.logger.info("Generated new large thumbnail object for %s" % File)
			if Dest:
				return	(Image,Dest,Options)
			else:
				return	(Image,Options)
		else:
			return False

	def medium_thumb(self,File,Dest=None,Obj=False):
		if Obj:
			Image	= File
		else:
			Image	= self.open_image(File)

		# Set additional options
		Options	= {}
		Options['quality']	= config.MEDIUM_THUMB_QUALITY
		Options['optimize']	= True
		Options['qtables']	= 'web_low'

		if Image:
			Size	= math.image_constraints(Image.size,config.MEDIUM_THUMB_SIZE)
			Image	= Image.resize(Size,resample=PIL.Image.BILINEAR)
			# self.lg.logger.info("Generated new medium thumbnail object for %s" % File)
			if Dest:
				return	(Image,Dest,Options)
			else:
				return	(Image,Options)
		else:
			return False

	def small_thumb(self,File,Dest=None,Obj=False):
		if Obj:
			Image	= File
		else:
			Image	= self.open_image(File)

		# Set additional options
		Options	= {}
		Options['quality']	= config.SMALL_THUMB_QUALITY
		Options['optimize']	= True
		Options['qtables']	= 'web_low'

		if Image:
			Size	= math.image_constraints(Image.size,config.SMALL_THUMB_SIZE)
			Image	= Image.resize(Size,resample=PIL.Image.BILINEAR)
			# self.lg.logger.info("Generated new small thumbnail object for %s" % File)
			if Dest:
				return	(Image,Dest,Options)
			else:
				return	(Image,Options)
		else:
			return False

	def image_dimensions(self,File):
		Image	= self.open_image(File)

		if Image:
			Size	= Image.size
			return Size
		else:
			self.lg.logger.error("Unable to determine size of %s" % File)

	def p_hash(self,Image,Size=None):
		if not Size:
			Size	= config.PHASH_SIZE

		ImageF	= self.open_image(Image)
		if Image:
			Hash	= str(imagehash.phash(ImageF,Size)).upper()
			self.lg.logger.info("Generated new PHASH for %s %s" % (Image,Hash))
			return Hash
		else:
			return False

	def d_hash(self,Image,Size=None):
		if not Size:
			Size	= config.DHASH_SIZE

		ImageF	= self.open_image(Image)
		if Image:
			Hash	= str(imagehash.dhash(ImageF,Size)).upper()
			self.lg.logger.info("Generated new DHASH for %s %s" % (Image,Hash))
			return Hash
		else:
			return False

	@staticmethod
	def is_image(File):
		Image	= False
		try:
			Image	= PIL.Image.open(File)
			Image.load()
		except IOError:
			raise IOError
		else:
			return True
		finally:
			if Image:
				Image.close()
			