/*
Tytuł: Słowa elfickie.

Treść: Otrzymujesz napis. Przy użyciu rekurencji sprawdź czy otrzymane słowo jest słowem elfickim. Przez słowo elfickie rozumiemy taki napis, w którym co najmniej raz występuje każda z liter słowa elf.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:
Dla otrzymanego napisu: "reflektor", powinna zostać zwrócona wartość logiczna: Prawda.
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

function assert(warunek, komunikat) {
  if (!warunek) {
    throw komunikat || "Wystąpił błąd";
  }
}

// Testy
function testCzyElfickie() {
  let slowo;
  let wynik;

  slowo = "reflektor";
  wynik = czyElfickie(slowo);
  assert(wynik === true, "Test 1 nieudany");

  slowo = "elefant";
  wynik = czyElfickie(slowo);
  assert(wynik === false, "Test 2 nieudany");

  slowo = "efektywnelekcje";
  wynik = czyElfickie(slowo);
  assert(wynik === true, "Test 3 nieudany");

  slowo = "wiolinistka";
  wynik = czyElfickie(slowo);
  assert(wynik === false, "Test 4 nieudany");
}

testCzyElfickie();
console.log("Wszystkie testy zakończone sukcesem");
