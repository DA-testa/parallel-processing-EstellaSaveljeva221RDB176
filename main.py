# Estella Saveljeva 221RDB176 7.gr

def parallel_processing(n, m, data):
    output = []
    nexthread = 0
    numthread = [0] * n
    for i in range(m):
        nexthread=0
        for j in range (1,n):
            if numthread[j]<numthread[nexthread]:
                nextread = j
                    
        start = numthread[nexthread]
        end = start + data[i]

        numthread[numthread] = end
        output.append((nexthread, start))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input(": ").split()))
    result = parallel_processing(n,m,data)
    for i,j in result:
        print(i, j)

if __name__ == "__main__":
    main()
