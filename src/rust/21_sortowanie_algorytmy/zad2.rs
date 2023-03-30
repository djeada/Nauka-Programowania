fn sort_v1(lista: &mut [i32]) {

	for i in 0..lista.len() {
		let mut pom = i;
		for j in (i + 1)..lista.len() {
			if lista[pom] > lista[j] {
				pom = j;
			}
		}
		lista.swap(i, pom);
	}
}

fn sort_v2(lista: &mut [i32]) {
	for x in 0..lista.len() {
		let min = lista[x..]
		.iter()
		.enumerate()
		.min_by_key(|&(_, v)| v)
		.map(|(i, _)| x + i)
		.expect("lista is non-empty");

		if x != min {
			lista.swap(x, min);
		}
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

