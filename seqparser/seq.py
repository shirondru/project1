# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement


    input  : A C T G A A C C C
             | | | | | | | | |
    output : U G A C U U G G G
    """

    assert "U" not in seq, "Input Sequence is not DNA" #Warn user they are attempting to transcribe RNA
    
    #map of nucleotides to complement, accounting for T->U in RNA. Replacing key with value will transcribe DNA -> RNA
    transcription_map = {
                    'C':'G',
                    'G':'C',
                    'T':'A',
                    'A':'U'
    }

    seq = seq.upper() # Force all seqs to be capitalized. In case given seq has weird casing
    new_seq = "" # This function is transcribing seq by building a new sequence base-by-base
    
    for base in seq:
        complement = transcription_map[base] #Get correct replacement nucleotide for the current nucleotide in the loop
        new_seq += complement #Add complement of original DNA nucleotide base to same position in new_seq. This accounts for T->U because transcription_map accounts for T->U
    

    return new_seq

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    input       : A C T G A A C C C
                  | | | | | | | | |
    transcribe  : U G A C U U G G G 

    output : G G G U U C A G U
    """
    rna = transcribe(seq) #first transcribe the sequence using function already defined
    reversed_rna = rna[::-1] #Reverse the seq. Slicing string with default start, default stop, and -1 step causes Python to start from the end and stop at the start, reversing the string
    return reversed_rna

