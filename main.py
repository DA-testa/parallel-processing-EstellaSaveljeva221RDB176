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
    if not(1 <= n <= 10**5):
        raise ValueError("n range is between 1 and 10^5")
    if not(1 <= m <= 10**5):
        raise ValueError("m range is between 1 and 10^5")
    data = list(map(int, input().split()))
    for i in range(m):
        if not(0 <= data[i] <= 10**9):
            raise ValueError("Elements between 0 and 10^9")
    result = parallel_processing(n,m,data)
    
    for i in range(m):
        print(result[i][0], result[i][1])

if __name__ == "__main__":
    main()
