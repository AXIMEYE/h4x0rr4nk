import string

# accept T
T = int(raw_input()) # number of test cases

count = 0
while count < T:
    # accept R, C
    R, C = map(int, raw_input().split())

    # accept grid G
    G = []
    i = 1
    while i <= R:
        input = raw_input()
        G.append(input)
        i = i + 1

    # convert strings into ints
    print 'G:', G

    # accept r, c
    r, c = map(int, raw_input().split())

    # accept pattern P
    P = []
    i = 1
    while i <= r:
        input = raw_input()
        P.append(input)
        i = i + 1

    # convert string into ints
    print 'P:', P

    # check if pattern P exists in grid G
    isPinG = "YES"
    i = 0
    while i < R:
        isPinG = "YES"
        j = i
        k = 0
        while k < r:
            if P[k] not in G[j]:
                isPinG = "NO"
                print "why is this getting executed?"
                print 'i:', i
                print 'k:', k
                print 'P[k]:', P[k]
                print 'G[j]:', G[j]
                break
            else:
                print "this is normal"
                print 'i:', i
                print 'k:', k
                print 'P[k]:', P[k]
                print 'G[j]:', G[j]
                k += 1
                j += 1
        if isPinG:
            break
        i += 1

    print isPinG

    count += 1