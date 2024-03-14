// function inception(){
//     inception();
// }

// let o = inception();
// console.log(o);

// Running the above function, we get stack overflow
// It's because we only have the recursive case and it goes to run on as it doesn't find any terminating or the base case.
// So we have to add one.

// let count = 0
// function inception(){
//     // debugger;
//     if(count > 3){
//         return 'done';
//     }
//     count++;
//     inception();
// }

// inception();

// let o = inception();
// console.log(o);

/*
    Running the above inception, we expected to get 'done' in output, but didn't get it although we added a base case. 
    The recursive calls to the functions gets to pushed in the memory stack.
    When it encounters the base case, it returns the output for that call.
    But it then starts to pop the function calls from the stack and as the last one where the base case was encountered is at the top,
    so, it gets popped along with it's returned output. Then other ones get popped but they didn't have any return case.
    So, in the end, we got undefined.

    View this entire situation in chrome console by turning on the debugger within that function.

    What happens here is:
        1          2          3          4          5  
    inception( inception( inception( inception( inception() ) ) ) )

    In the 5th call the base case was encountered and returned the value. The 5th call to inception() was immediately poped from the stack.
    As the base case is accessed, then the recursive calls from the stack will be poped one by one but they had no return value so, we get undefined in output.
*/


// Final solution

let count = 0
function inception(){
    // debugger;
    if(count > 3){
        return 'done';
    }
    count++;
    return inception();
}

inception();

let o = inception();
console.log(o);


/*
    View this entire situation in chrome console by turning on the debugger within that function.

    What happens here is:
        1          2          3          4          5  
    inception( inception( inception( inception( inception() ) ) ) )

    In the 5th call the base case was encountered and returned the value. The 5th call to inception() was immediately poped from the stack.
    As the base case is accessed, then the recursive calls from the stack will be poped one by one but each call here has it's return value.
    Whatever the return value is in the above call of the function in the same stack is the return value for its too. So, while poping the values
    will be returned to each of them and after final pop we get the output and return value. 
*/
