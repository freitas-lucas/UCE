import os

fasta_list = os.listdir("/path/to/filtered/uces/")

for fasta_file in fasta_list:
	dic_fasta = {}
	arquivo = open("/path/to/filtered/uces/" + str(fasta_file), "r")
	for line in arquivo:
		line = line.rstrip()
		if line.startswith(">"):
			seq_name = line[1:]
			dic_fasta[seq_name] = ""
		else:
			dic_fasta[seq_name] = dic_fasta[seq_name] + str(line)

	if len(dic_fasta) >= 18:
		new_fasta = open("/path/to/filtered/uces/taxons/" + str(fasta_file), "w")
		for key, value in dic_fasta.iteritems():
			new_fasta.write(">" + str(key) + "\n")
			new_fasta.write(str(value) + "\n")
		new_fasta.close()
	else:
		pass