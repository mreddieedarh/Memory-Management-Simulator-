
# Memory Management Simulator 
# This code supports Paging, Segmentation, Virtual Memory, Page Replacement: FIFO, LRU, Optimal
# Course: DCIT 301 (Operating Systems)

from collections import deque
import time

# ------------------ Physical Memory ------------------
class PhysicalMemory:
    def __init__(self, frames):
        self.frames = [None] * frames

    def display(self):
        print("\nPhysical Memory:")
        for i, f in enumerate(self.frames):
            print(f"Frame {i}: {f}")

# ------------------ Paging ------------------
class Paging:
    def __init__(self, memory):
        self.memory = memory
        self.page_table = {}
        self.page_faults = 0

    def access_page(self, page, replacement_algo):
        if page in self.page_table:
            return

        self.page_faults += 1
        if None in self.memory.frames:
            index = self.memory.frames.index(None)
        else:
            index = replacement_algo.replace(self.memory)

        self.memory.frames[index] = page
        self.page_table[page] = index
        replacement_algo.record(page)

    def display_page_table(self):
        print("\nPage Table:")
        for p, f in self.page_table.items():
            print(f"Page {p} -> Frame {f}")

# ------------------ Page Replacement ------------------
class FIFO:
    def __init__(self):
        self.queue = deque()

    def record(self, page):
        self.queue.append(page)

    def replace(self, memory):
        old = self.queue.popleft()
        return memory.frames.index(old)

class LRU:
    def __init__(self):
        self.history = {}

    def record(self, page):
        self.history[page] = time.time()

    def replace(self, memory):
        lru_page = min(self.history, key=self.history.get)
        del self.history[lru_page]
        return memory.frames.index(lru_page)

class Optimal:
    def __init__(self, page_sequence):
        self.page_sequence = page_sequence
        self.current_index = 0
        self.recorded_pages = []

    def record(self, page):
        self.recorded_pages.append(page)
        self.current_index += 1

    def replace(self, memory):
        # Find which page in memory will be used farthest in the future
        future_distances = {}
        for page in memory.frames:
            if page is None:
                continue
            try:
                # Find next occurrence of this page after current position
                next_use = self.page_sequence.index(page, self.current_index)
                future_distances[page] = next_use
            except ValueError:
                # Page won't be used again, replace this one first
                future_distances[page] = float('inf')

        # Replace the page that will be used farthest in the future
        page_to_replace = max(future_distances, key=future_distances.get)
        return memory.frames.index(page_to_replace)

# ------------------ Segmentation ------------------
class Segmentation:
    def __init__(self):
        self.segment_table = {}

    def allocate(self, seg, base, limit):
        self.segment_table[seg] = {"base": base, "limit": limit}

    def display(self):
        print("\nSegment Table:")
        for s, d in self.segment_table.items():
            print(f"Segment {s}: Base={d['base']} Limit={d['limit']}")

# ------------------ Virtual Memory ------------------
class VirtualMemory:
    def __init__(self, size):
        self.virtual_memory = [None] * size
        self.demand_paging_requests = 0

    def request_page(self, page, paging, replacement_algo):
        self.demand_paging_requests += 1
        paging.access_page(page, replacement_algo)

    def display(self):
        print("\nVirtual Memory:")
        for i, p in enumerate(self.virtual_memory):
            if p is not None:
                print(f"Virtual Address {i}: {p}")

# ------------------ Fragmentation ------------------
def internal_fragmentation(frame_size, process_size):
    return frame_size - (process_size % frame_size)

# ------------------ Demo ------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Memory Management Simulator Demo")
    print("=" * 60)

    pages = [1, 2, 3, 4, 1, 5]
    
    # ========== FIFO Demo ==========
    print("\n" + "=" * 60)
    print("1. FIFO (First-In-First-Out) Page Replacement")
    print("=" * 60)
    memory_fifo = PhysicalMemory(3)
    paging_fifo = Paging(memory_fifo)
    fifo = FIFO()

    for p in pages:
        paging_fifo.access_page(p, fifo)

    paging_fifo.display_page_table()
    print(f"Page Faults: {paging_fifo.page_faults}")
    memory_fifo.display()

    # ========== LRU Demo ==========
    print("\n" + "=" * 60)
    print("2. LRU (Least Recently Used) Page Replacement")
    print("=" * 60)
    memory_lru = PhysicalMemory(3)
    paging_lru = Paging(memory_lru)
    lru = LRU()

    for p in pages:
        paging_lru.access_page(p, lru)

    paging_lru.display_page_table()
    print(f"Page Faults: {paging_lru.page_faults}")
    memory_lru.display()

    # ========== Optimal Demo ==========
    print("\n" + "=" * 60)
    print("3. Optimal Page Replacement (Future References)")
    print("=" * 60)
    memory_optimal = PhysicalMemory(3)
    paging_optimal = Paging(memory_optimal)
    optimal = Optimal(pages)

    for p in pages:
        paging_optimal.access_page(p, optimal)

    paging_optimal.display_page_table()
    print(f"Page Faults: {paging_optimal.page_faults}")
    memory_optimal.display()

    # ========== Comparison ==========
    print("\n" + "=" * 60)
    print("4. Algorithm Comparison")
    print("=" * 60)
    print(f"FIFO Page Faults:    {paging_fifo.page_faults}")
    print(f"LRU Page Faults:     {paging_lru.page_faults}")
    print(f"Optimal Page Faults: {paging_optimal.page_faults}")
    print(f"\nPage Access Sequence: {pages}")

    # ========== Segmentation Demo ==========
    print("\n" + "=" * 60)
    print("5. Segmentation")
    print("=" * 60)
    seg = Segmentation()
    seg.allocate(0, 0, 100)
    seg.allocate(1, 100, 200)
    seg.allocate(2, 200, 150)
    seg.display()

    # ========== Virtual Memory Demo ==========
    print("\n" + "=" * 60)
    print("6. Virtual Memory (Demand Paging)")
    print("=" * 60)
    virtual_mem = VirtualMemory(10)
    memory_vm = PhysicalMemory(2)
    paging_vm = Paging(memory_vm)
    fifo_vm = FIFO()

    vm_pages = [3, 5, 3, 7, 5]
    for p in vm_pages:
        virtual_mem.request_page(p, paging_vm, fifo_vm)

    print(f"Virtual Memory Demand Paging Requests: {virtual_mem.demand_paging_requests}")
    paging_vm.display_page_table()
    print(f"Page Faults: {paging_vm.page_faults}")

    # ========== Fragmentation Demo ==========
    print("\n" + "=" * 60)
    print("7. Internal Fragmentation")
    print("=" * 60)
    print(f"Frame Size: 4 bytes, Process Size: 3 bytes")
    print(f"Internal Fragmentation: {internal_fragmentation(4, 3)} byte(s)")
    print(f"\nFrame Size: 8 bytes, Process Size: 5 bytes")
    print(f"Internal Fragmentation: {internal_fragmentation(8, 5)} byte(s)")
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)
