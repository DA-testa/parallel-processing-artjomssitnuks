import heapq

def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)

    start_times = [None] * m

    for i in range(m):
        start_time, thread_index = heapq.heappop(threads)

        start_times[i] = (thread_index, start_time)
        start_time += data[i]

        heapq.heappush(threads, (start_time, thread_index))

    return start_times

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    start_times = parallel_processing(n, m, data)

    for thread_index, start_time in start_times:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()
