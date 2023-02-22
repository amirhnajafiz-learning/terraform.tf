// create a function type annotation
let concatenate: (a: string, b: string) => string;

// give value to function
concatenate = function (a, b) {
    return a + b;
};

console.log(concatenate("Amir", "hossein"))
