#-*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B
"""
import itertools

import logging

def input_from_txt(number=1):
    import requests
    url = "https://judgedat.u-aizu.ac.jp/testcases/ALDS1_11_B/%s/in" % number
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
        logging.debug(" ".join(map(str, row)))

class Verticies:
    def __init__(self, id, value, degree, adjs:list):
        self.id = id
        self.value = value
        self.degree = degree
        self.d = 0 # timesamp
        self.f = 0 # timesamp
        self.adjs = adjs

    def visit(self, ts):
        logging.debug("miso0a: visiting id(%s)" % self.id)
        if not self.is_visited():
            self.d = ts
            logging.debug("visited id(%s) and ts stamped as %s" % (self.id, ts))
            logging.info("id:%s d:%s f:%s (preorder)" % (self.id, self.d, self.f))
            ts+=1
            logging.debug("miso1: ts incremented as %s" % ts)
        if self.adjs_all_visited() and not self.adjs_all_stamped():
            logging.debug("miso2")
            self.f = ts
            logging.info("visited all adjs(%s) of %s and ts stamped as %s" % ([x.id for x in self.adjs], self.id, ts))
            logging.info("id:%s d:%s f:%s" % (self.id, self.d, self.f))
            ts+=1
            logging.debug("miso2a: ts incremented as %s" % ts)
        return ts

    def is_visited(self):
        logging.debug ("miso9: id(%s) is_visited: %s(%s)" % (self.id, not self.d == 0, self.d))
        return (not self.d == 0)

    def adjs_all_visited(self):
        visited = [v.is_visited() for v in self.adjs]
        logging.debug("miso5: %s" % self.adjs)
        logging.debug("miso(visited): %s" % visited)
        completed = all(visited)
        logging.debug("miso(completed): %s" % completed)
        return completed

    def adjs_all_stamped(self):
        stamped = [v.f != 0 for v in self.adjs]
        logging.debug("--- miso5 ---: %s" % [x.f for x in self.adjs])
        logging.debug("miso(stamped): %s" % stamped)
        completed = all(stamped)
        logging.debug("miso(completed): %s" % completed)
        return completed


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


def dfs_all(vertex: list):
    stack = vertex
    ts = 1
    while len(stack) > 0:
        vertices = stack.pop(0)
        ts = dfs(vertices, ts)

def dfs(v: Verticies, ts):
    logging.info ("====== START ======= v.id = %s" % v.id)
    if not v.is_visited():
        logging.debug ("====== Visit ======= v.id = %s" % v.id)
        ts = v.visit(ts)
        for next_v in v.adjs:
            logging.debug ("next!!!!= %s" % next_v.id)
            ts = dfs(next_v, ts)
            logging.debug ("====== re-Visit ======= v.id = %s" % v.id)
            ts = v.visit(ts)
    logging.debug ("====== last-Visit ======= v.id = %s" % v.id)
    ts = v.visit(ts)
    return ts


if __name__ == '__main__':
    """
    これはうまく動作していません
    """
    logging.getLogger().setLevel(logging.INFO)
    #logging.getLogger().setLevel(logging.DEBUG)
    mode = "test"
    if mode == "test":
        (n, Ss) = input_from_txt(1)
    else:
        (n, Ss) = input_array()

    show_matrix(n, Ss)
    vertex = instanciate_vertex(Ss)
    logging.debug(vertex)
    #dfs(vertex[0], 1)
    dfs_all(vertex)


