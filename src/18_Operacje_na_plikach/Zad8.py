"""
Otrzymujesz napis reprezentujący ścieżkę folderu.
a) Dodaj swoje inicjały na końcu wszystkich plików tekstowych 
znajdujących się w folderze oraz podfolderach.
b) Usuń środkowy wiersz z każdego pliku csv znajdującego się 
w folderze oraz podfolderach.
"""
import pathlib

def znajdz_pliki_z_rozszerzeniem(sciezka, rozszerzenie):
    """
    Funkcja zwraca listę plików o podanym rozszerzeniu.
    """
    lista_plikow = []
    for plik in pathlib.Path(sciezka).glob('**/*.' + rozszerzenie):
        lista_plikow.append(str(plik.relative_to(pathlib.Path(sciezka).parent)))
    return lista_plikow

def dodaj_inicjaly(sciezka, inicjaly):
    """
    Funkcja dodaje inicjaly na koniec pliku tekstowego.
    """

    plik = pathlib.Path(sciezka)
    if plik.exists():
        plik.write_text(plik.read_text() + inicjaly + '\n')

def dodaj_inicjaly_do_plikow_w_folderze(sciezka, inicjaly):
    """
    Funkcja dodaje inicjaly na koniec kazdego pliku tekstowego w folderze.
    """

    for plik in znajdz_pliki_z_rozszerzeniem(sciezka, 'txt'):
        dodaj_inicjaly(plik, inicjaly)


def usun_srodkowy_wiersz(sciezka):
    """
    Funkcja usuwa srodkowy wiersz z pliku.
    """
    plik = pathlib.Path(sciezka)
    if plik.exists():
        tresc = plik.read_text().split('\n')
        plik.write_text("\n".join(tresc[:len(tresc)//2] + tresc[len(tresc)//2 + 1:]) + '\n')
    

def usun_srodkowy_wiersz_z_plikow_w_folderze(sciezka):
    """
    Funkcja usuwa srodkowy wiersz z kazdego pliku csv w folderze.
    """

    for plik in znajdz_pliki_z_rozszerzeniem(sciezka, 'csv'):
        usun_srodkowy_wiersz(plik)

def test_dodaj_inicjaly_do_plikow_w_folderze():
    
    # stworz folder testowy
    pathlib.Path('test').mkdir()
    pathlib.Path('test/test1').mkdir()

    # stworz pliki testowe
    plik1 = pathlib.Path('test/test1/test1.txt')
    plik1.touch()
    plik1.write_text('test1\n')

    plik2 = pathlib.Path('test/test1/test2.txt')
    plik2.touch()
    plik2.write_text('test2\n')

    # dodaj inicjaly
    inicjaly = 'A.D.'
    dodaj_inicjaly_do_plikow_w_folderze('test', inicjaly)

    # sprawdz czy pliki zostaly zmodyfikowane
    assert plik1.read_text().splitlines()[-1] == inicjaly
    assert plik2.read_text().splitlines()[-1] == inicjaly

    # usun folder testowy
    import shutil
    shutil.rmtree('test')

def test_usun_srodkowy_wiersz_z_plikow_w_folderze():
    
    # stworz folder testowy
    pathlib.Path('test').mkdir()
    pathlib.Path('test/test1').mkdir()

    # stworz pliki testowe
    plik1 = pathlib.Path('test/test1/test1.csv')
    plik1.touch()
    plik1.write_text("\n".join(['test1; test1', 'test2; test2', 'test3; test3']))

    plik2 = pathlib.Path('test/test1/test2.csv')
    plik2.touch()
    plik2.write_text("\n".join(['test1; test1', 'test2; test2', 'test3; test3']))

    # usun srodkowy wiersz z plikow
    usun_srodkowy_wiersz_z_plikow_w_folderze('test')

    # sprawdz czy pliki zostaly zmodyfikowane
    assert plik1.read_text().splitlines()[0] == 'test1; test1'
    assert plik1.read_text().splitlines()[1] == 'test3; test3'

    assert plik2.read_text().splitlines()[0] == 'test1; test1'
    assert plik2.read_text().splitlines()[1] == 'test3; test3'

    # usun folder testowy
    import shutil
    shutil.rmtree('test')

if __name__ == "__main__":
    
    test_dodaj_inicjaly_do_plikow_w_folderze()
    test_usun_srodkowy_wiersz_z_plikow_w_folderze()