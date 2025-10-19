// npx nodemon index.js
function repeatedStr(s) {
  let str = [];

  for (let i = 0; i < s.length; i++) {
    str.push(s.slice());

    console.log(`str = ${str}`);
  }

  return str;
}

console.log(repeatedStr('apple'));
