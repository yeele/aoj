#https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

uf = UnionFind(6)
print(uf.parents)

uf.union(0, 2)












class unionfind():
    def __init__(self, n):
        self.n = n
        self.pars = [-1] * n # 親のindexか、自信が親の場合は-(要素数)

    def find(self, x):
        if self.pars[x] < 0:
            return x
        else:
            # 親が根元ではないので、根元を探す旅
            oya = self.pars[x]
            #　#これが経路圧縮。なくてもうごくよ。有ると速い。
            # self.pars[x] = self.find[oya]; return self.pars[x]
            return self.find(oya)

    def union(self, x, y):
        X = self.find(x) # Xはxの親である
        Y = self.find(y)
        if X == Y: return

        # 親のマージ。親のグループの小さい方に、大き方を足したいので。
        if self.pars[X] > self.pars[Y]:
            X, Y = Y, X

        self.pars[X] += self.pars[Y]
        self.pars[Y] = X
