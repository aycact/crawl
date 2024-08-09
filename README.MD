# CLICKHOUSE
## Cú pháp
- Hầu hết được bê qua từ SQL
- Dùng USE để chọn database trong Terminal, không chọn trên HTTP/HTTPS được
## Truy cập
- Thông qua HTTP cổng 8123, HTTPS cổng 8443
- Terminal cổng 9000
- Muón dùng đa dòng và đa truy vấn phải dùng clickhouse-client --multiline --multiquery
## Trùng lặp dữ liệu
- Primary Key không UNIQUE
- Không có UNIQUE Key, Foreign Key, mọi thứ phải tự dùng hàm optimize
- Xóa trùng lặp bằng lệnh OPTIMIZE TABLE name DEDUPLICATE BY colX,colY,colZ; hoặc BY COLUMNS('column-matched-by-regex') EXCEPT (colX, colY);