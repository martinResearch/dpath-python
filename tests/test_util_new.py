import nose
import dpath.util

def test_set_new_separator():
    dict = {
        "a": {
            }
        }
    dpath.util.new(dict, ';a;b', 1, separator=";")
    assert(dict['a']['b'] == 1)
    dpath.util.new(dict, ['a', 'b'], 1, separator=";")
    assert(dict['a']['b'] == 1)

def test_set_new_dict():
    dict = {
        "a": {
            }
        }
    dpath.util.new(dict, '/a/b', 1)
    assert(dict['a']['b'] == 1)
    dpath.util.new(dict, ['a', 'b'], 1)
    assert(dict['a']['b'] == 1)

def test_set_new_list():
    dict = {
        "a": [
            ]
        }
    dpath.util.new(dict, '/a/1', 1)
    assert(dict['a'][1] == 1)
    assert(dict['a'][0] == None)
    dpath.util.new(dict, ['a', '1'], 1)
    assert(dict['a'][1] == 1)
    assert(dict['a'][0] == None)
	
def test_set_new_list_with_integer_as_list_index():
    dict = {}
    dpath.util.new(dict, 'a/2/3', 5,integer_as_list_index = True)
    assert(len(dict['a']) == 3)
    assert(dict['a'][0] == None)
    assert(dict['a'][1] == None)	
    assert(len(dict['a'][2]) == 4)
    assert(dict['a'][2][0] == None)
    assert(dict['a'][2][1] == None)	
    assert(dict['a'][2][2] == None)
    assert(dict['a'][2][3] == 5)

def test_set_new_list_path_with_separator():
    # This test kills many birds with one stone, forgive me
    dict = {
        "a": {}
        }
    dpath.util.new(dict, ['a', 'b/c/d', 0], 1)
    assert(len(dict['a']) == 1)
    assert(len(dict['a']['b/c/d']) == 1)
    assert(dict['a']['b/c/d'][0] == 1)
    
