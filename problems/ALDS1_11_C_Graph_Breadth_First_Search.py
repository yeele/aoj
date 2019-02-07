#-*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C
"""
import itertools
import time
import logging
import sys

ANSWER={}


def input_from_txt(number=1):
    import requests
    url = "https://judgedat.u-aizu.ac.jp/testcases/ALDS1_11_C/%s/in" % number
    res = requests.get(url)
    input = res.text.split("\n")
    n = int(input[0])
    Ss = []
    for i in range(n):
        S = list(map(int, input[1+i].split()))
        Ss.append(S)
    return (n, Ss)

def input_array():
    n = int(input())
    Ss = []
    for i in range(n):
        S = list(map(int, input().split()))
        Ss.append(S)
    return (n, Ss)

def show_matrix(n, Ss):
    for i in range(n):
        vth = Ss[i][0]
        vd = Ss[i][1]
        adjs = Ss[i][2:]
        row = []
        for j in range(1, 1+n):
            if j in adjs: row.append(1)
            else: row.append(0)
        logging.info(" ".join(map(str, row)))

class Verticies:
    def __init__(self, id, value, degree, adjs:list):
        self.id = id
        self.value = value
        self.degree = degree
        self.parent = None
        self.weigth = 1
        self.score = sys.maxsize
        self.visited = []
        self.adjs = adjs

    def reset(self):
        self.parent = None
        self.score = sys.maxsize
        self.visited = []

    def visit(self, parent):
        logging.info("visiting id(%s)" % self.id)
        self.visited.append(parent)
        #print("visit: self.visited : %s" % self.visited)
        parent_score = parent.score if parent else 0
        if self.score > parent_score + self.weigth:
            self.score = parent_score + self.weigth if parent else 0
            self.setParent(parent)
            logging.info("parent updated!!!!!! with self.id(%s) with parent.id(%s)" % (self.id, parent.id if parent else parent))


    def setParent(self, parent):
        self.parent = parent

    def get_distance(self):
        d = 0
        p = self.parent
        while p!= None:
            d+=1
            p = p.parent
        return d

    def get_distance_to(self, dest):
        # dest: Vertices
        d = 0
        p = self.parent
        while p!= None:
            d+=1
            if p.id == dest.id: return d
            p = p.parent
        return -1

    def is_visited(self):
        return len(self.visited) > 0

    def is_visited_by(self, pre_verticies):
        #print("is_visited_by self.id(%s) pre_verticies.id(%s)" % (self.id, pre_verticies.id if pre_verticies else pre_verticies))
        #print("self.visited: %s" % self.visited)
        return pre_verticies in self.visited


def instanciate_vertex(V:list):
    vertex = {}
    for v in V:
        id = int(v[0])
        degree = v[1]
        adjs = v[2:]
        vertices = Verticies(id, 0, degree, adjs)
        vertex[id] = vertices
    # switch from string to Instance
    for id, vertices in vertex.items():
        vertex[id].adjs = [ vertex[i] for i in vertex[id].adjs]
    # sort by young id ascendence
    return sorted(list(vertex.values()), key=lambda v: v.id)



def bfs(vs: Verticies, pre: Verticies, ve: Verticies):
    logging.info("%sbfs(vs.id:%s, pre.id:%s, ve.id:%s)" % (
        ("  " * vs.get_distance()),
        vs.id, pre.id if pre else pre, ve.id)
    )
    logging.info("before: pre.score(%s) vs.weight(%s) vs.score(%s)" % (pre.score if pre else pre, vs.weigth, vs.score))
    vs.visit(pre)
    logging.info("after : pre.score(%s) vs.weight(%s) vs.score(%s)" % (pre.score if pre else pre, vs.weigth, vs.score))
    if vs.id != ve.id:
        for next_v in vs.adjs:
            if not next_v.is_visited_by(vs):
                bfs(next_v, vs, ve)



def find_shortest_by_bfs(vs: Verticies, ve: Verticies):

    # 1.  BFS
    # 2.  Check each time
    # 2a. if reached End Verticies, check the distance
    bfs(vs, None, ve)


def find_shortest(vertex:list, id=1):
    v_start = None
    for v in vertex:
        if v.id == id:
            v_start = v
            break

    for v in vertex:
        logging.debug("===== start jorney to find distance for form %s to %s====" % (v_start.id, v.id))
        find_shortest_by_bfs(v_start, v)
        d = v.score if v.score != sys.maxsize else -1
        print("%s %s" % (v.id, d))

        for v in vertex: v.reset() # Reset everytime


if __name__ == '__main__':
    """
    なんか、visitedとか一回一回リセットしないといけないので、
    逆にこのオブジェクトのデータ構造がネックになっている気がしたので、
    v２はベタ書きをします
    """
    logging.getLogger().setLevel(logging.ERROR)
    mode = "prod"
    #mode = "test"
    if mode == "test":
        #logging.getLogger().setLevel(logging.INFO)
        #logging.getLogger().setLevel(logging.DEBUG)
        (n, Ss) = input_from_txt(3)
        show_matrix(n, Ss)
    else:
        (n, Ss) = input_array()

    vertex = instanciate_vertex(Ss)
    logging.debug(vertex)
    find_shortest(vertex, 1)
    from collections import OrderedDict
    for id, d, f in OrderedDict(sorted(ANSWER.items())).values():
        print("%s %s %s" % (id, d, f))
    #dfs_all(vertex)


