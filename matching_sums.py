from typing import Dict, List, Set, Tuple, Union

def find_matching_sums(arr: Union[List[int], Tuple[int]]) -> Dict[str, Set[Tuple[int, int]]]:
    """
    For an unsorted list of integers, find the number of pairs of integers in the list that sum to the same values.

    Args:
        arr (Union[List[int], Tuple[int]]): Input list or tuple of integers.
    Returns:
        Dict[str, Set[str]]: Dictionary of sums and their corresponding pairs.

    The results are sorted by key, as are the values.
    This function is compatible with inputs containing zero or negative integers.
    """
    # Type checking
    if not isinstance(arr, (list, tuple)) or not all(isinstance(i, int) for i in arr):
        raise ValueError("Input must be a list or set of integers")
    
    # Find sums
    sums: Dict[str, Set[str]] = {}
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sum = str(arr[i] + arr[j])
            if sum in sums:
                if (arr[j], arr[i]) in sums[sum]: # Check for reverse-order pair.
                    pass
                else:
                    sums[sum].add((arr[i], arr[j]))
            else:
                sums[sum] = {(arr[i], arr[j])}
    
    # Sort results
    ascending_order = sorted(sums.keys(), key=lambda x: int(x)) # Sort keys in ascending order
    matching_sums = {k:sorted(sums[k], key=lambda x: x[0]) for k in ascending_order if len(sums[k]) > 1} # Sort values in ascending order by the first element.

    if not matching_sums:
        print("No matching sums found")

    # Print as per prescribed output
    for key, values in matching_sums.items():
        print(key, ':', values)
        # print(f"Pairs : {', '.join(str(value) for value in values)} have sum : {key}") # Join elements to precisely match the prescribed output.
    return matching_sums