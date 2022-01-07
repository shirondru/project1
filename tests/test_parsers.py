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

    #testing first 5 records of test.fa
    expected_outputs = {
        0 : ('seq0','TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'),
        1 : ('seq1','TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT'),
        2 : ('seq2','TGTAGAGGCATTATTAGAGTTTCGCCACAACGGGGGCCTGCTGATCAAATCAGAATTCGTACAATCGGTTCGGGAGACACGGCTCTAAAGATACCGCTAG'),
        3 : ('seq3','AATCCAGCGCGTGTTGTATCGAGCCCTTGGAAGTCGATGGTGTCTTTGGTGAAGGTCGATGAACTTCCTTGGCGAGGACAGCGAAGTTAATTGGTGGCGA'),
        4 : ('seq4','GGTAGGCGGCTGCATAACGCCCCTGAAGAGACAGGGGGTTAGAGGTTCTCCCCCATCGTTCACAGTGAAGAGTGTGAGAGGCACACTGAAGAACATTGAG')
    }

    fasta_parser = FastaParser(os.path.join(currentdir,"data/test.fa"))
    for idx, record in enumerate(fasta_parser):
        if idx <= 4: # test first 5 records
            assert record == expected_outputs[idx]





def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """

    #testing first 5 records of test.fq
    expected_outputs = {
        0 : ('seq0','TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG',"""*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32="""),
        1 : ('seq1','CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG',"""\'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,,:%0!<),%646<8#%"."-'*-0:.+*&$5!'8)(%3*+9/&/%=363*,6$20($97,\""""),
        2 : ('seq2','GATAAACTTCTATCACGAATACTGCGGGACCATGCAGTTGTCCCTCACCTCGATAGTTCAGGTCTTTTGGTTCTGAGCGATATTGGGCGCGTCACCACTG',"""1,758$,:7654/7<0%5/12%-3>-2.>$$443-,'9,5$;""%7**)-'%:**&;<35(!<1'.5>51)1%:9>4=(&+3$2!-.8!>=+1$:,*&9!"""),
        3 : ('seq3','TCTAGTGGCTGGCCAGAGACTCAATGAAATCATAGTATACATGGGACAGTGTCTAAATAAACTTGTCTCCTGAATTCTCGTAATCACTTATGGAGCAACG',"""$8=)$38.%2*93,21>8+#71!/<)/<8<=#6;3-,4!51-!*/;;>'<620.;<2;'1=2,(6>"'$2<&;);).(3#2%.<>$'49<,"+.6704=&"""),
        4 : ('seq4','TGTGAATATGCAGCCCGGTCCCTCGCAGTCATTGTTTTCCCCACTCCGTCCCACGTTCCCTTAGAGATAGCGCTGAGCTAGCATATAGCGGTTTGAAGGC',"""#8,9(-$..-;&1$(1#1)"9-4"4<+;:6/+7##<:,8%4''-)95-,-8*!9(60-##8%:+>'58**4"#(+-'-"&)49"209,''1-+&=7;.&&""")
    }

    fastq_parser = FastqParser(os.path.join(currentdir,"data/test.fq"))
    for idx, record in enumerate(fastq_parser):
        if idx <= 4: # test first 5 records
            assert record == expected_outputs[idx]
