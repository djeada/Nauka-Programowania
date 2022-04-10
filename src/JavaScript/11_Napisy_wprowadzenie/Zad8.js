var Main = (function() {
            wyczysc = function(napis) {
                napis = napis.trim();
                return napis.replace(/[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, "");
            };
            slowaV1 = function(napis) {
                var pocz = 0;
                var konc = 0;
                while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
                    {
                        if (konc !== pocz) {
                            var slowo = napis.substring(pocz, konc);
                            slowo = wyczysc(slowo);
                            if (!(slowo.length === 0)) {
                                console.info(slowo);
                            }
                        }
                        pocz = konc + 1;
                    }
                };
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz);
                    slowo = wyczysc(slowo);
                    if (!(slowo.length === 0)) {
                        console.info(slowo);
                    }
                }
            };
            main = function(args) {
                var napis = "We think in generalities, but we live in details";
                slowaV1(napis);
            };

            main(null);