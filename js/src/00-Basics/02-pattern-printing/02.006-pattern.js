function pattern_6(){

    for(let y = 6; y > 0; y--){
        for(let x = 1; x < y; x++){
            process.stdout.write(String(x));
        }
        console.log('');
    }
}

console.clear();
pattern_6();