/*
Dla pobranej liczby, sprawdz czy liczba jest ujemna, dodatnia, czy jest
zerem.
*/

use ::std::*;

fn main() {

	println!("Podaj liczbe: ");
	let mut liczba = String::new();
	std::io::stdin().read_line(&mut liczba).expect("Blad odczytu");
	let liczba: i32 = liczba.trim().parse().expect("Blad parsowania");

	if liczba < 0 {
		println!("Liczba jest ujemna");
	} else if liczba > 0 {
		println!("Liczba jest dodatnia");
	} else {
		println!("Liczba jest zerem");
	}
	
}
