from lorempicsum import lorem_picsum
import concurrent.futures
import time

tic = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    [executor.submit(lorem_picsum, i) for i in range(1,16)]


toc=time.perf_counter()


print(f'Downloaded in {toc-tic} seconds')