class WordTemplateData:
    apis = [
        {
            "service_title": "Generate Access Token",
            "service_table": {
                "header": ["Nama Service", "Fungsi"],
                "rows": [
                    [
                        "Generate Access Token",
                        "API yang digunakan untuk generate clientSecret ..."
                    ]
                ]
            },
            "http_request": {
                "header": ["Method", "URL/Endpoint"],
                "rows": [
                    ["POST", "<context-path>/api/v1/switcher/data-processing/generate/access-token/merchant"]
                ]
            },
            "authorization_desc": "Token ... (belum lebih dari 1 jam).",
            "authorization_table": {
                "header": ["Authorization", "Bearer"],
                "rows": [
                    ["POST", "eyJhbGciOiJIUzI1NiJ9..."]
                ]
            },
            "headers_table": {
                "header": ["Header Key", "Header Value"],
                "rows": [
                    ["Authorization", "Bearer eyJhbGciOiJIUzI1NiJ9..."]
                ]
            },
            "parameters_table": {
                "header": ["Parameters", "Data Type", "Length", "Mandatory", "Description"],
                "rows": [
                    ["clientId", "Text", "50", "Mandatory", "kode client id untuk esb"]
                ]
            },
            "result_table": {
                "header": ["Parameters", "Description"],
                "rows": [
                    ["Status", "Representasi dari hasil request API (true/false)"],
                    ["Message", "Deskripsi ..."],
                    ["Data", "Informasi lengkap ..."],
                    ["Paging", "Informasi paging ..."]
                ]
            },
            "example_json_table": {
                "rows": [
                    ['Example JSON Request Body'],
                    ['{\n  "clientId": "MRCN002-switcher-app"\n}'],
                    ['JSON Response Body Success'],
                    ['{...}'],
                    ['JSON Response Body Error'],
                    ['{...}']
                ],
                "header_rows": [0, 2, 4],
                "special_rows": [1, 3, 5]
            }
        },
        {
            "service_title": "Refresh Token",
            "service_table": {
                "header": ["Nama Service", "Fungsi"],
                "rows": [
                    [
                        "Refresh Token",
                        "API untuk me-refresh token yang sudah ada ..."
                    ]
                ]
            },
            "http_request": {
                "header": ["Method", "URL/Endpoint"],
                "rows": [
                    ["POST", "<context-path>/api/v1/switcher/data-processing/refresh-token"]
                ]
            },
            # No authorization or headers for this API
            "parameters_table": {
                "header": ["Parameters", "Data Type", "Length", "Mandatory", "Description"],
                "rows": [
                    ["refreshToken", "Text", "100", "Mandatory", "refresh token"]
                ]
            },
            "result_table": {
                "header": ["Parameters", "Description"],
                "rows": [
                    ["Status", "true/false"],
                    ["Message", "Deskripsi ..."],
                    ["Data", "Informasi lengkap ..."]
                ]
            },
            "example_json_table": {
                "rows": [
                    ['Example JSON Request Body'],
                    ['{\n  "refreshToken": "..." \n}'],
                    ['JSON Response Body Success'],
                    ['{...}'],
                    ['JSON Response Body Error'],
                    ['{...}']
                ],
                "header_rows": [0, 2, 4],
                "special_rows": [1, 3, 5]
            }
        }
        # Add more APIs as needed...
    ]