from collections import deque
from queue import PriorityQueue

n = int(input())
foods = input().split()

food_restaurant = {}
for i, food in  enumerate(foods):
  item : deque = food_restaurant.get(int(food), deque())
  restaurant_num = i + 1
  item.append(restaurant_num)
  restaurant_num[food] = item


class HashQueue:
  value_index_hashmap = {}
  heap = []

  def insert(self, key, value):
    if value in self.value_index_hashmap:
      print("duplicate value")
      return
    index = len(self.heap)
    self.value_index_hashmap[value] = index
    self.heap.append((key, value))
    if len(self.heap) > 1:
      self.up_heapify(index)

  def up_heapify(self, index):
    me = self.heap[index]
    my_key = me[0]
    my_value = me[1]
    parent_index = (index - 1) // 2
    parent = self.heap[parent_index]
    parent_key = parent[0]
    parent_value = parent[1]
    if parent_key < my_key:
      self.heap[parent_index] = me
      self.heap[index] = parent
      self.value_index_hashmap[parent_value] = index
      self.value_index_hashmap[my_value] = parent_index
      self.up_heapify(parent_index)

  def down_heapify(self, index):
    size = len(self.heap)
    me = self.heap[index]
    my_key = me[0]
    my_value = me[1]
    
    largest_index = index

    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2

    if left_child_index < size and self.heap[left_child_index][0] > self.heap[largest_index][0]:
      largest_index = left_child_index

    if right_child_index < size and self.heap[right_child_index][0] > self.heap[largest_index][0]:
      largest_index = right_child_index
    largest_child = self.heap[largest_index]
    largest_child_key = largest_child[0]
    largest_child_value = largest_child[1]

    if largest_index != index:
      self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
      self.value_index_hashmap[my_value] = largest_index
      self.value_index_hashmap[largest_child_value] = index
      self.down_heapify(largest_index)

  def pop(self):
    if len(self.heap) <= 0:
      print("empty")
    target = self.heap[0]
    target_index = 0
    target_key = target[0]
    target_value = target[1]
    last = self.heap[-1]
    last_index = len(self.heap) - 1
    last_key = last[0]
    last_value = last[1]
    self.heap[target_index] = last
    self.heap.pop()
    del self.value_index_hashmap[target_value]
    self.value_index_hashmap[last_value] = 0
    self.down_heapify(target_index)
    
  def pop_by_value(self, value):
    if len(self.heap) <= 0:
      print("empty")
    target_index = self.value_index_hashmap[value]
    target = self.heap[target_index]
    target_key = target[0]
    target_value = target[1]
    last = self.heap[-1]
    last_index = len(self.heap) - 1
    last_key = last[0]
    last_value = last[1]
    self.heap[target_index] = last
    self.heap.pop()
    del self.value_index_hashmap[target_value]
    self.value_index_hashmap[last_value] = 0
    self.down_heapify(target_index)

  def get_top(self):
    return self.heap[0]




restaurant_number_queue = HashQueue()
restaurant_count_queue = HashQueue()

for food in food_restaurant.keys:
  restaurant_deque : deque = restaurant_num[food]
  restaurant_count = len(restaurant_deque)
  restaurant_count_queue.insert((restaurant_count, food))
  restaurant_num = restaurant_deque.popleft()
  restaurant_number_queue.insert((restaurant_num, food))
  
counter = n
last_food = -1
seq = []
for i in range(n):
  max_count_food = restaurant_count_queue.get_top()
  max_count_food_count = max_count_food[0]
  if max_count_food_count > counter // 2 + 1:
    max_count_food_restaurant_food = max_count_food[1]
    yes = restaurant_number_queue.pop_by_value(max_count_food_restaurant_food)
    restaurant_num = restaurant_deque.popleft()
    new_yes = (restaurant_deque[0], max_count_food_restaurant_food)
    restaurant_number_queue.insert(new_yes)
    seq.append(restaurant_num)
  else:
    min_restaurant = restaurant_number_queue.peek()
    min_restaurant_num = min_restaurant[0]
    min_restaurant_food = min_restaurant[1]
    
    restaurant_number_queue.get_top()

    