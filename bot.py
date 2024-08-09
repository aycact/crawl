from selenium import webdriver
from selenium.webdriver.common.by import By
from obj import tuvi, age, info, destiny
from bs4 import BeautifulSoup
from threading import Lock
import os
import json
import time
import re
import datetime
# Hàm loại bỏ CSS
def summary(content):
    # Parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # Find the sections marked by the <h2> tags
    sections = soup.find_all('h2')

    # Initialize variables to store the desired content
    desired_content = ""
    collect = False

    # Iterate through the HTML elements
    for element in soup.descendants:
        if element.name == 'h2' and 'III.' in element.get_text():
            collect = True
            continue
        elif element.name == 'h2' and 'IV.' in element.get_text():
            collect = False
        elif collect and element.name == 'div':
            desired_content += element.get_text() + "\n"

    # Clean up the content by removing non-breaking spaces
    desired_content = re.sub(r'&nbsp;', ' ', desired_content)

    # Remove empty lines
    non_empty_lines = [line for line in desired_content.splitlines() if line.strip()]

    # Join the non-empty lines back into a single string
    cleaned_content = "\n".join(non_empty_lines)

    return cleaned_content

def fengshui(content):
    # Tạo biểu thức chính quy
    pattern = re.compile(r'<strong>1\.3.*?<\/strong>(.*?)<h3>2\.', re.DOTALL)

    # Tìm kiếm và trích xuất đoạn văn bản
    match = pattern.search(content)
    if match:
        extracted_text = match.group(1).strip()
        soup = BeautifulSoup(extracted_text, 'html.parser')
        result = []

        # Duyệt qua tất cả các thẻ <ul> với class="list_order"
        for ul in soup.find_all('ul', class_='list_order'):
            li = ul.find('li')
            if li:
                strong_tag = li.find('strong')
                if strong_tag:
                    title = strong_tag.get_text(strip=True).rstrip(':')
                    content = li.get_text(separator=' ', strip=True).replace(f'{title}:', '').strip()
                    content = re.sub(r'^[^&]*&nbsp;', '', content).strip()  # Loại bỏ nội dung trước &nbsp;
                    result.append({
                        "Title": title,
                        "Content": content
                    })
        return result
    else:
        return "Không tìm thấy đoạn văn bản phù hợp."

# Hàm xử lý chuỗi
def xlc(line):
    # Loại bỏ dấu chấm, dấu gạch ngang, dấu sao và khoảng trắng
    pattern = re.compile(r'^\s*[\d\.\-\*\s]+')

    # Loại bỏ chữ xem, viết hoa chữ cái đầu tiên và xóa khoảng trắng ở đầu và cuối chuỗi
    cleaned_line = pattern.replace("Xem ", "").replace("- Theo ","").sub('', line).strip().capitalize()

    return cleaned_line
file_lock = Lock()
# def add_item_to_json(file_path, new_item, url):
# #   """Thêm một mục mới vào file JSON

# #   Args:
# #     file_path: Đường dẫn đến file JSON
# #     new_item: Mục mới cần thêm (dưới dạng một dictionary)
# #   """

#     try:
#         # Kiểm tra nếu file tồn tại và không rỗng
#         if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 data = json.load(f)
#             f.close()
#             del f
#         else:
#             data = []  # Khởi tạo một list rỗng nếu file không tồn tại hoặc rỗng

#         # Kiểm tra xem dữ liệu đã có chưa, nếu có thì cập nhật, không thì thêm mới
#         if isinstance(data, list):
#             for item in data:
#                 if item['url'] == url:
#                     item.update(new_item)
#                     break
#             else:
#                 data.append(new_item)
#         elif isinstance(data, dict):
#             data.update(new_item)
#         else:
#             raise ValueError("Dữ liệu trong file không phải là list hoặc dict")

#         # Ghi dữ liệu trở lại file
#         # with open(file_path, 'w', encoding='utf-8') as f:
#         #   json.dump(data, f, ensure_ascii=False, indent=4)
#         with open(file_path, 'w', encoding='utf-8') as f:
#             json.dump(data, f, ensure_ascii=False, indent=4)
#         f.close()
#         del f
        
#     except FileNotFoundError:
#         print(f"File {file_path} không tồn tại")
#     except json.JSONDecodeError:
#         print(f"Dữ liệu trong file {file_path} không hợp lệ")
def add_item_to_json(file_path, new_item, url):
    """Thêm một mục mới vào file JSON

    Args:
        file_path: Đường dẫn đến file JSON
        new_item: Mục mới cần thêm (dưới dạng một dictionary)
        url: URL của mục mới
    """
    try:
        with file_lock:
            # Kiểm tra nếu file tồn tại và không rỗng
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = []  # Khởi tạo một list rỗng nếu file không tồn tại hoặc rỗng

            # Kiểm tra xem dữ liệu đã có chưa, nếu có thì cập nhật, không thì thêm mới
            if isinstance(data, list):
                for item in data:
                    if item['url'] == url:
                        item.update(new_item)
                        break
                else:
                    data.append(new_item)
            elif isinstance(data, dict):
                data.update(new_item)
            else:
                raise ValueError("Dữ liệu trong file không phải là list hoặc dict")

            # Ghi dữ liệu trở lại file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        
    except FileNotFoundError:
        print(f"File {file_path} không tồn tại")
    except json.JSONDecodeError:
        print(f"Dữ liệu trong file {file_path} không hợp lệ")
def laytuoi(html_content):
    tuoi=age({}, {}, {}, {})
    soup = BeautifulSoup(html_content, 'html.parser')

    # Tìm tất cả các hàng trong bảng
    rows = soup.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 2:
            col1_text = cols[0].text.strip()
            col2_text = cols[1].text.strip()

            # Sử dụng regex để tìm kiếm các pattern
            if re.search("Năm dương lịch", col1_text):
                # Xử lý trường hợp "Năm dương lịch"
                tuoi.set_year(re.sub(r'\D', '', col2_text))
            elif re.search("Tuổi can chi", col1_text):
                # Xử lý trường hợp "Tuổi can chi"
                tuoi.set_sexagenary_age(col2_text)
            elif re.search("Giới tính", col1_text):
                # Xử lý trường hợp "Giới tính"
                tuoi.set_gender(col2_text)
    return tuoi

def scrap(url):
    # Khởi tạo WebDriver (ở đây sử dụng Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=options)
    # Truy cập trang web cần scraping
    driver.get(url)

    # Đợi trang web tải hoàn toàn (nếu cần thiết)
    # time.sleep(2)

    # Tìm kiếm các phần tử cần scraping (thay thế bằng XPath hoặc CSS Selector phù hợp)
    hi = driver.find_elements(By.TAG_NAME, 'h2')
    ps = driver.page_source

    if (re.search(r'Nội dung đang được cập nhật. Bạn vui lòng quay lại sau.', ps)):
        driver.quit()
        add_item_to_json('data.json', {
            "url": url,
            "content": "Đang cập nhật"
        }, url)
        print("Web chưa có")
    else:
        # Duyệt qua các phần tử và lấy dữ liệu
        
        inf = info({},{},{},{},{},{},{})
        vanhan = destiny({}, {}, {})
        tuoi = None
        sm = None
        fs = None
        for j, el in enumerate(hi, 1):
            if j==1:
                for i, l in enumerate(driver.find_elements(By.XPATH, '//*[@id="content-resp"]/ul['+str(j)+']/li'), 1):
                    tp=l.find_element(By.XPATH, '//*[@id="content-resp"]/ul['+str(j)+']/li[' + str(i) + ']').text
                    td, mt= tp.split(": ")
                    if td=="Năm sinh":
                        inf.set_birth_year(mt)
                    elif td=="Tuổi âm":
                        inf.set_lunar_age(mt)
                    elif td=="Vận niên":
                        inf.set_van_nien(mt)
                    elif td=="Sao hạn":
                        inf.set_sao_han(mt)
                    elif td=="Kim Lâu":
                        inf.set_kim_lau(mt)
                    elif td=="Tam Tai":
                        inf.set_tam_tai(mt)
                    elif td=="Hoang Ốc":
                        inf.set_hoang_oc(mt)
                tuoi = laytuoi(ps)
                tuoi.set_birth_year(inf.get_birth_year())
            elif j==2:
                u=5
                for l in driver.find_elements(By.XPATH, '//*[@id="content-resp"]/ul['+str(u)+']/li'):
                    for u in range(5, 8):
                        tp=l.find_element(By.XPATH, '//*[@id="content-resp"]/ul['+str(u)+']/li').text
                        td, mt= tp.split(": ")
                        if td.find("Tam Tai")==0:
                            vanhan.set_tam_tai(mt)
                        elif td.find("Kim Lâu")==0:
                            vanhan.set_kim_lau(mt)
                        elif td.find("Hoang Ốc")==0:
                            vanhan.set_hoang_oc(mt)
            elif j==3:
                sm = summary(ps)
            elif j==4:
                fs = fengshui(ps)
        
        # Tạo một đối tượng từ lớp tuvi
        tv=tuvi(url, tuoi, inf, vanhan, sm, fs)

        # Đóng trình duyệt
        driver.quit()
        del driver

        # Lưu dữ liệu vào file JSON
        add_item_to_json('data.json', tv.show(), url)

        del tv

        print("Scraping và lưu dữ liệu thành công!")
