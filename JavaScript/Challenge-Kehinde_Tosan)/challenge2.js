// Create a length converter function

// cm is for centimeters and inch is for inches
//1inch = 2.54cm

function lengthConverter(inch){
    const cm = inch * 2.54;
    return cm;
}
const cmValue = lengthConverter(5)
console.log(cmValue)


function converter(ft) {
    const results = {
        meters: ft * 0.3048,
        cm: ft * 30.48,
        inches: ft * 12,
        yard: ft * 0.333
    };
    return results
}
console.log(converter(6))