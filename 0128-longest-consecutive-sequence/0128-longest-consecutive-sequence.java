class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> seqMap = new HashMap<>();
        int maxLen = 0;

        for (int n: nums) {
            if (!seqMap.containsKey(n)) {
                int left = seqMap.getOrDefault(n-1, 0);
                int right = seqMap.getOrDefault(n+1, 0);
                int newLen = left + 1 + right;
                seqMap.put(n, newLen);
                seqMap.computeIfPresent(n-left, (k, len) -> len = newLen);
                seqMap.computeIfPresent(n+right, (k, len) -> len = newLen);

                maxLen = Math.max(maxLen, newLen);
            }
        }
        return maxLen;
    }
}