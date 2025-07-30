class WordTemplateData:
    items = [
    {
        "name": "Audit Trial",
        "items": [
            {
                "name": "Log Activity",
                "items": [
                    {
                        "name": "Get All",
                        "api": {
                            "service_title": "Get All",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Get All",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "GET",
                                        "{{baseUrl}}/log-activities"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "keyword",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "userId",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "activity",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "startDate",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "endDate",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ]
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        ""
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Ok\",\n    \"data\": [\n        {\n            \"id\": \"PFE2UGFG-gTe-fmhtqfTZg==\",\n            \"user\": {\n                \"id\": 1,\n                \"email\": \"robot123@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 100,\n                    \"name\": \"Staf Kerjasama Usaha Pusat \",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 1,\n                    \"nik\": \"392485943498\",\n                    \"name\": \"Robot 123\",\n                    \"detailAddress\": {\n                        \"address\": \"Bandung\",\n                        \"province\": {\n                            \"id\": 75,\n                            \"name\": \"GORONTALO\"\n                        },\n                        \"regency\": {\n                            \"id\": 7502,\n                            \"name\": \"KAB. BOALEMO\"\n                        },\n                        \"district\": {\n                            \"id\": 750206,\n                            \"name\": \"Botumoito\"\n                        },\n                        \"postalCode\": \"43242432\"\n                    },\n                    \"phone\": \"08123921894\",\n                    \"taxNumber\": \"12039120349\",\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Melakukan Approval Contract\",\n            \"url\": \"/v1/contracts/approve/143\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-05T03:07:26.435+00:00\"\n        },\n        {\n            \"id\": \"YIXpJ7oIrw1TVIKJIDAUrg==\",\n            \"user\": {\n                \"id\": 1,\n                \"email\": \"robot123@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 100,\n                    \"name\": \"Staf Kerjasama Usaha Pusat \",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 1,\n                    \"nik\": \"392485943498\",\n                    \"name\": \"Robot 123\",\n                    \"detailAddress\": {\n                        \"address\": \"Bandung\",\n                        \"province\": {\n                            \"id\": 75,\n                            \"name\": \"GORONTALO\"\n                        },\n                        \"regency\": {\n                            \"id\": 7502,\n                            \"name\": \"KAB. BOALEMO\"\n                        },\n                        \"district\": {\n                            \"id\": 750206,\n                            \"name\": \"Botumoito\"\n                        },\n                        \"postalCode\": \"43242432\"\n                    },\n                    \"phone\": \"08123921894\",\n                    \"taxNumber\": \"12039120349\",\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Memilih Opsi Pembayaran\",\n            \"url\": \"/v1/payments\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-05T02:48:45.923+00:00\"\n        },\n        {\n            \"id\": \"0BcIlhVGSnqDTAsldaUmaQ==\",\n            \"user\": {\n                \"id\": 1,\n                \"email\": \"robot123@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 100,\n                    \"name\": \"Staf Kerjasama Usaha Pusat \",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 1,\n                    \"nik\": \"392485943498\",\n                    \"name\": \"Robot 123\",\n                    \"detailAddress\": {\n                        \"address\": \"Bandung\",\n                        \"province\": {\n                            \"id\": 75,\n                            \"name\": \"GORONTALO\"\n                        },\n                        \"regency\": {\n                            \"id\": 7502,\n                            \"name\": \"KAB. BOALEMO\"\n                        },\n                        \"district\": {\n                            \"id\": 750206,\n                            \"name\": \"Botumoito\"\n                        },\n                        \"postalCode\": \"43242432\"\n                    },\n                    \"phone\": \"08123921894\",\n                    \"taxNumber\": \"12039120349\",\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Mengunggah dokumen\",\n            \"url\": \"/v1/submissions/upload-document/422\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-03T04:14:08.365+00:00\"\n        },\n        {\n            \"id\": \"yyRIDNq_u7ezxcpYeTDvdg==\",\n            \"user\": {\n                \"id\": 647,\n                \"email\": \"antonwowo@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 114,\n                    \"name\": \"Direktur Keuangan, TI dan Management Risiko - Kantor Pusat\",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 618,\n                    \"nik\": \"849304\",\n                    \"name\": \"Anton Wowo\",\n                    \"detailAddress\": {\n                        \"address\": null,\n                        \"province\": null,\n                        \"regency\": null,\n                        \"district\": null,\n                        \"postalCode\": null\n                    },\n                    \"phone\": \"0812345678\",\n                    \"taxNumber\": null,\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Melakukan update approval step\",\n            \"url\": \"/v1/approval-steps/227\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-03T03:55:49.519+00:00\"\n        },\n        {\n            \"id\": \"e0trj6dbRSrfQsq9vo0yuA==\",\n            \"user\": {\n                \"id\": 1,\n                \"email\": \"robot123@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 100,\n                    \"name\": \"Staf Kerjasama Usaha Pusat \",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 1,\n                    \"nik\": \"392485943498\",\n                    \"name\": \"Robot 123\",\n                    \"detailAddress\": {\n                        \"address\": \"Bandung\",\n                        \"province\": {\n                            \"id\": 75,\n                            \"name\": \"GORONTALO\"\n                        },\n                        \"regency\": {\n                            \"id\": 7502,\n                            \"name\": \"KAB. BOALEMO\"\n                        },\n                        \"district\": {\n                            \"id\": 750206,\n                            \"name\": \"Botumoito\"\n                        },\n                        \"postalCode\": \"43242432\"\n                    },\n                    \"phone\": \"08123921894\",\n                    \"taxNumber\": \"12039120349\",\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Membuat approval step\",\n            \"url\": \"/v1/approval-steps\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-03T03:39:02.823+00:00\"\n        },\n        {\n            \"id\": \"Ypn4LZX089-rH6wzWNDCpw==\",\n            \"user\": {\n                \"id\": 1,\n                \"email\": \"robot123@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 100,\n                    \"name\": \"Staf Kerjasama Usaha Pusat \",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 1,\n                    \"nik\": \"392485943498\",\n                    \"name\": \"Robot 123\",\n                    \"detailAddress\": {\n                        \"address\": \"Bandung\",\n                        \"province\": {\n                            \"id\": 75,\n                            \"name\": \"GORONTALO\"\n                        },\n                        \"regency\": {\n                            \"id\": 7502,\n                            \"name\": \"KAB. BOALEMO\"\n                        },\n                        \"district\": {\n                            \"id\": 750206,\n                            \"name\": \"Botumoito\"\n                        },\n                        \"postalCode\": \"43242432\"\n                    },\n                    \"phone\": \"08123921894\",\n                    \"taxNumber\": \"12039120349\",\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Mengunggah dokumen\",\n            \"url\": \"/v1/submissions/upload-document/422\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-03T03:19:27.826+00:00\"\n        },\n        {\n            \"id\": \"j7R4UucJN3IXxQqkB_yoiQ==\",\n            \"user\": {\n                \"id\": 1,\n                \"email\": \"robot123@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 100,\n                    \"name\": \"Staf Kerjasama Usaha Pusat \",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 1,\n                    \"nik\": \"392485943498\",\n                    \"name\": \"Robot 123\",\n                    \"detailAddress\": {\n                        \"address\": \"Bandung\",\n                        \"province\": {\n                            \"id\": 75,\n                            \"name\": \"GORONTALO\"\n                        },\n                        \"regency\": {\n                            \"id\": 7502,\n                            \"name\": \"KAB. BOALEMO\"\n                        },\n                        \"district\": {\n                            \"id\": 750206,\n                            \"name\": \"Botumoito\"\n                        },\n                        \"postalCode\": \"43242432\"\n                    },\n                    \"phone\": \"08123921894\",\n                    \"taxNumber\": \"12039120349\",\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Membuat berita acara\",\n            \"url\": \"/v1/news-events\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-03T03:17:11.441+00:00\"\n        },\n        {\n            \"id\": \"S5LtRmOt5ztg_8r4Ih5YzQ==\",\n            \"user\": {\n                \"id\": 1,\n                \"email\": \"robot123@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 100,\n                    \"name\": \"Staf Kerjasama Usaha Pusat \",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 1,\n                    \"nik\": \"392485943498\",\n                    \"name\": \"Robot 123\",\n                    \"detailAddress\": {\n                        \"address\": \"Bandung\",\n                        \"province\": {\n                            \"id\": 75,\n                            \"name\": \"GORONTALO\"\n                        },\n                        \"regency\": {\n                            \"id\": 7502,\n                            \"name\": \"KAB. BOALEMO\"\n                        },\n                        \"district\": {\n                            \"id\": 750206,\n                            \"name\": \"Botumoito\"\n                        },\n                        \"postalCode\": \"43242432\"\n                    },\n                    \"phone\": \"08123921894\",\n                    \"taxNumber\": \"12039120349\",\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Melakukan reset approval step\",\n            \"url\": \"/v1/approval-steps/reset\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-02T08:17:46.194+00:00\"\n        },\n        {\n            \"id\": \"c_6UgByKOcvt5xy4taLz6A==\",\n            \"user\": {\n                \"id\": 1,\n                \"email\": \"robot123@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 100,\n                    \"name\": \"Staf Kerjasama Usaha Pusat \",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 1,\n                    \"nik\": \"392485943498\",\n                    \"name\": \"Robot 123\",\n                    \"detailAddress\": {\n                        \"address\": \"Bandung\",\n                        \"province\": {\n                            \"id\": 75,\n                            \"name\": \"GORONTALO\"\n                        },\n                        \"regency\": {\n                            \"id\": 7502,\n                            \"name\": \"KAB. BOALEMO\"\n                        },\n                        \"district\": {\n                            \"id\": 750206,\n                            \"name\": \"Botumoito\"\n                        },\n                        \"postalCode\": \"43242432\"\n                    },\n                    \"phone\": \"08123921894\",\n                    \"taxNumber\": \"12039120349\",\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Melakukan reset approval step\",\n            \"url\": \"/v1/approval-steps/reset\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-02T08:17:18.811+00:00\"\n        },\n        {\n            \"id\": \"BFdJSIyMLJThuT54LA1EDg==\",\n            \"user\": {\n                \"id\": 1,\n                \"email\": \"robot123@gmail.com\",\n                \"usingSso\": false,\n                \"ssoName\": null,\n                \"isVerified\": false,\n                \"type\": null,\n                \"status\": \"ACTIVE\",\n                \"level\": \"ADMIN\",\n                \"note\": null,\n                \"role\": {\n                    \"id\": 100,\n                    \"name\": \"Staf Kerjasama Usaha Pusat \",\n                    \"description\": null,\n                    \"users\": null\n                },\n                \"profile\": {\n                    \"id\": 1,\n                    \"nik\": \"392485943498\",\n                    \"name\": \"Robot 123\",\n                    \"detailAddress\": {\n                        \"address\": \"Bandung\",\n                        \"province\": {\n                            \"id\": 75,\n                            \"name\": \"GORONTALO\"\n                        },\n                        \"regency\": {\n                            \"id\": 7502,\n                            \"name\": \"KAB. BOALEMO\"\n                        },\n                        \"district\": {\n                            \"id\": 750206,\n                            \"name\": \"Botumoito\"\n                        },\n                        \"postalCode\": \"43242432\"\n                    },\n                    \"phone\": \"08123921894\",\n                    \"taxNumber\": \"12039120349\",\n                    \"branchId\": null\n                }\n            },\n            \"activity\": \"Melakukan reset approval step\",\n            \"url\": \"/v1/approval-steps/reset\",\n            \"ipAddress\": \"172.18.1.11\",\n            \"osInfo\": \"Other null\",\n            \"deviceInfo\": \"Spider\",\n            \"browserInfo\": \"Other null\",\n            \"createdAt\": \"2025-06-02T07:59:08.064+00:00\"\n        }\n    ],\n    \"paging\": {\n        \"currentPage\": 0,\n        \"totalPage\": 78,\n        \"size\": 10,\n        \"totalData\": 779\n    }\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        ""
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    []
                                ]
                            }
                        }
                    },
                    {
                        "name": "Create",
                        "api": {
                            "service_title": "Create",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Create",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "POST",
                                        "{{baseUrl}}/log-activities"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    []
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        "{\r\n    \"userId\": 1,\r\n    \"activity\": \"Membuka Halaman Login\",\r\n    \"url\": \"https://www.google.com/\"\r\n}"
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Log activity created\",\n    \"data\": null,\n    \"paging\": null\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        ""
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    []
                                ]
                            }
                        }
                    },
                    {
                        "name": "Delete",
                        "api": {
                            "service_title": "Delete",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Delete",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "DELETE",
                                        "{{baseUrl}}/log-activities/:id"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    []
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        "{\r\n    \"userId\": null,\r\n    \"activity\": \"Membuka Halaman Login\",\r\n    \"url\": \"https://www.google.com/\"\r\n}"
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Log activity deleted\",\n    \"data\": null,\n    \"paging\": null\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        "{\n    \"status\": false,\n    \"message\": \"Input byte[] should at least have 2 bytes for base64 bytes\",\n    \"data\": \"uri=/v1/log-activities/3\",\n    \"paging\": null\n}"
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    []
                                ]
                            }
                        }
                    }
                ]
            },
            {
                "name": "Log Integration",
                "items": [
                    {
                        "name": "Get All",
                        "api": {
                            "service_title": "Get All",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Get All",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "GET",
                                        "{{baseUrl}}/log-integrations"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "keyword",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "categoryId",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "subCategoryId",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "sortBy",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "sortDirection",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ]
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        ""
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Ok\",\n    \"data\": [\n        {\n            \"id\": 462,\n            \"client\": \"coba\",\n            \"clientUri\": \"https://www.google.com\",\n            \"method\": \"POST\",\n            \"senderUri\": \"/v1/log-integrations\",\n            \"requestBody\": {\n                \"coba\": \"lalala\"\n            },\n            \"responseBody\": {\n                \"message\": \"ok\"\n            },\n            \"headers\": {\n                \"signature\": \"abcdef\"\n            },\n            \"category\": {\n                \"id\": 258,\n                \"parentId\": null,\n                \"name\": \"after terbit invoice\",\n                \"type\": \"integration-tab\",\n                \"value\": \"after-terbit-invoice\",\n                \"sequence\": null,\n                \"year\": null,\n                \"color\": null,\n                \"image\": null\n            },\n            \"subcategory\": {\n                \"id\": 259,\n                \"parentId\": 258,\n                \"name\": \"accru\",\n                \"type\": \"integration-tab\",\n                \"value\": \"accru\",\n                \"sequence\": null,\n                \"year\": null,\n                \"color\": null,\n                \"image\": null\n            },\n            \"invoice\": {\n                \"id\": 86,\n                \"invoiceNumber\": \"001/INV-KU/V/ASDP-2025\",\n                \"orderId\": \"ABC1752224691\"\n            },\n            \"createdAt\": \"2025-07-29T02:30:31.603+00:00\"\n        }\n    ],\n    \"paging\": {\n        \"currentPage\": 0,\n        \"totalPage\": 1,\n        \"size\": 10,\n        \"totalData\": 1\n    }\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        ""
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    []
                                ]
                            }
                        }
                    },
                    {
                        "name": "Get By Id",
                        "api": {
                            "service_title": "Get By Id",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Get By Id",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "GET",
                                        "{{baseUrl}}/log-integrations/:id"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    []
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        ""
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Log integration retrieved successfully\",\n    \"data\": {\n        \"id\": 462,\n        \"client\": \"coba\",\n        \"clientUri\": \"https://www.google.com\",\n        \"method\": \"POST\",\n        \"senderUri\": \"/v1/log-integrations\",\n        \"requestBody\": {\n            \"coba\": \"lalala\"\n        },\n        \"responseBody\": {\n            \"message\": \"ok\"\n        },\n        \"headers\": {\n            \"signature\": \"abcdef\"\n        },\n        \"category\": {\n            \"id\": 258,\n            \"parentId\": null,\n            \"name\": \"after terbit invoice\",\n            \"type\": \"integration-tab\",\n            \"value\": \"after-terbit-invoice\",\n            \"sequence\": null,\n            \"year\": null,\n            \"color\": null,\n            \"image\": null\n        },\n        \"subcategory\": {\n            \"id\": 259,\n            \"parentId\": 258,\n            \"name\": \"accru\",\n            \"type\": \"integration-tab\",\n            \"value\": \"accru\",\n            \"sequence\": null,\n            \"year\": null,\n            \"color\": null,\n            \"image\": null\n        },\n        \"invoice\": {\n            \"id\": 86,\n            \"invoiceNumber\": \"001/INV-KU/V/ASDP-2025\",\n            \"orderId\": \"ABC1752224691\"\n        },\n        \"createdAt\": \"2025-07-29T02:30:31.603+00:00\"\n    },\n    \"paging\": null\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        ""
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    []
                                ]
                            }
                        }
                    },
                    {
                        "name": "Create",
                        "api": {
                            "service_title": "Create",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Create",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "POST",
                                        "{{baseUrl}}/log-integrations"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    []
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        "{\r\n    \"client\": \"coba\",\r\n    \"clientUri\": \"https://www.google.com\",\r\n    \"method\": \"POST\",\r\n    \"requestBody\": {\r\n        \"coba\": \"lalala\"\r\n    },\r\n    \"responseBody\": {\r\n        \"message\": \"ok\"\r\n    },\r\n    \"headers\": {\r\n        \"signature\": \"abcdef\"\r\n    },\r\n    \"invoiceId\": 86,\r\n    \"categoryId\": 258,\r\n    \"subCategoryId\": 259\r\n}"
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Log integration created successfully\",\n    \"data\": null,\n    \"paging\": null\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        ""
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    [
                                        "userId",
                                        "1"
                                    ]
                                ]
                            }
                        }
                    },
                    {
                        "name": "Delete",
                        "api": {
                            "service_title": "Delete",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Delete",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "DELETE",
                                        "{{baseUrl}}/log-integrations/:id"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    []
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        ""
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Log integration deleted successfully\",\n    \"data\": null,\n    \"paging\": null\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        "{\n    \"status\": false,\n    \"message\": \"LogIntegration not found with id: 22\",\n    \"data\": \"uri=/v1/log-integrations/22\",\n    \"paging\": null\n}"
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    []
                                ]
                            }
                        }
                    }
                ]
            },
            {
                "name": "Log Access",
                "items": [
                    {
                        "name": "Get All",
                        "api": {
                            "service_title": "Get All",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Get All",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "GET",
                                        "{{baseUrl}}/log-access"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "keyword",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "userId",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "startDate",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ],
                                    [
                                        "endDate",
                                        "",
                                        "",
                                        "",
                                        ""
                                    ]
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        ""
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Ok\",\n    \"data\": [],\n    \"paging\": {\n        \"currentPage\": 0,\n        \"totalPage\": 8,\n        \"size\": 10,\n        \"totalData\": 76\n    }\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        ""
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    []
                                ]
                            }
                        }
                    },
                    {
                        "name": "Create",
                        "api": {
                            "service_title": "Create",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Create",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "POST",
                                        "{{baseUrl}}/log-access"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    []
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        ""
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Log access created successfully\",\n    \"data\": null,\n    \"paging\": null\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        ""
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    [
                                        "userId",
                                        "1"
                                    ]
                                ]
                            }
                        }
                    },
                    {
                        "name": "Delete",
                        "api": {
                            "service_title": "Delete",
                            "service_table": {
                                "header": [
                                    "Nama Service",
                                    "Fungsi"
                                ],
                                "rows": [
                                    [
                                        "Delete",
                                        ""
                                    ]
                                ]
                            },
                            "http_request": {
                                "header": [
                                    "Method",
                                    "URL/Endpoint"
                                ],
                                "rows": [
                                    [
                                        "DELETE",
                                        "{{baseUrl}}/log-access/:id"
                                    ]
                                ]
                            },
                            "parameters_table": {
                                "header": [
                                    "Parameters",
                                    "Data Type",
                                    "Length",
                                    "Mandatory",
                                    "Description"
                                ],
                                "rows": [
                                    []
                                ]
                            },
                            "result_table": {
                                "header": [
                                    "Field",
                                    "Description"
                                ],
                                "rows": [
                                    [
                                        "status",
                                        ""
                                    ],
                                    [
                                        "message",
                                        ""
                                    ],
                                    [
                                        "data",
                                        ""
                                    ],
                                    [
                                        "paging",
                                        ""
                                    ]
                                ]
                            },
                            "example_json_table": {
                                "rows": [
                                    [
                                        "Example JSON Request Body"
                                    ],
                                    [
                                        ""
                                    ],
                                    [
                                        "JSON Body Response Success"
                                    ],
                                    [
                                        "{\n    \"status\": true,\n    \"message\": \"Log access deleted successfully\",\n    \"data\": null,\n    \"paging\": null\n}"
                                    ],
                                    [
                                        "JSON Body Response Error "
                                    ],
                                    [
                                        "{\n    \"status\": false,\n    \"message\": \"Log access not found with id: 1222\",\n    \"data\": \"uri=/v1/log-access/1222\",\n    \"paging\": null\n}"
                                    ]
                                ],
                                "header_rows": [
                                    0,
                                    2,
                                    4
                                ],
                                "special_rows": [
                                    1,
                                    3,
                                    5
                                ]
                            },
                            "headers_table": {
                                "header": [
                                    "Header",
                                    "Value"
                                ],
                                "rows": [
                                    [
                                        "userId",
                                        "1"
                                    ]
                                ]
                            }
                        }
                    }
                ]
            }
        ]
    },
    {
        "name": "Callback",
        "api": {
            "service_title": "Callback",
            "service_table": {
                "header": [
                    "Nama Service",
                    "Fungsi"
                ],
                "rows": [
                    [
                        "Callback",
                        ""
                    ]
                ]
            },
            "http_request": {
                "header": [
                    "Method",
                    "URL/Endpoint"
                ],
                "rows": [
                    [
                        "POST",
                        "https://api.abcdev.swamedia.xyz/payment-service/v1/receipts/callback"
                    ]
                ]
            },
            "parameters_table": {
                "header": [
                    "Parameters",
                    "Data Type",
                    "Length",
                    "Mandatory",
                    "Description"
                ],
                "rows": [
                    []
                ]
            },
            "result_table": {
                "header": [
                    "Field",
                    "Description"
                ],
                "rows": [
                    [
                        "status",
                        ""
                    ],
                    [
                        "message",
                        ""
                    ],
                    [
                        "data",
                        ""
                    ],
                    [
                        "paging",
                        ""
                    ]
                ]
            },
            "example_json_table": {
                "rows": [
                    [
                        "Example JSON Request Body"
                    ],
                    [
                        "{\r\n  \"accessToken\": \"AhEWfxNVipe+Q0MzyQA1qc+Txi7wBivmByDnCODwkqlfc8lVBu/sX8gOm5LHZVhL9xApojjdvZPf71YjvYdHi7g=\",\r\n  \"merchantCode\": \"MRCN32268309\",\r\n  \"orderId\": \"ABC1752224679\",\r\n  \"paymentCode\": \"8029655356426646\",\r\n  \"paymentLink\": \"\",\r\n  \"paymentBlob\": \"\",\r\n  \"currency\": \"IDR\",\r\n  \"amount\": \"1.110.000\",\r\n  \"adminFee\": \"0\",\r\n  \"paymentRef\": \"3f93fb95-8547-4b94-af1d-eb4281dd2e65\",\r\n  \"paidAt\": \"2025-07-17T06:44:32.000Z\"\r\n}"
                    ],
                    [
                        "JSON Body Response Success"
                    ],
                    [
                        "{\n    \"status\": true,\n    \"message\": \"Callback processed successfully\",\n    \"data\": null,\n    \"paging\": null\n}"
                    ],
                    [
                        "JSON Body Response Error "
                    ],
                    [
                        ""
                    ]
                ],
                "header_rows": [
                    0,
                    2,
                    4
                ],
                "special_rows": [
                    1,
                    3,
                    5
                ]
            },
            "headers_table": {
                "header": [
                    "Header",
                    "Value"
                ],
                "rows": [
                    [
                        "signature",
                        "22f2619405bb4af3a8d35b19bfbd95d8814d854f5f2f158c235f6f9bb1ef2e78999ce593aaa38b7c835708560b394b68a53df41eb72c6ec411f9c01744ae28e6"
                    ],
                    [
                        "timestamp",
                        "2025-07-17T06:44:32.294Z"
                    ]
                ]
            }
        }
    }
]
