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
                                "service_title": "Get All Log Activities",
                                "service_table": {
                                    "header": ["Nama Service", "Fungsi"],
                                    "rows": [["Get All Log Activities", ""]]
                                },
                                "http_request": {
                                    "header": ["Method", "URL/Endpoint"],
                                    "rows": [["GET", "{{baseUrl}}/log-activities"]]
                                },
                                "authorization_desc": "Untuk mengakses endpoint ini, pengguna harus memiliki token akses yang valid.",
                                "authorization_table" : {
                                    "header": ["Authorization", "Bearer"],
                                    "rows": [["POST", "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoxLCJjb2RlIjpudWxsLCJlbWFpbCI6InJvYm90MTIzQGdtYWlsLmNvbSIsInVzaW5nU3NvIjpmYWxzZSwic3NvTmFtZSI6bnVsbCwiaXNWZXJpZmllZCI6ZmFsc2UsInZlcmlmaWVkVG9rZW4iOm51bGwsInZlcmlmaWVkVG9rZW5FeHBpcmVkIjpudWxsLCJ0eXBlIjpudWxsLCJzdGF0dXMiOiJBQ1RJVkUiLCJsZXZlbCI6IkFETUlOIiwibm90ZSI6bnVsbCwicm9sZSI6eyJpZCI6MTAwLCJuYW1lIjoiU3RhZiBLZXJqYXNhbWEgVXNhaGEgUHVzYXQgIiwiZGVzY3JpcHRpb24iOm51bGwsImxldmVsIjp7ImlkIjo4NCwibmFtZSI6Im1ha2VyIiwidHlwZSI6InJvbGUtbGV2ZWwiLCJkZXNjcmlwdGlvbiI6bnVsbCwidmFsdWUiOiJtYWtlciJ9fSwicHJvZmlsZSI6eyJpZCI6MSwibmlrIjoiMzkyNDg1OTQzNDk4IiwibmFtZSI6IlJvYm90IDEyMyIsImRldGFpbEFkZHJlc3MiOnsiYWRkcmVzcyI6IkJhbmR1bmciLCJwcm92aW5jZSI6eyJpZCI6NzUsIm5hbWUiOiJHT1JPTlRBTE8ifSwicmVnZW5jeSI6eyJpZCI6NzUwMiwibmFtZSI6IktBQi4gQk9BTEVNTyJ9LCJkaXN0cmljdCI6eyJpZCI6NzUwMjA2LCJuYW1lIjoiQm90dW1vaXRvIn0sInBvc3RhbENvZGUiOiI0MzI0MjQzMiJ9LCJwaG9uZSI6IjA4MTIzOTIxODk0IiwiaW1hZ2UiOm51bGwsImJyYW5jaCI6eyJpZCI6MiwibmFtZSI6InB1c2F0IiwiY29kZSI6IlBTVCIsInByb2ZpdENlbnRlciI6bnVsbCwiYWRkcmVzcyI6bnVsbCwibGluayI6bnVsbCwidG90YWxTaXplIjpudWxsfSwidGF4TnVtYmVyIjoiMTIwMzkxMjAzNDkiLCJiYW5rIjp7ImlkIjoxLCJuYW1lIjoiQkFOSyBCUkkiLCJjb2RlIjoiMDAyIiwiYWNjb3VudE51bWJlciI6Ijg5MzI0ODkzMjQ5NCIsImFjY291bnROYW1lIjoiUm9ib3QifSwiZ2VuZGVyIjpudWxsLCJwb3NpdGlvbklkIjpudWxsLCJwb3NpdGlvbiI6bnVsbCwic3ViRGl2aXNpb25JZCI6bnVsbCwic3ViRGl2aXNpb24iOm51bGwsImRpdmlzaW9uSWQiOm51bGwsImRpdmlzaW9uIjpudWxsLCJkaXJlY3RvcmF0ZUlkIjpudWxsLCJkaXJlY3RvcmF0ZSI6bnVsbCwiY3VzdG9tZXJJZCI6bnVsbCwicGljTmFtZSI6bnVsbCwicGljUGhvbmUiOm51bGx9LCJ2ZXJpZnlQcm9ncmVzcyI6bnVsbH0sInVzZXJJZCI6MSwic3ViIjoicm9ib3QxMjNAZ21haWwuY29tIiwiaWF0IjoxNzUzODU5MjQ1LCJleHAiOjE3NTM5MDI0NDV9.xluDVDBW2EkXauS23Db6PxVJidwR4y8Hq5s4U3mVMvE"]]
                                },
                                "headers_table": {
                                  "header": ["Header", "Value"],
                                  "rows": [["Authorization", "Bearer ey"]]
                                },
                                "parameters_table": {
                                    "header": ["Parameters", "Data Type", "Length", "Mandatory", "Description"],
                                    "rows": [
                                        ["keyword", "", "", "", "Kata kunci pencarian (opsional)"],
                                        ["userId", "", "", "", "ID Pengguna (opsional)"],
                                        ["activity", "", "", "", "Aktivitas (opsional)"],
                                        ["startDate", "", "", "", "Tanggal mulai (opsional)"],
                                        ["endDate", "", "", "", "Tanggal akhir (opsional)"]
                                    ]
                                },
                                "result_table": {
                                    "header": ["Field", "Description"],
                                    "rows": [
                                        ["status", "Status response (true/false)"],
                                        ["message", "Pesan response"],
                                        ["data", "Array data log aktivitas"],
                                        ["paging", "Informasi paging"]
                                    ]
                                },
                                "example_json_table": {
                                    "rows": [
                                        ["Example JSON Request Body"],
                                        ["{ ... Request Body ... }"],
                                        ["JSON Body Response Success"],
                                        ["{ ...response body... }"],
                                        ["JSON Body Response Error "],
                                        ["{ ...response body Error ... }"]
                                    ],
                                    "header_rows": [0, 2, 4],
                                    "special_rows": [1, 3, 5]
                                }
                            }
                        },
                        {
                            "name": "Create",
                            "api": {
                                "service_title": "Create Log Activity",
                                "service_table": {
                                    "header": ["Nama Service", "Fungsi"],
                                    "rows": [["Create Log Activity", "Membuat log aktivitas baru."]]
                                },
                                "http_request": {
                                    "header": ["Method", "URL/Endpoint"],
                                    "rows": [["POST", "{{baseUrl}}/log-activities"]]
                                },
                                "parameters_table": {
                                    "header": ["Field", "Type", "Description"],
                                    "rows": [
                                        ["userId", "integer", "ID Pengguna"],
                                        ["activity", "string", "Aktivitas"],
                                        ["url", "string", "URL terkait"]
                                    ]
                                },
                                "result_table": {
                                    "header": ["Field", "Description"],
                                    "rows": [
                                        ["status", "Status response (true/false)"],
                                        ["message", "Pesan response"],
                                        ["data", "Data log aktivitas yang dibuat"],
                                        ["paging", "Informasi paging"]
                                    ]
                                },
                                "example_json_table": {
                                    "rows": [
                                        ["Example JSON Request"],
                                        ["{\n  \"userId\": 1,\n  \"activity\": \"Membuka Halaman Login\",\n  \"url\": \"https://www.google.com/\"\n}"],
                                        ["Example JSON Response"],
                                        ["{ ...response body... }"]
                                    ],
                                    "header_rows": [0, 2],
                                    "special_rows": [1, 3]
                                }
                            }
                        },
                        {
                            "name": "Delete",
                            "api": {
                                "service_title": "Delete Log Activity",
                                "service_table": {
                                    "header": ["Nama Service", "Fungsi"],
                                    "rows": [["Delete Log Activity", "Menghapus log aktivitas."]]
                                },
                                "http_request": {
                                    "header": ["Method", "URL/Endpoint"],
                                    "rows": [["DELETE", "{{baseUrl}}/log-activities/:id"]]
                                },
                                "parameters_table": {
                                    "header": ["Field", "Type", "Description"],
                                    "rows": [
                                        ["id", "string", "ID log activity"],
                                        ["userId", "integer", "ID Pengguna (opsional)"],
                                        ["activity", "string", "Aktivitas (opsional)"],
                                        ["url", "string", "URL terkait (opsional)"]
                                    ]
                                },
                                "result_table": {
                                    "header": ["Field", "Description"],
                                    "rows": [
                                        ["status", "Status response (true/false)"],
                                        ["message", "Pesan response"],
                                        ["data", "Data log aktivitas yang dihapus"],
                                        ["paging", "Informasi paging"]
                                    ]
                                },
                                "example_json_table": {
                                    "rows": [
                                        ["Example JSON Request"],
                                        ["{\n  \"userId\": null,\n  \"activity\": \"Membuka Halaman Login\",\n  \"url\": \"https://www.google.com/\"\n}"],
                                        ["Example JSON Response"],
                                        ["{ ...response body... }"]
                                    ],
                                    "header_rows": [0, 2],
                                    "special_rows": [1, 3]
                                }
                            }
                        }
                    ]
                },
                # You can add more folders and APIs here following the same structure
            ]
        }
    ]