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

NAN = float("nan")

dist = euclidean_dist([1,2,NAN], [1,3,5])
print(dist)
dist = euclidean_dist([1,2,NAN], [1,3,NAN])
print(dist)
dist = euclidean_dist([NAN,2,NAN], [1,3,NAN])
print(dist)
dist = euclidean_dist([1,NAN,NAN], [NAN,3,5])
print(dist)

