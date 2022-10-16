from test_functions import is_valid_name, is_chronological

def test01():
    name = "Abcd"
    actual = is_valid_name(name)
    expected = True
    #assert actual == expected, f"{expected}, {num} is even?"
    if actual == expected:
        print("is_valid_name has passed.")
    else:
        print("is_valid_name has failed.")

def test02():
    name = "Ab-cd"
    actual = is_valid_name(name)
    expected = True
    #assert actual == expected, f"{expected}, {num} is even?"
    if actual == expected:
        print("is_valid_name has passed.")
    else:
        print("is_valid_name has failed.")

def test03():
    name = "ab cd"
    actual = is_valid_name(name)
    expected = True
    #assert actual == expected, f"{expected}, {num} is even?"
    if actual == expected:
        print("is_valid_name has passed.")
    else:
        print("is_valid_name has failed.") 

def test04():
    name = "ab@cd"
    actual = is_valid_name(name)
    expected = False
    #assert actual == expected, f"{expected}, {num} is even?"
    if actual == expected:
        print("is_valid_name has failed.")
    else:
        print("is_valid_name has passed.") 

def test05():
    name = "  "
    actual = is_valid_name(name)
    expected = False
    #assert actual == expected, f"{expected}, {num} is even?"
    if actual == expected:
        print("is_valid_name has failed.")
    else:
        print("is_valid_name has passed.")

def test06():
    name = 123
    actual = is_valid_name(name)
    expected = False
    #assert actual == expected, f"{expected}, {num} is even?"
    if actual == expected:
        print("is_valid_name has failed.")
    else:
        print("is_valid_name has passed.")

def test07():
    name = ""
    actual = is_valid_name(name)
    expected = False
    #assert actual == expected, f"{expected}, {num} is even?"
    if actual == expected:
        print("is_valid_name has failed.")
    else:
        print("is_valid_name has passed.")

def test08():
    early = "2000-01-12T16:30:01"
    later = "2001-02-12T23:23:11"
    actual = is_chronological(early,later)
    expected = True 
    if actual == expected:
        print("is_chronological has passed.")
        
    else:
        print("is_chronological has failed.")

def test09():
    early = "2000-01-12T16:30:01"
    later = "1999-02-12T23:23:11"
    actual = is_chronological(early,later)
    expected = False 
    if actual == expected:
        print("is_chronological has failed.")
    else:
        print("is_chronological has passed.")



#test01()
test02()
# test03()
# test04()
#test05()
#test06()
#test07()
test08()
#test09()
