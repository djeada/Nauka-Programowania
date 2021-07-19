#!/usr/bin/env bash

#Czy rok jes przestepny?

main() {

    echo "Podaj rok:"
    read rok

    if [[ $(($rok % 4)) -eq 0 ]]; then
        if [[ $(($rok % 100)) -eq 0 ]]; then
            if [[ $(($rok % 400)) -eq 0 ]]; then
                echo "rok jest przestepny"
            else
                echo "rok nie jest przestepny"
            fi
        else
            echo "rok jest przestepny"
        fi
    else
        echo "rok nie jest przestepny"
    fi
}

main "$@"

