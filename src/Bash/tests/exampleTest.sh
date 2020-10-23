#!/usr/bin/env bash

source ../assert.sh

main() {
 
	a=5
	b=4
	assert "$a -gt $b" $LINENO
}

main "$@"

