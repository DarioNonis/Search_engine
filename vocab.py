import numpy as np

def clear_words(vocab):

	blacklist_file = open("blacklist.txt", "r")
	blacklist = blacklist_file.read().split("\n")
	blacklist_file.close()

	for i in range(len(vocab)):
		if vocab[i][0] in blacklist or len(vocab[i][0]) == 1:
			vocab[i][1] = 0

	vocab = [v for v in vocab if v[1] != 0]

	return vocab

def get_vocab(documents):

	vocab = []

	for document in documents:

		words = list(dict.fromkeys(document.words))

		for i in range(len(words)):
			words[i] = [words[i], 1]

		for v in vocab:
			for w in words:
				if v[0] == w[0]:
					v[1] += 1
					w[1] = 0

		for w in words:
			if w[1] != 0:
				vocab.append(w)

		print("Document " + str(document.id) + " done.", end = "\r")

	vocab.sort(key = lambda x: x[1], reverse = True)
	vocab = clear_words(vocab)

	idf = np.log(len(documents) / np.array([v[1] for v in vocab]))
	idf /= np.linalg.norm(idf)

	vocab = [v[0] for v in vocab]
	reverse_vocab = { v: i for i, v in enumerate(vocab) }

	return vocab, reverse_vocab, idf
