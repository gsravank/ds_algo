from collections import defaultdict


def mult_terms(t1, t2):
    i1 = t1.split('*')
    i2 = t2.split('*')
    const = int(i1[0]) * int(i2[0])
    expr = sorted(i1[1:] + i2[1:])
    return '*'.join([str(const)] + expr)


def mult_expr(e1, e2):
    terms = list()
    for t1 in e1:
        for t2 in e2:
            t = mult_terms(t1, t2)
            terms.append(t)

    # terms = simplify(terms)
    return terms


def add_expr(e1, e2):
    terms = e1 + e2
    # terms = simplify(terms)
    return terms


def simplify(terms):
    expr_map = defaultdict(int)
    for term in terms:
        items = term.split('*')
        c = int(items[0])
        e = items[1:]
        expr_map['*'.join(e)] += c

    count_map = defaultdict(lambda : list())
    for key in expr_map:
        count_map[len(key.split('*'))].append(key)
    suffixes = list()
    for count in sorted(count_map.keys(), reverse=True):
        curr_suffixes = count_map[count]
        curr_suffixes = sorted(curr_suffixes, key=lambda x: ''.join(y[0] for y in x.split('*')[1:]))
        suffixes.extend(curr_suffixes)
#     suffixes = sorted(list(expr_map.keys()), key=lambda x: len(x.split('*')), reverse=True)
    prefixes = [expr_map[x] for x in suffixes]
    terms = ['*'.join([str(prefix)] + ([suffix] if len(suffix) else [])) for prefix, suffix in zip(prefixes, suffixes) if prefix != 0]
    return terms


e1 = ['-2*a', '-3']
e2 = ['5*c', '6*a', '8']
terms = mult_expr(e1, e2)
print(terms)
terms = simplify(terms)
print(terms)
