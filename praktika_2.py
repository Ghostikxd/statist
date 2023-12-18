from scipy import stats
import math

def distr(Distr_Name, Distr_Type, x = 0, p = 0.5):
    rez = 0 
    if (Distr_Name == "Norm"):
        if Distr_Type == "cdf":
            rez = stats.norm.cdf(x)
        if Distr_Type == "ppf":
            rez = stats.norm.ppf(p)
        if Distr_Type == "pdf":
            rez = stats.norm.pdf(x)
    return(rez)

z = distr("Norm", "cdf", x = 0.3, p = 0.9)
print(z)
z = distr("Norm", "ppf", x = 2.326, p = 0.99)
print(z)
z = distr("Norm", "pdf", x = 3.0, p = 0.5)
print(z)