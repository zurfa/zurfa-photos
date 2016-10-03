import logger
import config
import files

import exifread
import time
import base64
import re


class Exif(object):
	"""EXIF related methods"""
	def __init__(self):
		super(Exif, self).__init__()
		self.lg	= logger.Logger('Exif')

	def exif_raw(self,File,Details=False):
		"""returns raw exif tags in a dict"""
		fi	= files.Files()
		f	= fi.open_file(File,'rb')
		if f:
			Tags	= exifread.process_file(f, strict=True, details=Details)
			self.lg.log.info("EXIF data read from %s" % File)
			return Tags
		else:
			self.lg.log.error("Unable to get EXIF tags from %s" % File)
			return False

