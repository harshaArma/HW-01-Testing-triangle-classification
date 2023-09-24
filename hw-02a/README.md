# Triangle


### Test Report 1
Test ID   |   Input     |   Expected Results   |   Actual Result   |   Pass or Fail
----------|-------------|----------------------|-------------------|----------------
Test01    |  3,4,5      | Right                | InvalidInput      | Fail
Test02    |  5,3,4      | Right                | InvalidInput      | Fail
Test03    |  1,1,1      | Equilateral          | InvalidInput      | Fail
Test04    |  2,3,4      | Scalene              | InvalidInput      | Fail
Test05    |  2,2,3      | Isoceles             | InvalidInput      | Fail
Test06    |  2,3,2      | Isoceles             | InvalidInput      | Fail
Test07    |  1,2,3      | NotATriangle         | InvalidInput      | Fail
Test08    |  5,3,9      | NotATriangle         | InvalidInput      | Fail
Test09    | -1,1,1      | InvalidInput         | [Not displayed]   | [Not deduced]
Test10    |  0,1,1      | InvalidInput         | [Not displayed]   | [Not deduced]
Test11    | 201,201,201 | InvalidInput         | [Not displayed]   | [Not deduced]
Test12    | 'a',1,1     | InvalidInput         | TypeError         | Error

### Test Report 2 (After Corecting the Logic)
Test ID   |   Input     |   Expected Results   |   Actual Result   |   Pass or Fail
----------|-------------|----------------------|-------------------|----------------
Test01    |  3,4,5      | Right                | Right             | Pass
Test02    |  5,3,4      | Right                | Right             | Pass
Test03    |  1,1,1      | Equilateral          | Equilateral       | Pass
Test04    |  2,3,4      | Scalene              | Scalene           | Pass
Test05    |  2,2,3      | Isoceles             | Isoceles          | Pass
Test06    |  2,3,2      | Isoceles             | Isoceles          | Pass
Test07    |  1,2,3      | NotATriangle         | NotATriangle      | Pass
Test08    |  5,3,9      | NotATriangle         | NotATriangle      | Pass
Test09    | -1,1,1      | InvalidInput         | InvalidInput      | Pass
Test10    |  0,1,1      | InvalidInput         | InvalidInput      | Pass
Test11    | 201,201,201 | InvalidInput         | InvalidInput      | Pass
Test12    | 'a',1,1     | InvalidInput         | InvalidInput      | Pass
