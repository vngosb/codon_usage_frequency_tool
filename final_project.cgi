#!/usr/local/bin/python3

import sys, jinja2, cgi, json, mysql.connector

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader(searchpath="./")

# This creates environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('final_project_template.html')

# Get the DNA sequence from the form data
form = cgi.FieldStorage()
dna = form.getvalue("dna")
dna = dna.strip()

protein = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
           "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
           "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
           "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
           "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
           "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
           "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "TAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
           "TAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
           "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
           "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "TGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
           "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
           }

protein_sequence = ""
triplet_counts = {}
total_triplets = 0
tuple_list = []

# Generate protein sequence and count triplets
for i in range(0, len(dna)-(len(dna)%3), 3):
    codon = dna[i:i+3]
    protein_sequence += protein.get(codon, "-")  # Use '-' if codon not in dictionary
    if codon in triplet_counts:
        triplet_counts[codon] += 1
    else:
        triplet_counts[codon] = 1
    total_triplets += 1

# Calculate triplet frequencies
for triplet, count in triplet_counts.items():
    frequency = count / total_triplets
    protein_name = protein[triplet]
    triplet_tuple = (triplet, protein_name, count, frequency)
    tuple_list.append(triplet_tuple)

# Generate the data in a dictionary format
result_data = {
    "protein_sequence": protein_sequence,
    "data": tuple_list
}

# Generate the JSON response
json_response = json.dumps(result_data)

# Print the JSON response
print("Content-Type: application/json\n\n")
print(json_response)
