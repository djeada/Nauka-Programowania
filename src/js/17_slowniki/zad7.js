/*
Otrzymujesz tekst w postaci napisu. Znajdz czestosc wystepowania kazdego
ze slow w tekscie. Zignoruj roznice miedzy malymi i wielkimi literami.
Pamietaj, slowa skladaja sie wylacznie z liter.
*/

budujSlownik = function (napis) {
  histogram = {};
  for (const slowo of napis.split(" ")) {
    slowoBezZnakow = slowo.replace(/[^a-z]/gi, "");
    slowoBezZnakow = slowoBezZnakow.toLowerCase();
    if (histogram[slowoBezZnakow] === undefined) {
      histogram[slowoBezZnakow] = 1;
    } else {
      histogram[slowoBezZnakow]++;
    }
  }

  return histogram;
};

test1 = function () {
  slowo =
    "Here,,,, a tricksy corpus will exist; a very strange, a " +
    "sometimes cryptic corpus will dumbfound you maybe, " +
    "perhaps a bit; in particular since my tricksy corpus " +
    "will not match the pattern you EXPECT from it; nor " +
    "will it look like a fish, a boat, a sunflower, or a " +
    "very handsome kitten. The tricksy corpus will surprise " +
    "a user named Ami Tavory; this tricksy corpus will be " +
    "fun to follow a year or a month or a minute from now.";

  oczekiwane = {
    here: 1,
    a: 12,
    tricksy: 4,
    corpus: 5,
    will: 6,
    exist: 1,
    very: 2,
    strange: 1,
    sometimes: 1,
    cryptic: 1,
    dumbfound: 1,
    you: 2,
    maybe: 1,
    perhaps: 1,
    bit: 1,
    in: 1,
    particular: 1,
    since: 1,
    my: 1,
    not: 1,
    match: 1,
    the: 2,
    pattern: 1,
    expect: 1,
    from: 2,
    it: 2,
    nor: 1,
    look: 1,
    like: 1,
    fish: 1,
    boat: 1,
    sunflower: 1,
    or: 3,
    handsome: 1,
    kitten: 1,
    surprise: 1,
    user: 1,
    named: 1,
    ami: 1,
    tavory: 1,
    this: 1,
    be: 1,
    fun: 1,
    to: 1,
    follow: 1,
    year: 1,
    month: 1,
    minute: 1,
  };

  wynik = budujSlownik(slowo);
  if (oczekiwane.length !== wynik.length) {
    throw new Error(
      `Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`
    );
  }

  for (const key in oczekiwane) {
    if (oczekiwane[key] !== wynik[key]) {
      throw new Error(
        `Assertion error line 34: ${wynik[key]} != ${oczekiwane[key]}`
      );
    }
  }
};

test2 = function () {
  slowo =
    "The most intelligent people disguise the fact that they " +
    "are intelligent.  Wise men do not wear name tags., " +
    "The more people talk about their own skills, the more " +
    "desperate they are--their work should speak for itself.";

  oczekiwane = {
    itself: 1,
    should: 1,
    desperate: 1,
    aretheir: 1,
    own: 1,
    their: 1,
    tags: 1,
    name: 1,
    wear: 1,
    the: 4,
    work: 1,
    most: 1,
    they: 2,
    intelligent: 2,
    for: 1,
    speak: 1,
    skills: 1,
    not: 1,
    people: 2,
    fact: 1,
    about: 1,
    do: 1,
    talk: 1,
    more: 2,
    disguise: 1,
    that: 1,
    are: 1,
    wise: 1,
    men: 1,
  };

  wynik = budujSlownik(slowo);
  if (oczekiwane.length !== wynik.length) {
    throw new Error(
      `Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`
    );
  }

  for (const key in oczekiwane) {
    if (oczekiwane[key] !== wynik[key]) {
      throw new Error(
        `Assertion error line 34: ${wynik[key]} != ${oczekiwane[key]}`
      );
    }
  }
};

main = function () {
  test1();
  test2();
};

main();
