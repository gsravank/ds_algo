import heapq


class Item:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score or (self.score == other.score and self.name < other.name)

    def __eq__(self, other):
        return self.score == other.score and self.name == other.name

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return f"{self.val.name}, {self.val.score}"


class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self, x): heapq.heappush(self.h, x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self, i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self, i): return self.h[i].val

class SORTracker:
    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()
        self.query_count = 0

    def add(self, name: str, score: int) -> None:
        item = Item(name, score)

        if self.query_count == 0 or item <= self.min_heap[0]:
            self.max_heap.heappush(item)
        else:
            min_item = self.min_heap.heappop()
            self.max_heap.heappush(min_item)
            self.min_heap.heappush(item)

    def get(self) -> str:
        answer = self.max_heap.heappop()

        self.min_heap.heappush(answer)

        self.query_count += 1
        return answer.name

"""
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

"""