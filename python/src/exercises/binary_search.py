""" 
Pseudo-code
SUBROUTINE BinarySearch(the_list, target):
    start <- 0
    end <- LEN(the_list)
    WHILE start <= end
        mid = (start + end) DIV 2 # integer division (rounding down)
        IF the_list[mid] = target THEN
            RETURN mid
        ELSE IF the_list[mid] < target THEN
            start <- mid
        ELSE # the_list[mid] must be greater than target
            end <- mid
        ENDIF
    ENDWHILE
    RETURN -1
ENDSUBROUTINE

"""

def binary_search(target: int, the_list: list) -> int:
    """ Implementation of binary search. Precondition: the_list is sorted. """
    start = 0
    end = len(the_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if the_list[mid] == target:
            return mid
        elif the_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None
