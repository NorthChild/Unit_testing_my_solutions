# ONE AFTER THE OTHER, I M GOING TO INSERT ALL MY SOLUTIONS, AND HAVE IT LINKED TO A UNIT TEST INSIDE THE SAME FOLDER
# TO RUN, DOWNLOAD BOTH SCRIPTS, INSERT THEM INSIDE A FOLDER, cd TO THAT FOLDER, AND RUN THE test_solutions.py SCRIPT

# ARE THEY ANAGRAMS
def anagramCheck(one, two):
    one = one.lower()
    two = two.lower()

    firstString = list(one)
    secondString = list(two)

    sorted1st = sorted(firstString)
    sorted2nd = sorted(secondString)

    for i in sorted1st:
        if i == ' ':
            sorted1st.remove(i)

    for i in sorted2nd:
        if i == ' ':
            sorted2nd.remove(i)

    if (sorted1st == sorted2nd):
        # print('The chosen words: (' + one.upper() + ') and (' + two.upper() + '), are Anagrams \n')
        return True
    else:
        return False
        # print('The chosen words: (' + one.upper() + ') and (' + two.upper() + '), are NOT Anagrams \n')

# 
