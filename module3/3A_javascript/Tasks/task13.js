//My Personal library 2

const books = {
    title: "The Monk Who Sold His Ferrari", 
    description: "A leadership and mind shisfting oriented book", 
    numberOfPages: 357, 
    author: "Robin Sharma", 
    reading: true,
    toggleReadingStatus: function(){
        if(books.reading===true){
            books.reading = false
        } else {
            books.reading = true
        }
    }
}

books.toggleReadingStatus()
console.log(books.reading)