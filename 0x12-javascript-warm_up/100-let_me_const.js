#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
module.exports = function() {
myVar = 333;
}
console.log(myVar);
