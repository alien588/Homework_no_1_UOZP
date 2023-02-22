def manhattan_dist(r1, r2):
    """ Arguments r1 and r2 are lists of numbers """
    cum_sum = 0
    cnt = 0
    corrupt_cnt = 0
    if len(r1) == len(r2):
        for i in range(len(r1)):
            if (r1[i] == r1[i]) and (r2[i] == r2[i]):
                cum_sum += ((r1[i] - r2[i])**2)**(1/2)
                cnt += 1
            else:
                corrupt_cnt += 1
        if cnt == 0:
            return float("nan")

        if corrupt_cnt > 0:
            r = cum_sum / cnt
            for i in range(corrupt_cnt):
                cum_sum += r
        #cum_sum = cum_sum ** (1 / 2)
        return cum_sum
    raise NotImplementedError()


def euclidean_dist(r1, r2):
    # r1 in r2 sta stevilcna vektorja, ki lahko vsebujeta NAN vrednosti.
    # To resimo s normalizacijo koncne pridobljene sume.
    # V kolikor si vektorja nista enako dolga, to resimo na taksen nacin, da vrednosti, ki bi jih morali primerjati na
    # neenakih mestih pretiramo enako kot primerjave s NAN vnosi.
    cum_sum = 0
    cnt = 0
    corrupt_cnt = 0
    if len(r1) == len(r2):
        for i in range(len(r1)):
            if (r1[i] == r1[i]) and (r2[i] == r2[i]):
                cum_sum += (r1[i] - r2[i])**2
                cnt += 1
            else:
                corrupt_cnt += 1
        if cnt == 0:
            return float("nan")

        if corrupt_cnt > 0:
            r = cum_sum/cnt
            for i in range(corrupt_cnt):
                cum_sum += r
        cum_sum = cum_sum ** (1/2)
        return cum_sum
    elif len(r1) < len(r2):
        for i in range(len(r1)):
            if (r1[i] == r1[i]) and (r2[i] == r2[i]):
                cum_sum += (r1[i] - r2[i])**2
                cnt += 1
        cum_sum = cum_sum ** (1/2)
        return cum_sum
    else:
        for i in range(len(r1)):
            if (r1[i] == r1[i]) and (r2[i] == r2[i]):
                cum_sum += (r1[i] - r2[i])**2
                cnt += 1
        cum_sum = cum_sum ** (1/2)
        return cum_sum
    raise NotImplementedError()


def single_linkage(c1, c2, distance_fn):
    """ Arguments c1 and c2 are lists of lists of numbers
    (lists of input vectors or rows).
    Argument distance_fn is a function that can compute
    a distance between two vectors (like manhattan_dist)."""
    d,c = c2,c1
    c = 0
    running_min = float('inf')
    # Sprehod po listu
    if len(d) == len(c):
        v = len(d)
        for i in range(v):
            c = distance_fn(d[i],c[i])
        if (c == c) and (c < running_min):
                running_min = c
    elif len(d) > len(c):
        v = len(c)
        for i in range(v):
            c = distance_fn(d[i],c[i])
        if (c == c) and (c < running_min):
                running_min = c
    else: 
        v = len(d)
        for i in range(v):
            c = distance_fn(d[i],c[i])
            if (c == c) and (c < running_min):
                running_min = c
    if running_min == float('inf'):
        return float('NaN')
    
    return running_min
    
    raise NotImplementedError()


def complete_linkage(c1, c2, distance_fn):
     d,c = c2,c1
     c = 0
     running_max = float('-inf')
     if len(d) == len(c):
        v = len(d)
        for i in range(v):
            c = distance_fn(d[i],c[i])
        if (c == c) and (c > running_max):
                running_min = c
    elif len(d) > len(c):
        v = len(c)
        for i in range(v):
            c = distance_fn(d[i],c[i])
        if (c == c) and (c > running_min):
                running_min = c
    else: 
        v = len(d)
        for i in range(v):
            c = distance_fn(d[i],c[i])
            if (c == c) and (c > running_min):
                running_min = c
    if running_min == float('-inf'):
        return float('NaN')
    
    return running_min

    raise NotImplementedError()


def average_linkage(c1, c2, distance_fn):
    raise NotImplementedError()


class HierarchicalClustering:

    def __init__(self, cluster_dist, return_distances=False):
        # the function that measures distances clusters (lists of data vectors)
        self.cluster_dist = cluster_dist

        # if the results of run() also needs to include distances;
        # if true, each joined pair in also described by a distance.
        self.return_distances = return_distances

    def closest_clusters(self, data, clusters):
        """
        Return the closest pair of clusters and their distance.
        """
        raise NotImplementedError()

    def run(self, data):
        """
        Performs hierarchical clustering until there is only a single cluster left
        and return a recursive structure of clusters.
        """

        # clusters stores current clustering. It starts as a list of lists
        # of single elements, but then evolves into lists like
        # [[["Albert"], [["Branka"], ["Cene"]]], [["Nika"], ["Polona"]]]
        clusters = [[name] for name in data.keys()]

        while len(clusters) >= 2:
            first, second, distance = self.closest_clusters(data, clusters)
            # update the "clusters" variable
            raise NotImplementedError()

        return clusters


if __name__ == "__main__":

    data = {"a": [1, 2],
            "b": [2, 3],
            "c": [5, 5]}

    def average_linkage_w_manhattan(c1, c2):
        return average_linkage(c1, c2, manhattan_dist)

    hc = HierarchicalClustering(cluster_dist=average_linkage_w_manhattan)
    clusters = hc.run(data)
    print(clusters)  # [[['c'], [['a'], ['b']]]] (or equivalent)

    hc = HierarchicalClustering(cluster_dist=average_linkage_w_manhattan,
                                return_distances=True)
    clusters = hc.run(data)
    print(clusters)  # [[['c'], [['a'], ['b'], 2.0], 6.0]] (or equivalent)
