def distr(Distr_Name,Distr_Type,a=0,s=1,x=0,p=0.5,df=3,df1=3,df2=3,nc=0):
    rez=0
    match Distr_Name.split():
        case ["Norm"]:
            if Distr_Type=="cdf": rez=stats.norm.cdf(x,a,s)
            if Distr_Type=="ppf": rez=stats.norm.ppf(p)
            if Distr_Type=="pdf": rez=stats.norm.pdf(x,a,s)
        case ["T"]:
            if Distr_Type=="cdf": rez=stats.t.cdf(x,df)
            if Distr_Type=="ppf": rez=stats.t.ppf(p,df)
            if Distr_Type=="pdf": rez=stats.t.pdf(x,df)
        case ["Chi2"]:
            if Distr_Type=="cdf": rez=stats.chi2.cdf(x,df)
            if Distr_Type=="ppf": rez=stats.chi2.ppf(p,df)
            if Distr_Type=="pdf": rez=stats.chi2.pdf(x,df)
        case ["F"]:
            if Distr_Type=="cdf": rez=stats.f.cdf(x,df1,df2)
            if Distr_Type=="ppf": rez=stats.f.ppf(p,df1,df2)
            if Distr_Type=="pdf": rez=stats.f.pdf(x,df1,df2)
        case ["NonCT"]:
            if Distr_Type=="cdf": rez=stats.nct.cdf(x,df,nc)
            if Distr_Type=="ppf": rez=stats.nct.ppf(p,df,nc)
            if Distr_Type=="pdf": rez=stats.nct.pdf(x,df,nc)
        case ["Beta"]:
            if Distr_Type=="cdf": rez=stats.beta.cdf(x,df)
            if Distr_Type=="ppf": rez=stats.beta.ppf(p,df)
            if Distr_Type=="pdf": rez=stats.beta.pdf(x,df)
        case ["Gamma"]:
            if Distr_Type=="cdf": rez=stats.gamma.cdf(x,df)
            if Distr_Type=="ppf": rez=stats.gamma.ppf(p,df)
            if Distr_Type=="pdf": rez=stats.gamma.pdf(x,df)

    return(rez)