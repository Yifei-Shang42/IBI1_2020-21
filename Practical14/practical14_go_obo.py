# Practical 14: Working with Information

"""
All childNodes of the macromolecule-associated terms are counted
DUPLICATES NOT REMOVED
Therefore, childNodes numbers are larger than total term number
"""

# import modules
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

# define file path (absolute path)
path = "C:\\Users\\surface\\Documents\\Github\\IBI1_2020-21\\Practical14\\go_obo.xml"

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

# assistant function for all the children (including the parents from previous function)
def getAllChildren(term_id_dict, elements):
    allChildren = []
    for element in elements:
        is_a = element.getElementsByTagName("is_a")
        # basic condition: if current node has no children, total + 1
        if not is_a:
            allChildren.append(element)
        # get all children of the current node
        else:
            children_id = [child.childNodes[0].data for child in is_a]
            children = []
            for id in children_id:
                children.append(term_id_dict[id])
            # recursive method to count all children
            allChildren.append(element)
            allChildren += getAllChildren(term_id_dict, children)
    return allChildren

# main function outputting the final result
def count_childNodes_macromolecules_xml(terms, molecule_name):
    term_id_dict = {}
    for term in terms:
        id = term.getElementsByTagName("id")[0].childNodes[0].data
        term_id_dict[id] = term
    match_list = get_primary_matches(terms, molecule_name)
    count = len(getAllChildren(term_id_dict, match_list)) - len(match_list)
    return count

# Parse the xml file
terms = parse_xml(path)

# Calculate & print the data
dna = count_childNodes_macromolecules_xml(terms, "DNA")
rna = count_childNodes_macromolecules_xml(terms, "RNA")
protein = count_childNodes_macromolecules_xml(terms, "protein")
carbo = count_childNodes_macromolecules_xml(terms, "carbohydrate")

print("Number of childNodes of all DNA-associated terms: {}".format(dna))
print("Number of childNodes of all RNA-associated terms: {}".format(rna))
print("Number of childNodes of all protein-associated terms: {}".format(protein))
print("Number of childNodes of all carbohydrate-associated terms: {}".format(carbo))

# Plot the pie chart
data = {"DNA": dna, "RNA": rna,
        "Protein": protein, "Carbohydrate": carbo}
values = np.array([i for i in data.values()])
labels = np.array([j for j in data.keys()])
plt.pie(values, labels=labels, shadow=True, autopct='%1.1f%%')
plt.title("")
plt.show()
