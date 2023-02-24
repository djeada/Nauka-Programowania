"""
Otrzymujesz dwa napisy. Sprawdz czy napisy sa swoimi rotacjami.

"""

# Wersja 1
def czy_rotacja_v1(slowo_a, slowo_b):

    if len(slowo_a) != len(slowo_b):
        return False

    return (slowo_a + slowo_a).find(slowo_b) > -1


# Testy Poprawnosci
def test_1():
    slowo_a = "malpka"
    slowo_b = "kamapl"
    assert not czy_rotacja_v1(slowo_a, slowo_b)


def test_2():
    slowo_a = "malpka"
    slowo_b = "pkamal"
    assert czy_rotacja_v1(slowo_a, slowo_b)


def main():
    test_1()
    test_2()


if __name__ == "__main__":
    main()
