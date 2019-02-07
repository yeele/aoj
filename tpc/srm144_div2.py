"""
http://www.topcoder.com
"""
class Time:
    def solve(self, seconds):
        rest = seconds
        H = int(rest / 3600)
        rest -= (3600 * H)
        M = int(rest / 60)
        rest -= (60 * M)
        S = rest
        return "%d:%d:%d" % (H, M, S)

    def whatTime(self, seconds):
        return self.solve(seconds)



print(Time().solve(3661))