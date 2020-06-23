import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '192.168.1.8',
            'DB_NAME': 'retail',
            'DB_USER': 'retail_user',
            'DB_PASS': 'itversity'
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '192.168.1.8',
            'DB_NAME': 'retail_db_pg',
            'DB_USER': 'postgres',
            'DB_PASS': 'itversity'
        }
    }
}