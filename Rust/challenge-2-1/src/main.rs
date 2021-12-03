fn main() {
    let mut input = vec!["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"];
    let mut hpos = 0;
    let mut depth = 0;
    for i in 0..input.len() {
        let split = (input[i].split(" ")).collect::<Vec<&str>>();
        let direction = split[0];
        let distance = split[1].parse::<i32>().unwrap();
        println!("{}", direction);
        println!("{}", distance);
        if direction == "up" {
            depth = depth - distance;
        } else if direction == "down" {
            depth = depth + distance;
        } else if direction == "forward" {
            hpos = hpos + distance;
        }
    }
    let solution = hpos * depth;
    println!("{}", solution);
}
