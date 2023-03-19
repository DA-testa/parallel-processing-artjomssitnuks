import heapq

def parallel_processing(n, m, data):
    # create a priority queue (heap) to track the next available thread
    # initialize with (start_time, thread_index)
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)

    # create a list to store the start times for each job
    start_times = [None] * m

    for i in range(m):
        # pop the next available thread from the queue
        start_time, thread_index = heapq.heappop(threads)

        # assign the job to the thread and update its start time
        start_times[i] = (thread_index, start_time)
        start_time += data[i]

        # push the thread back into the queue with updated start time
        heapq.heappush(threads, (start_time, thread_index))

    return start_times

def main():
    # read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # get the start times for each job
    start_times = parallel_processing(n, m, data)

    # print the results
    for thread_index, start_time in start_times:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()
