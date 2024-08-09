import json
class age:
    def __init__(self, year, sexagenary_age, birth_year, gender):
        self.year = year
        self.sexagenary_age = sexagenary_age
        self.birth_year = birth_year
        self.gender = gender

    def show(self):
        return {
            "year": self.year,
            "sexagenary_age": self.sexagenary_age,
            "birth_year": self.birth_year,
            "gender": self.gender
        }
    
    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_sexagenary_age(self):
        return self.sexagenary_age

    def set_sexagenary_age(self, sexagenary_age):
        self.sexagenary_age = sexagenary_age

    def get_birth_year(self):
        return self.birth_year

    def set_birth_year(self, birth_year):
        self.birth_year = birth_year

    def get_gender(self):
        return self.gender
    
    def set_gender(self, gender):
        self.gender=gender
    
class info:
    def __init__(self, birth_year, lunar_age, van_nien, sao_han, kim_lau, tam_tai, hoang_oc):
        self.birth_year = birth_year
        self.lunar_age = lunar_age
        self.van_nien = van_nien
        self.sao_han = sao_han
        self.kim_lau = kim_lau
        self.tam_tai = tam_tai
        self.hoang_oc = hoang_oc

    def show(self):
        return {
            "birth_year": self.birth_year,
            "lunar_age": self.lunar_age,
            "van_nien": self.van_nien,
            "sao_han": self.sao_han,
            "kim_lau": self.kim_lau,
            "tam_tai": self.tam_tai,
            "hoang_oc": self.hoang_oc
        }

    def get_birth_year(self):
        return self.birth_year
    
    def set_birth_year(self, birth_year):
        self.birth_year = birth_year
    
    def get_lunar_age(self):
        return self.lunar_age

    def set_lunar_age(self, lunar_age):
        self.lunar_age = lunar_age

    def get_van_nien(self):
        return self.van_nien

    def set_van_nien(self, van_nien):
        self.van_nien = van_nien

    def get_sao_han(self):
        return self.sao_han

    def set_sao_han(self, sao_han):
        self.sao_han = sao_han

    def get_kim_lau(self):
        return self.kim_lau

    def set_kim_lau(self, kim_lau):
        self.kim_lau = kim_lau

    def get_tam_tai(self):
        return self.tam_tai

    def set_tam_tai(self, tam_tai):
        self.tam_tai = tam_tai

    def get_hoang_oc(self):
        return self.hoang_oc

    def set_hoang_oc(self, hoang_oc):
        self.hoang_oc = hoang_oc
class destiny:
    def __init__(self, tam_tai, kim_lau, hoang_oc):
        self.tam_tai = tam_tai
        self.kim_lau = kim_lau
        self.hoang_oc = hoang_oc
    def show(self):
        return {
            "tam_tai": self.tam_tai,
            "kim_lau": self.kim_lau,
            "hoang_oc": self.hoang_oc
        }
    def get_tam_tai(self):
        return self.tam_tai
    def set_tam_tai(self, tam_tai):
        self.tam_tai = tam_tai
    def get_kim_lau(self):
        return self.kim_lau
    def set_kim_lau(self, kim_lau):
        self.kim_lau = kim_lau
    def get_hoang_oc(self):
        return self.hoang_oc
    def set_hoang_oc(self, hoang_oc):
        self.hoang_oc = hoang_oc
class tuvi:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def __init__(self, url, age, info, destiny, summary, fengshui):
        self.url = url
        self.age = age
        self.info = info
        self.destiny = destiny
        self.summary = summary
        self.fengshui = fengshui

    def show(self):
        return {
            "url": self.url,
            "age": self.age.show(),
            "info": self.info.show(),
            "destiny": self.destiny.show(),
            "summary": self.summary,
            "fengshui": self.fengshui
        }
    
    def get_url(self):
        return self.url
    
    def set_url(self, url):
        self.url = url

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_destiny(self):
        return self.destiny

    def set_destiny(self, destiny):
        self.destiny = destiny

    def get_summary(self):
        return self.summary

    def set_summary(self, summary):
        self.summary = summary

    def get_fengshui(self):
        return self.fengshui

    def set_fengshui(self, fengshui):
        self.fengshui = fengshui