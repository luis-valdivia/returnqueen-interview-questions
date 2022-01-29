import json

# INPUTS: list of phrases P, list of queries Queries
# OUTPUT: array of arrays of fuzzy phrases for each query
# Notice: inner lists are sorted


def phrasel_search(P, Queries):
    # Write your solution here
    ans = []
    for Query in Queries:
        QueryArray = Query.split(' ')
        temp = []
        for p in P:
            phrase = p.split(' ')
            potentialIndex = findIndex(QueryArray, phrase[0])
            tempIndex = 0

            # there might be multiple fuzzy variations of the same phrase
            while(potentialIndex != -1):
                potentialIndex += tempIndex
                upperBound = potentialIndex + len(phrase) + 1
                QuerySubArray = QueryArray[potentialIndex: upperBound]

                # check for the original variation
                if(p in ' '.join(QuerySubArray)):
                    temp.append(p)

                # it's impossible for there to exist more variations if there is no more space
                if len(QueryArray[potentialIndex:]) - len(phrase) <= 0:
                    break

                # check variations of phrase by skipping a word in between wherever possible
                for j in range(1, len(phrase)):
                    dontAdd = False
                    k = 1
                    while (dontAdd == False and k < len(phrase)):
                        if (k < j):
                            if (phrase[k] != QueryArray[potentialIndex + k]):
                                dontAdd = True
                        elif (phrase[k] != QueryArray[potentialIndex + k + 1]):
                            dontAdd = True
                        k += 1
                    if (dontAdd == False):
                        temp.append(' '.join(QuerySubArray))

                # look for a next possible variation of the current phrase
                tempIndex = potentialIndex + 1
                potentialIndex = findIndex(
                    QueryArray[potentialIndex + 1:], phrase[0])
        ans.append(sorted(temp))
    return ans


# modified index function for arrays to return -1 if the target is not found in the array
# instead of throwing an exception error
def findIndex(array, target):
    try:
        return array.index(target)
    except:
        return -1


# these are my tests
# if __name__ == "__main__":
#     tests = ['fuzzy_phrases/sample.json', 'fuzzy_phrases/20_points.json',
#              'fuzzy_phrases/30_points.json', 'fuzzy_phrases/50_points.json']
#     for test in tests:
#         with open(test, 'r') as f:
#             sample_data = json.loads(f.read())
#             P, Queries, sample_answer = sample_data['phrases'], sample_data['queries'], sample_data['solution']
#             for i in range(len(sample_answer)):
#                 sample_answer[i] = sorted(sample_answer[i])
#             returned_ans = phrasel_search(P, Queries)
#             assert(returned_ans == sample_answer)
#     print('============= ALL TEST PASSED SUCCESSFULLY ===============')

# original tests
if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
