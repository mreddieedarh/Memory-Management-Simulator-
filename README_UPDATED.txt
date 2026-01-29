================================================================================
Memory Management Simulator
Course: DCIT 301 (Operating Systems)
================================================================================

DESCRIPTION:
This simulator demonstrates core memory management concepts including:
  - Paging (with multiple page replacement algorithms)
  - Segmentation
  - Virtual Memory (Demand Paging)
  - Page Replacement Algorithms: FIFO, LRU, Optimal
  - Internal Fragmentation

================================================================================
REQUIREMENTS:
  - Python 3.x installed on your system
  - No additional packages required (uses only standard library)

================================================================================
HOW TO RUN:

1. Extract the zip file to your desired location

2. Open a terminal/command prompt and navigate to the simulator folder:
   cd path/to/Simulator

3. Run the simulator:
   python simulator.py

4. The program will execute all demonstrations and display results in the console

================================================================================
OUTPUT BREAKDOWN:

The demo runs 7 comprehensive demonstrations:

1. FIFO Page Replacement
   - Shows First-In-First-Out algorithm behavior
   - Displays page table and page fault count

2. LRU Page Replacement
   - Shows Least Recently Used algorithm behavior
   - Compares results with FIFO

3. Optimal Page Replacement
   - Shows theoretically optimal algorithm (future lookahead)
   - Best case scenario for page replacement

4. Algorithm Comparison
   - Side-by-side comparison of page faults for all three algorithms
   - Same page access sequence: [1, 2, 3, 4, 1, 5]

5. Segmentation
   - Demonstrates memory segmentation with base and limit values
   - Shows allocation of multiple segments

6. Virtual Memory (Demand Paging)
   - Demonstrates virtual memory with demand paging
   - Shows how pages are loaded on demand

7. Internal Fragmentation
   - Calculates wasted space when processes fit into frames
   - Examples: 4-byte frame with 3-byte process, 8-byte frame with 5-byte process

================================================================================
REPORT:

PROJECT OVERVIEW:
This Memory Management Simulator is designed to help students understand 
fundamental OS memory management concepts. It provides hands-on demonstration 
of how different page replacement algorithms work.

KEY FEATURES:
✓ Paging with Physical Memory Frames
✓ Page Table Management
✓ Three Page Replacement Algorithms (FIFO, LRU, Optimal)
✓ Segmentation Support
✓ Virtual Memory Implementation
✓ Fragmentation Calculation
✓ Comprehensive Demo with Real Examples

ALGORITHMS IMPLEMENTED:

1. FIFO (First-In-First-Out):
   - Replaces the oldest page first
   - Simple implementation but can suffer from Belady's anomaly
   - Average performance on most workloads

2. LRU (Least Recently Used):
   - Replaces the page accessed longest ago
   - Better performance than FIFO in practice
   - Requires tracking page access times

3. Optimal:
   - Replaces the page that will not be used for the longest time
   - Requires knowledge of future page references
   - Theoretical best case (not practically implementable)

CONCEPTS DEMONSTRATED:

Page Faults: 
  Occur when a referenced page is not in physical memory and must be loaded
  Lower page faults = better algorithm performance

Segmentation:
  Divides memory into logical segments with base (starting address) and 
  limit (size) values

Virtual Memory:
  Allows programs to use more memory than physically available through 
  demand paging and swapping

Internal Fragmentation:
  Wasted space within allocated memory frames when process size doesn't 
  perfectly match frame size

================================================================================
FILES INCLUDED:

- simulator.py: Main simulator code with all classes and demo
- README.txt: This file (instructions and report)

================================================================================
USAGE NOTES:

- The simulator uses a fixed 3-frame physical memory for comparisons
- Page access sequence: [1, 2, 3, 4, 1, 5]
- Virtual memory demo uses a 2-frame physical memory
- All algorithms are tested with identical conditions for fair comparison

================================================================================
LEARNING OUTCOMES:

After running and studying this simulator, students should understand:
✓ How paging systems manage memory
✓ Differences between page replacement algorithms
✓ The concept of page faults and their impact on performance
✓ How segmentation provides logical memory organization
✓ Virtual memory and demand paging concepts
✓ Memory fragmentation issues and their solutions

================================================================================
TROUBLESHOOTING:

If "python" command not found:
  - Ensure Python 3.x is installed
  - Try "python3 simulator.py" instead
  - Add Python to your system PATH

If no output appears:
  - Check that simulator.py is in the same folder as README.txt
  - Ensure Python installation is correct
  - Try running from command prompt instead of file explorer

================================================================================
