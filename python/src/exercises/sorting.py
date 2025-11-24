"""
Pseudo-code

SUBROUTINE BubbleSort(the_list)
    max <- LEN(the_list) - 1
    FOR i <- 0 TO max
        FOR j <- 0 TO max - 1
            IF the_list[j] > the_list[j+1] THEN
                temp <- the_list[j]
                the_list[j] <- the_list[j+1]
                the_list[j+1] <- temp
            ENDIF
        ENDFOR
    ENDFOR
    RETURN the_list
ENDSUBROUTINE

SUBROUTINE SelectionSort(the_list)
    front <- 0
    FOR i <- 0 TO LEN(the_list)
        min <- the_list[front]
        FOR j <- front TO LEN(the_list) - 1
            IF the_list[j] < the_list[min] THEN
		     min <- j
            ENDIF
        ENDFOR
        temp <- the_list[front] # do the swap
        the_list[front] <- the_list[min]
        the_list[min] <- temp
        front <- front + 1
    ENDFOR
    RETURN the_list
ENDSUBROUTINE
             

"""

def bubble_sort(the_list):
    """
    Implementation of the Bubble Sort algorithm.
    Returns a sorted version of the input list.
    """
    max = len(the_list) # not subtracting 1 here because of the way range works.
    for i in range(max):
        for j in range(max-1):
            if the_list[j] > the_list[j+1]:
                # we can swap in one step
                the_list[j], the_list[j+1] = the_list[j+1],the_list[j]
    return the_list

def selection_sort(the_list):
    """
    Implementation of the Selection Sort algorithm.
    Returns a sorted version of the input list.
    """
    front  = 0
    for i in range(len(the_list)):
        min = front
        for j in range(front,len(the_list)):
            if the_list[j] < the_list[min]:
                min = j
        the_list[front], the_list[min] = the_list[min], the_list[front]
        front = front + 1
    return the_list