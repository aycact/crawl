# CLICKHOUSE
## Cú pháp
- Hầu hết được bê qua từ SQL
- Dùng USE để chọn database trong Terminal, không chọn trên HTTP/HTTPS được
- Dùng AS để đặt tên lại các cột
## Truy cập
- Thông qua HTTP cổng 8123, HTTPS cổng 8443
- Terminal cổng 9000
- Muốn dùng đa dòng và đa truy vấn phải dùng clickhouse-client --multiline --multiquery
- clickhouse-driver và HTTP/HTTPS không dùng đa dòng và đa truy vấn được
- Kết thúc 1 câu truy cấn bằng ; nếu dùng đa dòng và đa truy vấn
## Cài đặt bằng docker
- Chạy docker compose up -d tại vị trí có file compose.yaml này
- Mở các port 8123 và 9000 để truy cập ngoài docker
## Trùng lặp dữ liệu
- Primary Key không UNIQUE
- Không có UNIQUE Key, Foreign Key, mọi thứ phải tự dùng hàm optimize
- Xóa trùng lặp bằng lệnh OPTIMIZE TABLE name DEDUPLICATE BY colX,colY,colZ; hoặc BY COLUMNS('column-matched-by-regex') EXCEPT (colX, colY)
## Dùng kiểu JSON
- Chạy lệnh set allow_experimental_object_type = 1 trong clickhouse-client
## Viết script
- ClickHouse không có procedure, function chỉ sử dụng được lambda nên không viết lệnh phức tạp được, phải sử dụng ngôn ngữ lập trình