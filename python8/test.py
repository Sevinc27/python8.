def samitler_al(cumle):
    samitler = set()
    for harf in cumle:
        if harf.lower() not in "aeiou":
            samitler.add(harf)
    return samitler


