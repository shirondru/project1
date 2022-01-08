# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)



def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """

    # if seq is an empty string
    test0={
            'input':'',
            'expected_output':''
    }

    #if seq is a random DNA sequence
    test1 = {
                'input':'ATGCGCACTT',
                'expected_output':'UACGCGUGAA' 
    }

    #another example of a random DNA sequence
    test2 = {
                'input': 'TGCTACCGGT',
                'expected_output': 'ACGAUGGCCA'
    }

    #if seq only has one nucleotide repeated
    test3 = {
                'input': 'AAAAAAA',
                'expected_output':'UUUUUUU'
    }

    #example from README
    test4 = {
                'input': 'ACTGAACCC', 
                'expected_output' : 'UGACUUGGG'
    }

    tests = [test0,test1,test2,test3,test4]

    for test in tests:
        assert transcribe(test['input']) == test['expected_output']




def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """

    # if seq is an empty string
    test0={
            'input':'',
            'expected_output':''
    }

    #if seq is a random DNA sequence
    test1 = {
                'input':'ATGCGCACTT',
                'expected_output':'AAGUGCGCAU' #transcribed then reversed
    }

    #another example of a random DNA sequence
    test2 = {
                'input': 'TGCTACCGGT',
                'expected_output': 'ACCGGUAGCA'
    }

    #if seq only has one nucleotide repeated

    test3 = {
                'input': 'AAAAAAA',
                'expected_output':'UUUUUUU'
    }

    #example from README
    test4 = {
                'input': 'ACTGAACCC',
                'expected_output' : 'GGGUUCAGU'
    }
    #if seq 
    

    tests = [test0,test1,test2,test3,test4]

    for test in tests:
        assert reverse_transcribe(test['input']) == test['expected_output']





