from collections import deque

n = int(input())
foods = list(map(int, input().split()))

food_restaurant = {}
for i, food in  enumerate(foods):
  item : deque = food_restaurant.get(food, deque())
  restaurant_num = i + 1
  item.append(restaurant_num)
  food_restaurant[food] = item


class HashQueue:
  def __init__(self, reversed):
    self.heap = []
    self.value_index_hashmap = {}
    self.reversed = reversed

  def insert(self, key, value):
    if value in self.value_index_hashmap:
      print("duplicate value")
      return
    idx = len(self.heap)
    self.value_index_hashmap[value] = idx
    self.heap.append((key, value))
    if idx > 0:
      self.up_heapify(idx)

  def up_heapify(self, index):
    while index > 0:
      parent = (index - 1) // 2
      key, val = self.heap[index]
      pkey, pval = self.heap[parent]
      if (self.reversed and key > pkey) or (not self.reversed and key < pkey):
        self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
        self.value_index_hashmap[val] = parent
        self.value_index_hashmap[pval] = index
        index = parent
      else:
        break

  def down_heapify(self, index):
    size = len(self.heap)
    while True:
      left = 2 * index + 1
      right = 2 * index + 2
      best = index

      if left < size:
        lkey, _ = self.heap[left]
        bkey, _ = self.heap[best]
        if (self.reversed and lkey > bkey) or (not self.reversed and lkey < bkey):
          best = left

      if right < size:
        rkey, _ = self.heap[right]
        bkey, _ = self.heap[best]
        if (self.reversed and rkey > bkey) or (not self.reversed and rkey < bkey):
          best = right

      if best == index:
        break

      self.heap[index], self.heap[best] = self.heap[best], self.heap[index]
      _, val = self.heap[index]
      _, best_val = self.heap[best]
      self.value_index_hashmap[val] = index
      self.value_index_hashmap[best_val] = best
      index = best

  def pop(self):
    if not self.heap:
      print("empty")
      return None
    if len(self.heap) == 1:
      key, val = self.heap.pop()
      del self.value_index_hashmap[val]
      return (key, val)

    root_key, root_val = self.heap[0]
    last_key, last_val = self.heap.pop()
    del self.value_index_hashmap[root_val]
    self.heap[0] = (last_key, last_val)
    self.value_index_hashmap[last_val] = 0

    self.down_heapify(0)
    return (root_key, root_val)
    
  def pop_by_value(self, value):
    if not self.heap:
      print("empty")
      return None
    idx = self.value_index_hashmap.get(value)
    if idx is None:
      print("value not found")
      return None

    key, val = self.heap[idx]
    last_key, last_val = self.heap.pop()
    del self.value_index_hashmap[val]

    if idx == len(self.heap):
      return (key, val)

    self.heap[idx] = (last_key, last_val)
    self.value_index_hashmap[last_val] = idx

    self.up_heapify(idx)
    self.down_heapify(idx)
    return (key, val)

  def get_top(self):
    if not self.heap:
      print("empty")
      return None
    return self.heap[0]




restaurant_number_queue = HashQueue(reversed=False)
restaurant_count_queue = HashQueue(reversed=True)

def popup_food(food):
  restaurant_deque = food_restaurant[food]
  restaurant_num, _ = restaurant_number_queue.pop_by_value(food)
  next_min_restaurant = -1
  if len(restaurant_deque) > 0:
    next_min_restaurant = restaurant_deque.popleft()
    restaurant_number_queue.insert(next_min_restaurant, food)

  restaurant_count = restaurant_count_queue.pop_by_value(food)
  restaurant_count_value = restaurant_count[0]
  restaurant_count_queue.insert(restaurant_count_value - 1, food)
  return restaurant_num


for food in food_restaurant:
  restaurant_deque : deque = food_restaurant[food]
  restaurant_count = len(restaurant_deque)
  restaurant_count_queue.insert(restaurant_count, food)
  restaurant_num = restaurant_deque.popleft()
  restaurant_number_queue.insert(restaurant_num, food)
  
counter = n
last_food = -1
seq = []
for i in range(n):
  max_count_food = restaurant_count_queue.get_top()
  max_count_food_value = max_count_food[1]
  max_count_food_count = max_count_food[0]
  if max_count_food_count * 2 == counter + 1:
    restaurant_num = popup_food(max_count_food_value)
    last_food = max_count_food_value
    seq.append(restaurant_num)
    counter -= 1
  elif max_count_food_count * 2 > counter + 1:
    print(-1)
    exit()
  else:
    next_restaurant = restaurant_number_queue.get_top()
    next_restaurant_num = next_restaurant[0]
    next_restaurant_food = next_restaurant[1]
    if next_restaurant_food == last_food:
      restaurant_number_queue.pop()
      cur = next_restaurant
      next_restaurant = restaurant_number_queue.get_top()
      next_restaurant_num = next_restaurant[0]
      next_restaurant_food = next_restaurant[1]
      restaurant_number_queue.insert(cur[0], cur[1])
    popup_food(next_restaurant_food)
    last_food = next_restaurant_food
    seq.append(next_restaurant_num)
    counter -= 1
print(' '.join(map(str, seq)))
