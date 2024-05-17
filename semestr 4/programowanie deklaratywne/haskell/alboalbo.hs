--funkcja albo_albo (dopasowanie do wzorca)
albo_albo::(Bool,Bool)->Bool
albo_albo1 (p,q)=case (p,q) of (True,True)->False
                               (True,True)->True
                               (False,True)->True
                               (False,False)->False
