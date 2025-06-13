# Matching Sums
Simple function to find the pairs in a sequence of integers with identical sums.  
Careful attention is paid to the ordering of the results.  
The function is capable of accommodating zero, duplicate, and negative numbers.  

## Usage
### CLI
May be used through a commnd line interface by calling the file with a comma-separated list of integers  

Ex:  
python matching_sums.py n,n...  
python matching_sums.py 1,2,3,4,5,6  

### Functional use  
from matching_sums import find_matching_sums 

find_matching_sums([1, 2, 3, 4, 5, 6])
