# ZAD-09 — Słowa elfickie
# 
# **Poziom:** ★★☆
# **Tagi:** `rekurencja`, `napisy`
# 
# ### Treść
# 
# **Słowem elfickim** nazywamy napis, w którym każda z liter słowa `elf` (czyli `e`, `l` i `f`) występuje co najmniej raz, w dowolnej kolejności i na dowolnych pozycjach.
# 
# Napisz rekurencyjną funkcję `czy_elfickie(slowo, litery="elf")`, która sprawdza, czy każda litera z napisu `litery` występuje w napisie `slowo`. Program wczytuje słowo i wypisuje wynik sprawdzenia.
# 
# ### Wejście
# 
# Jedna linia: słowo złożone z małych liter alfabetu łacińskiego (`a`–`z`).
# 
# ### Wyjście
# 
# `Prawda`, jeśli słowo jest elfickie, w przeciwnym razie `Fałsz`.
# 
# ### Ograniczenia
# 
# * długość słowa: od 1 do 100 znaków
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# reflektor
# ```
# 
# **Wyjście:**
# 
# ```
# Prawda
# ```
# 
# W słowie `reflektor` występują litery `e`, `l` i `f`.
# 
# ### Uwagi
# 
# * Sprawdź, czy w słowie występuje pierwsza litera z `litery`, i wywołaj funkcję dla pozostałych liter (`litery[1:]`). Gdy `litery` jest pusty, wszystkie litery zostały znalezione.
# * Samo szukanie litery w słowie też możesz zapisać rekurencyjnie: litera występuje w słowie, jeśli jest jego pierwszym znakiem albo występuje w reszcie słowa.
# 
# ### Kod startowy
# 
# ```python
# def czy_elfickie(slowo, litery="elf"):
#     pass
# 
# 
# slowo = input().strip()
# print("Prawda" if czy_elfickie(slowo) else "Fałsz")
# ```
source ../assert.sh

zawiera() {
    # Kod wyjścia 0, jeśli litera $2 występuje w słowie $1.
    # Złożoność czasowa: O(n), złożoność pamięciowa: O(n) - przez stos rekurencji
    local slowo=$1
    local litera=$2

    if [[ -z $slowo ]]; then
        return 1
    fi

    if [[ ${slowo:0:1} == "$litera" ]]; then
        return 0
    fi

    zawiera "${slowo:1}" "$litera"
}

czy_elfickie() {
    # Kod wyjścia 0, jeśli każda litera z $2 (domyślnie "elf") występuje w słowie $1.
    # Złożoność czasowa: O(n * m), złożoność pamięciowa: O(n + m)
    local slowo=$1
    local litery=${2-elf}

    if [[ -z $litery ]]; then
        return 0
    fi

    zawiera "$slowo" "${litery:0:1}" || return 1

    czy_elfickie "$slowo" "${litery:1}"
}

main() {
    assertTrue "$(czy_elfickie reflektor && echo true || echo false)" $LINENO
    assertTrue "$(czy_elfickie flet && echo true || echo false)" $LINENO
    assertFalse "$(czy_elfickie elzbieta && echo true || echo false)" $LINENO
    assertFalse "$(czy_elfickie a && echo true || echo false)" $LINENO
}

main "$@"
