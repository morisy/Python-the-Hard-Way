from nose.tools import *
from ex49 import parser

def test_peek():
    word_list = [('noun', 'Dog'), ('verb', 'ran'), ('stop', 'to'), ('stop', 'the'), ('noun', 'cow')]
    assert_equal(parser.peek(word_list), 'noun')

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
