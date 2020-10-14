f = open("rosalind_rna.txt", "r")
dna = f.read()
f.close()

rna=dna.replace('T','U')
f = open("rosalind_rna_res.txt", "w")
f.write(rna)
f.close()