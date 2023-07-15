//if else if - sides of a triangle

const side1 = 60
const side2 = 60
const side3 = 60

if(side1 === side2 && side2 === side3) {
    console.log("Equilateral triangle")
} else if(side1 === side2 || side1 === side3 || side2 === side3) {
    console.log("Isosceles triangle")
} else {
    console.log("Scalene triangle")
}