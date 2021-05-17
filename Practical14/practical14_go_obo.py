# Practical 14: Working with Information

"""
Approach:

In this practical, I designed two additional classes: Vertex & Graph to establish connections between
parent nodes & child nodes, which greatly enhanced the search efficiency.

Later I found out that this could also be accomplished using python dictionaries only, but I'd still like
to put my knowledge about graphs into practice in this practical.

Hope this won't bring any inconvenience comprehending my codes.
"""

# import modules
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

# assistant function for parsing xml file
def parse_xml(path):
    DOMTree = xml.dom.minidom.parse(path)
    collection = DOMTree.documentElement
    terms = collection.getElementsByTagName("term")
    return terms

# assistant function for getting the parent nodes (molecule_name in <defstr> of the parent nodes)
def get_primary_matches(terms, molecule_name):
    match_list = []
    for term in terms:
        defstr_text = term.getElementsByTagName("defstr")[0].childNodes[0]
        data = defstr_text.data
        if molecule_name in data:
            match_list.append(term)
    return match_list

# 2 assistant classes: Vertex & Graph to establish connection between nodes for faster search
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' \
               + str([x.id for x in self.connectedTo])

    def getConnection(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# assistant function to build tree of terms
def buildTree(terms):
    tree = Graph()
    for term in terms:
        id = term.getElementsByTagName("id")[0].childNodes[0].data
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
        for child in is_a:
            tree.addEdge(id, child)
    return tree

# assistant recursive function to find all childNodes as vertices
def getAllChildren(tree, vertices):
    allChildren = []
    for vertex in vertices:
        if vertex:
            if not vertex.connectedTo:
                allChildren.append(vertex)
            else:
                children = [vtx for vtx in vertex.connectedTo]
                allChildren.append(vertex)
                allChildren += getAllChildren(tree, children)
    return allChildren

# main function outputting the final result
def count_childNodes_macromolecules_xml(tree, molecule_name):
    match_list = get_primary_matches(terms, molecule_name)
    vertices_list = [tree.getVertex(term.getElementsByTagName("id")[0].childNodes[0].data) for term in match_list]
    # add back obsolete DNA related nodes which were subtracted twice
    obo_list = [term for term in match_list if term.getElementsByTagName("is_obsolete")]
    # calculate result
    result_list = list(set(getAllChildren(tree, vertices_list)))

    def final_result(result_list):
        connected_list = []
        ancestors = []
        for vertex in result_list:
            connected_list += list(vertex.connectedTo.keys())
        connected_list = list(set(connected_list))
        return len(connected_list)

    # final result
    count = final_result(result_list)
    return count

# define file path (absolute path)
path = "C:\\Users\\surface\\Documents\\Github\\IBI1_2020-21\\Practical14\\go_obo.xml"

# Parse the xml file
terms = parse_xml(path)

# build tree
tree = buildTree(terms)

# Calculate & print the data
dna = count_childNodes_macromolecules_xml(tree, "DNA")  # 8651
print("Number of childNodes of all DNA-associated terms: {}".format(dna))

rna = count_childNodes_macromolecules_xml(tree, "RNA")  # 11004
print("Number of childNodes of all RNA-associated terms: {}".format(rna))

protein = count_childNodes_macromolecules_xml(tree, "protein")  # 33459
print("Number of childNodes of all protein-associated terms: {}".format(protein))

carbo = count_childNodes_macromolecules_xml(tree, "carbohydrate")  # 4879
print("Number of childNodes of all carbohydrate-associated terms: {}".format(carbo))

# Plot the pie chart
data = {"DNA": dna, "RNA": rna,
        "Protein": protein, "Carbohydrate": carbo}
values = np.array([i for i in data.values()])
labels = np.array([j for j in data.keys()])
plt.pie(values, labels=labels, shadow=True, autopct='%1.1f%%')
plt.title("Percentage of Child Nodes of 4 Macromolecules")
plt.show()
