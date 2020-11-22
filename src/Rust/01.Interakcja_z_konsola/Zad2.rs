
use ::std::*;

fn main() {
	
	/*
	Wypisz na konsole najpierw druga potem pierwsza pobrana dana.
	*/
    
	println!("Podaj dwie liczby oddzielone spacjami.");
	let cin = std::io::stdin();
	let mut buffer = String::new();
	cin.read_line(&mut buffer).unwrap();
	let wartosci = buffer.split_whitespace().map(|x| x.parse::<i32>()).collect::<Result<Vec<i32>, _>>().unwrap();
	assert!(wartosci.len() == 2);
	let a = wartosci[0];
	let b = wartosci[1];
	println!("{} {}", b, a);

}
