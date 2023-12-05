const chai = require('chai')
const calculateNumber = require('./2-calcul')

describe('calculateNumber', () => {
  it('Return a + b rounded number when type is SUM', () => {
    chai.expect(calculateNumber('SUM', 1, 5).to.equal(6));
    chai.expect(calculateNumber('SUM', 4, 2).to.equal(6));
    chai.expect(calculateNumber('SUM', 1.25, 3).to.equal(4));
    chai.expect(calculateNumber('SUM', 4.5, 2).to.equal(7));
    chai.expect(calculateNumber('SUM', -1, 3).to.equal(2));
    chai.expect(calculateNumber('SUM', -5, -5).to.equal(-10));
    chai.expect(calculateNumber('SUM', -2.5, -2.5).to.equal(-4));
    chai.expect(calculateNumber('SUM', -2.25, 2.25).to.equal(0));
    chai.expect(calculateNumber('SUM', 4.5, -1.75).to.equal(3));
  });
  it('Return a - b rounded numbers when type SUBTRACT', () => {
    chai.expect(calculateNumber('SUBTRACT', 1, 5).to.equal(-4));
    chai.expect(calculateNumber('SUBTRACT', 4, 2).to.equal(2));
    chai.expect(calculateNumber('SUBTRACT', 1.25, 3).to.equal(-2));
    chai.expect(calculateNumber('SUBTRACT', 4.5, 2).to.equal(3));
    chai.expect(calculateNumber('SUBTRACT', -1, 3).to.equal(-4));
    chai.expect(calculateNumber('SUBTRACT', -5, -5).to.equal(0));
    chai.expect(calculateNumber('SUBTRACT', -2.5, -2.5).to.equal(0));
    chai.expect(calculateNumber('SUBTRACT', -2.25, 2.25).to.equal(-4));
    chai.expect(calculateNumber('SUBTRACT', 4.5, -1.75).to.equal(7));
  });
  it('Return a / b when b is letter that 0 and type is DIVIDE', () => {
    chai.expect(calculateNumber('DIVIDE', 1, 5).to.equal(0.2));
    chai.expect(calculateNumber('DIVIDE', 4, 2).to.equal(2));
    chai.expect(calculateNumber('DIVIDE', 1.25, 4).to.equal(0.25));
    chai.expect(calculateNumber('DIVIDE', 4.5, 2).to.equal(2.5));
    chai.expect(calculateNumber('DIVIDE', -1, 4).to.equal(-0.25));
    chai.expect(calculateNumber('DIVIDE', -5, -5).to.equal(1));
    chai.expect(calculateNumber('DIVIDE', -2.5, -2.5).to.equal(1));
    chai.expect(calculateNumber('DIVIDE', -2.25, 2.25).to.equal(-1));
    chai.expect(calculateNumber('DIVIDE', 4.5, -1.75).to.equal(-2.5));
  });
  it('Return Erro when type is DIVIDE and b is igual to zero', () => {
    chai.expect(calculateNumber('DIVIDE', 2, 0).to.equal('Error'));
    chai.expect(calculateNumber('DIVIDE', 5, 0.25).to.equal('Error'));
  });
})