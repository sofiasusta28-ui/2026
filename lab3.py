def find_index(lst):
   total_sum = 0
   for num in lst:
       total_sum += num

   left_sum = 0
   result = -1

   for i in range(len(lst)):
       right_sum = total_sum - left_sum - lst[i]
       if left_sum == right_sum:
           result = i
           break

       left_sum += lst[i]

   return result


lst = [1, 2, 3, 11, 4, 10,1, 3, 2, 1]
result_index = find_index(lst)

print(f"Вхідний масив: {lst}")
print(f"Знайдений індекс: {result_index}")
