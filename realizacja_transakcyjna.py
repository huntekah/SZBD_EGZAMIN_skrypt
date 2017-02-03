

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

def test_Transaction():
    H = input()
    operations = [str(x).lower() for x in H.split()]
    print("RC: "+str(test_RC(operations)))
    print("ACA: "+str(test_ACA(operations)))
    print("ST: "+str(test_ST(operations)))

test_Transaction()
