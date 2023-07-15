//My Personal library 3

const books = [
    {
        title: "The Monk Who Sold His Ferrari",
        description: "A leadership and minds shifting oriented book",
        numberOfPages: 357,
        author: "Robin Sharma",
        reading: false,
    },
    {
        title: "Good Morning Holy Spirit",
        description: "A spiritual book",
        numberOfPages: 175,
        author: "Benny Hinn",
        reading: false,
    },
    {
        title: "Purple Hibiscus",
        description: "Poetry",
        numberOfPages: 210,
        author: "Chimamanda Ngozi. Adichie",
        reading: false,
    },
    {
        title: "Things Fall Apart",
        description: "Poetry",
        numberOfPages: 250,
        author: "Chinua Achebe",
        reading: false,
    },
    {
        title: "Chrislam",
        description: "Religious book",
        numberOfPages: 56,
        author: "Mamood Bello",
        reading: false,
    }
]
const filter = books.filter(function (books){
    return books.reading === true;
});
console.log(filter);