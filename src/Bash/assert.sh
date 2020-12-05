assert () {                     
	E_ASSERT_FAILED=99
	E_PARAM_ERR=98

	if [ -z "$2" ]; then
		return $E_PARAM_ERR
	fi

	lineno=$2

	if [ ! $1 ]; then
		echo "Assertion failed:  \"$1\""
		echo "File \"$0\", line $lineno"
		exit $E_ASSERT_FAILED
	fi
}  

assertTrue () {
	E_ASSERT_FAILED=99
	E_PARAM_ERR=98
	lineno=$2

	if [ "$1" = false ]; then
		echo "Assertion failed:  \"$1\""
		echo "File \"$0\", line $lineno"
		exit $E_ASSERT_FAILED
	fi

}

assertFalse () {
	E_ASSERT_FAILED=99
	E_PARAM_ERR=98
	lineno=$2

	if [ "$1" = true ]; then
		echo "Assertion failed:  \"$1\""
		echo "File \"$0\", line $lineno"
		exit $E_ASSERT_FAILED
	fi

}
