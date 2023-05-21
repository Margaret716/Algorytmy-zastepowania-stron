# Page-replacement-algorithms

<br />

Page replacement algorithms are used in operating systems to manage virtual memory. The main goal of these algorithms is to minimize the number of page faults and optimize the utilization of available physical memory.

Virtual memory is a mechanism that allows the operating system to allocate more memory than is physically available in the computer. Pages (segments of programs or data) are loaded into physical memory dynamically as needed. When memory becomes full, some pages need to be evicted to make room for new pages.

Page replacement algorithms are responsible for selecting which pages should be evicted when memory is full. They are used to minimize the number of page faults, which occur when a program needs to access a page that is not currently in physical memory.

A good page replacement algorithm should attempt to predict which pages will not be needed in the near future and select those for eviction. This aims to minimize the impact on system performance while ensuring an adequate amount of memory for running programs.

Popular page replacement algorithms include FIFO (First-In, First-Out), LRU (Least Recently Used), LFU (Least Frequently Used), and others. Each of these algorithms has its own advantages and limitations, and the choice of the appropriate algorithm depends on specific requirements and system characteristics.

In this program were compared two algorithms - FIFO and LRU.
