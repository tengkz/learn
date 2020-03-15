CC=g++
CPPFLAGS=-std=c++11
LDFLAGS=-lpthread

OBJ=sequential_consistency relaxed sstream acquire_release hello_thread thread_practise1 thread_practise2 mutex_practise1 mutex_practise2 lock_practise1 lock_practise2

all: $(OBJ)

lock_practise2: lock_practise2.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

lock_practise1: lock_practise1.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

mutex_practise2: mutex_practise2.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

mutex_practise1: mutex_practise1.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

thread_practise2: thread_practise2.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

thread_practise1: thread_practise1.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

sequential_consistency: sequential_consistency.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

relaxed: relaxed.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

sstream: sstream.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

acquire_release: acquire_release.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

hello_thread: hello_thread.cpp
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $@ $^

.PHONY:
	clean

clean:
	rm $(OBJ) 
