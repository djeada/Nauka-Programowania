# ZAD-06 — Scalanie nakładających się przedziałów
#
# **Poziom:** ★★☆
# **Tagi:** `sort`, `przedziały`, `tuple`
#
# ### Treść
#
# Wczytaj $N$ przedziałów domkniętych $[a, b]$ — np. godziny zajęcia sali przez kolejne rezerwacje. Scal wszystkie przedziały, które mają **co najmniej jeden wspólny punkt**, i wypisz otrzymane rozłączne przedziały w kolejności rosnącej.
#
# Przedziały, które się tylko stykają (koniec jednego jest początkiem drugiego), też mają wspólny punkt: $[1, 3]$ i $[3, 5]$ scalamy w $[1, 5]$. Scalanie może łączyć całe łańcuchy przedziałów, a przedział zawarty w innym po prostu w nim „znika”.
#
# ### Wejście
#
# * 1. linia: liczba przedziałów $N$
# * kolejne $N$ linii: dwie liczby całkowite $a$ i $b$ oddzielone spacją — początek i koniec przedziału
#
# Przedziały są podane w dowolnej kolejności.
#
# ### Wyjście
#
# Scalone przedziały posortowane rosnąco według początku — każdy w osobnej linii, jako dwie liczby (początek i koniec) oddzielone spacją.
#
# ### Ograniczenia
#
# * $1 \le N \le 10^4$
# * $-10^9 \le a \le b \le 10^9$
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 4
# 8 10
# 1 3
# 15 18
# 2 6
# ```
#
# **Wyjście:**
#
# ```
# 1 6
# 8 10
# 15 18
# ```
#
# Przedziały $[1, 3]$ i $[2, 6]$ mają część wspólną $[2, 3]$, więc tworzą przedział $[1, 6]$. Pozostałe przedziały są rozłączne z resztą.
#
# ### Uwagi
#
# * Najpierw posortuj przedziały według początku (listę krotek `(a, b)` posortuje samo `sorted()`). Potem przejdź po nich raz: jeśli kolejny przedział zaczyna się nie później niż kończy się ostatni scalony, wydłuż ostatni scalony do $\max$ obu końców; w przeciwnym razie zacznij nowy scalony przedział.
# * Przedziały $[1, 2]$ i $[3, 4]$ **nie** mają wspólnego punktu (choć są „sąsiadami” na osi liczb całkowitych), więc zostają osobno.
# * Bez sortowania trzeba by porównywać każdą parę przedziałów — sortowanie daje rozwiązanie w czasie $O(N \log N)$.
scal_przedzialy() {
    # Wejscie: linie "a b"; wyjscie: scalone przedzialy, rosnaco.
    # Sortowanie numeryczne wedlug poczatku (i konca), potem jedno przejscie.
    local a b poczatek="" koniec=""
    while read -r a b; do
        if [[ -n $poczatek ]] && ((a <= koniec)); then
            ((b > koniec)) && koniec=$b
        else
            [[ -n $poczatek ]] && echo "$poczatek $koniec"
            poczatek=$a
            koniec=$b
        fi
    done < <(sort -n -k1,1 -k2,2)
    [[ -n $poczatek ]] && echo "$poczatek $koniec"
    return 0
}

main() {
    local n i linia
    read -r n
    for ((i = 0; i < n; i++)); do
        read -r linia
        echo "$linia"
    done | scal_przedzialy
}

main "$@"
