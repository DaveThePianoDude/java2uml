import os
import argparse
import sys
from bisect import bisect


if __name__ == '__main__':

    relations = set()

    if (sys.argv[1] == '.'):
        for root, dir, files in os.walk(sys.argv[1]):
            for name in files:
                if '.java' in name:
                    #print(os.path.join(root,name))
                    with open(os.path.join(root,name), "r") as in_file:
                        try:
                            for line in in_file:
                                words = line.split()
                                ind = 0
                                target_ind = 0
                                for word in words:
                                    if word == sys.argv[2]:
                                        target_ind = ind+1
                                        print(words[target_ind])
                                        tuple = name, words[target_ind]
                                        relations.add(tuple)
                                    ind +=1
                        except Exception as e:
                            print(e)
    print (sys.getsizeof(relations))
    result = {}
    for tuple in relations:
        print(tuple)
        result[tuple[0]] = tuple[1]
    for entry in sorted(result.items()):
        print(entry)
