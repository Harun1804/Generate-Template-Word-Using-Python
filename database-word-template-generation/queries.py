# queries.py

tables_data = [
    {
        'table_name': 'tb_users',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'nik', 'data_type': 'VARCHAR(50)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'YES', 'description': 'Employee identification number'},
            {'field': 'fullname', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'YES', 'description': 'Full name of the user'},
            {'field': 'email_address', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'YES', 'description': 'Email address of the user'},
            {'field': 'password', 'data_type': 'VARCHAR(255)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'YES', 'description': 'Encrypted password'},
            {'field': 'avatar', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User avatar image path'},
            {'field': 'jabatan', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Job position'},
            {'field': 'departemen', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Department'},
            {'field': 'bagian', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Division'},
            {'field': 'unit', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Unit'},
            {'field': 'id_authority', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Authority identifier'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'phone', 'data_type': 'VARCHAR(20)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'YES', 'description': 'Phone number'}
        ],
        'create_query': '''CREATE TABLE tb_users (
    id SERIAL PRIMARY KEY,
    nik VARCHAR(50),
    fullname VARCHAR(100),
    email_address VARCHAR(100),
    password VARCHAR(255),
    avatar TEXT,
    jabatan VARCHAR(100),
    departemen VARCHAR(100),
    bagian VARCHAR(100),
    unit VARCHAR(100),
    id_authority INT,
    created_date TIMESTAMP,
    created_by VARCHAR(100),
    phone VARCHAR(20)
);''',
        'select_query': 'SELECT * FROM tb_users WHERE email_address = ?;',
        'insert_query': 'INSERT INTO tb_users (nik, fullname, email_address, password, jabatan, departemen, created_date, created_by) VALUES (?, ?, ?, ?, ?, ?, NOW(), ?);',
        'update_query': 'UPDATE tb_users SET fullname = ?, email_address = ?, jabatan = ?, departemen = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_users WHERE id = ?;'
    },
    {
        'table_name': 'tb_roles',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'name', 'data_type': 'VARCHAR(50)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Role name'},
            {'field': 'description', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Role description'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'}
        ],
        'create_query': '''CREATE TABLE tb_roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description TEXT,
    created_by VARCHAR(100),
    created_date TIMESTAMP
);''',
        'select_query': 'SELECT * FROM tb_roles WHERE name = ?;',
        'insert_query': 'INSERT INTO tb_roles (name, description, created_by, created_date) VALUES (?, ?, ?, NOW());',
        'update_query': 'UPDATE tb_roles SET name = ?, description = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_roles WHERE id = ?;'
    },
    {
        'table_name': 'tb_user_role',
        'fields': [
            {'field': 'user_id', 'data_type': 'INT', 'nullable': 'NO', 'key': 'PRI, FOR', 'data_pribadi': 'NO', 'description': 'User identifier, foreign key to tb_users'},
            {'field': 'role_id', 'data_type': 'INT', 'nullable': 'NO', 'key': 'PRI, FOR', 'data_pribadi': 'NO', 'description': 'Role identifier, foreign key to tb_roles'}
        ],
        'create_query': '''CREATE TABLE tb_user_role (
    user_id INT,
    role_id INT,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES tb_users(id),
    FOREIGN KEY (role_id) REFERENCES tb_roles(id)
);''',
        'select_query': 'SELECT * FROM tb_user_role WHERE user_id = ?;',
        'insert_query': 'INSERT INTO tb_user_role (user_id, role_id) VALUES (?, ?);',
        'update_query': 'UPDATE tb_user_role SET role_id = ? WHERE user_id = ? AND role_id = ?;',
        'delete_query': 'DELETE FROM tb_user_role WHERE user_id = ? AND role_id = ?;'
    },
    {
        'table_name': 'tb_menus',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_domain', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Domain identifier'},
            {'field': 'name', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Menu name'},
            {'field': 'icon', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Menu icon'},
            {'field': 'alias', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Menu alias'}
        ],
        'create_query': '''CREATE TABLE tb_menus (
    id SERIAL PRIMARY KEY,
    id_domain INT,
    name VARCHAR(100),
    icon VARCHAR(100),
    alias VARCHAR(100)
);''',
        'select_query': 'SELECT * FROM tb_menus WHERE id_domain = ?;',
        'insert_query': 'INSERT INTO tb_menus (id_domain, name, icon, alias) VALUES (?, ?, ?, ?);',
        'update_query': 'UPDATE tb_menus SET name = ?, icon = ?, alias = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_menus WHERE id = ?;'
    },
    {
        'table_name': 'tb_menu_role',
        'fields': [
            {'field': 'menu_id', 'data_type': 'INT', 'nullable': 'NO', 'key': 'PRI, FOR', 'data_pribadi': 'NO', 'description': 'Menu identifier, foreign key to tb_menus'},
            {'field': 'role_id', 'data_type': 'INT', 'nullable': 'NO', 'key': 'PRI, FOR', 'data_pribadi': 'NO', 'description': 'Role identifier, foreign key to tb_roles'}
        ],
        'create_query': '''CREATE TABLE tb_menu_role (
    menu_id INT,
    role_id INT,
    PRIMARY KEY (menu_id, role_id),
    FOREIGN KEY (menu_id) REFERENCES tb_menus(id),
    FOREIGN KEY (role_id) REFERENCES tb_roles(id)
);''',
        'select_query': 'SELECT * FROM tb_menu_role WHERE role_id = ?;',
        'insert_query': 'INSERT INTO tb_menu_role (menu_id, role_id) VALUES (?, ?);',
        'update_query': 'UPDATE tb_menu_role SET menu_id = ? WHERE menu_id = ? AND role_id = ?;',
        'delete_query': 'DELETE FROM tb_menu_role WHERE menu_id = ? AND role_id = ?;'
    },
    {
        'table_name': 'tb_domain',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'description', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Domain description'},
            {'field': 'id_parent', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Parent domain identifier'},
            {'field': 'param_type', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Parameter type'}
        ],
        'create_query': '''CREATE TABLE tb_domain (
    id SERIAL PRIMARY KEY,
    description TEXT,
    id_parent INT,
    param_type VARCHAR(100)
);''',
        'select_query': 'SELECT * FROM tb_domain WHERE param_type = ?;',
        'insert_query': 'INSERT INTO tb_domain (description, id_parent, param_type) VALUES (?, ?, ?);',
        'update_query': 'UPDATE tb_domain SET description = ?, param_type = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_domain WHERE id = ?;'
    },
    {
        'table_name': 'tb_domain_role',
        'fields': [
            {'field': 'domain_id', 'data_type': 'INT', 'nullable': 'NO', 'key': 'PRI, FOR', 'data_pribadi': 'NO', 'description': 'Domain identifier, foreign key to tb_domain'},
            {'field': 'role_id', 'data_type': 'INT', 'nullable': 'NO', 'key': 'PRI, FOR', 'data_pribadi': 'NO', 'description': 'Role identifier, foreign key to tb_roles'}
        ],
        'create_query': '''CREATE TABLE tb_domain_role (
    domain_id INT,
    role_id INT,
    PRIMARY KEY (domain_id, role_id),
    FOREIGN KEY (domain_id) REFERENCES tb_domain(id),
    FOREIGN KEY (role_id) REFERENCES tb_roles(id)
);''',
        'select_query': 'SELECT * FROM tb_domain_role WHERE role_id = ?;',
        'insert_query': 'INSERT INTO tb_domain_role (domain_id, role_id) VALUES (?, ?);',
        'update_query': 'UPDATE tb_domain_role SET domain_id = ? WHERE domain_id = ? AND role_id = ?;',
        'delete_query': 'DELETE FROM tb_domain_role WHERE domain_id = ? AND role_id = ?;'
    },
    {
        'table_name': 'tb_param',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'description', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Parameter description'},
            {'field': 'id_parent', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Parent parameter identifier'},
            {'field': 'value', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Parameter value'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'}
        ],
        'create_query': '''CREATE TABLE tb_param (
    id SERIAL PRIMARY KEY,
    description TEXT,
    id_parent INT,
    value TEXT,
    created_by VARCHAR(100),
    created_date TIMESTAMP
);''',
        'select_query': 'SELECT * FROM tb_param WHERE id_parent = ?;',
        'insert_query': 'INSERT INTO tb_param (description, id_parent, value, created_by, created_date) VALUES (?, ?, ?, ?, NOW());',
        'update_query': 'UPDATE tb_param SET description = ?, value = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_param WHERE id = ?;'
    },
    {
        'table_name': 'tb_repository',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_param', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Parameter identifier, foreign key to tb_param'},
            {'field': 'file_name', 'data_type': 'VARCHAR(255)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Name of the file'},
            {'field': 'file_type', 'data_type': 'VARCHAR(50)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Type of the file'},
            {'field': 'file_size', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Size of the file in bytes'},
            {'field': 'file_path', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Full path to the file'},
            {'field': 'unlock_expired_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'When the unlock expires'},
            {'field': 'unlock_time', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Unlock time duration'},
            {'field': 'document_id', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Document identifier, foreign key to tb_document'},
            {'field': 'id_schedule', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Schedule identifier'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'licapable', 'data_type': 'BOOLEAN', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'License capable flag'}
        ],
        'create_query': '''CREATE TABLE tb_repository (
    id SERIAL PRIMARY KEY,
    id_param INT,
    file_name VARCHAR(255),
    file_type VARCHAR(50),
    file_size INT,
    file_path TEXT,
    unlock_expired_date TIMESTAMP,
    unlock_time INT,
    document_id INT,
    id_schedule INT,
    created_by VARCHAR(100),
    created_date TIMESTAMP,
    licapable BOOLEAN,
    FOREIGN KEY (id_param) REFERENCES tb_param(id),
    FOREIGN KEY (document_id) REFERENCES tb_document(id)
);''',
        'select_query': 'SELECT * FROM tb_repository WHERE document_id = ?;',
        'insert_query': 'INSERT INTO tb_repository (id_param, file_name, file_type, file_size, file_path, document_id, created_by, created_date) VALUES (?, ?, ?, ?, ?, ?, ?, NOW());',
        'update_query': 'UPDATE tb_repository SET file_name = ?, file_type = ?, file_size = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_repository WHERE id = ?;'
    },
    {
        'table_name': 'tb_document',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_domain', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Domain identifier, foreign key to tb_domain'},
            {'field': 'doc_name', 'data_type': 'VARCHAR(255)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Document name'},
            {'field': 'description', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Document description'},
            {'field': 'report_type', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Type of report'},
            {'field': 'status', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Document status'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'valid_from', 'data_type': 'DATE', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Document validity start date'},
            {'field': 'valid_until', 'data_type': 'DATE', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Document validity end date'},
            {'field': 'unlock_expired_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'When the unlock expires'},
            {'field': 'unlock_time', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Unlock time duration'},
            {'field': 'document_time', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Document timestamp'},
            {'field': 'id_schedule', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Schedule identifier'}
        ],
        'create_query': '''CREATE TABLE tb_document (
    id SERIAL PRIMARY KEY,
    id_domain INT,
    doc_name VARCHAR(255),
    description TEXT,
    report_type INT,
    status INT,
    created_date TIMESTAMP,
    created_by VARCHAR(100),
    valid_from DATE,
    valid_until DATE,
    unlock_expired_date TIMESTAMP,
    unlock_time INT,
    document_time TIMESTAMP,
    id_schedule INT,
    FOREIGN KEY (id_domain) REFERENCES tb_domain(id)
);''',
        'select_query': 'SELECT * FROM tb_document WHERE id_domain = ? AND status = ?;',
        'insert_query': 'INSERT INTO tb_document (id_domain, doc_name, description, report_type, status, created_date, created_by, valid_from, valid_until) VALUES (?, ?, ?, ?, ?, NOW(), ?, ?, ?);',
        'update_query': 'UPDATE tb_document SET doc_name = ?, description = ?, status = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_document WHERE id = ?;'
    },
    {
        'table_name': 'tb_approval',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'document_id', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Document identifier, foreign key to tb_document'},
            {'field': 'process_id', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Process identifier'},
            {'field': 'status', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Approval status'},
            {'field': 'comment', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Approval comment'},
            {'field': 'user_id', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'User identifier, foreign key to tb_users'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'updated_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record update timestamp'},
            {'field': 'last_user_id', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Last user identifier, foreign key to tb_users'},
            {'field': 'last_risk', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Last risk level'}
        ],
        'create_query': '''CREATE TABLE tb_approval (
    id SERIAL PRIMARY KEY,
    document_id INT,
    process_id INT,
    status INT,
    comment TEXT,
    user_id INT,
    created_date TIMESTAMP,
    updated_date TIMESTAMP,
    last_user_id INT,
    last_risk INT,
    FOREIGN KEY (document_id) REFERENCES tb_document(id),
    FOREIGN KEY (user_id) REFERENCES tb_users(id),
    FOREIGN KEY (last_user_id) REFERENCES tb_users(id)
);''',
        'select_query': 'SELECT * FROM tb_approval WHERE document_id = ? AND status = ?;',
        'insert_query': 'INSERT INTO tb_approval (document_id, process_id, status, comment, user_id, created_date) VALUES (?, ?, ?, ?, ?, NOW());',
        'update_query': 'UPDATE tb_approval SET status = ?, comment = ?, updated_date = NOW(), last_user_id = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_approval WHERE id = ?;'
    },
    {
        'table_name': 'tb_risk',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_domain', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Domain identifier, foreign key to tb_domain'},
            {'field': 'id_document', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Document identifier, foreign key to tb_document'},
            {'field': 'objectives', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk objectives'},
            {'field': 'objective_unit', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Unit of objectives measurement'},
            {'field': 'risk_name', 'data_type': 'VARCHAR(255)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Name of the risk'},
            {'field': 'risk_desc', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk description'},
            {'field': 'id_category', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk category identifier'},
            {'field': 'id_risk_source', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk source identifier'},
            {'field': 'mitigation_existing', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Existing mitigation measures'},
            {'field': 'qualitative_impact', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Qualitative impact description'},
            {'field': 'id_linkage', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk linkage identifier'},
            {'field': 'status', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk status'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'strategy', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk management strategy'},
            {'field': 'risk_exposure', 'data_type': 'NUMERIC', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk exposure value'}
        ],
        'create_query': '''CREATE TABLE tb_risk (
    id SERIAL PRIMARY KEY,
    id_domain INT,
    id_document INT,
    objectives TEXT,
    objective_unit TEXT,
    risk_name VARCHAR(255),
    risk_desc TEXT,
    id_category INT,
    id_risk_source INT,
    mitigation_existing TEXT,
    qualitative_impact TEXT,
    id_linkage INT,
    status INT,
    created_date TIMESTAMP,
    strategy TEXT,
    risk_exposure NUMERIC,
    FOREIGN KEY (id_domain) REFERENCES tb_domain(id),
    FOREIGN KEY (id_document) REFERENCES tb_document(id)
);''',
        'select_query': 'SELECT * FROM tb_risk WHERE id_domain = ? AND status = ?;',
        'insert_query': 'INSERT INTO tb_risk (id_domain, id_document, objectives, risk_name, risk_desc, id_category, created_date, strategy) VALUES (?, ?, ?, ?, ?, ?, NOW(), ?);',
        'update_query': 'UPDATE tb_risk SET risk_name = ?, risk_desc = ?, status = ?, strategy = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_risk WHERE id = ?;'
    },
    {
        'table_name': 'tb_risk_detail',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_risk', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Risk identifier, foreign key to tb_risk'},
            {'field': 'id_level_likelihood', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Likelihood level identifier, foreign key to tb_param'},
            {'field': 'id_level_impact', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Impact level identifier, foreign key to tb_param'},
            {'field': 'risk_level', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk level value'},
            {'field': 'target_likelihood', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Target likelihood value'},
            {'field': 'target_impact', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Target impact value'},
            {'field': 'justification_likelihood', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Justification for likelihood assessment'},
            {'field': 'justification_impact', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Justification for impact assessment'},
            {'field': 'id_risk_owner', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Risk owner identifier, foreign key to tb_users'},
            {'field': 'desc_risk_level', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Description of risk level'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'quarter', 'data_type': 'VARCHAR(10)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Quarter period'},
            {'field': 'target_likelihood_value', 'data_type': 'NUMERIC', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Target likelihood numeric value'},
            {'field': 'target_impact_value', 'data_type': 'NUMERIC', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Target impact numeric value'},
            {'field': 'target_exposure', 'data_type': 'NUMERIC', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Target exposure value'}
        ],
        'create_query': '''CREATE TABLE tb_risk_detail (
    id SERIAL PRIMARY KEY,
    id_risk INT,
    id_level_likelihood INT,
    id_level_impact INT,
    risk_level INT,
    target_likelihood INT,
    target_impact INT,
    justification_likelihood TEXT,
    justification_impact TEXT,
    id_risk_owner INT,
    desc_risk_level TEXT,
    created_date TIMESTAMP,
    quarter VARCHAR(10),
    target_likelihood_value NUMERIC,
    target_impact_value NUMERIC,
    target_exposure NUMERIC,
    FOREIGN KEY (id_risk) REFERENCES tb_risk(id),
    FOREIGN KEY (id_level_likelihood) REFERENCES tb_param(id),
    FOREIGN KEY (id_level_impact) REFERENCES tb_param(id),
    FOREIGN KEY (id_risk_owner) REFERENCES tb_users(id)
);''',
        'select_query': 'SELECT * FROM tb_risk_detail WHERE id_risk = ? AND quarter = ?;',
        'insert_query': 'INSERT INTO tb_risk_detail (id_risk, id_level_likelihood, id_level_impact, risk_level, id_risk_owner, quarter, created_date) VALUES (?, ?, ?, ?, ?, ?, NOW());',
        'update_query': 'UPDATE tb_risk_detail SET risk_level = ?, target_likelihood = ?, target_impact = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_risk_detail WHERE id = ?;'
    },
    {
        'table_name': 'tb_risk_universe',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_category', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Category identifier, foreign key to tb_param'},
            {'field': 'risk_universe_name', 'data_type': 'VARCHAR(255)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk universe name'},
            {'field': 'risk_universe_desc', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Risk universe description'},
            {'field': 'id_likelihood', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Likelihood identifier, foreign key to tb_param'},
            {'field': 'id_impact', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Impact identifier, foreign key to tb_param'},
            {'field': 'effective_mitigation', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Effective mitigation measures'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'}
        ],
        'create_query': '''CREATE TABLE tb_risk_universe (
    id SERIAL PRIMARY KEY,
    id_category INT,
    risk_universe_name VARCHAR(255),
    risk_universe_desc TEXT,
    id_likelihood INT,
    id_impact INT,
    effective_mitigation TEXT,
    created_by VARCHAR(100),
    created_date TIMESTAMP,
    FOREIGN KEY (id_category) REFERENCES tb_param(id),
    FOREIGN KEY (id_likelihood) REFERENCES tb_param(id),
    FOREIGN KEY (id_impact) REFERENCES tb_param(id)
);''',
        'select_query': 'SELECT * FROM tb_risk_universe WHERE id_category = ?;',
        'insert_query': 'INSERT INTO tb_risk_universe (id_category, risk_universe_name, risk_universe_desc, id_likelihood, id_impact, created_by, created_date) VALUES (?, ?, ?, ?, ?, ?, NOW());',
        'update_query': 'UPDATE tb_risk_universe SET risk_universe_name = ?, risk_universe_desc = ?, effective_mitigation = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_risk_universe WHERE id = ?;'
    },
    {
        'table_name': 'tb_indicator',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'indicator_desc', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Indicator description'},
            {'field': 'lower_limit', 'data_type': 'NUMERIC', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Lower limit value'},
            {'field': 'upper_limit', 'data_type': 'NUMERIC', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Upper limit value'},
            {'field': 'indicator_type', 'data_type': 'VARCHAR(50)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Type of indicator'},
            {'field': 'trend', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Trend information'},
            {'field': 'unit', 'data_type': 'VARCHAR(20)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Unit of measurement'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'}
        ],
        'create_query': '''CREATE TABLE tb_indicator (
    id SERIAL PRIMARY KEY,
    indicator_desc TEXT,
    lower_limit NUMERIC,
    upper_limit NUMERIC,
    indicator_type VARCHAR(50),
    trend TEXT,
    unit VARCHAR(20),
    created_date TIMESTAMP,
    created_by VARCHAR(100)
);''',
        'select_query': 'SELECT * FROM tb_indicator WHERE indicator_type = ?;',
        'insert_query': 'INSERT INTO tb_indicator (indicator_desc, lower_limit, upper_limit, indicator_type, unit, created_date, created_by) VALUES (?, ?, ?, ?, ?, NOW(), ?);',
        'update_query': 'UPDATE tb_indicator SET indicator_desc = ?, lower_limit = ?, upper_limit = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_indicator WHERE id = ?;'
    },
    {
        'table_name': 'tb_risk_governance',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_risk', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Risk identifier, foreign key to tb_risk'},
            {'field': 'action', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Governance action'},
            {'field': 'uic', 'data_type': 'VARCHAR(50)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Unit in charge'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'}
        ],
        'create_query': '''CREATE TABLE tb_risk_governance (
    id SERIAL PRIMARY KEY,
    id_risk INT,
    action TEXT,
    uic VARCHAR(50),
    created_date TIMESTAMP,
    created_by VARCHAR(100),
    FOREIGN KEY (id_risk) REFERENCES tb_risk(id)
);''',
        'select_query': 'SELECT * FROM tb_risk_governance WHERE id_risk = ?;',
        'insert_query': 'INSERT INTO tb_risk_governance (id_risk, action, uic, created_date, created_by) VALUES (?, ?, ?, NOW(), ?);',
        'update_query': 'UPDATE tb_risk_governance SET action = ?, uic = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_risk_governance WHERE id = ?;'
    },
    {
        'table_name': 'tb_risk_governance_indicator',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_governance', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Governance identifier, foreign key to tb_risk_governance'},
            {'field': 'id_indicator', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Indicator identifier, foreign key to tb_indicator'},
            {'field': 'indicator_value', 'data_type': 'NUMERIC', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Indicator value'},
            {'field': 'indicator_level', 'data_type': 'VARCHAR(50)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Indicator level'}
        ],
        'create_query': '''CREATE TABLE tb_risk_governance_indicator (
    id SERIAL PRIMARY KEY,
    id_governance INT,
    id_indicator INT,
    indicator_value NUMERIC,
    indicator_level VARCHAR(50),
    FOREIGN KEY (id_governance) REFERENCES tb_risk_governance(id),
    FOREIGN KEY (id_indicator) REFERENCES tb_indicator(id)
);''',
        'select_query': 'SELECT * FROM tb_risk_governance_indicator WHERE id_governance = ?;',
        'insert_query': 'INSERT INTO tb_risk_governance_indicator (id_governance, id_indicator, indicator_value, indicator_level) VALUES (?, ?, ?, ?);',
        'update_query': 'UPDATE tb_risk_governance_indicator SET indicator_value = ?, indicator_level = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_risk_governance_indicator WHERE id = ?;'
    },
    {
        'table_name': 'tb_likelihood',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_domain', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Domain identifier, foreign key to tb_domain'},
            {'field': 'likelihood_desc', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Likelihood description'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'year', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Year'},
            {'field': 'status', 'data_type': 'BOOLEAN', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Status flag'}
        ],
        'create_query': '''CREATE TABLE tb_likelihood (
    id SERIAL PRIMARY KEY,
    id_domain INT,
    likelihood_desc TEXT,
    created_date TIMESTAMP,
    created_by VARCHAR(100),
    year INT,
    status BOOLEAN,
    FOREIGN KEY (id_domain) REFERENCES tb_domain(id)
);''',
        'select_query': 'SELECT * FROM tb_likelihood WHERE id_domain = ? AND year = ?;',
        'insert_query': 'INSERT INTO tb_likelihood (id_domain, likelihood_desc, created_date, created_by, year, status) VALUES (?, ?, NOW(), ?, ?, ?);',
        'update_query': 'UPDATE tb_likelihood SET likelihood_desc = ?, status = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_likelihood WHERE id = ?;'
    },
    {
        'table_name': 'tb_impact',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_domain', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Domain identifier, foreign key to tb_domain'},
            {'field': 'impact_type', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Type of impact'},
            {'field': 'impact_desc', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Impact description'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'year', 'data_type': 'INT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Year'},
            {'field': 'status', 'data_type': 'BOOLEAN', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Status flag'}
        ],
        'create_query': '''CREATE TABLE tb_impact (
    id SERIAL PRIMARY KEY,
    id_domain INT,
    impact_type TEXT,
    impact_desc TEXT,
    created_date TIMESTAMP,
    created_by VARCHAR(100),
    year INT,
    status BOOLEAN,
    FOREIGN KEY (id_domain) REFERENCES tb_domain(id)
);''',
        'select_query': 'SELECT * FROM tb_impact WHERE id_domain = ? AND year = ?;',
        'insert_query': 'INSERT INTO tb_impact (id_domain, impact_type, impact_desc, created_date, created_by, year, status) VALUES (?, ?, ?, NOW(), ?, ?, ?);',
        'update_query': 'UPDATE tb_impact SET impact_type = ?, impact_desc = ?, status = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_impact WHERE id = ?;'
    },
    {
        'table_name': 'tb_pic',
        'fields': [
            {'field': 'activity_id', 'data_type': 'INT', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Activity identifier, part of composite primary key'},
            {'field': 'nik', 'data_type': 'VARCHAR(50)', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'YES', 'description': 'Employee identification number, part of composite primary key'},
            {'field': 'name', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'YES', 'description': 'Person in charge name'},
            {'field': 'position', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Position or role'},
            {'field': 'email', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'YES', 'description': 'Email address'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'phone', 'data_type': 'VARCHAR(20)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'YES', 'description': 'Phone number'}
        ],
        'create_query': '''CREATE TABLE tb_pic (
    activity_id INT,
    nik VARCHAR(50),
    name VARCHAR(100),
    position VARCHAR(100),
    email VARCHAR(100),
    created_date TIMESTAMP,
    created_by VARCHAR(100),
    phone VARCHAR(20),
    PRIMARY KEY (activity_id, nik)
);''',
        'select_query': 'SELECT * FROM tb_pic WHERE activity_id = ?;',
        'insert_query': 'INSERT INTO tb_pic (activity_id, nik, name, position, email, created_date, created_by, phone) VALUES (?, ?, ?, ?, ?, NOW(), ?, ?);',
        'update_query': 'UPDATE tb_pic SET name = ?, position = ?, email = ?, phone = ? WHERE activity_id = ? AND nik = ?;',
        'delete_query': 'DELETE FROM tb_pic WHERE activity_id = ? AND nik = ?;'
    },
    {
        'table_name': 'tb_mitigation_plan',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_risk', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Risk identifier, foreign key to tb_risk'},
            {'field': 'mitigation_name', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Name of the mitigation plan'},
            {'field': 'cost', 'data_type': 'NUMERIC', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Cost of mitigation'},
            {'field': 'obstacles', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Obstacles to implementation'},
            {'field': 'obstacle_impact', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Impact of obstacles'},
            {'field': 'lesson_learned', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Lessons learned'},
            {'field': 'target_start', 'data_type': 'DATE', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Target start date'},
            {'field': 'target_end', 'data_type': 'DATE', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Target end date'},
            {'field': 'action', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Action plan'},
            {'field': 'success_point', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Success criteria'},
            {'field': 'output', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Expected output'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'}
        ],
        'create_query': '''CREATE TABLE tb_mitigation_plan (
    id SERIAL PRIMARY KEY,
    id_risk INT,
    mitigation_name TEXT,
    cost NUMERIC,
    obstacles TEXT,
    obstacle_impact TEXT,
    lesson_learned TEXT,
    target_start DATE,
    target_end DATE,
    action TEXT,
    success_point TEXT,
    output TEXT,
    created_by VARCHAR(100),
    created_date TIMESTAMP,
    FOREIGN KEY (id_risk) REFERENCES tb_risk(id)
);''',
        'select_query': 'SELECT * FROM tb_mitigation_plan WHERE id_risk = ?;',
        'insert_query': 'INSERT INTO tb_mitigation_plan (id_risk, mitigation_name, cost, target_start, target_end, action, created_by, created_date) VALUES (?, ?, ?, ?, ?, ?, ?, NOW());',
        'update_query': 'UPDATE tb_mitigation_plan SET mitigation_name = ?, cost = ?, action = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_mitigation_plan WHERE id = ?;'
    },
    {
        'table_name': 'tb_mitigation_activity',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'id_mitigation', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Mitigation identifier, foreign key to tb_mitigation_plan'},
            {'field': 'name_activity', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Name of the activity'},
            {'field': 'start_date', 'data_type': 'DATE', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Activity start date'},
            {'field': 'end_date', 'data_type': 'DATE', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Activity end date'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'valid_from', 'data_type': 'DATE', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Validity start date'},
            {'field': 'valid_until', 'data_type': 'DATE', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Validity end date'}
        ],
        'create_query': '''CREATE TABLE tb_mitigation_activity (
    id SERIAL PRIMARY KEY,
    id_mitigation INT,
    name_activity TEXT,
    start_date DATE,
    end_date DATE,
    created_by VARCHAR(100),
    created_date TIMESTAMP,
    valid_from DATE,
    valid_until DATE,
    FOREIGN KEY (id_mitigation) REFERENCES tb_mitigation_plan(id)
);''',
        'select_query': 'SELECT * FROM tb_mitigation_activity WHERE id_mitigation = ?;',
        'insert_query': 'INSERT INTO tb_mitigation_activity (id_mitigation, name_activity, start_date, end_date, created_by, created_date) VALUES (?, ?, ?, ?, ?, NOW());',
        'update_query': 'UPDATE tb_mitigation_activity SET name_activity = ?, start_date = ?, end_date = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_mitigation_activity WHERE id = ?;'
    },
    {
        'table_name': 'tb_mitigation_evaluation',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'mitigation_id', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Mitigation identifier, foreign key to tb_mitigation_plan'},
            {'field': 'domain_id', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Domain identifier, foreign key to tb_domain'},
            {'field': 'id_document', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Document identifier, foreign key to tb_document'},
            {'field': 'notes', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Evaluation notes'},
            {'field': 'action', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Action taken'},
            {'field': 'lesson_learned', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Lessons learned'},
            {'field': 'id_user', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'User identifier, foreign key to tb_users'},
            {'field': 'status', 'data_type': 'VARCHAR(50)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Evaluation status'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'}
        ],
        'create_query': '''CREATE TABLE tb_mitigation_evaluation (
    id SERIAL PRIMARY KEY,
    mitigation_id INT,
    domain_id INT,
    id_document INT,
    notes TEXT,
    action TEXT,
    lesson_learned TEXT,
    id_user INT,
    status VARCHAR(50),
    created_date TIMESTAMP,
    created_by VARCHAR(100),
    FOREIGN KEY (mitigation_id) REFERENCES tb_mitigation_plan(id),
    FOREIGN KEY (id_user) REFERENCES tb_users(id),
    FOREIGN KEY (id_document) REFERENCES tb_document(id)
);''',
        'select_query': 'SELECT * FROM tb_mitigation_evaluation WHERE mitigation_id = ? AND status = ?;',
        'insert_query': 'INSERT INTO tb_mitigation_evaluation (mitigation_id, domain_id, id_document, notes, action, id_user, status, created_date, created_by) VALUES (?, ?, ?, ?, ?, ?, ?, NOW(), ?);',
        'update_query': 'UPDATE tb_mitigation_evaluation SET notes = ?, action = ?, status = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_mitigation_evaluation WHERE id = ?;'
    },
    {
        'table_name': 'tb_mitigation_support',
        'fields': [
            {'field': 'id', 'data_type': 'SERIAL', 'nullable': 'NO', 'key': 'PRI', 'data_pribadi': 'NO', 'description': 'Primary key for the table'},
            {'field': 'evaluation_id', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Evaluation identifier, foreign key to tb_mitigation_evaluation'},
            {'field': 'domain_id', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Domain identifier, foreign key to tb_domain'},
            {'field': 'document_id', 'data_type': 'INT', 'nullable': 'YES', 'key': 'FOR', 'data_pribadi': 'NO', 'description': 'Document identifier, foreign key to tb_document'},
            {'field': 'notes', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Support notes'},
            {'field': 'schedule', 'data_type': 'TEXT', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Support schedule'},
            {'field': 'created_date', 'data_type': 'TIMESTAMP', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Record creation timestamp'},
            {'field': 'created_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who created the record'},
            {'field': 'supported_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User providing support'},
            {'field': 'approved_by', 'data_type': 'VARCHAR(100)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'User who approved the support'},
            {'field': 'approved_state', 'data_type': 'VARCHAR(50)', 'nullable': 'YES', 'key': '', 'data_pribadi': 'NO', 'description': 'Approval state'}
        ],
        'create_query': '''CREATE TABLE tb_mitigation_support (
    id SERIAL PRIMARY KEY,
    evaluation_id INT,
    domain_id INT,
    document_id INT,
    notes TEXT,
    schedule TEXT,
    created_date TIMESTAMP,
    created_by VARCHAR(100),
    supported_by VARCHAR(100),
    approved_by VARCHAR(100),
    approved_state VARCHAR(50),
    FOREIGN KEY (evaluation_id) REFERENCES tb_mitigation_evaluation(id),
    FOREIGN KEY (document_id) REFERENCES tb_document(id)
);''',
        'select_query': 'SELECT * FROM tb_mitigation_support WHERE evaluation_id = ? AND approved_state = ?;',
        'insert_query': 'INSERT INTO tb_mitigation_support (evaluation_id, domain_id, document_id, notes, schedule, created_date, created_by, supported_by) VALUES (?, ?, ?, ?, ?, NOW(), ?, ?);',
        'update_query': 'UPDATE tb_mitigation_support SET notes = ?, schedule = ?, approved_by = ?, approved_state = ? WHERE id = ?;',
        'delete_query': 'DELETE FROM tb_mitigation_support WHERE id = ?;'
    }
]
