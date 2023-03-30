/*
Wypisz wynik nastepujacych operacji arytmetycznych dla dwoch liczb pobranych od
uzytkownika:

a) Suma liczb.
b) Roznica pierwszej i drugiej liczby.
c) Iloczyn liczb.
d) Iloraz pierwszej liczby przez druga.
e) Reszta z dzielenia pierwszej liczby przez druga.
f) Pierwsza liczba podniesiona do potegi rownej drugiej liczbie.
*/

use ::std::*;

fn main() {
	

	println!("Podaj dwie liczby oddzielone spacjami.");
	let mut line = String::new();
	std::io::stdin().read_line(&mut line).unwrap();
	let numbers: Vec<i32> = line.trim().split(' ').map(|x| x.parse::<i32>().unwrap()).collect();
	println!("{} {}", numbers[0], numbers[1]);
	
	println!("Suma liczb: {}", numbers[0] + numbers[1]);
	println!("Roznica pierwszej i drugiej liczby: {}", numbers[0] - numbers[1]);
	println!("Iloczyn liczb: {}", numbers[0] * numbers[1]);
	println!("Iloraz pierwszej liczby przez druga: {}", numbers[0] / numbers[1]);
	println!("Reszta z dzielenia pierwszej liczby przez druga: {}", numbers[0] % numbers[1]);
	println!("Pierwsza liczba podniesiona do potegi rownej drugiej liczbie: {}", numbers[0].pow(numbers[1]));

}

