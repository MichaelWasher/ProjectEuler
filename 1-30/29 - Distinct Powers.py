# Consider all integer combinations for powers from 2 -> Max
terms={}
MAX_BASE = 100
MAX_EXPONENT = 100

for base in range(2, MAX_BASE+1):
    for exponent in range(2, MAX_EXPONENT+1):
        term = base ** exponent
        terms[term] = True

distinct_terms = len(terms.keys())
print(f'Distinct Terms: {distinct_terms}')
