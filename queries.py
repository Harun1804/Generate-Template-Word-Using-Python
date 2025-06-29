# queries.py

tables_data = [
    {
        'table_name': 'oauth_personal_access_clients',
        'fields': [
            {
                'field': 'id',
                'data_type': 'bigint',
                'nullable': 'NO',
                'key': 'PRI',
                'data_pribadi': 'NO',
                'description': 'Primary key for the table'
            },
            {
                'field': 'client_id',
                'data_type': 'bigint',
                'nullable': 'NO',
                'key': 'UNI',
                'data_pribadi': 'NO',
                'description': 'Client identifier'
            },
            {
                'field': 'created_at',
                'data_type': 'timestamp',
                'nullable': 'YES',
                'key': '',
                'data_pribadi': 'NO',
                'description': 'Record creation timestamp'
            }
        ],
        'create_query': '''CREATE TABLE oauth_personal_access_clients (
    id bigint NOT NULL AUTO_INCREMENT,
    client_id bigint NOT NULL,
    created_at timestamp NULL DEFAULT NULL,
    updated_at timestamp NULL DEFAULT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY oauth_personal_access_clients_client_id_unique (client_id)
);''',
        'select_query': 'SELECT * FROM oauth_personal_access_clients WHERE client_id = ?;',
        'insert_query': 'INSERT INTO oauth_personal_access_clients (client_id, created_at, updated_at) VALUES (?, NOW(), NOW());',
        'update_query': 'UPDATE oauth_personal_access_clients SET updated_at = NOW() WHERE id = ?;',
        'delete_query': 'DELETE FROM oauth_personal_access_clients WHERE id = ?;'
    },
    {
        'table_name': 'users',
        'fields': [
            {
                'field': 'id',
                'data_type': 'bigint',
                'nullable': 'NO',
                'key': 'PRI',
                'data_pribadi': 'NO',
                'description': 'Primary key for the table'
            },
            {
                'field': 'name',
                'data_type': 'varchar(255)',
                'nullable': 'NO',
                'key': '',
                'data_pribadi': 'YES',
                'description': 'User full name'
            },
            {
                'field': 'email',
                'data_type': 'varchar(255)',
                'nullable': 'NO',
                'key': 'UNI',
                'data_pribadi': 'YES',
                'description': 'User email address'
            }
        ],
        'create_query': '''CREATE TABLE users (
    id bigint NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    created_at timestamp NULL DEFAULT NULL,
    updated_at timestamp NULL DEFAULT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY users_email_unique (email)
);''',
        'select_query': 'SELECT * FROM users WHERE email = ?;',
        'insert_query': 'INSERT INTO users (name, email, created_at, updated_at) VALUES (?, ?, NOW(), NOW());',
        'update_query': 'UPDATE users SET name = ?, updated_at = NOW() WHERE id = ?;',
        'delete_query': 'DELETE FROM users WHERE id = ?;'
    }
]
