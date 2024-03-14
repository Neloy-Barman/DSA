<h1 align='center'>Recursion</h1>

<strong>Recursion is technically not an algorithm rather it's a concept. When we will do sorting and searching through a binary searcch tree, we are going to use recursion a lot.  To search file we use ls -r, the r stands for recurssively. Recursion is when you define something in terms of itself. Simply it's a function that refers to itself inside of that function.

    function inception(){
        inception();
    }
This is a recursive function because when this function runs it's going to all itself again and again. Recursion is really good for tasks that have repeated subtasks to do that. 
</strong>

<strong>Recursion has 3 rules. Those are: - </strong>
<ul>
    <li>Identify the base case.</li>
    <li>Identify the recursive case.</li>
    <li>Get closer and closer and return when needed. Usually we have 2 returns. Those are for the base case and the recursive case because you might want to return at the end of the function.</li>
</ul>
<strong>In one word, the function simply gets closer and closer to the base case and once it gets to the base case, it finally returns and pops functions of the stack. </strong>


