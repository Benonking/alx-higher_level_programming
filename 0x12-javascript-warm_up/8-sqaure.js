#!/usr/bin/node
const size  = Math.floor(Number(process.argv[2]));

if (isNaN(size)){
	console.log('Missing size');
}
else{
	for (let i = 1; i <= size;i++)
	{
		let row = '';
		for (let x = 1; x <= size; x++) row += 'X';
		console.log(row);
	}
}

