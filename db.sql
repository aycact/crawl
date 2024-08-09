set allow_experimental_object_type = 1;
create database tuvi;
use tuvi;
create table age(
id UUID default generateUUIDv7() primary key,
year Int16 not null default 0,
s_age String not null,
b_year Int16 not null default 0,
gender bool not null
)engine = MergeTree
order by (id);
create table info(
id UUID default generateUUIDv7() primary key,
b_year Int16 not null default 0,
l_age Int16 not null default 0,
van_nien String not null,
sao_han String not null,
kim_lau String not null,
tam_tai String not null,
hoang_oc String not null
)engine = MergeTree
order by (id);
create table destiny(
id UUID default generateUUIDv7() primary key,
kim_lau String not null,
tam_tai String not null,
hoang_oc String not null
)engine = MergeTree
order by (id);
create table tv(
url String not null primary key,
age_id UUID not null,
info_id UUID not null,
destiny_id UUID not null,
summary String null,
fengshui JSON not null
)engine = MergeTree;
create view if not exists tv_view as select tv.url, age.year, age.s_age, age.b_year, age.gender, info.l_age, info.van_nien, info.sao_han, info.kim_lau, info.tam_tai, info.hoang_oc, destiny.kim_lau, destiny.tam_tai, destiny.hoang_oc, tv.summary, tv.fengshui from tv join age on tv.age_id = age.id join info on tv.info_id = info.id join destiny on tv.destiny_id = destiny.id;