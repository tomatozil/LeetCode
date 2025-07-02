class Foo {
public:
    mutex mtx;
    condition_variable cv;
    int cur = 1;
    Foo() { }

    void first(function<void()> printFirst) {
        printFirst();
        cur = 2;
        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [this]{ return cur == 2; });
        printSecond();
        cur = 3;
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [this]{ return cur == 3; });
        printThird();
    }
};