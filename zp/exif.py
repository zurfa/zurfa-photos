import logger
import config
import files
import image
import exp

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
		try:
			im	= image.Image()
			i	= im.open_image(File)
			EXIF	= i._getexif()
		except:
			return False
		else:
			if EXIF:
				return EXIF
			else:
				return False
		finally:
			im.close_image(i)

	def exif_tags(self,File,Dump=False):
		"""parse and format ONLY the EXIF tags used in the library"""
		RAW	= self.exif_raw(File)

		if RAW:
			# EXIF data found
			# Parse the tags we want into a dictionary
			Keys	= {
						'make'		:	0x010f,
						'model'		:	0x0110,
						'taken'		:	0x9003,
						'taken_tz'	:	0x9011}
			Values	= {}

			Tags	= self.parse_tags(RAW,Keys)
			GPS		= self.exif_gps(RAW)
			if GPS:
				Values['lat']		= GPS[0]
				Values['lon']		= GPS[1]
			if 'make' in Tags and 'model' in Tags:
				Values['device']	= "%s %s" % (Tags['make'],Tags['model'])
			if 'taken' in Tags:
				# Assume timestamp is UTC
				Values['taken']		= self.unix_time(Tags['taken'])
			return Values
		else:
			# No EXIF data found
			return False

	def exif_gps(self,RAW):
		"""Parse and format GPS tags from the provided EXIF data"""
		# Does this exif dataset have GPS data?
		if 0x8825 in RAW:
			# Remove everything except GPS data
			RAW	= RAW[0x8825]
			if (0x0001,0x0002,0x0003,0x0004) in RAW:
				Lat	= self.gps_dms_dd(GPS['lat'],GPS['lat_ref'])
				Lon	= self.gps_dms_dd(GPS['lon'],GPS['lon_ref'])
				return (Lat,Lon)
			else:
				# No GPS data found in EXIF
				return False
				
		
	@staticmethod
	def gps_dms_dd(DMS,Direction):
		DEG	= DMS[0][0]
		MIN	= DMS[1][0]
		SEC	= (DMS[2][0]/DMS[2][1])

		dd	= float(DEG) + float(MIN)/60 + float(SEC)/3600
		if Direction == 'W' or Direction == 'S':
			dd *= -1
		return dd

	@staticmethod
	def parse_tags(RAW,Tags):
		"""Check is provided tags exist, parses and returns keyword values"""

		Values	= {}
		for Key,Tag in Tags.iteritems():
			if Tag in RAW:
				Values.update({Key:RAW[Tag]})
		return Values

	@staticmethod
	def unix_time(Time,TZ=False):
		"""Convert timestamp to unix time, assumes %Y:%m:%d %H:%M:%S"""
		Time	= time.strptime(Time,"%Y:%m:%d %H:%M:%S")
		return int(time.mktime(Time))