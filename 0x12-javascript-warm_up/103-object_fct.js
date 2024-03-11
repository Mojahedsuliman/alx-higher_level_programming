#!/usr/bin/node
const myObj = {
	type: 'object',
	value: 12,
	incr: function()
	{
		this.value++;
	}
};
console.log(myObj);
myObj.incr();
console.log(myObj);
myObj.incr();
console.log(myObj);
myObj.incr();
console.log(myObj);
