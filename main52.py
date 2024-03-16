def czy_przestepny(rok):
    if rok % 4 == 0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

rok = 2024
if czy_przestepny(rok):
    print(rok, "jest rokiem przestępnym.")
else:
    print(rok, "nie jest rokiem przestępnym.")
