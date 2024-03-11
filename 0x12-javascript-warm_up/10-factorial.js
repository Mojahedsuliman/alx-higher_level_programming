#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg))
{
	console.log('NaN');
}
else if (arg === 0)
{
	console.log('1');
}
else
{
	let fact = 1;
	for (let i = 1; i <= arg; i++)
	{
		fact *= i;
	}
	console.log(fact);
}
