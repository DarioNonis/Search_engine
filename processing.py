import numpy as np
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()

def set_words(documents):

	for document in documents:
		doc = document.title + " " + document.author + " " + document.abstract
		document.words = []
		word = ""
		for i in range(len(doc)):
			if doc[i].isalpha() or (doc[i - 1].isalpha() and doc[i] == "-" and doc[i + 1].isalpha()):
				word += doc[i].lower()
			elif word != "":
				document.words.append(wnl.lemmatize(word))
				word = ""

def set_tfidf(documents, vocab, reverse_vocab, idf):

	for document in documents:

		document.tf = np.zeros(len(vocab))

		for word in document.words:
			if word in reverse_vocab and document.tf[reverse_vocab[word]] == 0.:
				document.tf[reverse_vocab[word]] = float(document.words.count(word)) / float(len(document.words))

		document.tf /= np.linalg.norm(document.tf)

		document.tfidf = document.tf * idf
		document.tfidf /= np.linalg.norm(document.tfidf)

def find_best_documents(query, documents, nb, type, K1 = 0.5, B = 0.5):

	scores = np.zeros(len(documents))

	if type == "tfidf":

		for i in range(len(documents)):
			scores[i] = np.dot(query.tfidf, documents[i].tfidf)

	elif type == "bm25":

		average = np.mean(np.array([len(d.words) for d in documents]))

		for i in range(len(documents)):
			scores[i] = 0.
			for word in documents[i].words:
				tf = float(documents[i].words.count(word)) / float(len(documents[i].words))
				scores[i] += (tf * (K1 + 1.)) / (tf + K1 * (1. - B + B * (float(len(documents[i].words)) / float(average))))

	scores = np.argsort(scores)[::-1]

	return scores[:nb] + 1
