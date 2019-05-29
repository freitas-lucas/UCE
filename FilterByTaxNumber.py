#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# UCEs fasta files list in a specific directory. One file = one UCEs locus.
fasta_list = os.listdir("/path/to/uces/")

# Loop to remove UCEs loci with less than 19 species/individuals.
for fasta_file in fasta_list:
	dic_fasta = {}
	arquivo = open("/path/to/uces/" + str(fasta_file), "r")
	for line in arquivo:
		line = line.rstrip()
		if line.startswith(">"):
			seq_name = line[1:]
			dic_fasta[seq_name] = ""
		else:
			dic_fasta[seq_name] = dic_fasta[seq_name] + str(line)

	if len(dic_fasta) >= 18:
		new_fasta = open("/path/to/filtered/uces/" + str(fasta_file), "w")
		for key, value in dic_fasta.iteritems():
			new_fasta.write(">" + str(key) + "\n")
			new_fasta.write(str(value) + "\n")
		new_fasta.close()
	else:
		pass
