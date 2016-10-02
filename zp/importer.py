import logger
import config

import string
import random


class Importer(object):
	"""does importing things"""
	def __init__(self):
		super(Importer, self).__init__()
		self.lg	= logger.Logger('Importer')

	def new_ufid(self, chars=string.ascii_uppercase + string.digits):
		UFID	= ''.join(random.choice(chars) for _ in range(config.UFID_LENGTH))
		self.lg.log.info("Generated new UFID %s" % UFID)
		return UFID