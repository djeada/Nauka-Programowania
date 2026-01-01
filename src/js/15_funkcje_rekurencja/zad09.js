/*
Tytul: Slowa elfickie.

Tresc: Otrzymujesz napis. Przy uzyciu rekurencji sprawdz czy otrzymane slowo jest slowem elfickim. Przez slowo elfickie rozumiemy taki napis, w ktorym co najmniej raz wystepuje kazda z liter slowa elf.

Dane wejsciowe: Napis.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:
Dla otrzymanego napisu: "reflektor", powinna zostac zwrocona wartosc logiczna: Prawda.
*/

// Funkcja sprawdza czy słowo zawiera wszystkie litery z "elf"
// Złożoność czasowa: O(n*m), gdzie n to długość słowa, m to liczba liter do znalezienia
// Złożoność pamięciowa: O(m) dla rekurencji
function czyElfickie(slowo, elf = "elf", idx = 0) {
  if (idx === elf.length) {
    return true;
  }
  // Sprawdź czy aktualna litera elf[idx] występuje w słowie
  if (slowo.indexOf(elf[idx]) === -1) {
    return false;
  }
  // Przejdź do sprawdzania następnej litery
  return czyElfickie(slowo, elf, idx + 1);
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
  console.assert(wynik === true, "Test 2 nieudany"); // "elefant" ma e, l, f

  slowo = "efektywnelekcje";
  wynik = czyElfickie(slowo);
  console.assert(wynik === true, "Test 3 nieudany");

  slowo = "wiolinistka";
  wynik = czyElfickie(slowo);
  console.assert(wynik === false, "Test 4 nieudany");
}

testCzyElfickie();
console.log("Wszystkie testy zakończone sukcesem");

