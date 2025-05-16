function pattern_3(){
    let row =5;

    for (let y = 1; y < row + 1; y++) {
        for (let x = 1; x < y + 1; x++) {
            process.stdout.write(String(x));
        }
        console.log('');
    }
}

console.clear();
pattern_3();
