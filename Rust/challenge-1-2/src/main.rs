fn main() {
    let values = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    let mut increases = 0;
    for i in 3..values.len() {
        if values[i] > values[i-3] {
            increases = increases + 1;
        }
    }
    println!("{}", increases);
}
