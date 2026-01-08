def printBooks(i,t,a,y):
    return(
        f"Book id:{i}\n"
        f"Book title:{t}\n"
        f"Authour name:{a}\n"
        f"Year of publication:{y}"
    )

if __name__ == "__main__":
    id=2000
    title="the conjuring"
    authour="Dr. Om"
    year=1997

    res=printBooks(id,title,authour,year)
    print(res)
