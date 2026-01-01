/*
ZAD-04 — Dziedziczenie wielopoziomowe: Człowiek → Student → StudentFizyki

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `konstruktory`, `super`

### Treść

Zaprojektuj hierarchię klas:

1. **Człowiek** — pola:

   * imię
   * nazwisko
   * miejsce urodzenia
   * zawód

2. **Student** (dziedziczy po `Człowiek`) — dodatkowo:

   * numer albumu
   * kierunek studiów

3. **StudentFizyki** (dziedziczy po `Student`) — dodatkowo:

   * średnia z laboratoriów
   * średnia z wykładów

Program:

* wczytuje dane dla trzech obiektów (Człowiek, Student, StudentFizyki),
* tworzy obiekty,
* wypisuje je w formacie jak w przykładzie.

**Uwaga do wejścia:** wszystko w osobnych liniach, w podanej kolejności.

### Wejście

**Dane dla Człowiek:**

1. imię
2. nazwisko
3. miejsce urodzenia
4. zawód

**Dane dla Student:**
5. imię
6. nazwisko
7. miejsce urodzenia
8. zawód
9. numer albumu (int)
10. kierunek studiów

**Dane dla StudentFizyki:**
11. imię
12. nazwisko
13. miejsce urodzenia
14. zawód
15. numer albumu (int)
16. kierunek studiów
17. średnia z laboratoriów (float)
18. średnia z wykładów (float)

### Wyjście

Trzy bloki jak w przykładzie, oddzielone pustą linią.

### Przykład

**Wejście:**

```
Jan
Kowalski
Kraków
Inżynier
Anna
Nowak
Warszawa
Student
12345
Informatyka
Piotr
Wiśniewski
Gdańsk
Student
54321
Fizyka
4.5
4.0
```

**Wyjście:**

```
Człowiek:
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Kraków
Zawód: Inżynier

Student:
Imię: Anna
Nazwisko: Nowak
Miejsce urodzenia: Warszawa
Zawód: Student
Numer albumu: 12345
Kierunek studiów: Informatyka

Student Fizyki:
Imię: Piotr
Nazwisko: Wiśniewski
Miejsce urodzenia: Gdańsk
Zawód: Student
Numer albumu: 54321
Kierunek studiów: Fizyka
Średnia z laboratoriów: 4.5
Średnia z wykładów: 4.0
```

*/

use std::io;

// Struktura bazowa Człowiek
// Złożoność pamięciowa: O(n), gdzie n to długość stringów
#[derive(Debug, Clone)]
struct Czlowiek {
    imie: String,
    nazwisko: String,
    miejsce_urodzenia: String,
    zawod: String,
}

impl Czlowiek {
    fn new(imie: String, nazwisko: String, miejsce_urodzenia: String, zawod: String) -> Self {
        Czlowiek {
            imie,
            nazwisko,
            miejsce_urodzenia,
            zawod,
        }
    }
    
    fn wypisz(&self) {
        println!("Imię: {}", self.imie);
        println!("Nazwisko: {}", self.nazwisko);
        println!("Miejsce urodzenia: {}", self.miejsce_urodzenia);
        println!("Zawód: {}", self.zawod);
    }
}

// Struktura Student dziedzicząca (kompozycja) po Człowiek
#[derive(Debug, Clone)]
struct Student {
    czlowiek: Czlowiek,
    numer_albumu: i32,
    kierunek: String,
}

impl Student {
    fn new(imie: String, nazwisko: String, miejsce_urodzenia: String, 
           zawod: String, numer_albumu: i32, kierunek: String) -> Self {
        Student {
            czlowiek: Czlowiek::new(imie, nazwisko, miejsce_urodzenia, zawod),
            numer_albumu,
            kierunek,
        }
    }
    
    fn wypisz(&self) {
        self.czlowiek.wypisz();
        println!("Numer albumu: {}", self.numer_albumu);
        println!("Kierunek studiów: {}", self.kierunek);
    }
}

// Struktura StudentFizyki dziedzicząca po Student
#[derive(Debug, Clone)]
struct StudentFizyki {
    student: Student,
    srednia_lab: f64,
    srednia_wyklady: f64,
}

impl StudentFizyki {
    fn new(imie: String, nazwisko: String, miejsce_urodzenia: String,
           zawod: String, numer_albumu: i32, kierunek: String,
           srednia_lab: f64, srednia_wyklady: f64) -> Self {
        StudentFizyki {
            student: Student::new(imie, nazwisko, miejsce_urodzenia, zawod, numer_albumu, kierunek),
            srednia_lab,
            srednia_wyklady,
        }
    }
    
    fn wypisz(&self) {
        self.student.wypisz();
        println!("Średnia z laboratoriów: {}", self.srednia_lab);
        println!("Średnia z wykładów: {}", self.srednia_wyklady);
    }
}

fn wczytaj_linie() -> String {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Błąd wczytywania");
    input.trim().to_string()
}

fn main() {
    // Wczytaj dane dla Człowiek
    let c_imie = wczytaj_linie();
    let c_nazwisko = wczytaj_linie();
    let c_miejsce = wczytaj_linie();
    let c_zawod = wczytaj_linie();
    
    // Wczytaj dane dla Student
    let s_imie = wczytaj_linie();
    let s_nazwisko = wczytaj_linie();
    let s_miejsce = wczytaj_linie();
    let s_zawod = wczytaj_linie();
    let s_album: i32 = wczytaj_linie().parse().unwrap_or(0);
    let s_kierunek = wczytaj_linie();
    
    // Wczytaj dane dla StudentFizyki
    let sf_imie = wczytaj_linie();
    let sf_nazwisko = wczytaj_linie();
    let sf_miejsce = wczytaj_linie();
    let sf_zawod = wczytaj_linie();
    let sf_album: i32 = wczytaj_linie().parse().unwrap_or(0);
    let sf_kierunek = wczytaj_linie();
    let sf_lab: f64 = wczytaj_linie().parse().unwrap_or(0.0);
    let sf_wyklady: f64 = wczytaj_linie().parse().unwrap_or(0.0);
    
    // Twórz obiekty i wypisuj
    let czlowiek = Czlowiek::new(c_imie, c_nazwisko, c_miejsce, c_zawod);
    czlowiek.wypisz();
    println!();
    
    let student = Student::new(s_imie, s_nazwisko, s_miejsce, s_zawod, s_album, s_kierunek);
    student.wypisz();
    println!();
    
    let student_fizyki = StudentFizyki::new(sf_imie, sf_nazwisko, sf_miejsce, sf_zawod, 
                                            sf_album, sf_kierunek, sf_lab, sf_wyklady);
    student_fizyki.wypisz();
}
