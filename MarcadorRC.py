#Marcador de la RC
from Bio import SeqIO
from Bio.Seq import Seq

def modificar_secuencia(secuencia):
    motif = "ggggttggtgta"
    if motif in secuencia.lower():
        posicion_g = secuencia.lower().find(motif)

        # Colocar "+" 120 posiciones a la izquierda del primer nucleótido del motif
        posicion_mas = (posicion_g - 120) % len(secuencia)
        secuencia = secuencia[:posicion_mas] + "+" + secuencia[posicion_mas:]

        # Colocar "-" 6 posiciones a la derecha del nucleótido "a"
        posicion_a = secuencia.lower().find("a", posicion_g)
        posicion_menos = (posicion_a + 7) % len(secuencia)
        secuencia = secuencia[:posicion_menos] + "-" + secuencia[posicion_menos:]

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
archivo_salida = archivo_entrada.replace(".fasta", "-c.fasta")
# Modificar el archivo FASTA
modificar_archivo_fasta(archivo_entrada, archivo_salida)
print(f"Archivo modificado guardado como {archivo_salida}")
