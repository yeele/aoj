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
def find_grants_cap(grantsArray, newBudget):
    cap = 2**31#sys.maxsize
    impacted = len(grantsArray)

    # 0, 1, 2, 3, 4, 5
    grantsArray.sort()
    for i in range(len(grantsArray)+1):
        if i ==0:
            tmp_cap = sum(grantsArray)/(len(grantsArray)-i)
        else:
            tmp_cap = sum(grantsArray[i:])/(len(grantsArray)-i) if (len(grantsArray)-i) > 0 else 1
        # validate
        tmp_impacted = len([g for g in grantsArray if g != tmp_cap])
        print(tmp_cap, tmp_impacted, impacted)
        if tmp_impacted < impacted:
            print("m1")
            impacted = tmp_impacted
            cap = tmp_cap
    return cap




grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
print(find_grants_cap(grantsArray, newBudget) )

