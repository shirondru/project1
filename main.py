from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    fasta_parser = FastaParser("data/test.fa")

    # Create instance of FastaParser
    fastq_parser = FastqParser("data/test.fq")


    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    print('*'*20)
    print('Parsing Fasta') #Add a print statement to console to help keep track of the print statements
    print('*'*20)
    for record in fasta_parser: #Have FastaParser loop through records in test.fa
        header = record[0] #first element of tuple returned by FastaParser is header
        seq = record[1] #second element of tuple returned by FastaParser is sequence
        transcribed_seq = transcribe(seq)
        reverse_transcribed_seq = reverse_transcribe(seq) 

        #print the record
        print(header)
        print(f"Transcribed: {transcribed_seq}") 
        print(f"Reverse Transcribed: {reverse_transcribed_seq}")
        print('\n')


    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    print('*'*20)
    print('Parsing Fastq')
    print('*'*20)
    for record in fastq_parser:
        header = record[0]
        seq = record[1]
        transcribed_seq = transcribe(seq)
        reverse_transcribed_seq = reverse_transcribe(seq)

        #print the record
        print(header)
        print(f"Transcribed: {transcribed_seq}") 
        print(f"Reverse Transcribed: {reverse_transcribed_seq}")
        print('\n')

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
