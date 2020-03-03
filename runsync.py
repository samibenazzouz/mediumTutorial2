from lorempicsum import lorem_picsum
import threading
import time

tic = time.perf_counter()

threads = []

for i in range(0,15):
    threads.append(threading.Thread(target=lorem_picsum, args=[i]))
    threads[i].start()
for thread in threads:
    thread.join()

toc = time.perf_counter()

print(f'Downloaded in {toc-tic} seconds')