
class binar:
    def __init__(self, x):
        x = float(x)
        self.int = x
        print("Created!")

    def change_int(self):
        l = []
        i = int(self.int)
        f = self.int - int(self.int)
        if i == 0:
            l.append(i)
        else:
            while i != 0:
                  j = i % 2
                  i = i // 2
                  l.append(j)
        l = l[::-1]

        while f != 0:
              f = f * 2
              i = int(f)
              f = f - int(f)
              l.append(i)
        l = ','.join(map(str, l))
        l = l.replace(",", "")
        print(l)

bi = binar(x = input())
print(bi)
bi.change_int()
