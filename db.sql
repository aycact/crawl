set allow_experimental_object_type = 1;
create database tuvi;
use tuvi;
create table age(
url String not null primary key,
year Int16 not null default 0,
s_age String not null,
b_year Int16 not null default 0,
gender bool not null
)engine = MergeTree;
create table info(
url String not null primary key,
b_year Int16 not null default 0,
l_age Int16 not null default 0,
van_nien String not null,
sao_han String not null,
kim_lau String not null,
tam_tai String not null,
hoang_oc String not null
)engine = MergeTree;
create table destiny(
url String not null primary key,
kim_lau String not null,
tam_tai String not null,
hoang_oc String not null
)engine = MergeTree;
create table tv(
url String not null primary key,
summary String null,
fengshui JSON not null
)engine = MergeTree;
CREATE VIEW IF NOT EXISTS tv_view AS
SELECT 
    tv.url, 
    age.year AS year, 
    age.s_age AS s_age, 
    age.b_year AS b_year, 
    age.gender AS gender, 
    info.l_age AS l_age, 
    info.van_nien AS van_nien, 
    info.sao_han AS sao_han, 
    info.kim_lau AS info_kim_lau, 
    info.tam_tai AS info_tam_tai, 
    info.hoang_oc AS info_hoang_oc, 
    destiny.kim_lau AS destiny_kim_lau, 
    destiny.tam_tai AS destiny_tam_tai, 
    destiny.hoang_oc AS destiny_hoang_oc, 
    tv.summary, 
    tv.fengshui
FROM 
    tv 
JOIN 
    age ON tv.url = age.url
JOIN
    info ON tv.url = info.url
JOIN
    destiny ON tv.url = destiny.url;

