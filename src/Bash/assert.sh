E_ASSERT_FAILED=99
E_PARAM_ERR=98


assert () {
    if [ -z "$2" ]; then
        return $E_PARAM_ERR
    fi

    local lineno=$2

    if [ ! $1 ]; then
        echo "Assertion failed:  \"$1\""
        echo "File \"$0\", line $lineno"
        exit $E_ASSERT_FAILED
    fi
}

assertEqual () {
    local lineno=$3

    if [ $1 -ne $2 ]; then
        echo "Assertion failed:  \"$1\""
        echo "File \"$0\", line $lineno"
        exit $E_ASSERT_FAILED
    fi
}

assertNotEqual () {
    local lineno=$3

    if [ $1 -eq $2 ]; then
        echo "Assertion failed:  \"$1\""
        echo "File \"$0\", line $lineno"
        exit $E_ASSERT_FAILED
    fi
}

assertArrayEqual() {
    local -n array_a=$1
    local -n array_b=$2
    local lineno=$3

    #check length equal
    n=$(( ${#array_a[@]}))
    m=$(( ${#array_b[@]}))

    assertEqual $n $m $lineno

    #check element for element
    for (( i=0; i<n; i++ ))
    do
        assertEqual ${array_a[$i]} ${array_b[$i]} $lineno
    done

}

assertTrue () {
    local lineno=$2

    if [ "$1" = false ]; then
        echo "Assertion failed:  \"$1\""
        echo "File \"$0\", line $lineno"
        exit $E_ASSERT_FAILED
    fi
}

assertFalse () {
    local lineno=$2

    if [ "$1" = true ]; then
        echo "Assertion failed:  \"$1\""
        echo "File \"$0\", line $lineno"
        exit $E_ASSERT_FAILED
    fi
}
