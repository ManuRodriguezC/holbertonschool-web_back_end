const assert = require('assert')
const calculateNumber = require('./1-calcul')

describe('calculateNumber', () => {
  it('Return a + b rounded number when type is SUM', () => {
    assert.equal(calculateNumber('SUM', 1, 5), 6);
    assert.equal(calculateNumber('SUM', 4, 2), 6);
    assert.equal(calculateNumber('SUM', 1.25, 3), 4);
    assert.equal(calculateNumber('SUM', 4.5, 2), 7);
    assert.equal(calculateNumber('SUM', -1, 3), 2);
    assert.equal(calculateNumber('SUM', -5, -5), -10);
    assert.equal(calculateNumber('SUM', -2.5, -2.5), -4);
    assert.equal(calculateNumber('SUM', -2.25, 2.25), 0);
    assert.equal(calculateNumber('SUM', 4.5, -1.75), 3);
  });
  it('Return a - b rounded numbers when type SUBTRACT', () => {
    assert.equal(calculateNumber('SUBTRACT', 1, 5), -4);
    assert.equal(calculateNumber('SUBTRACT', 4, 2), 2);
    assert.equal(calculateNumber('SUBTRACT', 1.25, 3), -2);
    assert.equal(calculateNumber('SUBTRACT', 4.5, 2), 3);
    assert.equal(calculateNumber('SUBTRACT', -1, 3), -4);
    assert.equal(calculateNumber('SUBTRACT', -5, -5), 0);
    assert.equal(calculateNumber('SUBTRACT', -2.5, -2.5), 0);
    assert.equal(calculateNumber('SUBTRACT', -2.25, 2.25), -4);
    assert.equal(calculateNumber('SUBTRACT', 4.5, -1.75), 7);
  });
  it('Return a / b when b is letter that 0 and type is DIVIDE', () => {
    assert.equal(calculateNumber('DIVIDE', 1, 5), 0.2);
    assert.equal(calculateNumber('DIVIDE', 4, 2), 2);
    assert.equal(calculateNumber('DIVIDE', 1.25, 4), 0.25);
    assert.equal(calculateNumber('DIVIDE', 4.5, 2), 2.5);
    assert.equal(calculateNumber('DIVIDE', -1, 4), -0.25);
    assert.equal(calculateNumber('DIVIDE', -5, -5), 1);
    assert.equal(calculateNumber('DIVIDE', -2.5, -2.5), 1);
    assert.equal(calculateNumber('DIVIDE', -2.25, 2.25), -1);
    assert.equal(calculateNumber('DIVIDE', 4.5, -1.75), -2.5);
  });
  it('Return Erro when type is DIVIDE and b is igual to zero', () => {
    assert.equal(calculateNumber('DIVIDE', 2, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', 5, 0.25), 'Error');
  });
})