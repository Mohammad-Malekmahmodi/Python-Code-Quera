# x = int(input(""))
# y =""
# for _ in range(x):
#     y += "unlim"
# print(y)






# n = int(input(""))
# g = 0
# for _ in range(n):
#     x = input("")
#     xx = list(map(int,x.split()))
#
#     if sum(xx)==2:
#         g +=1
# print(g)






# n = int(input())
# floors = list(map(int, input().split()))
#
#
# floors.sort()
#
# additional_floors = 0
#
# for i in range(1, n):
#     if floors[i] <= floors[i - 1]:
#
#         additional_floors += floors[i - 1] - floors[i] + 1
#
#         floors[i] = floors[i - 1] + 1
#
# print(additional_floors)






# def count_pairs(birds):
#     counts = {}
#     for bird in birds:
#         if bird in counts:
#             counts[bird] += 1
#         else:
#             counts[bird] = 1
#
#     pairs = 0
#     for count in counts.values():
#         pairs += count * (count - 1) // 2
#     return pairs
#
# n = int(input())
# birds = list(map(int, input().split()))
#
# print(count_pairs(birds))


# from collections import defaultdict
#
# def calculate_memory(process_id, processes, memory_dict):
#     # اگر حافظه برای این پروسه قبلاً محاسبه شده باشد، آن را برگردان
#     if process_id in memory_dict:
#         return memory_dict[process_id]
#
#     # محاسبه حافظه برای این پروسه
#     memory = processes[process_id][2]
#
#     # محاسبه حافظه برای هر یک از فرزندان
#     for child_id in graph[process_id]:
#         memory += calculate_memory(child_id, processes, memory_dict)
#
#     # ذخیره حافظه محاسبه شده
#     memory_dict[process_id] = memory
#
#     return memory
#
# # خواندن ورودی
# n, q = map(int, input().split())
# processes = {}
# graph = defaultdict(list)
#
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     processes[a] = (a, b, c)
#     graph[b].append(a)
#
# # محاسبه حافظه برای هر یک از پروسه‌ها
# memory_dict = {}
# for process_id in processes:
#     calculate_memory(process_id, processes, memory_dict)
#
# # ذخیره خروجی‌ها
# outputs = []
# # انجام استعلام‌ها
# for _ in range(q):
#     p = int(input())
#     outputs.append(memory_dict[p])
#
# # چاپ خروجی‌ها با اینتر جداکننده
# print(*outputs, sep='\n')
