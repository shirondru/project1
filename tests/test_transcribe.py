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
                'input':'ATGCGCCCTT',
                'expected_output':'AUGCGCCCUU' #not reversed
    }

    #if seq only has one nucleotide repeated

    test2 = {
                'input': 'TTTTTTT',
                'expected_output':'UUUUUUU'
    }

    tests = [test0,test1,test2]

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
                'input':'ATGCGCCCTT',
                'expected_output':'UUCCCGCGUA' #reversed
    }

    #if seq only has one nucleotide repeated

    test2 = {
                'input': 'TTTTTTT',
                'expected_output':'UUUUUUU'
    }

    tests = [test0,test1,test2]

    for test in tests:
        assert reverse_transcribe(test['input']) == test['expected_output']





