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
    ##################################################################################################################
    #Creating 5 tests including: 
    #Two random DNA sequences to ensure the function can properly transcribe a string of ATGC nucleotides
    #The exact DNA sequence given as an example by the TAs in the README file to ensure the function returns precisely what they expected
    #An empty string to ensure the function doesn't break and properly returns an empty string
    #The same nucleotide repeated over and over to ensure it doesn't break and properly returns its complement (also repeated)

    #the unit test does not test for certain edge cases, such as if a non-DNA nucleotide was used in an input string.
    #This is because the original transcribe function asserts that "U" is not in the input string to enfore DNA only
    #And beacuse we were told we did not need to consder edge cases
    ##################################################################################################################


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

    #example from README. The expected output was defined by the TAs
    test4 = {
                'input': 'ACTGAACCC', 
                'expected_output' : 'UGACUUGGG'
    }

    tests = [test0,test1,test2,test3,test4]

    for test in tests: #loop through each test and assert that if the input were passed into transcribe() that the expected output is returned
        assert transcribe(test['input']) == test['expected_output']




def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """

    #####################################################################################################################################
    #Using 5 tests with same inputs as in the transcribe function, but with the outputs reversed
    
    #####################################################################################################################################

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

    #example from README. The expected output was defined by the TAs
    test4 = {
                'input': 'ACTGAACCC',
                'expected_output' : 'GGGUUCAGU'
    }
    
    

    tests = [test0,test1,test2,test3,test4]

    for test in tests: #loop through each test and assert that if the input were passed into reverse_transcribe() that the expected output is returned
        assert reverse_transcribe(test['input']) == test['expected_output']





