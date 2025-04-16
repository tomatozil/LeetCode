class Node {
    int key;
    int value;

    Node(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

class LRUCache {
    private Map<Integer, Node> cache;
    private LinkedList<Node> memory;
    private int capacity;

    public LRUCache(int capacity) {
        this.cache = new HashMap<>();
        this.memory = new LinkedList<>();
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (cache.containsKey(key)) {
            Node targetNode = cache.get(key);
            memory.remove(targetNode);
            memory.offerLast(targetNode);
            return targetNode.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        // cache에 없으면 linked list에 새로운 node를 저장하고 그 node를 cache에 추가
        // cache에 이미 있으면 해당 node에 접근, 
        // 1. value 수정
        // 2. node를 linked list에서 삭제하고 add last 한다
        // capacity와 cache 사이즈를 비교해서 초과시 remove first 한다
        if (cache.containsKey(key)) {
            Node targetNode = cache.get(key);
            memory.remove(targetNode);
            memory.offerLast(targetNode);
            targetNode.value = value;
        } else {
            Node newNode = new Node(key, value);
            memory.offer(newNode);
            cache.put(key, newNode);
        }

        if (capacity < cache.size()) {
            Node targetNode = memory.pollFirst();
            cache.remove(targetNode.key);
        }
    }
}
