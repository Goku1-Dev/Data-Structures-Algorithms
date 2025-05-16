function pattern_4(){
    let row = 7;
    let column = 5;

    for (let y = 1; y < row; y++) {
        for (let x = 1; x <= y; x++) {
            process.stdout.write(String(y));
        }
        console.log('');
    }
}

console.clear();
pattern_4();