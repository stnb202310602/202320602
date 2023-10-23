from collections import deque

def solution(my_dict, target_index):
    my_deque = deque(my_dict.items())
    removal_count = 0

    while my_deque:
        max_priority = max(my_deque, key=lambda x: x[1])

        if my_deque[0] == max_priority:
            removed_item = my_deque.popleft()
            removal_count += 1

            if removed_item[0] == target_index:
                return removal_count
        else:
            removed_item = my_deque.popleft()
            my_deque.append(removed_item)

    return removal_count

priorities = {0: 1, 
              1: 1, 
              2: 9, 
              3: 2, 
              4: 3, 
              5: 4}

location = 1

removed_priority = solution(priorities, location)

print("\npriorities | location | 인쇄 순서")
print(f"{list(priorities.values())} | {location} | {removed_priority}")
