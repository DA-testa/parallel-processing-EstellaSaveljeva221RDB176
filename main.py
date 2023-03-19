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

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
