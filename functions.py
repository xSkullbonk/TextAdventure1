import sys, time 

def slow_print(input_str):
    for c in input_str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')