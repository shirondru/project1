# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """

    assert "U" not in seq, "Input Sequence is not DNA" #Warn user they are attempting to transcribe RNA

    seq = seq.upper() # Force all seqs to be capitalized. In case givev seq has weird casing
    seq = seq.replace("T","U") # scans seq and replaces each T with a U
    return seq

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    assert "U" not in seq, "Input Sequence is not DNA" #Warn user they are attempting to transcribe RNA

    seq = seq.upper() # Force all seqs to be capitalized
    seq = seq.replace("T","U")# scans seq and replaces each T with a U
    seq = seq[::-1] #Slicing string with default start, default stop, and -1 step causes Python to start from the end and stop at the start, reversing the string
    return seq

