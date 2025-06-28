def traitDecider(fathers_trait,mothers_trait):
    # implement your function here
    # You may have multiple functions, but make sure that the 
    # entry point function signature is referenced inside your prompt.md
    
    #one integer validation
    for parent, traits in [("father", fathers_trait),("mother",mothers_trait)]:
        for trait, value in traits.items():
            if not isinstance(value,str):
                raise TypeError(f"All trait values must be strings,  but {parent}'s '{trait}' is {type(value).__name__}")
    
    inherited = {}
    
    allTraits = set(fathers_trait.keys()) | set(mothers_trait.keys())
    
    for x in allTraits:
        fatherValue=fathers_trait.get(x,"")
        motherValue=mothers_trait.get(x,"")
        
        #cal capital  letter in each trait
        countOfFatherCapital= sum( 1 for ch in fatherValue if ch.isupper())
        countOfMotherCapital= sum( 1 for ch in motherValue if ch.isupper())
        
        
        if countOfMotherCapital > countOfFatherCapital :
            inherited[x]=motherValue
        #in else case if number of capital letters are equal, then also father's trait are dominant
        else:
            inherited[x]=fatherValue
            
    return inherited

    pass 