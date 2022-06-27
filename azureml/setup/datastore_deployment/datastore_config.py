DATASTORE_CONFIG = [
    {
        "DATASTORE_NAME": "owm_blob",
        "STORAGE_NAME": "owmadls001",
        "TYPE": "BLOB",
        "CONTAINER": "dataplatform",
        "AUTH": {
            "ACCOUNT_KEY_SECRET": "owm-adls-account-key"
        },
        "DATASETS": {
            "weather_data": {
                "TYPE": "file",
                "PATH": "silver/weather/**"
            }
        }
    }
]