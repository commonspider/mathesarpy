from pathlib import Path

BASE_DIR = Path("{base_dir}").resolve()

SECRET_KEY = "mathesarpy"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "modernrpc",
    "mathesar",
    "allauth",
    "allauth.socialaccount",
]

MODERNRPC_METHODS_MODULES = [
    'mathesar.rpc.analytics',
    'mathesar.rpc.collaborators',
    'mathesar.rpc.columns',
    'mathesar.rpc.columns.metadata',
    'mathesar.rpc.constraints',
    'mathesar.rpc.data_modeling',
    'mathesar.rpc.databases',
    'mathesar.rpc.databases.configured',
    'mathesar.rpc.databases.privileges',
    'mathesar.rpc.databases.setup',
    'mathesar.rpc.explorations',
    'mathesar.rpc.forms',
    'mathesar.rpc.records',
    'mathesar.rpc.roles',
    'mathesar.rpc.roles.configured',
    'mathesar.rpc.schemas',
    'mathesar.rpc.schemas.privileges',
    'mathesar.rpc.servers.configured',
    'mathesar.rpc.tables',
    'mathesar.rpc.tables.metadata',
    'mathesar.rpc.tables.privileges',
    'mathesar.rpc.users'
]
