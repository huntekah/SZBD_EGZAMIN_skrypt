## Script test's Transactions for RC, ACA, ST and CSR

## Skrypt przystosowany do egzaminu na Politechnice Poznańskiej z Baz Danych 2.
## Program nie powinien być case sensitive, jednak należy trzymać się notacji z zadania.
# przykładowy input:

# input
# w2(a) r1(b) c1 r3(a) c2 c3

# output:
# RC: True
# ACA: False
# ST: False
# CSR: True

# input
# r3(c) r1(c) r3(c) w2(b) c2 c1 r3(a) w3(b) w3(c) c3

def test_RC(list):
    RC = True
    for i, e1 in enumerate(list):
        for j, e2 in enumerate(list):
            if i<j and e1[0] == 'w' and e2[0] == 'r' and e1[1] != e2[1] and e1[3] == e2[3]:
                for k, c1 in enumerate(list):
                    for l, c2 in enumerate(list):
                        if c1[0] == 'c' and c2[0] == 'c' and e1[1] == c1[1] and e2[1] == c2[1]:
                            if k>l:
                                RC = False
    return RC

def test_ACA(list):
    ACA = True
    for i, w1 in enumerate(list):
        for j, r1 in enumerate(list):
            if i < j and w1[0] == 'w' and r1[0] == 'r' and r1[1] != w1[1] and r1[3] == w1[3]:

                for k, c1 in enumerate(list):
                        if c1[0] == 'c' and w1[1] == c1[1]:
                            if j < k:
                                ACA = False
    return ACA

def test_ST(list):
    ST = True
    for i, e1 in enumerate(list):
        for j, w2 in enumerate(list):
            if j < i and (e1[0] == 'w' or e1[0] == 'r') and w2[0] == 'w' and e1[1] != w2[1] and e1[3] == w2[3]:

                for k, c1 in enumerate(list):
                        if c1[0] == 'c' and w2[1] == c1[1]:
                            if i < k:
                                ST = False
    return ST

#r2(c) r1(a) r3(c) w1(b) r2(a) w2(c) w2(a) r2(a) w3(a) c2 c3 c1
def test_CSR(list):
    kolejnosc = []
    read_f = False
    for i, e1 in enumerate(list):
        alter_kol = ''
        read_f = False
        if e1[0] == 'r':
            read_f = True
        if e1[0] != 'c':
            for j, e2 in enumerate(list):
                if not(e2[0] == 'c') and not(read_f == True and e2[0] == 'r') and e1[3] == e2[3] and i<j:
                    alter_kol+=e2[1]
            kolejnosc.append(alter_kol)
    CSR = True
    for order1 in kolejnosc:
        for order2 in kolejnosc:
            for i, t11 in enumerate(order1):
                for j, t12 in enumerate(order1):
                    for k, t21 in enumerate(order2):
                        for l, t22 in enumerate(order2):
                            if t11 == t22 and t12 == t21 and i<j and k<l:
                                CSR = False
                                #print("CSR: " + str(kolejnosc))
                                return CSR
    #print("CSR: " + str(kolejnosc))
    return CSR


def test_Transaction():
    H = input()
    operations = [str(x).lower() for x in H.split()]
    print("RC: "+str(test_RC(operations)))
    print("ACA: "+str(test_ACA(operations)))
    print("ST: "+str(test_ST(operations)))
    print("CSR: " + str(test_CSR(operations)))


test_Transaction()
