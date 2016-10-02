import logger

import os


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