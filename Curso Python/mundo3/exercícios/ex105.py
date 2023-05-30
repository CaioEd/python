def notas(*n):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)

    return r


resp = (notas(5.5, 2.5, 7.8))
print(resp)