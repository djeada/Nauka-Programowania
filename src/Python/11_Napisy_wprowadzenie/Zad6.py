"""
Otrzymujesz napis. Zamien litery a na znaki zapytania.
"""


def zamien_litery_a_na_znaki_zapytania(napis):
    return napis.replace("a", "?")


def test_zamien_litery_a_na_znaki_zapytania():
    assert zamien_litery_a_na_znaki_zapytania("ala ma kota") == "?l? m? kot?"
    assert (
        zamien_litery_a_na_znaki_zapytania("ala ma kota a kot ma ale")
        == "?l? m? kot? ? kot m? ?le"
    )


if __name__ == "__main__":
    test_zamien_litery_a_na_znaki_zapytania()
