def fd(dictionary, path=None):
    #print("%s:path:%s" % (dictionary, path))
    ans = {}
    for k, v in dictionary.items():
        if isinstance(v, dict):
            #ans.update(fd(v, None if k == "" else k if path is None else path+"."+k))
            ans.update(fd(v, None if k == "" else k if path is None else path+"."+k if k != "" else path))
        else:
            ans.update({k if path is None else path+"."+k if k != "" else path: v})
    return ans

def flatten_dictionary(dictionary):
    """
    {
      "a": 2,
      "b": "foo"
    }

    "d" : "3",
    "e" : {
       "a" : "1"
    }
    """
    ans = {}
    return fd(dictionary, None)


e1 = {
    "a": 2,
    "b": "foo"
}
e2 = {
    "d" : "3",
    "e" : {
        "a" : "1"
    }
}

e3 = {
    "a" : {
        "bc" : {
            "f" : 3,
            "" : "this should be hidden",
            "def" : "hello"
        }
    },
    "d" : "3",
    "e" : {
        "a" : "1"
    }
}
e4 = {"":{"a":"1"},"b":"3"}

e5={"a":{"b":{"c":{"d":{"e":{"f":{"":"pramp"}}}}}}}
# print(flatten_dictionary(e1))
# print(flatten_dictionary(e2))
# print(flatten_dictionary(e4))
print(flatten_dictionary(e5))
