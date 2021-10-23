Jeśli chcesz poprawić istniejące rozwiązanie, dodać test lub rozwiązanie alternatywne postępuj zgodnie z tą instruckją:

<h2>Jakie zmiany są mile widziane?</h2>

1. Nowe rozwiązanie do zadania, które jeszcze nie zostało roziwązane.
2. Dodanie alternatywnej wersji do rozwiązania już istniejącego, która redukuje złożoność czasową lub pamięciową.
3. Dodanie alternatywnej wersji do rozwiązania już istniejącego, która nie redukuje złożoności czasowej ani pamięciowej, ale zwiększa czytelność kodu.
4. Dodanie alternatywnej wersji do rozwiązania już istniejącego, która nie redukuje złożoności czasowej ani pamięciowej, ale używa nowszej wersji składni.
5. Poprawnie błędu składni, literówki lub błędów logicznych w rozwiązaniach już istniejącyh.

<h2>Instrukcja techniczna</h2>

1. Utwórz kopię "Fork" tego repozytorium na swoim koncie na stronie <a href="https://github.com">github.com</a>.
2. Sklonuj ten projekt na swój komputer.

```bash
git clone https://github.com/djeada/Nauka-programowania.git
```

3. Dodaj nową gałąź. Możesz na przkład nazwać ją 

```bash
git checkout -b nazwa-galezi
```

4. Dodaj zmiany i opisz je w wiadomości "commit". Przykład: "Dodano rozwiazanie do zadania 6 z wprowadzenie do list - java".
5. Użyj komendy <i>git push</i>.

```bash
git add changed_file
git commit -m "twoj komentarz do wprowadzanych zmian"
git push origin nazwa-galezi
```
Zaloguj się na stronę <a href="https://github.com">github.com</a> i stwórz pull-request w swojej kopii repozytorium.
