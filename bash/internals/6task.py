def palidrom_check(k):
    try:
        l = list(k)
        l.reverse()
        s = "".join(l)
        if s == k:
            return True
        else:
            return False
    except Exception as err:
        print err.message

if __name__ == "__main__":
    k = raw_input("Enter your word: ")
    while not k:
        k = raw_input("Please Enter your word: ")
    try:
        result  = palidrom_check(k)
        if result:
            print "The given word '" + k.upper() + "' is Polydrom"
        else:
            print "The given word '" + k.upper() + "' is NOT Polydrom"

    except Exception as err:
        print err.message

