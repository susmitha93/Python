def solution(S):
    k='BALLOON'
    count={}
    for i in k:
        cout=0
        for j in S:
            if j==i:
                cout=cout+1
        count[i]=cout
    return validate(count)

def validate(count):
    minlo=min(count['L'],count['O'])
    minlomoves=int(minlo)/2
    minallothers=min(count['B'],count['A'],count['N'])
    if minlomoves<minallothers:
        return minlomoves
    elif minlomoves>minallothers:
        return minallothers
    else:
        return minallothers
        
print(solution('BALLONO'))


        