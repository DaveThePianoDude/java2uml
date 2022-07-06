import os
import argparse
import sys
from bisect import bisect

def prune(word, char):
    return word.split(char)[0]

def getRelations(relations, relation):
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
                                    if word == relation:
                                        target_ind = ind+1
                                        name = prune(name,'.')
                                        while True:
                                            repeater = False
                                            word = prune(words[target_ind],'<')
                                            if (words[target_ind][:-1] == ','):
                                                repeater = True
                                            word = prune(words[target_ind],',')
                                            tuple = name, word, relation
                                            relations.add(tuple)
                                            ind +=1
                                            if repeater == False:
                                                break;
                                    ind += 1
                        except Exception as e:
                            print(e)

def writeGviz(relations, outfile):
    with open(os.path.join(outfile), "w") as out_file:
        try:
            out_file.write("digraph unix {\n")
            out_file.write("	fontname=\"Helvetica,Arial,sans-serif\"\n")
            out_file.write("node [fontname=\"Helvetica,Arial,sans-serif\"]\n")
            out_file.write("edge [fontname=\"Helvetica,Arial,sans-serif\"]\n")
            out_file.write("node [color=lightblue2, style=filled];\n")

            result = {}
            for tuple in relations:
                result[tuple[0]] = str(tuple[1]) + " " + str(tuple[2])
            #for entry in sorted(result.items()):
                #print(entry)

            for entry in sorted(result.items()):
                try:
                    out_file.write("\""+ str(entry[0]) + "\"" + "->" + "\"" + str(entry[1]).split(" ")[0] + "\" [ label = \"" + str(entry[1]).split(" ")[1] + "\" ];\n")
                except Exception as e:
                    print(e)

            out_file.write("}")
        except Exception as e:
            print(e)


if __name__ == '__main__':

    relations = set()

    getRelations(relations, "implements")
    getRelations(relations, "extends")
    writeGviz(relations, "output.gv")
    print("DONE")
