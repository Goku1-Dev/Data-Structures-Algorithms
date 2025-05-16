function pattern_5() {
    let row = 7;

    for (let y = 5; y > 0; y--) {
        for (let x = 0; x < y; x++) {
            process.stdout.write('*');
        }

        console.log();
    }
}

console.clear();
pattern_5();