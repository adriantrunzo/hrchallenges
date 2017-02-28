///
///    arrays.rs
///
///    Solution to puzzle found at
///    https://www.hackerrank.com/challenges/arrays-ds
///
///    Author: Adrian Trunzo

use std::io;

// Take a slice and print it in reverse using an iterator. An iterator
// here seems more idiomatic than a for loop with a counter.
fn reverse_print(v: &[i32]) {

    let mut reverse = v.iter().rev();
    while let Some(i) = reverse.next() {
        print!("{} ", i);
    }
}

fn main() {

    // We'll read into this mutable buffer.
    let mut buffer = String::new();

    io::stdin().read_line(&mut buffer).expect("Failed to read N!");

    // Get the pre-determined length of the array
    let length: i32 = buffer.trim().parse()
        .expect("Did not receive an integer for N!");

    // read_line appends!
    buffer.clear();

    io::stdin().read_line(&mut buffer).expect("Failed to read the array!");

    // Split the array and parse into integers. Here .ok() just unwraps the
    // Ok value of the Result. Use filter_map (as opposed to map) to skip
    // any values that might be empty due to parse error.
    let a: Vec<i32> = 
        buffer.split_whitespace()
        .filter_map(|s| s.parse().ok())
        .collect();

    if a.len() != (length as usize) {
        panic!("Invalid number of elements!");
    }

    reverse_print(a.as_slice());

    // Just print a newline. Seems like older versions of rust require an "".
    println!();
}
