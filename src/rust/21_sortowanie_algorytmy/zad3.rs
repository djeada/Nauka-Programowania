fn sort_v1(lista: &mut [i32]) {

	for i in 1..lista.len() {
		let mut j = i;
		while j > 0 && lista[j - 1] > lista[j] {
			lista.swap(j - 1, j);
			j -= 1;
		}
	}
}

fn sort_v2(lista: &mut [i32]) {
	for x in 1..lista.len() {
		let i = match lista[..x].binary_search(&lista[x]) {
			Ok(i) => i,
			Err(i) => i,
		};
		lista[i..=x].rotate_right(1);
	}
}

fn test_1() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v1(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn test_2() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v2(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn main() {
	test_1();
	test_2();
}
