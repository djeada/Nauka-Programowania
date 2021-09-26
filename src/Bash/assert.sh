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

check_integer() {

    if [[ "$1" =~ ^-?[0-9]+$ ]]; then
        echo 1
        return
    fi

    echo 0

}

assertEqual () {
    local lineno=$3

    if [ $(check_integer "$1") -eq 1 ] && [ $(check_integer "$2") -eq 1 ]; then
        if [ "$1" -ne "$2" ]; then
            echo "Assertion failed:  \"$1\""
            echo "File \"$0\", line $lineno"
            exit $E_ASSERT_FAILED
        fi
    else
        if [[ "$1" != "$2" ]]; then
            echo "Assertion failed:  \"$1\""
            echo "File \"$0\", line $lineno"
            exit $E_ASSERT_FAILED
        fi
    fi
}

assertNotEqual () {
    local lineno=$3

    if [ $(check_integer "$1") -eq 1 ] && [ $(check_integer "$2") -eq 1 ]; then
        if [ "$1" -eq "$2" ]; then
            echo "Assertion failed:  \"$1\""
            echo "File \"$0\", line $lineno"
            exit $E_ASSERT_FAILED
        fi
    else
        if [[ "$1" == "$2" ]]; then
            echo "Assertion failed:  \"$1\""
            echo "File \"$0\", line $lineno"
            exit $E_ASSERT_FAILED
        fi
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
        assertEqual "${array_a[$i]}" "${array_b[$i]}" $lineno
    done

}

assertSetsEqual() {
    local -n array_1=$1
    local -n array_2=$2
    local lineno=$3

    IFS=$'\n' array_1=($(sort <<<"${array_1[*]}")); unset IFS
    IFS=$'\n' array_2=($(sort <<<"${array_2[*]}")); unset IFS

    assertArrayEqual array_1 array_2 $lineno

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
