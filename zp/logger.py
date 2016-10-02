import logging

class Logger(object):
	"""logs things"""
	def __init__(self,Name=__name__):
		super(Logger, self).__init__()
		#  Do setup
		self.setup(Name)
		
	def setup(self,Name):
		"""setup and configure logger"""
		logger = logging.getLogger(Name)
		logger.setLevel(logging.DEBUG)

		CLog	= logging.DEBUG # Console log level
		FLog	= logging.DEBUG	# Logfile log level
		Logfile	= 'library.log'	# Logfile
		# Log format
		Format	= "[%(asctime)s] %(levelname)s (%(name)s) %(module)s.%(funcName)s: %(message)s"
		
		# Create logfile handler
		fh = logging.FileHandler(Logfile)
		fh.setLevel(FLog)
		# Create console handler
		ch = logging.StreamHandler()
		ch.setLevel(CLog)
		# Set formatter
		formatter = logging.Formatter(Format,datefmt='%Y-%m-%d %H:%M:%S')
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)
		# Add handlers to logger
		logger.addHandler(fh)
		logger.addHandler(ch)

		# Set log object
		self.log	= logger
