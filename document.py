import numpy as np

class Document:

	def __init__(self, id = 0, title = "", author = "", abstract = "", crossrefs = []):
		self.id = id
		self.title = title
		self.author = author
		self.abstract = abstract
		self.crossrefs = crossrefs
		self.words = []
		self.tfidf = np.array([])
