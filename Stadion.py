class Stadion:

    def __init__(self,nev,varos,csapatok_szama,elso,utolso):
        self.__nev = nev
        self.__varos = varos
        self.__csapatok_szama = csapatok_szama
        self.__elso = elso
        self.__utolso = utolso

    def __str__(self):
        return f"Stadion: {self.__nev}, Város: {self.__varos}, Csapatok száma: {self.__csapatok_szama}, Első: {self.__elso}, Utolsó: {self.__utolso}"

    def get_nev(self):
        return self.__nev

    def get_varos(self):
        return self.__varos

    def get_csapatok_szama(self):
        return self.__csapatok_szama

    def get_elso(self):
        return self.__elso

    def get_utolso(self):
        return self.__utolso

    def set_nev(self, nev):
        self.__nev = nev

    def set_varos(self, varos):
        self.__varos = varos

    def set_csapatok_szama(self, csapatok_szama):
        self.__csapatok_szama = csapatok_szama

    def set_elso(self, elso):
        self.__elso = elso

    def set_utolso(self, utolso):
        self.__utolso = utolso