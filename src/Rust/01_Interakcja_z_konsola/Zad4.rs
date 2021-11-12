
use ::std::*;

fn main() {
	
	/*
	Wypisz wynik podstawowych operacji arytmetycznych 
	dla dwoch liczb pobranych od uzytkownika.
	*/
    
	println!("Podaj dwie liczby oddzielone spacjami.");
	let cin = std::io::stdin();
	let mut buffer = String::new();
	cin.read_line(&mut buffer).unwrap();
	let wartosci = buffer.split_whitespace().map(|x| x.parse::<i32>()).collect::<Result<Vec<i32>, _>>().unwrap();
	assert!(wartosci.len() == 2);
	let x: i32 = wartosci[0];
	let y: i32 = wartosci[1];

	println!("Suma {} oraz {} wynosi {}", x, y, x + y);
	println!("Roznica {} i {} wynosi {}", x, y, x - y);
	println!("Iloczyn {} i {} wynosi {}", x, y, x * y);
	println!("Iloraz {} przez {} wynosi {}", x, y, x / y);
	println!("Reszta z dzielenia {} przez {} wynosi {}", x, y, x % y);

    	let z: u32 = y as u32;
	println!("{} podniesione do {} wynosi {}", x, y, x.pow(z));
}
