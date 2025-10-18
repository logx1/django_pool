def my_var():
    var1 = 42
    var2 = "42"
    var3 = "quarante-deux"
    var4 = 42.0
    var5 = True
    var6 = [42]
    var7 = {42: 42}
    var8 = (42,)
    var9 = set()

    print(var1 , "has a type ", type(var1))
    print(var2 , "has a type ", type(var2))
    print(var3 , "has a type ", type(var3))
    print(var4 , "has a type ", type(var4))
    print(var5 , "has a type ", type(var5))
    print(var6 , "has a type ", type(var6))
    print(var7 , "has a type ", type(var7))
    print(var8 , "has a type ", type(var8))
    print(var9 , "has a type ", type(var9))

if __name__ == "__main__":
    my_var()
