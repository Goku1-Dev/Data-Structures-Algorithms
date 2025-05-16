function pattern_2() {
    let row = 7;

    for (let y = 1; y < row + 1; y++) {
        for (let x = 0; x < y; x++) {
            process.stdout.write('*');
        }

        console.log();
    }
}

console.clear();
pattern_2();