from document import Document
from query import Query
import processing

def get_documents():

	documents_file = open('CISI.ALL', 'r')
	documents = []
	finished = False
	document = Document()
	line = documents_file.readline()

	while not finished:

		if line.startswith(".I"):
			if document.id != 0:
				documents.append(document)
			document = Document()
			document.id = int(line.strip()[3:])
			line = documents_file.readline()

		elif line.startswith(".T"):
			while True:
				line = documents_file.readline()
				if line.startswith(".A"):
					break
				document.title += line.strip()

		elif line.startswith(".A"):
			while True:
				line = documents_file.readline()
				if line.startswith(".W"):
					break
				document.author += line.strip()

		elif line.startswith(".W"):
			while True:
				line = documents_file.readline()
				if line.startswith(".X"):
					document.abstract = document.abstract.strip()
					break
				document.abstract += line

		elif line.startswith(".X"):
			document.crossrefs = []
			while True:
				line = documents_file.readline()
				if line.startswith(".I"):
					break
				elif not line:
					finished = True
					break
				l = line.strip().split("\t")
				l = [int(i) for i in l]
				document.crossrefs.append(l)

	documents.append(document)
	documents_file.close()

	processing.set_words(documents)

	return documents

def get_queries():

	queries_file = open('CISI.QRY', 'r')
	results_file = open('CISI.REL', 'r')
	queries = []
	finished = False
	query = Query()
	line = queries_file.readline()

	while not finished:

		if line.startswith(".I"):
			if query.id != 0:
				queries.append(query)
			query = Query()
			query.id = int(line.strip()[3:])
			line = queries_file.readline()

		elif line.startswith(".T"):
			while True:
				line = queries_file.readline()
				if line.startswith(".A"):
					break
				query.title += line.strip()

		elif line.startswith(".A"):
			while True:
				line = queries_file.readline()
				if line.startswith(".W"):
					break
				query.author += line.strip()

		elif line.startswith(".W"):
			while True:
				line = queries_file.readline()
				if line.startswith(".B") or line.startswith(".I"):
					query.abstract = query.abstract.strip()
					break
				elif not line:
					query.abstract = query.abstract.strip()
					finished = True
					break
				query.abstract += line

		elif line.startswith(".B"):
			while True:
				line = queries_file.readline()
				if line.startswith(".I"):
					break
				elif not line:
					finished = True
					break
				query.source += line.strip()

	queries.append(query)

	while True:

		line = results_file.readline()

		if not line:
			break

		n1 = int(line[:6].strip())
		n2 = int(line[7:13].strip())

		queries[n1 - 1].results.append(n2)

	queries_file.close()
	results_file.close()

	processing.set_words(queries)

	return queries
