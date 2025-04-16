class Node {
    int key;
    int value;
    Node prev;
    Node next;

    Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    private Map<Integer, Node> cache;
    private Node head = new Node(-1, -1);
    private Node tail = new Node(-1, -1);
    private int capacity;

    public LRUCache(int capacity) {
        this.cache = new HashMap<>();
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (cache.containsKey(key)) {
            Node target = cache.get(key);
            this.remove(target);
            this.addLast(target);
            return target.value;
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
            Node target = cache.get(key);
            this.remove(target);
            this.addLast(target);
            target.value = value;
        } else {
            Node newbe = new Node(key, value);
            this.addLast(newbe);
            cache.put(key, newbe);
        }

        if (capacity < cache.size()) {
            Node target = this.head.next;
            this.remove(target);
            cache.remove(target.key);
        }
    }

    public void addLast(Node target) {
        Node last = this.tail.prev;
        last.next = target;
        target.prev = last;
        this.tail.prev = target;
        target.next = this.tail;
    }

    public void remove(Node target) {
        Node prev = target.prev;
        Node next = target.next;
        prev.next = next;
        next.prev = prev;
    }
}