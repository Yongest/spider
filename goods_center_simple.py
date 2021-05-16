# coding=utf-8
# Version:Python 3.8.0
# Tools:PyCharm 2020.2 x64
__date__ = '2021/5/12 14:14'
__author__ = '张勇'
import requests
import re
import json
from lxml import etree
domain = 'https://www.jiazhuangpei.com'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
    'Cookie':'PHPSESSID=bb9b83861c8971c800616ed7f6884449; SERVERID=44eaeffc8bad2a92fe4cdc77619b902d|1620952773|1620951387'
}
key_li_all = ["J-JL-BZ-LSB-CZ3507-74022-CZ", "J-JL-BZ-LSB-CJ3501-73495-CJ", "J-JL-BZ-LSB-CD3518-73982-CD",
 "J-JL-BZ-LSB-ZD3513-72973-SZD", "J-JL-BZ-LSB-SZT3510-72709-SZT", "J-JL-BZ-LSB-SZ3506-73427-SZ",
 "J-JL-BZ-LSB-YJ3520-74025-XYJ", "J-JL-BZ-LSB-CG3509-72705-CTG", "J-JL-BZ-LSB-C3512-72714-18C",
 "J-JL-BZ-LSB-CG3509-72707-CTG", "J-JL-BZ-LSB-C3512-72742-15C", "J-JL-BZ-LSB-TV3508-73491-DSG", "J-SPYX-MD-MG-09A-3RW",
 "J-DDYM-CS-B-265-CY", "J-DDYM-CS-B-203-130-CZ", "J-DDYM-CS-B-123-135-CJ", "J-DDYM-CS-B-007-180-18C",
 "J-DDYM-CS-B-009-180-18C", "J-DDYM-CS-B-030-CTG", "J-DDYM-CS-B-031-CTG", "J-DDYM-CS-B-100-160-DG",
 "J-DDYM-CS-B-139-YZJ", "J-LD-BS-A328+A380-18GXC", "J-LD-BS-B301-CTG", "J-LD-BS-H325C+H325D-DSGTZ", "J-LD-BS-E303L-DSG",
 "J-LD-BS-B328-CTG", "J-LD-BS-H301C-DSG", "J-LD-BS-G302-CBG", "J-LD-BS-S310-ZZJ", "J-LD-BS-I307-5-5DG",
 "J-LD-BS-H302C-DSG", "J-LD-BS-S312-2-2RW", "J-LD-BS-H328C-DSG", "J-LD-BS-R325-JG", "J-LD-BS-S312-1-1RW",
 "J-LD-BS-S328E-2-JJ", "J-LD-BS-S332E-2-JJ", "J-LD-BS-S328E-1-CJ", "J-LD-BS-P325SC-SY", "J-LD-BS-S316E-1-CJ",
 "J-LD-BS-S325E-1-CJ", "J-LD-BS-S332E-1-CJ", "J-LD-BS-C303D-ZD", "J-LD-BS-T328-CZ", "J-LD-BS-S316E-2-JJ",
 "J-LD-BS-C325+C325G-ZTJ", "J-LD-BS-P325C-CY", "J-LD-BS-P302XC-XXY", "J-EK-EK-1906-CY", "J-EK-EK-B6024-TYCJ",
 "J-EK-EK-G-JJ-089-14CZ", "J-EK-EK-18125-2RW", "J-SSBF-YGJ-BW2007-CTG", "J-SSBF-YGJ-BW2009-CTG", "J-EK-EK-8807-1-DSG",
 "J-EK-EK-18093-3RW", "J-EK-EK-K2742-15C", "J-YXMS-MLS-YX1165-18C", "J-EK-EK-18125-3RW", "J-EK-EK-18125-2RW",
 "J-EK-EK-011-CTG", "J-EK-EK-W-027-18C", "J-EK-EK-9940-18C", "J-EK-EK-011-CTG", "J-EK-EK-18125-3RW", "J-EK-EK-819-XXY",
 "J-EK-EK-XK04-2-DCJ", "J-EK-EK-XK04-1-XCJ", "J-EK-EK-Z01-14CZ", "J-EK-EK-J1830-CY", "J-EK-EK-8887-18C",
 "J-EK-EK-B1553-22DSG", "J-EK-EK-G-826-CTG", "J-EK-EK-G-827-CTG", "J-EK-EK-18101-3RW", "J-YXMS-MLS-571-CTG",
 "J-EK-EK-9926-18C", "J-EK-EK-18125-3RW", "J-EK-EK-JM-816-3RW", "J-EK-EK-G-828-CTG", "J-EK-EK-QS233-DSG",
 "J-EK-EK-T17-1-CY", "J-EK-EK-T18-14CZ", "J-EK-EK-CJ010-CJ", "J-EK-EK-G-828-CTG", "J-EK-EK-G-829-CTG",
 "J-EK-EK-80072-18C", "J-EK-EK-9933-18C", "J-MSH-ZY-CJ-9003B-CJ", "J-MSH-ZY-C-9005-2CY", "J-MSH-ZY-T-9003-18CZ",
 "J-MSH-ZY-CJ-9003A-CJ", "J-MSH-ZY-BT-9001-18C", "J-MSH-ZY-BT-9002-18C", "J-MSH-ZY-BT-9003-18C", "J-MSH-ZY-BG-9002-CTG",
 "J-MSH-ZY-BG-9003-CTG", "J-MSH-ZY-DG-9006A-ZHDG", "J-MSH-ZY-SF-9006BZ-DF2",
 "J-MSH-ZY-SF-9006C-3RW","J-MSH-ZY-SF-9006E-JT","J-MSH-ZY-SF-9006AZ-ZJW","J-MSL-LP-ZC-064-BJ","J-MSL-LP-ZE-084-CJ","J-MSL-LP-ZD-034-CZ","J-MSL-LP-YX-006-CY","J-WML-LP-GN-040-CTG","J-MSL-LP-GT-059-DSG","J-ZZ-SH-327026-3RW","J-MSL-LP-GN-029-CTG","J-MSL-LP-C-060-18C","J-FT-FT-919#-ZZJ","J-FT-FT-CJ-01-CJ","J-FT-FT-DS-01-DSG","J-FT-FT-C-01-18C","J-FT-FT-G-01-CTG","J-FT-FT-G-04-CTG","J-FT-FT-CZ-05-13CZ","J-FT-FT-Y-02-BCY","J-FT-FT-C-03-18C","J-DGXDBO-JJM-259-XCZ","J-DGXDBO-JJM-257-XCJ","J-DGXDBO-JJM-257-DSG","J-DGXDBO-JJM-257-YZJ","J-ZZ-SH-362070H-18C","J-SSBF-YGJ-BW2005-CTG","J-SSBF-YGJ-BW2006-CTG","J-ZZ-SH-362086-18C","J-MSG-ZGX-FY-710-18C","J-MSG-ZGX-FY-515-CTG","J-MSG-ZGX-FY-723-18C","J-MSG-ZGX-FY-866-ZZJ","J-MSG-ZGX-FY-10-DSG","J-MSG-ZGX-FY12-CJTZ","J-MSG-ZGX-FY-515-CTG-1","J-MSG-ZGX-FY-06-2CY","J-MSG-ZGX-FY-13-CZ","J-MT-MWY-C1204-CY","J-MBL-FK-R-9803-18C","J-MBL-FK-R-9002B-18C","J-MBL-FK-26-CTG","J-MBL-FK-33-CTG","J-MBL-FK-8077-YZJ-1","J-MBL-FK-203-DSG","J-MBL-FK-203-CJ","J-MBL-FK-F800-15-CZ","J-EK-EK-16-18C","J-EK-EK-BY025-18C","J-SSBF-YGJ-BW2009-CTG","J-EK-EK-G-816-1-DSG","J-SSBF-YGJ-BW2007-CTG","J-EK-EK-S052-3RW","J-EK-EK-8809-CJ","J-EK-EK-G-JJ-089-14CZ","J-EK-EK-Y16-1-CY","J-KQ-MJMJ-CG-107-18C","J-KQ-MJMJ-CG-106-18C","J-KQ-MJMJ-CG-105-18C","J-KQ-MJMJ-CG-102-18C","J-KQ-MJMJ-CG-810-2RW","J-KQ-MJMJ-CG-805-3RW","J-KQ-MJMJ-CG-810-1RW","J-KQ-MJMJ-CG-805-2RW","J-KQ-MJMJ-CG-801-ZZJ","J-KQ-MJMJ-CG-805-1RW","J-KQ-MJMJ-CG-7008-DSG","J-KQ-MJMJ-CG-7006-DSG","J-KQ-MJMJ-CG-106-CTG","J-KQ-MJMJ-CG-102-CTG","J-KQ-MJMJ-CG-810-3RW","J-KQ-MJMJ-CG-101-18C","J-KQ-MJMJ-CG-102-SZ","J-KQ-MJMJ-CG-902-CY","J-KQ-MJMJ-CG-306-CJ","J-KQ-MJMJ-CG-306-YJ","J-KQ-MJMJ-CG-205-CZ","J-KQ-MJMJ-CG-903-CY","J-KQ-MJMJ-CG-303-CJ","J-KQ-MJMJ-CG-106-ZT","J-KQ-MJMJ-CG-901-ZD","J-KQ-MJMJ-CG-208-YCZ","J-MDJT-QY-03B-18C","J-MDJT-QY-02B-18C","J-MDJT-QY-95SJ-SJ","J-MDJT-QY-01B-18C","J-MDJT-QY-M01SJ-SJ","J-MDJT-QY-88SJ-SJ","J-MDJT-QY-28SJ-SJ","J-MDJT-QY-42SF-1RW","J-MDJT-QY-42SF-3RW","J-MDJT-QY-99SF-3RW","J-MDJT-QY-72H-HJ","J-MDJT-QY-85XG-XG","J-MDJT-QY-16XG-XG","J-MDJT-QY-88H-HJ","J-MDJT-QY-33H-HJ","J-MDJT-QY-78X-XGG","J-MDJT-QY-11G-CTG","J-MDJT-QY-67D-DSG","J-MDJT-QY-82DG-DG","J-MDJT-QY-88SF-DRW","J-MDJT-QY-04XG-XG","J-MDJT-QY-87XG-XG","J-MDJT-QY-93SF-XXY","J-MDJT-QY-32DG-DG","J-MDJT-QY-32D-DSG","J-MDJT-QY-91G-CTG","J-MDJT-QY-66D-DSG","J-MDJT-QY-07D-DSG","J-MDJT-QY-88SF2-2RW","J-MDJT-QY-08G-CTG","J-MDJT-QY-29B-SJ","J-MDJT-QY-105D-DSG","J-MDJT-QY-25X-XGG","J-MDJT-QY-36CBG-CBG","J-MDJT-QY-42SF-2RW","J-MDJT-QY-103D-DSG","J-MDJT-QY-15D-DSG","J-MDJT-QY-19D-DSG","J-MDJT-QY-29G-CTG","J-MDJT-QY-34CBG-CBG","J-MDJT-QY-03X-XGG","J-MDJT-QY-03D-DSG","J-MDJT-QY-35X-XGG","J-MDJT-QY-47SF-1RW","J-MDJT-QY-99SF-1RW","J-MDJT-QY-86D-DSG","J-MDJT-QY-41X-XGG","J-MDJT-QY-102G-CTG","J-MDJT-QY-60G-CTG","J-MDJT-QY-05XG-XG","J-MDJT-QY-47SF-2RW","J-MDJT-QY-62D-DSG","J-MDJT-QY-72G-CTG","J-MDJT-QY-47SF-3RW","J-MDJT-QY-M01D-DSG","J-MDJT-QY-99SF-2RW","J-MDJT-QY-23X-XGG","J-MDJT-QY-90D-DSG","J-MDJT-QY-32X-XGG","J-MDJT-QY-15CBG-CBG","J-MDJT-QY-18C-CJ","J-MDJT-QY-05C-CJ","J-MDJT-QY-26C-CJ","J-MDJT-QY-04SZ-SZ","J-MDJT-QY-33J-JJ","J-MDJT-QY-17J-JJ","J-MDJT-QY-74CZ-CZ","J-MDJT-QY-41C-CJ","J-MDJT-QY-02J-JJ","J-MDJT-QY-101SD-ZD","J-MDJT-QY-22C-CJ","J-MDJT-QY-M01S-ZT","J-MDJT-QY-25CZ-CZ","J-MDJT-QY-27J-JJ","J-MDJT-QY-101S-ZT","J-MDJT-QY-04J-JJ","J-MDJT-QY-M01CZ-CZ","J-MDJT-QY-27C-CJ","J-MDJT-QY-M01C-CJ","J-MDJT-QY-04C-CJ","J-MDJT-QY-41CZ-CZ","J-MDJT-QY-28SZ-SZ","J-MDJT-QY-44J-JJ","J-MDJT-QY-21CWD-CWD","J-MDJT-QY-69S-ZT","J-MDJT-QY-73CZ-CZ","J-MDJT-QY-15J-JJ","J-MDJT-QY-101CZ-CZ","J-MDJT-QY-98C-CJ","J-MDJT-QY-M08SZ-SZ","J-MDJT-QY-30S-ZT","J-MDJT-QY-03C-CJ","J-MDJT-QY-102SZ-SZ","J-MDJT-QY-41J-JJ","J-MDJT-QY-02C-CJ","J-MDJT-QY-32J-JJ","J-MDJT-QY-102CY-CY","J-MDJT-QY-72C-CJ","J-MDJT-QY-101CY-CY","J-MDJT-QY-18J-JJ","J-MDJT-QY-03J-JJ","J-MDJT-QY-23S-ZT","J-MDJT-QY-33SF-DRW","J-MDJT-QY-96CZ-CZ","J-MDJT-QY-40J-JJ","J-MDJT-QY-20C-CJ","J-MDJT-QY-103C-CJ","J-MDJT-QY-05J-JJ","J-MDJT-QY-46C-CJ-1","J-MDJT-QY-57SD-ZT","J-MDJT-QY-41S-ZT", ]
key_li = ["J-MDJT-QY-03B-18C",
"J-MDJT-QY-02B-18C",
"J-MDJT-QY-95SJ-SJ",
"J-MDJT-QY-01B-18C",
"J-MDJT-QY-M01SJ-SJ",
"J-MDJT-QY-88SJ-SJ",
"J-MDJT-QY-28SJ-SJ",
"J-MDJT-QY-42SF-1RW",
"J-MDJT-QY-42SF-3RW",
"J-MDJT-QY-99SF-3RW",
"J-MDJT-QY-72H-HJ",
"J-MDJT-QY-85XG-XG",
"J-MDJT-QY-16XG-XG",
"J-MDJT-QY-88H-HJ",
"J-MDJT-QY-33H-HJ",
"J-MDJT-QY-78X-XGG",
"J-MDJT-QY-11G-CTG",
"J-MDJT-QY-67D-DSG",
"J-MDJT-QY-82DG-DG",
"J-MDJT-QY-88SF-DRW",
"J-MDJT-QY-04XG-XG",
"J-MDJT-QY-87XG-XG",
"J-MDJT-QY-93SF-XXY",
"J-MDJT-QY-32DG-DG",
"J-MDJT-QY-32D-DSG",
"J-MDJT-QY-91G-CTG",
"J-MDJT-QY-66D-DSG",
"J-MDJT-QY-07D-DSG",
"J-MDJT-QY-88SF2-2RW",
"J-MDJT-QY-08G-CTG",
"J-MDJT-QY-29B-SJ",
"J-MDJT-QY-105D-DSG",
"J-MDJT-QY-25X-XGG",
"J-MDJT-QY-36CBG-CBG",
"J-MDJT-QY-42SF-2RW",
"J-MDJT-QY-103D-DSG",
"J-MDJT-QY-15D-DSG",
"J-MDJT-QY-19D-DSG",
"J-MDJT-QY-29G-CTG",
"J-MDJT-QY-34CBG-CBG",
"J-MDJT-QY-03X-XGG",
"J-MDJT-QY-03D-DSG",
"J-MDJT-QY-35X-XGG",
"J-MDJT-QY-47SF-1RW",
"J-MDJT-QY-99SF-1RW",
"J-MDJT-QY-86D-DSG",
"J-MDJT-QY-41X-XGG",
"J-MDJT-QY-102G-CTG",
"J-MDJT-QY-60G-CTG",
"J-MDJT-QY-05XG-XG",
"J-MDJT-QY-47SF-2RW",
"J-MDJT-QY-62D-DSG",
"J-MDJT-QY-72G-CTG",
"J-MDJT-QY-47SF-3RW",
"J-MDJT-QY-M01D-DSG",
"J-MDJT-QY-99SF-2RW",
"J-MDJT-QY-23X-XGG",
"J-MDJT-QY-90D-DSG",
"J-MDJT-QY-32X-XGG",
"J-MDJT-QY-15CBG-CBG",
"J-MDJT-QY-18C-CJ",
"J-MDJT-QY-05C-CJ",
"J-MDJT-QY-26C-CJ",
"J-MDJT-QY-04SZ-SZ",
"J-MDJT-QY-33J-JJ",
"J-MDJT-QY-17J-JJ",
"J-MDJT-QY-74CZ-CZ",
"J-MDJT-QY-41C-CJ",
"J-MDJT-QY-02J-JJ",
"J-MDJT-QY-101SD-ZD",
"J-MDJT-QY-22C-CJ",
"J-MDJT-QY-M01S-ZT",
"J-MDJT-QY-25CZ-CZ",
"J-MDJT-QY-27J-JJ",
"J-MDJT-QY-101S-ZT",
"J-MDJT-QY-04J-JJ",
"J-MDJT-QY-M01CZ-CZ",
"J-MDJT-QY-27C-CJ",
"J-MDJT-QY-M01C-CJ",
"J-MDJT-QY-04C-CJ",
"J-MDJT-QY-41CZ-CZ",
"J-MDJT-QY-28SZ-SZ",
"J-MDJT-QY-44J-JJ",
"J-MDJT-QY-21CWD-CWD",
"J-MDJT-QY-69S-ZT",
"J-MDJT-QY-73CZ-CZ",
"J-MDJT-QY-15J-JJ",
"J-MDJT-QY-101CZ-CZ",
"J-MDJT-QY-98C-CJ",
"J-MDJT-QY-M08SZ-SZ",
"J-MDJT-QY-30S-ZT",
"J-MDJT-QY-03C-CJ",
"J-MDJT-QY-102SZ-SZ",
"J-MDJT-QY-41J-JJ",
"J-MDJT-QY-02C-CJ",
"J-MDJT-QY-32J-JJ",
"J-MDJT-QY-102CY-CY",
"J-MDJT-QY-72C-CJ",
"J-MDJT-QY-101CY-CY",
"J-MDJT-QY-18J-JJ",
"J-MDJT-QY-03J-JJ",
"J-MDJT-QY-23S-ZT",
"J-MDJT-QY-33SF-DRW",
"J-MDJT-QY-96CZ-CZ",
"J-MDJT-QY-40J-JJ",
"J-MDJT-QY-20C-CJ",
"J-MDJT-QY-103C-CJ",
"J-MDJT-QY-05J-JJ",
"J-MDJT-QY-46C-CJ-1",
"J-MDJT-QY-57SD-ZT",
"J-MDJT-QY-41S-ZT",
"J-EK-EK-BY025-18C",
"J-SSBF-YGJ-BW2009-CTG",
"J-EK-EK-G-816-1-DSG",
"J-SSBF-YGJ-BW2007-CTG",
"J-EK-EK-S052-3RW",
"J-EK-EK-8809-CJ",
"J-EK-EK-G-JJ-089-14CZ",
"J-EK-EK-Y16-1-CY",
"J-DDYM-CS-B-265-CY",
"J-DDYM-CS-B-203-130-CZ",
"J-DDYM-CS-B-123-135-CJ",
"J-DDYM-CS-B-007-180-18C",
"J-DDYM-CS-B-009-180-18C",
"J-DDYM-CS-B-030-CTG",
"J-DDYM-CS-B-031-CTG",
"J-DDYM-CS-B-100-160-DG",
"J-DDYM-CS-B-139-YZJ",
"J-LD-BS-A328+A380-18GXC",
"J-LD-BS-B301-CTG",
"J-LD-BS-H325C+H325D-DSGTZ",
"J-LD-BS-E303L-DSG",
"J-LD-BS-B328-CTG",
"J-LD-BS-H301C-DSG",
"J-LD-BS-G302-CBG",
"J-LD-BS-S310-ZZJ",
"J-LD-BS-I307-5-5DG",
"J-LD-BS-H302C-DSG",
"J-LD-BS-S312-2-2RW",
"J-LD-BS-H328C-DSG",
"J-LD-BS-R325-JG",
"J-LD-BS-S312-1-1RW",
"J-LD-BS-S328E-2-JJ",
"J-LD-BS-S332E-2-JJ",
"J-LD-BS-S328E-1-CJ",
"J-LD-BS-P325SC-SY",
"J-LD-BS-S316E-1-CJ",
"J-LD-BS-S325E-1-CJ",
"J-LD-BS-S332E-1-CJ",
"J-LD-BS-C303D-ZD",
"J-LD-BS-T328-CZ",
"J-LD-BS-S316E-2-JJ",
"J-LD-BS-C325+C325G-ZTJ",
"J-LD-BS-P325C-CY",
"J-LD-BS-P302XC-XXY",
"J-EK-EK-1906-CY",
"J-EK-EK-B6024-TYCJ",
"J-EK-EK-G-JJ-089-14CZ",
"J-EK-EK-18125-2RW",
"J-SSBF-YGJ-BW2007-CTG",
"J-SSBF-YGJ-BW2009-CTG",
"J-EK-EK-8807-1-DSG",
"J-EK-EK-18093-3RW",
"J-EK-EK-K2742-15C",
"J-YXMS-MLS-YX1165-18C",
"J-EK-EK-18125-3RW",
"J-EK-EK-18125-2RW",
"J-EK-EK-011-CTG",
"J-EK-EK-W-027-18C",
"J-EK-EK-9940-18C",
"J-EK-EK-011-CTG",
"J-EK-EK-18125-3RW",
"J-EK-EK-819-XXY",
"J-EK-EK-XK04-2-DCJ",
"J-EK-EK-XK04-1-XCJ",
"J-EK-EK-Z01-14CZ",
"J-EK-EK-J1830-CY",
"J-EK-EK-8887-18C",
"J-EK-EK-B1553-22DSG",
"J-EK-EK-G-826-CTG",
"J-EK-EK-G-827-CTG",
"J-EK-EK-18101-3RW",
"J-YXMS-MLS-571-CTG",
"J-EK-EK-9926-18C",
"J-EK-EK-18125-3RW",
"J-EK-EK-JM-816-3RW",
"J-EK-EK-G-828-CTG",
"J-EK-EK-QS233-DSG",
"J-EK-EK-T17-1-CY",
"J-EK-EK-T18-14CZ",
"J-EK-EK-CJ010-CJ",
"J-EK-EK-G-828-CTG",
"J-EK-EK-G-829-CTG",
"J-EK-EK-80072-18C",
"J-EK-EK-9933-18C",
"J-MSH-ZY-CJ-9003B-CJ",
"J-MSH-ZY-C-9005-2CY",
"J-MSH-ZY-T-9003-18CZ",
"J-MSH-ZY-CJ-9003A-CJ",
"J-MSH-ZY-BT-9001-18C",
"J-MSH-ZY-BT-9002-18C",
"J-MSH-ZY-BT-9003-18C",
"J-MSH-ZY-BG-9002-CTG",
"J-MSH-ZY-BG-9003-CTG",
"J-MSH-ZY-DG-9006A-ZHDG",
"J-MSH-ZY-SF-9006BZ-DF2",
"J-MSH-ZY-SF-9006C-3RW",
"J-MSH-ZY-SF-9006E-JT",
"J-MSH-ZY-SF-9006AZ-ZJW",
"J-MSL-LP-ZC-064-BJ",
"J-MSL-LP-ZE-084-CJ",
"J-MSL-LP-ZD-034-CZ",
"J-MSL-LP-YX-006-CY",
"J-WML-LP-GN-040-CTG",
"J-MSL-LP-GT-059-DSG",
"J-ZZ-SH-327026-3RW",
"J-MSL-LP-GN-029-CTG",
"J-MSL-LP-C-060-18C",
"J-FT-FT-919#-ZZJ",
"J-FT-FT-CJ-01-CJ",
"J-FT-FT-DS-01-DSG",
"J-FT-FT-C-01-18C",
"J-FT-FT-G-01-CTG",
"J-FT-FT-G-04-CTG",
"J-FT-FT-CZ-05-13CZ",
"J-FT-FT-Y-02-BCY",
"J-FT-FT-C-03-18C",
"J-DGXDBO-JJM-259-XCZ",
"J-DGXDBO-JJM-257-XCJ",
"J-DGXDBO-JJM-257-DSG",
"J-DGXDBO-JJM-257-YZJ",
"J-ZZ-SH-362070H-18C",
"J-SSBF-YGJ-BW2005-CTG",
"J-SSBF-YGJ-BW2006-CTG",
"J-ZZ-SH-362086-18C",
"J-MSG-ZGX-FY-710-18C",
"J-MSG-ZGX-FY-515-CTG",
"J-MSG-ZGX-FY-723-18C",
"J-MSG-ZGX-FY-866-ZZJ",
"J-MSG-ZGX-FY-10-DSG",
"J-MSG-ZGX-FY12-CJTZ",
"J-MSG-ZGX-FY-515-CTG-1",
"J-MSG-ZGX-FY-06-2CY",
"J-MSG-ZGX-FY-13-CZ",
"J-MT-MWY-C1204-CY",
"J-MBL-FK-R-9803-18C",
"J-MBL-FK-R-9002B-18C",
"J-MBL-FK-26-CTG",
"J-MBL-FK-33-CTG",
"J-MBL-FK-8077-YZJ-1",
"J-MBL-FK-203-DSG",
"J-MBL-FK-203-CJ",
"J-MBL-FK-F800-15-CZ",
"J-EK-EK-16-18C"]

def get(url):
    return requests.get(domain+url,headers=headers,timeout=30)




jsonfile = open('goods_simple.json', 'w', encoding='utf-8')
index0 = 0
big_obj = []
err_link = []
for keykey in key_li:
    print(keykey)
    response = get('/search?kw='+keykey)
    print('页开始第几页：',index0)
    # while True:
    response = response.content.decode()
    html = etree.HTML(response)

    # print(html)
    node_list = html.xpath('//div[@class="all_de_clist"]/ul/li')


    for goods_index,goods in enumerate(node_list):

        obj = {}

        obj["sale_link_all"] = domain+str(goods.xpath('./a[1]/@href')[0])  # 销售网址
        obj["style"] = goods.xpath('./a[2]/div/h3/text()')[0].split(' |')[0]  # 风格

        sale_link = goods.xpath('./a[1]/@href')[0]  # 销售网址
        response_detail_origin = get(sale_link)
        try:
            response_detail = response_detail_origin.content.decode()
            detail = etree.HTML(response_detail)
        except:
            print(keykey,'orror------------')
            # err_link.append(obj['sale_link'])
        obj["brand"] = detail.xpath('//span[@class="brand_name fl"]/text()')[0]  # 品牌
        obj["name"] = detail.xpath('//div[@class="top_r fr"]/h3/text()')[0]  # 产品名称


        # 获取对应的产品的规格、型号、颜色、编码、价格

        goods_json = re.findall(r'var goods_list =(.*?);', response_detail)
        goods_json_arr = []
        if len(goods_json):
            try:
                for goods_item in goods_json:
                    item = json.loads(goods_item)
                    for key in item:
                        if keykey==item[key]['code']:
                            obj['size'] = key
                            obj['sku'] = keykey
                            obj['market_price'] = item[key]['market_price']
                            obj['price'] = item[key]['price']
                            obj['shop_price'] = item[key]['shop_price']
                            obj['supply_price'] = item[key]['supply_price']

            except:
                err_link.append(sale_link)

        big_obj.append(obj)

    if index0 == len(key_li)-1:
        print(big_obj)
        # 大
        big_strs = json.dumps(big_obj, ensure_ascii=False)
        jsonfile.write(big_strs)
        jsonfile.close()
        break
    index0 = index0+1

