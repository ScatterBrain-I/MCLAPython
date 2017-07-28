def userInt(prompt):
    print prompt,
    i = int(raw_input())
    return i

def kmToMi(km):
    return .62 * km
    
def userString(prompt):
    print prompt,
    s = raw_input()
    return s
    
def userFloat(prompt):
    print prompt,
    f = float(raw_input())
    return f
    
def percentToDecimal(percent):
    return (.01 * percent)
    
def goAgain(prompt):
    y = userString(prompt)
    if y.lower() == 'y':
        go = True
    else:    
        go = False
    return go   

