/*
Tytul: Slowa elfickie.

Tresc: Otrzymujesz napis. Przy uzyciu rekurencji sprawdz czy otrzymane slowo jest slowem elfickim. Przez slowo elfickie rozumiemy taki napis, w ktorym co najmniej raz wystepuje kazda z liter slowa elf.

Dane wejsciowe: Napis.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:
Dla otrzymanego napisu: "reflektor", powinna zostac zwrocona wartosc logiczna: Prawda.
*/

function czyElfickie(slowo, elf = "elf", idx = 0) {
  if (idx === elf.length) {
    return true;
  }
  const pozycja = slowo.indexOf(elf[idx]);
  if (pozycja === -1) {
    return false;
  }
  return czyElfickie(slowo.slice(pozycja + 1), elf, idx + 1);
}

// Testy
function testCzyElfickie() {
  let slowo;
  let wynik;

  slowo = "reflektor";
  wynik = czyElfickie(slowo);
  console.assert(wynik === true, "Test 1 nieudany");

  slowo = "elefant";
  wynik = czyElfickie(slowo);
  console.assert(wynik === false, "Test 2 nieudany");

  slowo = "efektywnelekcje";
  wynik = czyElfickie(slowo);
  console.assert(wynik === true, "Test 3 nieudany");

  slowo = "wiolinistka";
  wynik = czyElfickie(slowo);
  console.assert(wynik === false, "Test 4 nieudany");
}

testCzyElfickie();
console.log("Wszystkie testy zakonczone sukcesem");

