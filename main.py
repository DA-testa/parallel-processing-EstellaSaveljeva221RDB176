# Estella Saveljeva 221RDB176 7.gr

def parallel_processing(n, m, data):
    output = []
    nexthread = 0
    numthread = [0] * n
    for i in range(m):
        thread=nexthread
       
        start = numthread[thread]
        end = start + data[i]

        numthread[numthread] = end
        nexthread = (nexthread + 1) % n
        output.append((thread, start))

    return output

def main():
    n, m = map(int, input(": ").split())
    data = list(map(int, input(": ").split()))
    result = parallel_processing(n,m,data)
    for i,j in result:
        print(i, j)

if __name__ == "__main__":
    main()
