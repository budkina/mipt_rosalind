f = open("rosalind_revc.txt", "r")
dna = f.read()
f.close()

complement={'A':'T','T':'A','G':'C','C':'G'}
cdna=''
for n in dna:
	if n=='\n': break
	cdna=cdna+complement[n]
r_cdna=cdna[::-1]

f = open("rosalind_revc_res.txt", "w")
f.write(r_cdna)
f.close()