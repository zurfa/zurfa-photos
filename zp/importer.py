import logger
import config

import string
import random
import logging


class Importer(object):
	"""does importing things"""
	def __init__(self):
		super(Importer, self).__init__()
		self.lg	= logger.Logger()
		self.lg.setup(self.__class__.__name__)

	def new_ufid(self, chars=string.ascii_uppercase + string.digits):
		UFID	= ''.join(random.choice(chars) for _ in range(config.UFID_LENGTH))
		# self.lg.logger.info("Generated new UFID %s" % UFID)
		return UFID