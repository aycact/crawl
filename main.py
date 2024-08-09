import datetime
import gc
from bot import scrap
from concurrent.futures import ThreadPoolExecutor, as_completed
can = ["giap", "at", "binh", "dinh", "mau", "ky", "canh", "tan", "nham", "quy"]
chi = ["ty", "suu", "dan", "mao", "thin", "ti", "ngo", "mui", "than", "dau", "tuat", "hoi"]
gt = ["nam", "nu"]
print("Nhập năm kết thúc: ")
nam = int(input())
def scrap_url(n, i, j, k):
    url = f"https://lichngaytot.com/tu-vi-{n}-tuoi-{i}-{j}-{k}-mang.html"
    if url != "https://lichngaytot.com/tu-vi-2024-tuoi-giap-ngo-nu-mang.html":
        print(url)
        scrap(url)
        del url

try:
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for n in range(datetime.date.today().year, nam):
            for i in can:
                for j in chi:
                    for k in gt:
                        futures.append(executor.submit(scrap_url, n, i, j, k))
        
        # Wait for all threads to complete
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")
    
    print("Hoàn thành!")
except Exception as e:
    print(e)
# for n in range(datetime.date.today().year, nam):
#     for i in can:
#         for j in chi:
#             for k in gt:
#                 url = f"https://lichngaytot.com/tu-vi-{n}-tuoi-{i}-{j}-{k}-mang.html"
#                 print(url)
#                 scrap(url)
#                 del url
#                 gc.collect()
# print("Hoàn thành!")