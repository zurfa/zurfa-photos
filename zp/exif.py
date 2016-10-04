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
		# self.lg = logger.logger
		# logger.Logger(self.__class__.__name__)

	def exif_raw(self,File,Details=False):
		"""returns raw exif tags in a dict"""
		fi	= files.Files()
		f	= fi.open_file(File,'rb')
		if f:
			Tags	= exifread.process_file(f, strict=True, details=Details)
			return Tags
		else:
			# No EXIF data found
			return False

