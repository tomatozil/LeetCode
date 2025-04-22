class KthLargest {
    PriorityQueue<Integer> pq;
    Integer k;

    public KthLargest(int k, int[] nums) {
        this.pq = new PriorityQueue<>();
        this.k = k;

        for (Integer n: nums) {
            this.pq.offer(n);
        }
        int i = pq.size();
        while (i-- > this.k) {
            pq.poll();
        }
    }
    
    public int add(int val) {
        this.pq.offer(val);

        if (pq.size() > this.k) {
            pq.poll();
        }

        return pq.peek();
    }
}



/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */