// Fibonacci series
// Normal approach
// Time complexity: O(2^n)
// Space complexity: O(1)
let calculations = 0;
function fibonacci(n){
    calculations++;
    if (n < 2){
        return n
    }
    return fibonacci(n-1)+fibonacci(n-2)
}
console.log("Noormal approach: ");
var number = fibonacci(30);
console.log("Total steps: ", calculations, ", Number: ", number);

// Using dynamic programming
// Time complexity: O(n)
// Space complexity: O(n)
// Top-Down approach
calculations = 0;
function memoizedFibonacci(n){
    let cache = {};
    return function fibonacci(n){
        calculations++;
        if(n in cache){
            return cache[n];
        }
        else{
            if(n<2){
                cache[n] = n;
                return cache[n];
            }
            cache[n] = fibonacci(n-1) + fibonacci(n-2);
            return cache[n];
        }
    };
}

console.log("Dynamic programming: ")
console.log("Top-Down approach:");
const memoized = memoizedFibonacci();
var number = memoized(30);
console.log("Total steps: ", calculations, ", Number: ", number);

// Bottom-Up approach
calculations = 0;
function memoizedFibonacci2(n){
    let answers = [0, 1];
    for(i=2; i<=n; i++){
        calculations++;
        answers.push(answers[i-1]+answers[i-2]);
    }
    return answers.pop();
}

console.log("Bottom-Up approach:");
const memoized2 = memoizedFibonacci2();
var number = memoized2(30);
console.log("Total steps: ", calculations, ", Number: ", number);