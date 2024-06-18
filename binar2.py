
class binar2:
    def __init__(self, x):
        x = float(x)
        self.int = x
        print("Created!")

    def change_int(self):
        i = int(self.int)
        i = [int(a) for a in str(i)]
        i = i[::-1]
        m = 0
        q = 0
        for aaa in i:
            n = i[m]
            n = n * (2 ** q)
            i[m] = n
            m += 1
            q += 1

        g = []
        f = str(self.int)
        s_i, s_d = f.split('.')
        f = int(s_d)
        f = [int(a) for a in str(f)]
        r = 0
        s = -1
        for bbb in f:
            t = f[r]
            t = t * (2 ** s)
            f[r] = t
            r += 1
            s -= 1
        listsum = sum(i)
        listsum2 = sum(f)
        l = listsum + listsum2
        print(l)

bi = binar2(x = input())
print(bi)
bi.change_int()
