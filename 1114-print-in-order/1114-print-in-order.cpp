class Foo {
public:
    std::mutex m;
    std::condition_variable cv;
    int cur = 1;
    Foo() { }

    void first(function<void()> printFirst) {
        printFirst();
        cur = 2;
        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        std::unique_lock lk(m);
        cv.wait(lk, [this]{ return cur == 2; });
        printSecond();
        cur = 3;
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        std::unique_lock lk(m);
        cv.wait(lk, [this]{ return cur == 3; });
        printThird();
    }
};