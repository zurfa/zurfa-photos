import logger
import config
import exp

import os
import time
import hashlib
import logging


class Files(object):
	"""handles file related stuff"""
	def __init__(self):
		super(Files, self).__init__()
		self.lg	= logger.Logger()
		self.lg.setup(self.__class__.__name__)

	global lg
	lg	= logger.Logger('Files')
		
	def get_imports(self,Dir=None):
		"""returns list of valid available images in a directory"""
		valid	= ['.jpg','.jpeg']
		if not Dir:
			# Did the user specify a directory?
			self.lg.logger.error("Directory not specified or invalid")
			raise OSError
		else:
			try:
				Files		= os.listdir(Dir)
			except OSError:
				self.lg.logger.critical("Error opening directory, does it exist? %s" % Dir)
				raise exp.DirectoryError(Dir)
			else:
				file_paths	= []
				Lf	= len(Files)
				if Lf > 0:
					# Found files in directory
					self.lg.logger.info("Searching for files in %s" % Dir)
					for File in Files:
						ext	= os.path.splitext(File)[1]
						if ext in valid:
							# File has a valid extension
							file_paths.append(File)
						else:
							# File does not have a valid extension
							pass
					Lfp	= len(file_paths)
					if Lfp > 0:
						# Found atleast one valid file
						self.lg.logger.info("Found %s/%s files with valid extensions in %s" % (Lfp,Lf,Dir))
						return file_paths
					else:
						# Did not find any valid files
						self.lg.logger.error("Did not find any valid files in directory. %s" % Dir)
						raise exp.ValidFilesError(Dir)
				else:
					# Did not find files in directory
					self.lg.logger.error("Did not find any files in directory. %s" % Dir)
					raise exp.NullDirectoryError(Dir)

	def open_file(self,In,Mode='r'):
		try:
			f	= open(In, Mode)
		except IOError:
			return False
			self.lg.logger.error("Error opening file %s" % In)
		else:
			return f

	def copy_file(self,In,Out):
		try:
			shutil.copy2(In,Out)
		except IOError:
			self.lg.logger.error("File does not exist or is not readable")
			return False
		except shutil.Error:
			self.lg.logger.error("Destination does not exist or is not writeable")
			return False
		else:
			return True

	def move_file(self,In,Out):
		try:
			shutil.move(In,Out)
		except IOError:
			self.lg.logger.error("File does not exist or is not readable")
			return False
		except shutil.Error:
			self.lg.logger.error("Destination does not exist or is not writeable")
			return False
		else:
			return True

	def sha1_checksum(self,File):
		"""calculate sha1 checksum on given file."""

		BLOCKSIZE	= 65536
		hasher	= hashlib.sha1()
		handle	= self.open_file(File)
		if handle:
			self.lg.logger.info("Unable to generate checksum for %s" % File)
			with handle as afile:
				buf = afile.read(BLOCKSIZE)
				while len(buf) > 0:
					hasher.update(buf)
					buf = afile.read(BLOCKSIZE)
			checksum	= hasher.hexdigest()
			SHA1	= checksum.upper()
			return(SHA1)
		else:
			# self.lg.logger.info("Generated SHA1 checksum for %s" % File)
