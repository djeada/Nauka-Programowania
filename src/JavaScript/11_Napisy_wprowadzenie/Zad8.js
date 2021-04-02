var Main =  (function() {
    function Main() {}
    Main.wyczysc = function(napis) {
        napis = napis.trim();
        return napis.replace(/[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, "");
    };
    Main.slowaV1 = function(napis) {
        var pocz = 0;
        var konc = 0;
        while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
            {
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz, konc);
                    slowo = Main.wyczysc(slowo);
                    if (!(slowo.length === 0)) {
                        console.info(slowo);
                    }
                }
                pocz = konc + 1;
            }
        };
        if (konc !== pocz) {
            var slowo = napis.substring(pocz);
            slowo = Main.wyczysc(slowo);
            if (!(slowo.length === 0)) {
                console.info(slowo);
            }
        }
    };
    Main.main = function(args) {
        var napis = "We think in generalities, but we live in details";
        Main.slowaV1(napis);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
