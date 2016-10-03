import logger

import os
import hashlib


class Files(object):
	"""handles file related stuff"""
	def __init__(self):
		super(Files, self).__init__()
		self.lg	= logger.Logger('Files')
		
	def get_imports(self,Dir=None):
		"""returns list of available files in a directory"""
		if not Dir:
			self.lg.log.error("Directory not specified or invalid")
			return False
		else:
			file_paths = []
			self.lg.log.info("Walking through %s" % Dir)
			for root, directories, files in os.walk(Dir):
				for filename in files:
					filepath = os.path.join(root, filename)
					file_paths.append(filepath)
			if len(file_paths) > 0:
				self.lg.log.info("Found %s files in %s" % (len(file_paths),Dir))
				return file_paths
			else:
				self.lg.log.error("No files found in path")
				return False

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