use std::iter::Iterator;
use std::iter::FromIterator;

fn sort_v1(napis: String ) -> String {
    let s_slice: &str = &napis[..];
    let mut chars: Vec<char> = s_slice.chars().collect();
    chars.sort_by(|a, b| a.cmp(b));
    return String::from_iter(chars);
}

fn test_1() {
	let napis: String = "cab".to_owned();
	let wynik = "abc".to_owned();
	assert_eq!(sort_v1(napis), wynik);
}

fn test_2() {
	let napis: String = "eDedCBcbAaa".to_owned();
	let wynik = "ABCDabcdeae".to_owned();
	assert_eq!(sort_v1(napis), wynik);
}

fn main() {
	test_1();
	test_2();
}
