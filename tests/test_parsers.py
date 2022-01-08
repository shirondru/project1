# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import os
currentdir = os.getcwd() #GitHub/project1/




def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """

    #testing first 5 records of test.fa + last record of test.fa to also ensure the parser successfuly parses entire file
    #these expected outputs were created by manually copying and pasting from the test.fa file
    expected_outputs = {
        0 : ('seq0','TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'),
        1 : ('seq1','TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT'),
        2 : ('seq2','TGTAGAGGCATTATTAGAGTTTCGCCACAACGGGGGCCTGCTGATCAAATCAGAATTCGTACAATCGGTTCGGGAGACACGGCTCTAAAGATACCGCTAG'),
        3 : ('seq3','AATCCAGCGCGTGTTGTATCGAGCCCTTGGAAGTCGATGGTGTCTTTGGTGAAGGTCGATGAACTTCCTTGGCGAGGACAGCGAAGTTAATTGGTGGCGA'),
        4 : ('seq4','GGTAGGCGGCTGCATAACGCCCCTGAAGAGACAGGGGGTTAGAGGTTCTCCCCCATCGTTCACAGTGAAGAGTGTGAGAGGCACACTGAAGAACATTGAG'),
        99: ('seq99','CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA')
    }

    fasta_parser = FastaParser(os.path.join(currentdir,"data/test.fa")) #instantiate FastaParser Object with provided test.fa file
    for idx, record in enumerate(fasta_parser): #Loop through records in test.fa using FastaParser
        if idx in expected_outputs.keys(): # When loop idx in [0,1,2,3,4,99] 
            assert record == expected_outputs[idx] #Compare record returned by FastaParser to expected output for same record in the dictionary above





def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """

    #testing first 5 records of test.fq + last record of test.fq to also ensure the parser successfuly parses entire file
    #these expected outputs were created by manually copying and pasting from the test.fq file
    expected_outputs = {
        0 : ('seq0','TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG',"""*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32="""),
        1 : ('seq1','CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG',"""\'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,,:%0!<),%646<8#%"."-'*-0:.+*&$5!'8)(%3*+9/&/%=363*,6$20($97,\""""),
        2 : ('seq2','GATAAACTTCTATCACGAATACTGCGGGACCATGCAGTTGTCCCTCACCTCGATAGTTCAGGTCTTTTGGTTCTGAGCGATATTGGGCGCGTCACCACTG',"""1,758$,:7654/7<0%5/12%-3>-2.>$$443-,'9,5$;""%7**)-'%:**&;<35(!<1'.5>51)1%:9>4=(&+3$2!-.8!>=+1$:,*&9!"""),
        3 : ('seq3','TCTAGTGGCTGGCCAGAGACTCAATGAAATCATAGTATACATGGGACAGTGTCTAAATAAACTTGTCTCCTGAATTCTCGTAATCACTTATGGAGCAACG',"""$8=)$38.%2*93,21>8+#71!/<)/<8<=#6;3-,4!51-!*/;;>'<620.;<2;'1=2,(6>"'$2<&;);).(3#2%.<>$'49<,"+.6704=&"""),
        4 : ('seq4','TGTGAATATGCAGCCCGGTCCCTCGCAGTCATTGTTTTCCCCACTCCGTCCCACGTTCCCTTAGAGATAGCGCTGAGCTAGCATATAGCGGTTTGAAGGC',"""#8,9(-$..-;&1$(1#1)"9-4"4<+;:6/+7##<:,8%4''-)95-,-8*!9(60-##8%:+>'58**4"#(+-'-"&)49"209,''1-+&=7;.&&"""),
        99 : ('seq99','CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG',"""2$7)*5:"=+++!:.=>!5>79)8!566$!3*/4$=4.%=//;900$9)!%)4%$=0":02"0=!0#/>+*1$1$39!.8+9<'1$*1$321&<'&9,)2""")
    }

    fastq_parser = FastqParser(os.path.join(currentdir,"data/test.fq")) #instantiate FastqParser Object with provided test.fq file
    for idx, record in enumerate(fastq_parser): #Loop through records in test.fa using FastqParser
        if idx <= 4: # When loop idx in [0,1,2,3,4,99] 
            assert record == expected_outputs[idx] #Compare record returned by FastqParser to expected output for same record in the dictionary above
