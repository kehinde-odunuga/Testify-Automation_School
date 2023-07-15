// Calculate the sum of numbers within an array.

// Creating an array of numbers
const numbers = [1, 3, 5, 27, 9, 11, 13, 15, 17, 19];

// Creating variable to store the sum
let sumOfNumbers = 0;
  
// Running the for loop
for (let i = 0; i < numbers.length; i++) {
    sumOfNumbers = sumOfNumbers + numbers[i];
}

console.log('Sum is ' + sumOfNumbers);

