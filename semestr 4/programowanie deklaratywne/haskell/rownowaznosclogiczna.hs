rownowaznosc::(Bool,Bool)->Bool
rownowaznosc (p,q)=case (p,q) of (True,True)->True
                                 (True,False)->False
                                 (False,True)->False
                                 (False,False)->True