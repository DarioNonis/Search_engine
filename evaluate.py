def evaluate(results, expected):

	precision = 0.
	recall = 0.
	f_score = 0.

	for i in range(len(results)):
		if results[i] in expected:
			precision += 1.
			recall += 1.

	if len(expected) > 0:
		recall /= float(len(expected))
	else:
		recall = 1.

	if len(results) > 0:
		precision /= float(len(results))
	else:
		precision = 1.

	if precision + recall > 0.:
		f_score = 2. * ((recall * precision) / (recall + precision))
	else:
		f_score = 0.

	return precision, recall, f_score

def evaluate_all(results, queries):

	precision = 0.
	recall = 0.
	f_score = 0.

	for i in range(len(queries)):
		p, r, f = evaluate(results[i], queries[i].results)
		precision += p
		recall += r
		f_score += f

	precision /= float(len(queries))
	recall /= float(len(queries))
	f_score /= float(len(queries))

	return precision, recall, f_score
