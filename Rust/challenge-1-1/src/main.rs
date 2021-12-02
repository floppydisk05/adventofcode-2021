fn main() {
    let values = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    let mut increases = 0;
    for i in 1..values.len() {
        if (i != 0) && (values[i] > values[i-1]) {
            increases = increases + 1;
        }
    }
    println!("{}", increases);
}
