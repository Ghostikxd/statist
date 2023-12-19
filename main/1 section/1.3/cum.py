def cum(n):
    fcum=[(i+0.5)/n for i in range(n)]
    #fcum=[(i+1.-0.375)/(n + 0.25) for i in range(n)] #Blom
    #fcum=[(i+1.)/(n+1) for i in range(n)] #order statistics theory
    return(fcum)