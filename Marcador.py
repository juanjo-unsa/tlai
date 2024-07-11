!pip install biopython
#Marcador de CSB3
from Bio import SeqIO
from Bio.Seq import Seq

def modificar_secuencia(secuencia):
    motif = "GGGGTTGGTGTA"
    if motif in secuencia:
        primera_coincidencia = secuencia.find(motif)
        secuencia_modificada = secuencia[:primera_coincidencia] + motif.lower() + secuencia[primera_coincidencia + len(motif):]
        return secuencia_modificada
    else:
        return secuencia

def modificar_archivo_fasta(archivo_entrada, archivo_salida):
    secuencias_modificadas = []

    # Leer el archivo FASTA
    for registro in SeqIO.parse(archivo_entrada, "fasta"):
        id_secuencia = registro.id
        secuencia_original = str(registro.seq)
        secuencia_modificada = modificar_secuencia(secuencia_original)
        secuencia_modificada = SeqIO.SeqRecord(Seq(secuencia_modificada), id=id_secuencia)
        secuencias_modificadas.append(secuencia_modificada)

    # Guardar el archivo modificado
    SeqIO.write(secuencias_modificadas, archivo_salida, "fasta")

# Nombre del archivo de entrada
archivo_entrada = ""

# Nombre del archivo de salida
archivo_salida = archivo_entrada.replace(".fasta", "-m.fasta")
