def add_tip(total, tip_percent): 
    '''This is a multi-line comment  
       Return the total amount including tip
    '''
    tip = tip_percent*total
    return total + tip
def hyp(leg1, leg2):
    h = leg1**2 + leg2**2
    return h**.5
    
def mean(a ,b ,c):
    m = a + b + c
    return m/3.0

def perimeter(base, height):
    p = base + height + base + height
    return p*1