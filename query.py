import numpy as np

class Query:

	def __init__(self, id = 0, title = "", author = "", abstract = "", source = ""):
		self.id = id
		self.title = title
		self.author = author
		self.abstract = abstract
		self.source = source
		self.results = []
		self.words = []
		self.tfidf = np.array([])
