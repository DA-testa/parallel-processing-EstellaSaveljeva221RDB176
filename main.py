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
    n = 0
    m = 0

    data = []

    
    result = parallel_processing(n,m,data)
    
    



if __name__ == "__main__":
    main()
