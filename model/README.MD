# URL của database CockroachDB
- Kết cấu URL của CockroachDB: postgresql://``username``:``password``@``host``:``port``/``database``?sslmode=``ssl mode``&... Chúng ta chỉ cần thay các biến trong quote thôi
* Ví dụ: ``postgresql://ayclqt:ayclqt@127.0.0.1:26257/tuvi?sslmode=prefer``
- Dán vào file .env thay dòng DATABASE_URL