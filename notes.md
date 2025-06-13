## Notes ##

Observations from the examples:  
- Results are sorted by key in ascending order  

- While input sequences may produce more than two pairs with the same sum, the example results include only pairs of pairs. This has the potential for causing confusion, but reading the problem description carefully, it appears that results may be of any length > 1.
    
- Values are sorted in ascending order by the first element of each pair.
  - This is observable only in the instance of the results of the first example: (4, 12) (6, 10). When using element-wise traversal of the input sequence, (6, 10) would be identified before (4, 12); all other pairs in the examples are circumstantially in the correct order.

- From the above, we must acknowledge that the order of the input sequence is important. Consequently, the input type must be a list.
    
- While the result values are sorted, this indicates that the order of the elements in each pair *when identifying* the pairs is inconsequential. Otherwise, each pair would have a corresponding pair with the same elements in reverse order ie. (4, 12) and (12, 4). This may improve the efficiency of our strategy for identifying pairs using element-wise traversal.
    
- Subsequently, we may conclude that if the input sequence contains naturally occurring reverse order pairs, these pairs are to be interpreted as duplicates which are not to be included in the result.
  - Examples: [1, 2, 3, 1, 2, 3] -> (1, 2) (2, 1) = 3, or (2, 3) (3, 2) = 5. (Or even, (2', 2) (2, 2') = 4). These are identified as duplicates.

- Duplicate numbers in the input sequence may still qualify as a result provided all other criteria are met.
  - Example: [1, 2, 2, 3] -> (1, 3) (2, 2) = 4

All other tests passed.