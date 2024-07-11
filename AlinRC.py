#Alineador de RC
from Bio import SeqIO
from Bio.Seq import Seq
def reorganizar_secuencia(secuencia):
    posicion_mas = secuencia.find("+")
    secuencia_reorganizada = secuencia[posicion_mas:] + secuencia[:posicion_mas]
    return secuencia_reorganizada

def reorganizar_archivo_fasta(archivo_entrada, archivo_salida):
    secuencias_reorganizadas = []

    for registro in SeqIO.parse(archivo_entrada, "fasta"):
        id_secuencia = registro.id
        secuencia_original = str(registro.seq)
        secuencia_reorganizada = reorganizar_secuencia(secuencia_original)
        secuencia_reorganizada = SeqIO.SeqRecord(Seq(secuencia_reorganizada), id=id_secuencia)
        secuencias_reorganizadas.append(secuencia_reorganizada)

    SeqIO.write(secuencias_reorganizadas, archivo_salida, "fasta")

archivo_entrada = ""
archivo_salida = archivo_entrada.replace(".fasta", "-a.fasta")
reorganizar_archivo_fasta(archivo_entrada, archivo_salida)
print(f"Archivo alineado guardado como {archivo_salida}")
