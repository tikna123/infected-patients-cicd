# Algorithm
Use Breadth-first search because we need to find the minimum time which is equivalent to finding the shortest path. The algorithm can be implemented as follows:
1. Create a Queue and store all the matrix cells of all the infected patients. Create another temporary queue to separate the infected patients in the previous pass from the infected patients in the current.

2. Do till first Queue is empty
    * Copy the contents of the original Queue to the temporary queue and empty the original queue.
    * Do till the temporary queue is empty
        1) Remove the front node from the temporary queue and check all four adjacent patients of the current infected patients.
        2) if any of the four adjacent patients are uninfected, then make them infected and insert them into the first queue.
    * Increment steps by 1.

3. If all the nodes in the first Queue are processed, return the total number of steps. Also, check if there is still uninfected
    person is left in the ward if yes then return -1.


# How to run and test
python infected_patients.py inputTestFile.txt  
Example: python infected_patients.py unit_test1.txt

