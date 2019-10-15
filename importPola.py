# mengimport modul PolaBaju
import PolaBaju
def main():
    #lingkar badan
    a = 84
    b = 4

    lingkar = PolaBaju.lingkarBadan(a, b)

    print("LINGKAR BADAN")
    print("Ukuran Badan\t: ", a)
    print("Rumus Lingkar Badan\t: ", b)
    print("Lingkar Badan\t = ", lingkar)

    #lingkar leher
    a = 37
    c = 6

    lingkar = PolaBaju.lingkarLeher(a, c)

    print("LINGKAR LEHER")
    print("Ukuran Leher\t: ", a)
    print("Rumus Lingkar Leher\t: ", c)
    print("Lingkar Leher\t = ", lingkar)
    
    #lingkar pinggang
    d =72
    m = 4

    lingkar = PolaBaju.lingkarPinggang(d, m)

    print("LINGKAR PINGGANG")
    print("Ukuran Pinggang\t: ", d)
    print("Rumus Lingkar Pinggang\t: ", m)
    print("Lingkar Leher\t = ", lingkar)
    
if __name__=="__main__":
    main()


    
    
    
    
