import pytest
from solution import traitDecider

"""
REMEMBER:
- Your tests should be comprehensive. They should test 
  - edge cases 
  - large inputs 
  - as many scenarios as possible.
- Minimum 5 tests. Maximum 10 tests.
- More tests, higher-quality tests === higher payouts.
"""

#1- test case
def test_one():
    
    fatherTraits = {
        "hair_color":"Blue",
        "eye_color":"BlAcK",
        "vision" :"NoRmaL",
        "blood_type": "O-PosiTive"
    }
    
    motherTraits={
        "hair_color":"BlACk",
        "eye_color":"bRowN",
        "vision" :"NoRmaL",
        "blood_type": "O-PosiTivE"
    }
    
    expected={
        "hair_color":"BlACk",
        "eye_color":"BlAcK",
        "vision" :"NoRmaL",
        "blood_type": "O-PosiTivE"
    }
    result= traitDecider(fatherTraits,motherTraits)
    if (result != expected):
        print("Test 1 FAILED")
        print("Expected: "+expected)
        print("Actual :" +result)
    
    assert traitDecider(fatherTraits,motherTraits)==expected

#2 - basic test where all fathers trait are dominant
def test_two():
    fatherTraits = {
        "hair_color":"BLONDE",
        "eye_color":"GREEN",
        "vision" :"TALL",
        "blood_type": "FAIR"
    }
    
    motherTraits={
        "hair_color":"brown",
        "eye_color":"blue",
        "vision" :"short",
        "blood_type": "dark"
    }
    
    expected={
        "hair_color":"BLONDE",
        "eye_color":"GREEN",
        "vision" :"TALL",
        "blood_type": "FAIR"
    }
    result= traitDecider(fatherTraits,motherTraits)
    if (result != expected):
        print("Test 2 FAILED")
        print("Expected: "+expected)
        print("Actual :" +result)
    assert traitDecider(fatherTraits,motherTraits)==expected

#3- mixed traits where parents have different sets of traits
def test_three():
    fatherTraits = {
        "hair_color":"Red",
        "skin_tone":"FAIR",
        "build" :"MuScUlAr",

    }
    
    motherTraits={
        "hair_color":"BLACK",
        "eye_color":"HAZEL",
        "voice":"SoFt"
    }
    
    expected={
        "hair_color":"BLACK",
        "skin_tone":"FAIR",
        "eye_color":"HAZEL",
        "build" :"MuScUlAr",
        "voice": "SoFt"
    }
    result= traitDecider(fatherTraits,motherTraits)
    if (result != expected):
        print("Test 3 FAILED")
        print("Expected: "+expected)
        print("Actual :" +result)
    assert traitDecider(fatherTraits,motherTraits)==expected

#4 - Empty one
def test_four():
    fatherTraits={}
    motherTraits={}
    expected={}
    result= traitDecider(fatherTraits,motherTraits)
    if (result != expected):
        print("Test 4 FAILED")
        print("Expected: "+expected)
        print("Actual :" +result)
    assert traitDecider(fatherTraits,motherTraits)==expected

#5 - Tie Breaking
def test_five():
    fatherTraits={
        "hair_color":"BrOwN",
        "eye_color":"GrEeN",
        "height" :"TaLl",
        "personality": "KiND"
    }
    motherTraits={
        "hair_color":"BlOnD",
        "eye_color":"BlUe",
        "height" :"ShOrT",
        "personality": "SmArt"
    }
    expected={
        "hair_color":"BrOwN",
        "eye_color":"GrEeN",
        "height":"ShOrT",
        "personality":"KiND"
    }
    result= traitDecider(fatherTraits,motherTraits)
    if (result != expected):
        print("Test 5 FAILED")
        print("Expected: "+expected)
        print("Actual :" +result)
    assert traitDecider(fatherTraits,motherTraits)==expected
    
#6 - empty traits
def test_six():
    fatherTraits={
        "hair_color":"",
        "eye_color":"BLUE_GREEN",
        "special_trait":"X-RAY_VISION"
    }
    motherTraits={
        "hair_color":"ReD",
        "eye_color":"brown-hazel",
        "special_trait":"telepathy"
    }
    expected={
        "hair_color":"ReD",
        "eye_color":"BLUE_GREEN",
        "special_trait":"X-RAY_VISION"
    }
    result= traitDecider(fatherTraits,motherTraits)
    if (result != expected):
        print("Test 6 FAILED")
        print("Expected: "+expected)
        print("Actual :" +result)
    assert traitDecider(fatherTraits,motherTraits)==expected
    
#7 -one parent with traits , other with out any trait
def test_seven():
    fatherTraits={
        "hair_color":"BLONDE",
        "eye_color":"GREEN"
    }
    motherTraits={}
    expected={
        "hair_color":"BLONDE",
        "eye_color":"GREEN"
    }
    result= traitDecider(fatherTraits,motherTraits)
    if (result != expected):
        print("Test 7 FAILED")
        print("Expected: "+expected)
        print("Actual :" +result)
    assert traitDecider(fatherTraits,motherTraits)==expected
    
#8 Extreme capital letters 
def test_eight():
    fatherTraits={
        "trait1":"A"*100,
        "trait2":"a"*100
    }
    motherTraits={
        "trait1":"A"*99,
        "trait2":"A"*1
    }
    expected={
        "trait1":"A"*100,
        "trait2":"A"*1
    }
    result= traitDecider(fatherTraits,motherTraits)
    if (result != expected):
        print("Test 9 FAILED")
        print("Expected: "+expected)
        print("Actual :" +result)
    assert traitDecider(fatherTraits,motherTraits)==expected
    
    
#9 - integer attack
def test_nine():
    try:
        fatherTraits={
            "height":182,
            "weight":75,
            "hair_color":"BLACK"
        }
        motherTraits={
            "height":165,
            "weight":60.2,
            "hair_color":"blonde"
        }
        traitDecider(fatherTraits,motherTraits)
        assert False, "Expected error was not raised"
        # result= traitDecider(fatherTraits,motherTraits)
        # if (result != expected):
        #     print("Test 2 FAILED")
        #     print("Expected: "+expected)
        #     print("Actual :" +result)
    except TypeError as e:
        assert "must be strings" in str(e), f"Expected error message"
    except Exception as e:
        assert False, f"Expected typeError but got other: {str(e)}"
    
#last : special characters and numbers
def test_ten():
    fatherTraits={
        "hair_color":"123",
        "eye_color":"B!U@E",
        "blood_type":"o+"
    }
    motherTraits={
        "hair_color":"BL4CK",
        "eye_color":"G#E%N",
        "blood_type":"AB+"
    }
    expected={
        "hair_color":"BL4CK",
        "eye_color":"B!U@E",
        "blood_type":"AB+"
    }
    result= traitDecider(fatherTraits,motherTraits)
    if (result != expected):
        print("Test 10 FAILED")
        print("Expected: "+expected)
        print("Actual :" +result)
    assert traitDecider(fatherTraits,motherTraits)==expected