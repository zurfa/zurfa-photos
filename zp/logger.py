import logging

logger = None
class Logger(object):
	"""logs things"""
	def __init__(self):
		super(Logger, self).__init__()	
		
	def setup(self,Name):
		"""setup and configure logger"""
		self.logger = logging.getLogger(Name)
		self.logger.setLevel(logging.DEBUG)
		if self.logger.handlers == []:
			CLog	= logging.DEBUG # Console log level
			FLog	= logging.DEBUG	# Logfile log level
			Logfile	= 'library.log'	# Logfile
			# Log format
			Format	= "[%(asctime)s] %(levelname)s (%(module)s) %(name)s.%(funcName)s: %(message)s"
			
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
			self.logger.addHandler(fh)
			self.logger.addHandler(ch)
