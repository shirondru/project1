# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """

    assert "U" not in seq, "Input Sequence is not DNA"

    seq = seq.upper() # Force all seqs to be capitalized
    seq = seq.replace("T","U") # replace T with U
    return seq

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    assert "U" not in seq, "Input Sequence is not DNA"

    seq = seq.upper() # Force all seqs to be capitalized
    seq = seq.replace("T","U") # replace T with U
    seq = seq[::-1] #reverse seq
    return seq

