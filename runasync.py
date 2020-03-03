from lorempicsum import lorem_picsum
import time
tic = time.perf_counter()
for i in range(1,16):
    lorem_picsum(f'image{i}')
toc = time.perf_counter()
print(f'Downloaded in {toc-tic} seconds')