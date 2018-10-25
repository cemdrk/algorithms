#!/usr/bin/env python

def knap(w, v , W):
    w.insert(0, 0)
    v.insert(0, 0)
    print w
    print v

    cache_table = [[-1 for _ in xrange(W+1)] for _ in xrange(len(w))]

    def ks(k, g):
        if cache_table[k][g] != -1:
            # print 'hit'
            return cache_table[k][g]

        if k == 0 or g == 0:
            result = 0
        elif w[k] > g:
            result = ks(k-1, g)
        else:
            result = max(ks(k-1, g), v[k]+ks(k-1, g-w[k]))

        cache_table[k][g] = result
        # print 'table updated'
        return result

    print 'result'
    print ks(len(w)-1, W)

    for row in cache_table:
        print row

    def backtrack(g):
        index_list = []
        for k in xrange(len(w)-1, 0, -1):
            if cache_table[k][g] != cache_table[k-1][g] and g != 0:
                index_list.append(k)
                g -= w[k]
        return index_list

    print 'index'
    print backtrack(W)

w = [5, 4, 6, 3]
v = [10, 40, 30, 50]
W = 10
knap(w, v, W)
