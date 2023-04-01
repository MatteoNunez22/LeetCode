class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heapq = new PriorityQueue<Integer>(stones.length);
        for (int n : stones) {
            heapq.add(-n);
        }
        
        while (heapq.size() > 1) {
            int y = -1 * heapq.poll();
            int x = -1 * heapq.poll();
            if (x != y) {
                heapq.add(x - y);
            }
        }
        
        if (heapq.size() == 0) return 0;
        return -1 * heapq.poll();
    }
}