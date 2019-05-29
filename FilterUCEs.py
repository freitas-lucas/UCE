#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

fasta_list = os.listdir("/path/to/uces/")

dic_fastas = {}

for fasta_file in fasta_list:
	arquivo = open("/path/to/uces/" + str(fasta_file), "r")
	for line in arquivo:
		line = line.rstrip("\r\n")
		if line.startswith(">"):
			seq_name = line[1:] 
			dic_fastas[seq_name] = ""
		else:
			dic_fastas[seq_name] = dic_fastas[seq_name] + str(line)

dic_uces = {}

for key, value in dic_fastas.iteritems():
	match = re.search(".*_(uce-[0-9]+)", key)
	if match.group(1) in dic_uces:
		dic_uces[match.group(1)] += 1
	else:
		dic_uces[match.group(1)] = 1

count_uces = 0
for chave, valor in dic_uces.iteritems():
	if valor == 23:
		count_uces += 1

print count_uces


for key, value in dic_fastas.iteritems():
	match = re.search(".*_(uce-[0-9]+)", key)
	if "G1_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")			
			new_file.write(">" + "G1_Spheniscus_mendiculus" + "\n") 
			new_file.write(str(value) + "\n")
	elif "G2_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G2_Spheniscus_humboldti" + "\n")
			new_file.write(str(value) + "\n")
	elif "G3_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G3_Spheniscus_magellanicus" + "\n")
			new_file.write(str(value) + "\n")
	elif "G4_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G4_Pygoscelis_papua-Antarctica" + "\n")
			new_file.write(str(value) + "\n")
	elif "G5_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G5_Pygoscelis_papua-Falkland" + "\n")
			new_file.write(str(value) + "\n")
	elif "G6_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G6_Pygoscelis_papua-Kerguelen" + "\n")
			new_file.write(str(value) + "\n")
	elif "G7_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G7_Pygoscelis_papua-Crozet" + "\n")
			new_file.write(str(value) + "\n")
	elif "G8_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G8_Pygoscelis_antarcticus" + "\n")
			new_file.write(str(value) + "\n")
	elif "G9_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G9_Pygoscelis_adeliae" + "\n")
			new_file.write(str(value) + "\n")
	elif "G10_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G10_Aptenodytes_patagonicus" + "\n")
			new_file.write(str(value) + "\n")
	elif "G11_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G11_Eudyptes_schlegeli" + "\n")
			new_file.write(str(value) + "\n")
	elif "G12_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G12_Eudyptes_chrysolophus-Marion" + "\n")
			new_file.write(str(value) + "\n")
	elif "G13_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G13_Eudyptes_filholi" + "\n")
			new_file.write(str(value) + "\n")
	elif "G14_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G14_Eudyptes_chrysocome" + "\n")
			new_file.write(str(value) + "\n")
	elif "G15_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G15_Eudyptes_moseleyi" + "\n")
			new_file.write(str(value) + "\n")
	elif "G16_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G16_Eudyptula_minor" + "\n")
			new_file.write(str(value) + "\n")
	elif "G17_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G17_Eudyptes_chrysolophus-Elephant" + "\n")
			new_file.write(str(value) + "\n")
	elif "G18_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G18_Eudyptes_pachyrhynchus" + "\n")
			new_file.write(str(value) + "\n")
	elif "G19_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G19_Eudyptes_sclateri" + "\n")
			new_file.write(str(value) + "\n")
	elif "G20_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G20_Aptenodytes_forsteri" + "\n")
			new_file.write(str(value) + "\n")
	elif "G21_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G21_Spheniscus_demersus" + "\n")
			new_file.write(str(value) + "\n")
	elif "G22_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G22_Megadyptes_antipodes" + "\n")
			new_file.write(str(value) + "\n")
	elif "G23_" in key:
		count_n = 0
		for char in value:
			if char == "N" or char == "n":
				count_n += 1
			else:
				pass
		if count_n < 2:
			new_file = open("/path/to/filtered/uces/" + str(match.group(1)) + ".fasta", "a")
			new_file.write(">" + "G23_Macronectes_giganteus" + "\n")
			new_file.write(str(value) + "\n")
	new_file.close()
#"""
	
