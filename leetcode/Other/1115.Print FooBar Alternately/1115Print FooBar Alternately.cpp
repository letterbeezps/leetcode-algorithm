class FooBar {
private:
    int n;
    std::mutex m1_, m2_;

public:
    FooBar(int n) {
        this->n = n;
        m2_.lock();
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            m1_.lock();
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            m2_.unlock();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            m2_.lock();
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            m1_.unlock();
        }
    }
};