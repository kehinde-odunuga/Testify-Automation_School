// Print a table containing multiplication tables

const multiple = 8;
const limit = 12;

for (let num = 1; num <= limit; num++) {
    printRow(multiple, num);
}

function printRow(multiple, num) {
    let output = `${multiple} X ${num} = ${multiple * num}`;
    console.log(output);
}
