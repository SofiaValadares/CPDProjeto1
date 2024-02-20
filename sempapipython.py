import time

def OnMult(m_ar, m_br):
    pha = [1.0] * (m_ar * m_ar)
    phb = [0.0] * (m_br * m_br)
    phc = [0.0] * (m_ar * m_ar)

    for i in range(m_br):
        for j in range(m_br):
            phb[i*m_br + j] = i + 1.0

    Time1 = time.time()


    for i in range(m_ar):
        for j in range(m_br):
            temp = 0

            for k in range(m_ar):
                temp += pha[i*m_ar + k] * phb[k*m_br + j]

            phc[i*m_ar + j] = temp


    Time2 = time.time()
    #print(f"Time: {Time2 - Time1} seconds")
    print(f"Time: {((Time2 - Time1)):.3f} seconds\n")


    print("Result matrix: ")
    for i in range(1):
        for j in range(min(10, m_br)):
            print("{:.0f}".format(phc[j]), end=" ")
        print()


def OnMultLine(m_ar, m_br):
    pha = [1.0] * (m_ar * m_ar)
    phb = [0.0] * (m_br * m_br)
    phc = [0.0] * (m_ar * m_ar)

    for i in range(m_br):
        for j in range(m_br):
            phb[i*m_br + j] = i + 1.0

    Time1 = time.time()
    

    for i in range(m_ar):
        for j in range(m_ar):
            for k in range(m_br):
                phc[i*m_ar + k] += pha[i*m_ar + k] * phb[j*m_ar + k]


    
    Time2 = time.time()
    #print(f"Time: {Time2 - Time1} seconds")
    print(f"Time: {((Time2 - Time1)):.3f} seconds\n")


    print("Result matrix: ")
    for i in range(1):
        for j in range(min(10, m_br)):
            print("{:.0f}".format(phc[j]), end=" ")
        print()


def OnMultBlock(m_ar, m_br, bkSize):
    pha = [1.0] * (m_ar * m_ar)
    phb = [0.0] * (m_br * m_br)
    phc = [0.0] * (m_ar * m_ar)

    for i in range(m_br):
        for j in range(m_br):
            phb[i*m_br + j] = i + 1.0

    Time1 = time.time()


    for ib in range(0, m_ar, bkSize):
        for jb in range(0, m_br, bkSize):
            for kb in range(0, m_ar, bkSize):
                for i in range(ib, min(ib+bkSize, m_ar), 1):
                    for j in range(jb, min(jb+bkSize, m_ar), 1):
                        for k in range(kb, min(kb+bkSize, m_ar), 1):
                            phc[i*m_ar + j] += pha[i*m_ar + k] * phb[k*m_br + j]
    

    Time2 = time.time()
    #print(f"Time: {Time2 - Time1} seconds")
    print(f"Time: {((Time2 - Time1)):.3f} seconds\n")


    print("Result matrix: ")
    for i in range(1):
        for j in range(min(10, m_br)):
            print("{:.0f}".format(phc[j]), end=" ")
        print()
        
        
#MAIN

c = ''

while True:
    print("\n1. Multiplication")
    print("2. Line Multiplication")
    print("3. Block Multiplication")
    op = int(input("Selection?: "))

    if op == 0:
        break

    lin = int(input("Dimensions: lins=cols ? "))
    col = lin

    if op == 1:
        OnMult(lin, col)
    elif op == 2:
        OnMultLine(lin, col)
    elif op == 3:
        blockSize = int(input("Block Size? "))
        OnMultBlock(lin, col, blockSize)
