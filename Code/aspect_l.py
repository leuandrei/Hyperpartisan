import aspectlib

@aspectlib.Aspect
def logger(*args, **kwargs):
    print("Called with args: %s kwargs: %s" % (args, kwargs))
    result = yield
    print("Result = " + str(result))

def weightFunction(weight1, weight2, weight3):
    firstHeuristic=computeFirstResult()*weight1
    secondHeuristic = computeSecondResult()*weight2
    thirdHeuristic = computeThirdResult()*weight3
    list=[firstHeuristic, secondHeuristic, thirdHeuristic]
    if(int(max(list))>=50):
        print(max(list))
    else:
        decision=sum(list)
        if decision<=-0.5 or decision>=0.5:
            print("Hyperpartisan")
        else:
            print ("Neutral")
