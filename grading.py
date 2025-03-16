num_tests = 5 
test_scores = [100,100,100,0,0]
test_total = sum(test_scores) - min(test_scores)
hw_scores = [100,100,40,100]
num_hw = 4
hw_total = float(4*sum(hw_scores) - 3*min(hw_scores))/float(4*num_hw - 3) 

if test_total < 280:
    print('Sorry, you will not pass the course')
else: # student will pass the course. Now we determine the grade
    if hw_total < 25: # low score on HW
        if test_total < 350: # ok performance on tests
            print('You will get a C.')
        else: # test total is good
            print('You will get at least a B-')
    if hw_total >= 25 and hw_total < 45: # ok performance on HW
        print('You will get at least a B-')
    if hw_total >= 45 and hw_total < 85: # good performance on HW
        print('You will get at least a B')
    if hw_total >= 85: # strong performance on HW
        if test_total < 350: # ok performance on tests
            print('You will get at least a B+')
        else: # strong performance on HW and tests
            print('You will get at least an A-')

print('\nI will decide the plusses and minuses at the end of the quarter')