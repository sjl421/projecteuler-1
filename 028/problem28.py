#!/usr/bin/python2

def main():
    size = 1001
    n = 1
    result = 0
    cnt = 0
    step = 2

    while n <= size*size:
        result += n
        cnt += 1
        n += step

        if not cnt & 3: # layer done
            step += 2

    return result

if __name__ == "__main__":
    print main()
