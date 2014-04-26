var assert = require("assert")

function strrev(str)
{
    var aux = '';
    for (var i = str.length - 1; i >= 0; i--) {
        aux += str[i];
    }
    return aux;
}

describe('ReverseString', function(){
  it('should return the reverse string', function(){
    assert.equal("xunil", strrev("linux"));
    assert.equal("lizarb", strrev("brazil"));
  })
})
