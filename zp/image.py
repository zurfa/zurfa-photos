import logger
import config
import math

from PIL import Image, ImageDraw as PIL
import imagehash


class Image(object):
	"""handles image related functions"""
	def __init__(self):
		super(Image, self).__init__()
		self.lg	= logger.Logger('Image')

	def open_image(self,File):
		try:
			Image	= PIL.Image.open(File)
		except IOError:
			self.lg.log.error("Error opening file, does it exist? %s" % File)
			return False
		else:
			return Image

	def save_image(self,Image,Dest,Options=None):
		try:
			if Options:
				Image.save(Dest,**Options)
			else:
				Image.save(Dest)
		except IOError:
			self.lg.log.error("Error saving file %s" % Dest)
			return False
		else:
			self.lg.log.info("Saved image %s" % Dest)
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
			self.lg.log.info("Generated new thumbnail object for %s" % File)
			if Dest:
				return	(Image,Dest,Options)
			else:
				return	(Image,Options)

	def large_thumb(self,File,Dest=None):
		Image	= self.open_image(File)

		# Set additional options
		Options	= {}
		Options['quality']	= config.LARGE_THUMB_QUALITY
		Options['optimize']	= True
		Options['qtables']	= 'web_high'

		if Image:
			Size	= math.image_constraints(Image.size,config.LARGE_THUMB_SIZE)
			Image	= Image.resize(Size,resample=PIL.Image.BILINEAR)
			self.lg.log.info("Generated new large thumbnail object for %s" % File)
			if Dest:
				return	(Image,Dest,Options)
			else:
				return	(Image,Options)

	def medium_thumb(self,File,Dest=None):
		Image	= self.open_image(File)

		# Set additional options
		Options	= {}
		Options['quality']	= config.MEDIUM_THUMB_QUALITY
		Options['optimize']	= True
		Options['qtables']	= 'web_low'

		if Image:
			Size	= math.image_constraints(Image.size,config.MEDIUM_THUMB_SIZE)
			Image	= Image.resize(Size,resample=PIL.Image.BILINEAR)
			self.lg.log.info("Generated new medium thumbnail object for %s" % File)
			if Dest:
				return	(Image,Dest,Options)
			else:
				return	(Image,Options)

	def small_thumb(self,File,Dest=None):
		Image	= self.open_image(File)

		# Set additional options
		Options	= {}
		Options['quality']	= config.SMALL_THUMB_QUALITY
		Options['optimize']	= True
		Options['qtables']	= 'web_low'

		if Image:
			Size	= math.image_constraints(Image.size,config.SMALL_THUMB_SIZE)
			Image	= Image.resize(Size,resample=PIL.Image.BILINEAR)
			self.lg.log.info("Generated new small thumbnail object for %s" % File)
			if Dest:
				return	(Image,Dest,Options)
			else:
				return	(Image,Options)

	def p_hash(self,Image,Size=None):
		if not Size:
			Size	= config.PHASH_SIZE

		ImageF	= self.open_image(Image)
		if Image:
			Hash	= str(imagehash.phash(ImageF,Size)).upper()
			self.lg.log.info("Generated new PHASH for %s %s" % (Image,Hash))
			return Hash
		else:
			return False

	def d_hash(self,Image,Size=None):
		if not Size:
			Size	= config.DHASH_SIZE

		ImageF	= self.open_image(Image)
		if Image:
			Hash	= str(imagehash.dhash(ImageF,Size)).upper()
			self.lg.log.info("Generated new DHASH for %s %s" % (Image,Hash))
			return Hash
		else:
			return False