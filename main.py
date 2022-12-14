import load
from vocab import get_vocab
import processing
import numpy as np
import evaluate

documents = load.get_documents()
queries = load.get_queries()

vocab, reverse_vocab, idf = get_vocab(documents)

processing.set_tfidf(documents, vocab, reverse_vocab, idf)
processing.set_tfidf(queries, vocab, reverse_vocab, idf)

print("\n\nCalculating random results...")

results = list(np.random.uniform(1, len(documents) + 1, (len(queries), 10)))
precision, recall, f_score = evaluate.evaluate_all(results, queries)

print("Random results: precision = %.2f%%, recall = %.2f%%, f-score = %.2f%%" % (precision * 100, recall * 100, f_score * 100))

print("\nCalculating model results...")

results = []

for query in queries:
	results.append(processing.find_best_documents(query, documents, 10, "tfidf"))

precision, recall, f_score = evaluate.evaluate_all(results, queries)
print("Model results: precision = %.2f%%, recall = %.2f%%, f-score = %.2f%%" % (precision * 100, recall * 100, f_score * 100))
