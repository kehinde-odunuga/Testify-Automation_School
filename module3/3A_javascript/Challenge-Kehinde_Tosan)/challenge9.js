// Return the number of vowels in a string

function countVowel(str) {
    let count = 0;
    let vowels = ['a', 'e', 'i', 'o', 'u']

for (let i = 0; i < str.length; i++){
    if(vowels.indexOf(str[i].toLowerCase()) > -1){
        count++;
    }
}
return count;
}
console.log('Number of vowels in this string is ' + countVowel("JavaScript Coding Challenge is fun with Tosan and the team Zuckerberg"));
