/*
Pobierz od uzytkownika trzy dlugosci bokow i sprawdz, czy mozna z nich zbudowac
trojkat.
*/

use ::std::*;

fn main() {

	println!("Podaj trzy boki trojkata oddzielone spacjami: ");
	let mut wiersz = String::new();
	std::io::stdin().read_line(&mut wiersz).expect("Blad odczytu");
	let liczby: Vec<i32> = wiersz.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();

	let bok_a = liczby[0];
	let bok_b = liczby[1];
	let bok_c = liczby[2];

	if bok_a + bok_b > bok_c && bok_a + bok_c > bok_b && bok_b + bok_c > bok_a {
		println!("Można zbudować trojkat z podanych boków.");
	} else {
		println!("Nie można zbudować trojkata z podanych boków.");
	}
	
}
