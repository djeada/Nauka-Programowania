    usunCzescWspolnaV1 = function(listaA, listaB) {
        for (var i = 0; i < listaA.length; i++) {
            {
                if ((listaB.indexOf((listaA[i])) >= 0)) {
                    listaA.splice(i, 1)[0];
                    i--;
                }
            };
        }
        return listaA;
    };
    test1 = function() {
        var listaA = [3, 6, 2, 7, 9]
        var listaB = [4, 2, 3, 5, 6]
        var oczekiwane = [7, 9]
        var wynik = usunCzescWspolnaV1(listaA, listaB);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 33: ${wynik[i]} != ${oczekiwane[i]}`);
            }
        }
    };
    main = function(args) {
        test1();
    };

    main(null);