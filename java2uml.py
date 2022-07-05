import os
import argparse
import sys
from bisect import bisect

def getRelations(relations):
    if (sys.argv[1] == '.'):
        for root, dir, files in os.walk(sys.argv[1]):
            for name in files:
                if '.java' in name:
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

def writeGviz(relations, outfile):
    with open(os.path.join(outfile), "w") as out_file:
        try:
            out_file.write("digraph unix {\n")
            out_file.write("	fontname='Helvetica,Arial,sans-serif'\n")
            out_file.write("node [fontname='Helvetica,Arial,sans-serif']\n")
            out_file.write("edge [fontname='Helvetica,Arial,sans-serif']\n")
            out_file.write("node [color=lightblue2, style=filled];\n")

            result = {}
            for tuple in relations:
                result[tuple[0]] = tuple[1]
            for entry in sorted(result.items()):
                print(entry)

            for entry in sorted(result.items()):
                out_file.write("\""+ str(entry[0]) + "\"" + "->" + "\"" + str(entry[1] + "\"\n"))

            out_file.write("}")
        except Exception as e:
            print(e)


if __name__ == '__main__':

    relations = set()

    getRelations(relations)

    writeGviz(relations, "output.gv")
