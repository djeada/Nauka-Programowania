# ZAD-15 — Akronim ze zdania
#
# **Poziom:** ★☆☆
# **Tagi:** `napisy`, `słowa`, `upper`
#
# ### Treść
#
# **Akronim** to skrót utworzony z pierwszych liter kolejnych słów, np. „Polska Akademia Nauk” → `PAN`.
#
# Wczytaj zdanie i wypisz jego akronim: pierwsze znaki wszystkich słów (zgodnie z konwencją rozdziału — bez interpunkcji), zapisane jeden za drugim **wielkimi** literami.
#
# ### Wejście
#
# * 1. linia: zdanie (zawiera co najmniej jedno słowo; może zawierać polskie litery)
#
# ### Wyjście
#
# Jedna linia: akronim.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Polska Akademia Nauk
# ```
#
# **Wyjście:**
#
# ```
# PAN
# ```
#
# ### Uwagi
#
# * Słowa mogą być rozdzielone kilkoma spacjami, a zdanie może zaczynać się lub kończyć spacjami — `split()` bez argumentu poradzi sobie z tym.
# * Interpunkcja nie należy do słowa: w zdaniu `(Unia Europejska)` słowami są `Unia` i `Europejska`, więc akronim to `UE`. Samotny myślnik `-` nie jest słowem.
# * Zamiana na wielką literę dotyczy także polskich liter: `żółta łódź` → `ŻŁ`.
export LC_ALL=C.UTF-8
shopt -s extglob

akronim() {
    # Akronim: wielkie pierwsze litery kolejnych slow (bez interpunkcji)
    local zdanie=$1 fragment slowo wynik="" pierwsza
    local -a fragmenty
    read -ra fragmenty <<<"$zdanie"
    for fragment in "${fragmenty[@]}"; do
        slowo=${fragment##+([[:punct:]])}
        slowo=${slowo%%+([[:punct:]])}
        if [[ -n $slowo ]]; then
            pierwsza=${slowo:0:1}
            wynik+=${pierwsza^^}
        fi
    done
    echo "$wynik"
}

main() {
    local zdanie
    IFS= read -r zdanie
    akronim "$zdanie"
}

main "$@"
