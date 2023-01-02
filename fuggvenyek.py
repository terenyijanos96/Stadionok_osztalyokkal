from Stadion import *
from datetime import *

def beolvas():
    f = open("stadionok.txt", "r", encoding="utf-8")
    tartalom = f.readlines()[1:]
    lista = []
    for s in tartalom:
        sor  = s.strip().split(";")

        nev = sor[0]
        varos = sor[1]
        csapatok_szama = int(sor[2])
        elso = datetime.strptime(sor[3], "%Y-%m-%d")
        utolso = datetime.strptime(sor[4], "%Y-%m-%d")

        lista.append(Stadion(nev,varos,csapatok_szama,elso,utolso))

    f.close()
    return lista

def objektum_lista_iteracio(lista):
    stadion_db = 0
    csapatok_osszesen = 0
    merkozes_1900_elott = []
    ketezer_ota_nincs = 0
    buffalo_db = 0

    ezerkilencszaz = datetime.strptime('1900-01-01', '%Y-%m-%d')
    ketezer_egy = datetime.strptime('2001-01-01', '%Y-%m-%d')

    for i in lista:
        stadion_db = stadionok_szama_newyorkban(stadion_db, i.get_varos())
        csapatok_osszesen = csapatszam_szamolo(csapatok_osszesen, i.get_csapatok_szama())
        merkozes_1900_elott = elso_merkozes_1900_elott(merkozes_1900_elott, i.get_nev(), i.get_elso(), ezerkilencszaz)
        ketezer_ota_nincs = ketezer_ota_nincs_merkozes(ketezer_ota_nincs, i.get_utolso(), ketezer_egy)
        buffalo_db = hany_csapat_jatszott_buffaloban(buffalo_db, i.get_varos(), i.get_csapatok_szama())
    print(f"Összesen hány stadion van New Yorkban? {stadion_db}")
    print(f"Mennyi az összes csapatszám? {csapatok_osszesen}")
    print(f"Listázd ki azokat a stadionokat, amelyekben  1900.01.01 előtt volt az első mérkőzésük! \n{merkozes_1900_elott}")
    print(f"Hány olyan stadion van, amelyben 2000 óta nem volt mérkőzés? {ketezer_ota_nincs}")
    print(f"Összesen hány csapat játszott Buffalo-ban? {buffalo_db}")

def stadionok_szama_newyorkban(stadion_db, varos):
    if varos == "New York":
        stadion_db += 1

    return stadion_db

def csapatszam_szamolo(csapatok_osszesen, csapatok_szama):
    return csapatok_osszesen + csapatok_szama

def elso_merkozes_1900_elott(lista, nev, elso, ezerkilencszaz):
    if elso < ezerkilencszaz:
        lista.append(nev)
    return lista

def ketezer_ota_nincs_merkozes(ketezer_ota_nincs, utolso, ketezer_egy):
    if utolso < ketezer_egy:
        ketezer_ota_nincs += 1

    return ketezer_ota_nincs


def hany_csapat_jatszott_buffaloban(buffalo_db, varos, csapatok_szama):
    if varos == "Buffalo":
        buffalo_db += csapatok_szama

    return buffalo_db