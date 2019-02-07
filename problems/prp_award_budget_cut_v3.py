"""
grantsArray = [2, 100, 50, 120, 1000]
  newBudget = 190

  ans = cap
  condition: most people should recieve cap,
             least people recieve less cap.
             cap should be maximum

  190/5 = 38 --> 5 impacted
  190/4 = 47 --> 4
  190-(50+2)/3 = 46 -> 3 impacted [2, 46, 50, 46, 46]
"""
import sys
def find_grants_cap2(grants, newBudget):
    print(grants)
    grants.sort(key=int)
    print(grants)
    ans = -1
    affected = len(grants)
    for i, award in enumerate(grants):
        # todo: adjust double
        avg = (newBudget - sum(grants[:i])) / len(grants[i:])
        print("avg:%s" % avg)
        avg = int(avg)
        print(i, avg)
        print(avg * len(grants[i:]), sum(grants[:i]), newBudget)
        if avg * len(grants[i:]) + sum(grants[:i]) == newBudget:
            print(grants[:i] + [avg] * len(grants[i:]))
            if len(grants)-i < affected:
                affected = len(grants)-i
                ans = avg
    return ans

def find_grants_cap(S, new_budget):
    S.sort()
    print(S)
    cap = new_budget/(len(S)*1.0)
    ttl = 0
    for i, s in enumerate(S):
        ttl += s
        rest = (len(S) -1 - i)*1.0
        if rest == 0: break
        tmp_cap = (new_budget - ttl)/rest
        print("i:%s, s:%s, cap:%s, ttl:%s, tmp_cap:%s" % (i, s, cap, ttl, tmp_cap))
        if s > cap:
            break
        cap = tmp_cap
    return cap







grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190

grantsArray = [2, 4]
newBudget = 3

grantsArray = [2,100,50,120,167]
newBudget = 400

grantsArray = [21, 50, 100, 110, 120, 130]
newBudget = 140
print(find_grants_cap(grantsArray, newBudget) )

