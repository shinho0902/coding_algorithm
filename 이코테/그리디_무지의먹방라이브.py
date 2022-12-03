def solution(food_times, k):
    answer = 0
    while(True):
        if k == 0:
            break
        k -= 1
        for j in range(0,len(food_times)):
            
            if food_times[j]!=0 :
                food_times[j] -= 1
                answer = j+1
                print(answer)
            else:
              continue


    return answer




food_times = [3,1,2]
k = 5
print('최종:',solution(food_times, k)) 
