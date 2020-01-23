# El programa toma una secuencia de DNA 3' a 5' y lo traduce a un ARN mensajero 5' a 3'
import os.path as path

# Esta función se encarga de traducir 
def ARNm(dnadata):
  rnam = ""
  rna_t = ""
  for s in dnadata:
    if s == "G":
      rnam += "C"
    elif s == "A":
      rnam += "U"
    elif s == "T":
      rnam += "A"
    else:
      rnam += "G"
  print("RNAm: 5\'", rnam, "3\'")
  for s in rnam:
    if s == "G":
      rna_t+= "C"
    elif s == "U":
      rna_t+= "A"
    elif s == "A":
      rna_t+= "U"
    else:
      rna_t+= "G"
  print ("RNAt: 3\'", rna_t, "5\'")
  return ""


ifile = ('sample_dna.txt')
if path.exists('sample_dna.txt'):
    a = open(ifile, 'r')
    adn_saved = a.read()
    print ("DNA: 3\'", adn_saved, "5\'")
    adn = ARNm(adn_saved)
else:
    print("No hay muestra")
    data = str(input("Introduzca la secuencia genetica 3\' a 5\'"))
    print ("DNA: 3\'", data, "5\'")
    x = ARNm(data)
    print (x)

#Transcripcion de ARNm a aminoacidos

#primera letra [U,C,A,G]
#segunda letra [U,C,A,G]
#tercera letra [U,C,A,G]

# esenciales
#aaEscenciales [Val,Leu, Thr, Lys, Trp, His, Phe, Ile, Arg, Met]
#aaNoEscenciales [Ala, Pro, Gly, Ser, Cys, Asn, Gln, Tyr, Asp, Glu]