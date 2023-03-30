"""
Tytul: Statystyki dla pliku tekstowego.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego. Oblicz:
a) Liczbe wierszy w pliku.
b) Liczbe slow w pliku (slowa oddzielone sa spacjami i moga skladac sie wylacznie z liter).
c) Srednia dlugosc wiersza.
d) Srednia liczbe slow na wiersz.
e) Czestosc wystepowania kazdego ze slow w pliku.
Dane wejsciowe: Napis reprezentujacy sciezke do pliku.
Dane wyjsciowe:
a) Liczba naturalna reprezentujaca liczbe wierszy.
b) Liczba naturalna reprezentujaca liczbe slow.
c) Liczba zmiennoprzecinkowa reprezentujaca srednia dlugosc wiersza.
d) Liczba zmiennoprzecinkowa reprezentujaca srednia liczbe slow na wiersz.
e) Slownik par: napis (slowo), liczba naturalna (czestotliwosc wystepowania slowa).
Przyklad:
Dla otrzymanego napisu: "C:\Users\Username\Documents\text_file.txt" powinno zostac zwrocone:
a) Liczba naturalna reprezentujaca liczbe wierszy, np. 6
b) Liczba naturalna reprezentujaca liczbe slow, np. 25
c) Liczba zmiennoprzecinkowa reprezentujaca srednia dlugosc wiersza, np. 41.5
d) Liczba zmiennoprzecinkowa reprezentujaca srednia liczbe slow na wiersz, np. 4.2
e) Slownik par: napis (slowo), liczba naturalna (czestotliwosc wystepowania slowa): {'The': 2, 'quick': 2, 'brown': 2, 'fox': 2, 'jumped': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog.': 1, 'cat': 1, 'sat': 1, 'on': 1, 'mat.': 1, 'Foxes': 1, 'are': 1, 'known': 1, 'for': 1, 'their': 2, 'cunning': 1, 'and': 1, 'intelligence.': 1, 'Dogs': 1, 'loyalty': 1, 'kindness.': 1, 'Cats': 1, 'independent': 1, 'animals': 1, 'but': 1, 'can': 1, 'be': 1, 'affectionate.': 1, 'This': 1, 'text': 1, 'file': 1, 'contains': 1, 'ten': 1, 'lines': 1, 'and': 1, 'words.': 1}
Tekst pliku:
The quick brown fox jumped over the lazy dog.
The quick brown cat sat on the mat.
Foxes are known for their cunning and intelligence.
Dogs are known for their loyalty and kindness.
Cats are independent animals but can be affectionate.
This text file contains six lines and 25 words.

"""
import pathlib
import string

def wczytaj_plik(sciezka):
    """
    Funkcja wczytujaca plik tekstowy
    """
    return pathlib.Path(sciezka).read_text().splitlines()

def liczba_wierszy(tresc_pliku):
    """
    Funkcja liczaca liczbe wierszy w pliku
    """
    return len(tresc_pliku)

def podziel_zdanie_na_slowa(zdanie):
    """
    Funkcja rozdziela zdanie na slowa.
    """
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()

def na_male_litery(slowa):
    """
    Funkcja zamienia wielkie litery ze slow z listy slowa na male litery.
    """
    return [slowo.lower() for slowo in slowa]

def liczba_slow(tresc_pliku):
    """
    Funkcja liczaca liczbe slow w pliku
    """
    licznik = 0
    for wiersz in tresc_pliku:
        licznik += len(podziel_zdanie_na_slowa(wiersz))
    return licznik

def srednia_dlugosc_wiersza(tresc_pliku):
    """
    Funkcja liczaca srednia dlugosc wiersza
    """
    return sum(len(wiersz) for wiersz in tresc_pliku) / liczba_wierszy(tresc_pliku)

def srednia_liczba_slow_na_wiersz(tresc_pliku):
    """
    Funkcja liczaca srednia liczbe slow na wiersz
    """
    return liczba_slow(tresc_pliku) / liczba_wierszy(tresc_pliku)

def czestosc_slow(tresc_pliku):
    """
    Funkcja liczaca czestosc wystepowania kazdego slowa w pliku
    """
    histogram = {}
    for wiersz in tresc_pliku:
        for slowo in na_male_litery(podziel_zdanie_na_slowa(wiersz)):
            if slowo in histogram:
                histogram[slowo] += 1
            else:
                histogram[slowo] = 1
    return histogram

def test_statystyki():

    # stworz folder testowy
    pathlib.Path("test").mkdir(parents=True, exist_ok=True)

    # utworz plik tekstowy
    plik = pathlib.Path("test/test.txt")
    plik.write_text(
        "\n".join(
            [
                "Hej ",
                "This is an example of a simple ASCII text file stored on a Web server. Note that it has a file",
                'extension of ".txt".\n',
                "Although such files may contains some basic layout formatting, such as paragraphs, there is no",
                "support for the text to have attributes, such as bolding.\n",
                "Text files can contain Hypertext Mark-up codes but these will not be interpreted by the ",
                "browser. For example, if the following characters <strong>hello</strong> were typed into an",
                '"html" file then the word "hello" would be shown in bold.',
            ]
        )
    )

    # wczytaj plik tekstowy
    tresc_pliku = wczytaj_plik(plik)

    # sprawdz statystyki
    assert liczba_wierszy(tresc_pliku) == 10
    assert liczba_slow(tresc_pliku) == 88
    assert abs(srednia_dlugosc_wiersza(tresc_pliku) - 50.5) < 0.1
    assert (srednia_liczba_slow_na_wiersz(tresc_pliku) - 8.8) < 0.1
    assert czestosc_slow(tresc_pliku) == {
        "bold": 1,
        "in": 1,
        "shown": 1,
        "word": 1,
        "then": 1,
        "html": 1,
        "simple": 1,
        "basic": 1,
        "contains": 1,
        "layout": 1,
        "were": 1,
        "may": 1,
        "such": 3,
        "file": 3,
        "extension": 1,
        "files": 2,
        "it": 1,
        "hypertext": 1,
        "hello": 1,
        "note": 1,
        "web": 1,
        "ascii": 1,
        "is": 2,
        "an": 2,
        "example": 2,
        "hej": 1,
        "following": 1,
        "this": 1,
        "of": 2,
        "txt": 1,
        "although": 1,
        "text": 3,
        "stored": 1,
        "that": 1,
        "by": 1,
        "on": 1,
        "formatting": 1,
        "support": 1,
        "browser": 1,
        "typed": 1,
        "a": 3,
        "server": 1,
        "would": 1,
        "contain": 1,
        "as": 2,
        "markup": 1,
        "characters": 1,
        "there": 1,
        "for": 2,
        "the": 4,
        "to": 1,
        "have": 1,
        "these": 1,
        "will": 1,
        "paragraphs": 1,
        "attributes": 1,
        "bolding": 1,
        "can": 1,
        "has": 1,
        "codes": 1,
        "if": 1,
        "some": 1,
        "no": 1,
        "but": 1,
        "not": 1,
        "be": 2,
        "interpreted": 1,
        "stronghellostrong": 1,
        "into": 1,
    }

    # usun folder testowy
    import shutil

    shutil.rmtree("test")

if __name__ == "__main__":
    test_statystyki()

