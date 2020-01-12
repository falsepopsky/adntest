# El programa toma una secuencia de DNA 3' a 5' y lo traduce a un ARN mensajero 5' a 3'

file = open('sample_dna.txt', 'r')
dna = file.read()
print ("DNA: 3\'", dna, "5\'")
rnam = ""

for i in dna:
    if i == "G":
        rnam += "C"
    elif i == "A":
        rnam += "U"
    elif i == "T":
        rnam += "A"
    else:
        rnam += "G"

print ("RNAm: 5\'", rnam, "3\'")

rna_t = ""

for i in rnam:
    if i == "G":
        rna_t+= "C"
    elif i == "U":
        rna_t+= "A"
    elif i == "A":
        rna_t+= "U"
    else:
        rna_t+= "G"

print ("RNAt: 3\'", rna_t, "5\'")


#def dnatoRNAm(a,t,c,g)
#    if i == "a"


#def rnamtoRNAt()


#Transcripcion de DNA 5' a 3' a ARNm 3' a 5'





#Transcripcion de ARNm a aminoacidos

#primera letra [U,C,A,G]
#segunda letra [U,C,A,G]
#tercera letra [U,C,A,G]

# esenciales
#aaEscenciales [Val,Leu, Thr, Lys, Trp, His, Phe, Ile, Arg, Met]
#aaNoEscenciales [Ala, Pro, Gly, Ser, Cys, Asn, Gln, Tyr, Asp, Glu]