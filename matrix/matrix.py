
def hisla(a1):
    a1 = list(''.join(a1))
    a1.append(" ")

    x = 0
    y = 0
    A = []

    dl = len(a1) - 1

    while dl > 0:
        w = ''
        z = 0
        while str(a1[x]) != " ":
            w += a1[x]
            x += 1
            dl -= 1
            if a1[x] =='^':
                z = 1
        if z ==1:
            ''.join(a1)
        if w != '' and w != " ":
            A.append(int(w))
            dl -= 1
        else:
            x += 1
        y += 1
    return A

def pr():
    o = 0
    while o < Rmat_1[0]:
        y = Rmat_1[1]
        print(rezult[o*y:(o+1)*y])
        o += 1

znak1 = list(''.join(input('Введите действие над матрицами:')))
#Rmat_1 = hisla(input('Введите размер матрицы:'))
#mat_1 = hisla(input('Введите матрицу:'))



mat_x = []


m = 0
n = 1
while m < len(znak1)+1:
    mat_x.append(hisla(input('Введите размер матрицы '+str(m+1)+':')))
    mat_x.append(hisla(input('Введите матрицу '+str(m+1)+':')))
    m+=1
print(mat_x)
mat_1 = mat_x[1]
Rmat_1 = mat_x[0]
mat_2 = mat_x[3]
Rmat_2 = mat_x[2]
kon = 0
if Rmat_2 == []:
    Rmat_2.append(Rmat_1[0])
    Rmat_2.append(Rmat_1[1])
    kon = 1


m = 0
p = 2
while m < len(znak1):
    rezult = []
    #print(Rmat_2)
    #Rmat_1[0] = Rmat_2[0]
    #Rmat_1[1] = Rmat_2[1]
    # print(Rmat_1)
    Rmat_2 = mat_x[p]
    p += 1
    mat_2 = mat_x[p]
    p += 1
    znak = str(znak1[m])

    #print(mat_1,mat_2)
    print(Rmat_1,Rmat_2)
    if znak == '+':
        e = 0
        v = len(mat_1)
        while v > 0:
            rezult.append(int(mat_1[e]) + int(mat_2[e]))
            v -= 1
            e += 1
        pr()

    if znak == '-':

        e = 0
        v = len(mat_1)
        while v > 0:
            rezult.append(int(mat_1[e]) - int(mat_2[e]))
            v -= 1
            e += 1
        pr()

    if znak == '*':
        if kon == 1:
            s = 0
            while s < Rmat_1[0]*Rmat_1[1]:
                rezult.append(mat_1[s]*mat_2[0])
                s+=1
            pr()
        else:
            v = Rmat_1[0]
            h = 0
            r =0
            while v > 0:
                o = 0
                l = 0
                d=0
                while o < Rmat_2[0]*Rmat_2[1]:
                    r += ((mat_1[l + Rmat_1[1]*h])* mat_2[Rmat_2[1]*l+d])
                    l+=1
                    if l >= Rmat_2[0]:

                        l = 0
                        d+=1
                        rezult.append(r)
                        print(rezult)
                        r = 0

                    o += 1
                h += 1
                if h >= Rmat_1[0]:
                    h = 0
                v -= 1

            u = 0
            while u < Rmat_1[0]:
                y = Rmat_2[1]
                print(rezult[u * y:(u + 1) * y])
                u += 1

    if znak == 'o':
        if Rmat_1[0] == 2:
            print(mat_1[0]*mat_1[3]-mat_1[1] * mat_1[2])

        elif Rmat_1[0] == 3:
            a = mat_1
            print(a[0]*a[4]*a[8]+a[1]*a[5]*a[6]+a[3]*a[7]*a[2]-a[2]*a[4]*a[6]-a[1]*a[3]*a[8]-a[5]*a[7]*a[0])

    del mat_1
    mat_1 = rezult
    del rezult
    m += 1
