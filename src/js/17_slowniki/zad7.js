/*


Tytuł: Histogram słów w tekście

Treść: Otrzymujesz tekst w postaci napisu. Twoim zadaniem jest znaleźć częstość występowania każdego ze słów w tekście. Należy zignorować różnice między małymi i wielkimi literami. Pamiętaj, że słowa składają się wyłącznie z liter.

Dane wejściowe: Napis.

Dane wyjściowe: Słownik par: napis, liczba naturalna.

Przykład:

Dla otrzymanego napisu: "Here, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, perhaps a bit; in particular since my tricksy corpus will not match the pattern you expect from it; nor will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now."

Powinien zostać zwrócony słownik:

{"here": 1, "a": 12, "tricksy": 4, "corpus": 5, "will": 6, "exist": 1, "very": 2, "strange": 1, "sometimes": 1, "cryptic": 1, "dumbfound": 1, "you": 2, "maybe": 1, "perhaps": 1, "bit": 1, "in": 1, "particular": 1, "since": 1, "my": 1, "not": 1, "match": 1, "the": 2, "pattern": 1, "expect": 1, "from": 2, "it": 2, "nor": 1, "look": 1, "like": 1, "fish": 1, "boat": 1, "sunflower": 1, "or": 3, "handsome": 1, "kitten": 1, "surprise": 1, "user": 1, "named": 1, "ami": 1, "tavory": 1, "this": 1, "be": 1, "fun": 1, "to": 1, "follow": 1, "year": 1, "month": 1, "minute": 1, "now": 1}
*/

function histogramSlow(napis) {
  const slowa = napis.toLowerCase().match(/\b\w+\b/g);
  const slownik = {};
  for (let i = 0; i < slowa.length; i++) {
    const slowo = slowa[i];
    if (slownik[slowo]) {
      slownik[slowo]++;
    } else {
      slownik[slowo] = 1;
    }
  }
  return slownik;
}

function testHistogramSlow() {
  const napis1 =
    "Here, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, perhaps a bit; in particular since my tricksy corpus will not match the pattern you expect from it; nor will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now.";
  const wynik1 = histogramSlow(napis1);
  assert(wynik1["here"] === 1, "Test 1 nie powiódł się");
  assert(wynik1["a"] === 12, "Test 2 nie powiódł się");
  assert(wynik1["tricksy"] === 4, "Test 3 nie powiódł się");
  assert(wynik1["corpus"] === 5, "Test 4 nie powiódł się");
  assert(wynik1["will"] === 6, "Test 5 nie powiódł się");

  const napis2 = "Ala ma kota, a kot ma Alę.";
  const wynik2 = histogramSlow(napis2);
  assert(wynik2["ala"] === 2, "Test 6 nie powiódł się");
  assert(wynik2["ma"] === 2, "Test 7 nie powiódł się");
  assert(wynik2["kota"] === 1, "Test 8 nie powiódł się");
}

// test
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Asercja nie powiodła się");
  }
}

testHistogramSlow();
