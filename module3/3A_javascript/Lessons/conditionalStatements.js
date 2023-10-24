// Conditional Statements

const age = 65

// If statement
if(age<18) {
    console.log('You are too YOUNG to vote')
} else if(age<=64){
    console.log('You are eligible to vote')
} else {
    console.log('You are too OLD to vote')
}


const day = 'Tuesday'

// if(day == 'Friday'){
//     console.log('TGIF')
// } else if(day == 'Saturday') {
//     console.log('Happy weekend')
// } else if(day == 'Sunday') {
//     console.log('Happy Sunday')
// } else {
//     console.log('Go to work!')
// }

//Switch statements

switch(day){
    case 'Friday':
        console.log('TGIF')
        break
    case 'Saturday':
        console.log('Happy weekend')
        break
    case 'Sunday':
        console.log('Happy Sunday')
        break
    default:
        console.log('Go to work!')
}


/*
Task: Odd or even?

Write a Javascript program that checks if a given number, number is odd or even. 

If the number is odd, print to the console: number is odd. If  the number is even, print to the console: number is even 


Hint: An even number is divisible by 2. Hence, for an even number, the expression, 

number % 2 === 0 will evaluate to true


Steps

- Initialize a variable, number and assign it any number of your choice.
- Write an if statement check if number is divisible by 2 (HINT: use the modulus operator)
- Log the string number is even to the console if the number is divisible by 2
- Add an else block
- Inside the else block, log number is even to the console
You can test your code by assigning different values to the number variable in step 1 

const num = 35

if(num % 2 == 0 ) {
    console.log('Number is Even')
} else {
    console.log('Number is Odd')
}
*/