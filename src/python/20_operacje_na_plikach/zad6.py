"""
Tytul: Usun pliki spelniajace warunek.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do folderu. Usun wszystkie pliki o rozmiarze wiekszym niz 10 kB znajdujace sie w podanym folderze i jego podfolderach.
Dane wejsciowe: Napis reprezentujacy sciezke do folderu.
Dane wyjsciowe: Brak.

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

