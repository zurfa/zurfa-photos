import logger
import config
import exp

import os
import time
import hashlib


class Files(object):
	"""handles file related stuff"""
	def __init__(self):
		super(Files, self).__init__()

	global lg
	lg	= logger.Logger('Files')
		
	def get_imports(self,Dir=None):
		"""returns list of valid available images in a directory"""
		valid	= ['.jpg','.jpeg']
		if not Dir:
			# Did the user specify a directory?
			lg.log.error("Directory not specified or invalid")
			raise OSError
		else:
			try:
				Files		= os.listdir(Dir)
			except OSError:
				lg.log.critical("Error opening directory, does it exist? %s" % Dir)
				raise exp.DirectoryError(Dir)
			else:
				file_paths	= []
				Lf	= len(Files)
				if Lf > 0:
					# Found files in directory
					lg.log.info("Searching for files in %s" % Dir)
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
						lg.log.info("Found %s/%s valid files in %s" % (Lfp,Lf,Dir))
						return file_paths
					else:
						# Did not find any valid files
						lg.log.error("Did not find any valid files in directory. %s" % Dir)
						raise exp.ValidFilesError(Dir)
				else:
					# Did not find files in directory
					lg.log.error("Did not find any files in directory. %s" % Dir)
					raise exp.NullDirectoryError(Dir)

	def open_file(self,In,Mode='r'):
		try:
			f	= open(In, Mode)
		except IOError:
			self.lg.log.error("Error opening file %s" % In)
			return False
		else:
			return f

	def copy_file(self,In,Out):
		try:
			shutil.copy2(In,Out)
		except IOError:
			self.lg.log.error("File does not exist or is not readable")
			return False
		except shutil.Error:
			self.lg.log.error("Destination does not exist or is not writeable")
			return False
		else:
			return True

	def move_file(self,In,Out):
		try:
			shutil.move(In,Out)
		except IOError:
			self.lg.log.error("File does not exist or is not readable")
			return False
		except shutil.Error:
			self.lg.log.error("Destination does not exist or is not writeable")
			return False
		else:
			return True

	def sha1_checksum(self,File):
		"""calculate sha1 checksum on given file."""

		BLOCKSIZE	= 65536
		hasher	= hashlib.sha1()
		handle	= self.open_file(File)
		if handle:
			with handle as afile:
				buf = afile.read(BLOCKSIZE)
				while len(buf) > 0:
					hasher.update(buf)
					buf = afile.read(BLOCKSIZE)
			checksum	= hasher.hexdigest()
			SHA1	= checksum.upper()
			self.lg.log.info("Generated SHA1 checksum for %s : %s" % (File,SHA1))
			return(SHA1)
		else:
			self.lg.log.info("Unable to generate checksum for %s" % File)