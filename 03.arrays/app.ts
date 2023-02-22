// let's create a array of objects
let numbers = [1, 2, 3, 4, 5];

// creating a new array of first array
let new_numbers = numbers.map(e => 2*e);

new_numbers.forEach(e => {
    console.log(e);
});
