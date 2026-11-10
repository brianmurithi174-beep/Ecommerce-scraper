import time

count = 0
start_time = time.perf_counter()
for x in range(1,1000):
    if x%2==1:
        print(x)

        count +=1


print(f'count is{count}')
end_time = time.perf_counter()-start_time