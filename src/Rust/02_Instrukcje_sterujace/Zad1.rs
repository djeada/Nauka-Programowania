/*
Wypisz pobrana od uzytkownika liczbe, jesli jest ona wieksza niz 5.
*/

use ::std::*;

fn main() {

	println!("Podaj liczbe: ");
	let mut liczba = String::new();
	std::io::stdin().read_line(&mut liczba).expect("Blad odczytu");
	let liczba: i32 = liczba.trim().parse().expect("Blad parsowania");
	
	if liczba > 5 {
		println!("Liczba {} jest wieksza od 5", liczba);
	}
}
