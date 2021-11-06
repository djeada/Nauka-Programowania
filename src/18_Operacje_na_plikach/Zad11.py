
"""
Otrzymujesz dwa napisy reprezentujące ścieżki plików. 
Podmień treści obu plików.
"""

import pathlib
import datetime

def podmien_tresci(plik1, plik2):
    '''
    Funkcja zamienia treści plików.
    '''
    pom_nazwa = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    pathlib.Path(plik2).rename(pom_nazwa)
    pathlib.Path(plik1).rename(plik2)
    pathlib.Path(pom_nazwa).rename(plik1)
   
def test_podmien_tresci():

    # stworz folder testowy
    pathlib.Path('test').mkdir()
    
    # stworz pliki testowe
    plik_1 = pathlib.Path('test/plik_1.txt')
    plik_1.touch()
    tekst_1 = 'tekst_1'
    plik_1.write_text(tekst_1)

    plik_2 = pathlib.Path('test/plik_2.txt')
    plik_2.touch()
    tekst_2 = 'tekst_2'
    plik_2.write_text(tekst_2)

    # podmień treści plików
    podmien_tresci(plik_1, plik_2)

    # sprawdź czy treść plików została zmieniona
    assert plik_1.read_text() == tekst_2
    assert plik_2.read_text() == tekst_1

    # usuń folder testowy
    import shutil
    shutil.rmtree('test')

if __name__ == "__main__":
    
    test_podmien_tresci()
