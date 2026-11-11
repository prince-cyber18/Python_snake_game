Test Cases and Validation

I implemented test cases to verify the correctness of the Snake Game logic and handle different game scenarios.

The test cases focus on validating snake movement, direction handling, food consumption, score updates, and collision detection.

Test Scenarios

Test case 1 - normal input           expected output
              moves: R,R             Head: (6,5)
                                     Food eaten at(7,5)!
                                     score: 10 | Length: 2 | Head: (7,5) 

Test case2 - Boundary/ Minimum input      expected output
               moves: R,R,R,R,R           Food eaten at (7,5)! Score: 10
                                          Head: (8,5), Head: (9,5)
                                          Game Over! Wall hit at(10,5)
                                          Final Score: 10

Test case 3: Invalid Input              expexted output
(a) Key: X                              (a) Invalid key Use R,L,U or D
(b) Key: L(snake is moving Right)       (b) Reverse move not allowed. Snake continues Right.

Test case 4: Different valid Scenario    expected output
Moves: R,R,U,U                           Food eaten at(7,5)! Score: 10
                                         Snake: (7,3), (7,4)
                                         Length: 2 | Head: (7,3)

What I Learned from Testing

- How to validate different movement scenarios.
- How to identify logical errors in Python code.
- How to handle boundary conditions.
- How to test collision detection.
- How to verify score and snake length updates.

Testing Approach

I used predefined movement sequences and food positions to test different scenarios and check whether the game logic produces the expected results.

Testing helped me understand the importance of edge cases, debugging, and validating program behaviour.

Learning: Writing test cases improved my logical thinking and helped me make my Python project more reliable.