def extract_example_json_table(request, responses):
    # Get request body (if exists)
    req_body = None
    if request:
        if 'body' in request and request['body'].get('mode') == 'raw':
            req_body = request['body']['raw']
    # Get response bodies
    resp_success = None
    resp_error = None
    for resp in responses:
        if str(resp.get('code', '')) == '200' or resp.get('status', '').lower() == 'ok':
            resp_success = resp.get('body')
        elif str(resp.get('code', '')) in ['400', '404'] or 'error' in resp.get('name', '').lower():
            resp_error = resp.get('body')
    rows = [
        ["Example JSON Request Body"],
        [req_body or ""],
        ["JSON Body Response Success"],
        [resp_success or ""],
        ["JSON Body Response Error "],
        [resp_error or ""]
    ]
    return {
        "rows": rows,
        "header_rows": [0, 2, 4],
        "special_rows": [1, 3, 5]
    }

def extract_parameters_table(request):
    # Try to extract query params
    params = []
    if request:
        url = request.get('url', {})
        query = url.get('query', [])
        if isinstance(query, list):
            for q in query:
                params.append([
                    q.get('key', ''),
                    '', '', '',
                    q.get('description', '') or ''
                ])
    if not params:
        params = [[]]
    return {
        "header": ["Parameters", "Data Type", "Length", "Mandatory", "Description"],
        "rows": params
    }

def extract_result_table(responses):
    # Try to extract top-level keys from first 200/OK response
    import json as _json
    for resp in responses:
        if str(resp.get('code', '')) == '200' or resp.get('status', '').lower() == 'ok':
            try:
                body = resp.get('body')
                if body:
                    data = _json.loads(body)
                    if isinstance(data, dict):
                        rows = [[k, ""] for k in data.keys()]
                        if rows:
                            return {"header": ["Field", "Description"], "rows": rows}
            except Exception:
                pass
    return {"header": ["Field", "Description"], "rows": [[]]}

def extract_headers_table(request):
    # Only extract headers from the request
    headers = []
    if request and 'header' in request:
        for h in request['header']:
            headers.append([h.get('key', ''), h.get('value', '')])
    if not headers:
        headers = [[]]
    return {
        "header": ["Header", "Value"],
        "rows": headers
    }

def convert_postman_item(item):
    # Folder
    if 'item' in item:
        return {
            "name": item['name'],
            "items": [convert_postman_item(child) for child in item['item']]
        }
    # API
    else:
        request = item.get('request')
        responses = item.get('response', [])
        # Check for Authorization header in request or response
        has_auth = False
        # Check request headers
        if request and 'header' in request:
            for h in request['header']:
                if h.get('key', '').lower() == 'authorization':
                    has_auth = True
                    break
        # Check response headers if not found in request
        if not has_auth:
            for resp in responses:
                if 'header' in resp:
                    for h in resp['header']:
                        if h.get('key', '').lower() == 'authorization':
                            has_auth = True
                            break
                if has_auth:
                    break

        api = {
            "service_title": item['name'],
            "service_table": {"header": ["Nama Service", "Fungsi"], "rows": [[item['name'], ""]]},
            "http_request": {"header": ["Method", "URL/Endpoint"], "rows": [[request['method'], request['url']['raw']]]} if request else {"header": ["Method", "URL/Endpoint"], "rows": [[]]},
            "parameters_table": extract_parameters_table(request),
            "result_table": {
                "header": ["Field", "Description"],
                "rows": [
                    ["status", "Representasi dari hasil request API (true/false)"],
                    ["message", "Deskripsi atau keterangan sesuai dengan response code yang dikirim server"],
                    ["data", f"Representasi pengambilan data dari request {item['name']}"],
                    ["paging", "Memberikan informasi terkait current page, total page, size, total data"]
                ]
            },
            "example_json_table": extract_example_json_table(request, responses),
            "headers_table": extract_headers_table(request)
        }
        if has_auth:
            api["authorization_desc"] = "Untuk mengakses endpoint ini, pengguna harus memiliki token akses yang valid. Token berlaku selama 12 jam"
            api["authorization_table"] = {
                "header": ["Authorization", "Bearer"],
                "rows": [["POST", "ey..."]]
            }
        return {"name": item['name'], "api": api}
