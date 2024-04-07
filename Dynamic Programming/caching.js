function addTo80(n){
    console.log("Long Time")
    return n + 80;
}

// addTo80(5)
// addTo80(5)
// addTo80(5)

// let cache = {}
// function memoizedAddTo80(n){
//     if (n in cache){
//         return cache[n];
//     }
//     else{
//         console.log("Long Time")
//         cache[n] = n + 80;
//         return cache[n]
//     }
// }


// console.log("1", memoizedAddTo80(5))
// console.log("2", memoizedAddTo80(5))


// Caching implementation using closer and avoiding global scope.
function memoizedAddTo80(n){
    let cache = {}
    return function(n){
        if (n in cache){
            return cache[n];
        } else {
            console.log("long time")
            cache[n] = n + 80;
            return cache[n];
        }
    }
}

const memoized = memoizedAddTo80();
console.log("1", memoized(5));
console.log("2", memoized(5))

