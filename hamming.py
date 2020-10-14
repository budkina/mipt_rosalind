f = open("rosalind_hamm.txt", "r")
dna1 = f.readline()
dna2 = f.readline()
f.close()

score = 0
for i,n in enumerate(dna1):
    if dna1[i]!=dna2[i]: 
        score+=1

f = open("rosalind_hamm_res.txt", "w")
f.write(str(score))
f.close()