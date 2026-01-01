# ZAD-08 — Cyfry w słowach
#
# **Poziom:** ★★☆
# **Tagi:** `regex`, `string`
#
# ### Treść
#
# Otrzymujesz zdanie. Wyodrębnij wszystkie ciągi cyfr, które są częścią słów (czyli są bezpośrednio połączone z literami). Nie uwzględniaj cyfr oddzielonych od liter spacjami.
#
# ### Wejście
#
# Jedna linia:
#
# * `zdanie`
#
# ### Wyjście
#
# Każdy znaleziony ciąg cyfr w osobnej linii (w kolejności występowania).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego
# ```
#
# **Wyjście:**
#
# ```
# 29
# 37
# 3
# 91
# ```

source ../assert.sh

cyfry_bedace_czescia_slow() {
    local zdanie="$1"
    local cyfry=()

    for slowo in $zdanie; do
        if [[ $slowo =~ [a-zA-Z]+ ]]; then
            cyfry+=($(echo $slowo | sed -r 's/[a-zA-Z|]+//g'))
        fi
    done

    echo ${cyfry[@]}
}

test_cyfry_bedace_czescia_slow() {
    local zdanie="jerzy29 i an37a s3uc8ali91 lekcji jezyka polki3go"
    local wynik=($(cyfry_bedace_czescia_slow "$zdanie"))
    local oczekiwane=(29 37 3891 3)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_cyfry_bedace_czescia_slow
}

main "$@"
