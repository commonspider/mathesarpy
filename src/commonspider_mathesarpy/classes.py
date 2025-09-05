from typing import TypedDict, Union, Any, NotRequired, Literal


class AnalyticsState(TypedDict):
    enabled: bool


class AnalyticsReport(TypedDict):
    installation_id: NotRequired[str]
    mathesar_version: str
    user_count: int
    active_user_count: int
    configured_role_count: int
    connected_database_count: int
    connected_database_schema_count: int
    connected_database_table_count: int
    connected_database_record_count: int
    exploration_count: int


class CollaboratorInfo(TypedDict):
    id: int
    user_id: int
    database_id: int
    configured_role_id: int


class TypeOptions(TypedDict):
    precision: int
    scale: int
    fields: str
    length: int
    item_type: str


class ColumnDefault(TypedDict):
    value: str
    is_dynamic: bool


class CreatableColumnInfo(TypedDict):
    name: NotRequired[str]
    type: NotRequired[str]
    type_options: NotRequired[TypeOptions]
    nullable: NotRequired[bool]
    default: NotRequired[ColumnDefault]
    description: NotRequired[str]


class ColumnInfo(TypedDict):
    id: int
    name: str
    type: str
    type_options: TypeOptions
    nullable: bool
    primary_key: bool
    default: ColumnDefault
    has_dependents: bool
    description: str
    current_role_priv: list[Literal['SELECT', 'INSERT', 'UPDATE', 'REFERENCES']]


class SettableColumnInfo(TypedDict):
    id: int
    name: NotRequired[str]
    type: NotRequired[str]
    type_options: NotRequired[TypeOptions]
    nullable: NotRequired[bool]
    default: NotRequired[ColumnDefault]
    description: NotRequired[str]


class ColumnMetaDataRecord(TypedDict):
    database_id: int
    table_oid: int
    attnum: int
    bool_input: NotRequired[Literal['dropdown', 'checkbox']]
    bool_true: NotRequired[str]
    bool_false: NotRequired[str]
    num_min_frac_digits: NotRequired[int]
    num_max_frac_digits: NotRequired[int]
    num_grouping: NotRequired[str]
    num_format: NotRequired[str]
    mon_currency_symbol: NotRequired[str]
    mon_currency_location: NotRequired[Literal['after-minus', 'end-with-space']]
    time_format: NotRequired[str]
    date_format: NotRequired[str]
    duration_min: NotRequired[str]
    duration_max: NotRequired[str]
    display_width: NotRequired[int]


class ColumnMetaDataBlob(TypedDict):
    attnum: int
    bool_input: NotRequired[Literal['dropdown', 'checkbox']]
    bool_true: NotRequired[str]
    bool_false: NotRequired[str]
    num_min_frac_digits: NotRequired[int]
    num_max_frac_digits: NotRequired[int]
    num_grouping: NotRequired[str]
    num_format: NotRequired[str]
    mon_currency_symbol: NotRequired[str]
    mon_currency_location: NotRequired[Literal['after-minus', 'end-with-space']]
    time_format: NotRequired[str]
    date_format: NotRequired[str]
    duration_min: NotRequired[str]
    duration_max: NotRequired[str]
    display_width: NotRequired[int]


class ForeignKeyConstraint(TypedDict):
    type: str
    columns: list[int]
    fkey_relation_id: int
    fkey_columns: list[int]
    name: NotRequired[str]
    deferrable: NotRequired[bool]
    fkey_update_action: NotRequired[str]
    fkey_delete_action: NotRequired[str]
    fkey_match_type: NotRequired[str]


class PrimaryKeyConstraint(TypedDict):
    type: str
    columns: list[int]
    name: NotRequired[str]
    deferrable: NotRequired[bool]


class UniqueConstraint(TypedDict):
    type: str
    columns: list[int]
    name: NotRequired[str]
    deferrable: NotRequired[bool]


class ConstraintInfo(TypedDict):
    oid: int
    name: str
    type: str
    columns: list[int]
    referent_table_oid: NotRequired[int]
    referent_columns: NotRequired[list[int]]


class MappingColumn(TypedDict):
    column_name: str
    referent_table_oid: int


class SplitTableInfo(TypedDict):
    extracted_table_oid: int
    new_fkey_attnum: int


class DatabaseInfo(TypedDict):
    oid: int
    name: str
    owner_oid: int
    current_role_priv: list[Literal['CONNECT', 'CREATE', 'TEMPORARY']]
    current_role_owns: bool


class ConfiguredDatabaseInfo(TypedDict):
    id: int
    name: str
    server_id: int
    last_confirmed_sql_version: str
    needs_upgrade_attention: bool
    nickname: NotRequired[str]


class ConfiguredDatabasePatch(TypedDict):
    name: NotRequired[str]
    nickname: NotRequired[str]


class DBPrivileges(TypedDict):
    role_oid: int
    direct: list[Literal['CONNECT', 'CREATE', 'TEMPORARY']]


class ConfiguredServerInfo(TypedDict):
    id: int
    host: str
    port: NotRequired[int]


class ConfiguredRoleInfo(TypedDict):
    id: int
    name: str
    server_id: int


class DatabaseConnectionResult(TypedDict):
    server: ConfiguredServerInfo
    database: ConfiguredDatabaseInfo
    configured_role: ConfiguredRoleInfo


class ExplorationDef(TypedDict):
    database_id: int
    name: str
    base_table_oid: int
    schema_oid: int
    initial_columns: list
    transformations: NotRequired[list]
    display_options: NotRequired[list]
    display_names: NotRequired[dict]
    description: NotRequired[str]


class ExplorationInfo(TypedDict):
    id: int
    database_id: int
    name: str
    base_table_oid: int
    schema_oid: int
    initial_columns: list
    transformations: NotRequired[list]
    display_options: NotRequired[list]
    display_names: NotRequired[dict]
    description: NotRequired[str]


class ExplorationResult(TypedDict):
    query: dict
    records: dict
    output_columns: tuple
    column_metadata: dict
    limit: NotRequired[int]
    offset: NotRequired[int]


class RecordAdded(TypedDict):
    results: list[dict]
    linked_record_summaries: dict[str, dict[str, str]]
    record_summaries: dict[str, str]


class Group(TypedDict):
    id: int
    count: int
    results_eq: list[dict]
    result_indices: list[int]


class GroupingResponse(TypedDict):
    columns: list[int]
    preproc: list[str]
    groups: list[Group]


class RecordList(TypedDict):
    count: int
    results: list[dict]
    grouping: GroupingResponse
    linked_record_summaries: dict[str, dict[str, str]]
    record_summaries: dict[str, str]


class OrderBy(TypedDict):
    attnum: int
    direction: Literal['asc', 'desc']


class FilterAttnum(TypedDict):
    type: Literal['attnum']
    value: int


class FilterLiteral(TypedDict):
    type: Literal['literal']
    value: Any


class Filter(TypedDict):
    type: str
    args: list[Union['Filter', FilterAttnum, FilterLiteral]]


class Grouping(TypedDict):
    columns: list[int]
    preproc: list[str]


class SearchParam(TypedDict):
    attnum: int
    literal: Any


class RoleMember(TypedDict):
    oid: int
    admin: bool


class RoleInfo(TypedDict):
    oid: int
    name: str
    super: bool
    inherits: bool
    create_role: bool
    create_db: bool
    login: bool
    description: NotRequired[str]
    members: NotRequired[list[RoleMember]]


class SchemaInfo(TypedDict):
    oid: int
    name: str
    description: NotRequired[str]
    owner_oid: int
    current_role_priv: list[Literal['USAGE', 'CREATE']]
    current_role_owns: bool
    table_count: int


class SchemaPatch(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]


class SchemaPrivileges(TypedDict):
    role_oid: int
    direct: list[Literal['USAGE', 'CREATE']]


class ConfiguredServerPatch(TypedDict):
    host: NotRequired[str]
    port: NotRequired[int]


class CreatablePkColumnInfo(TypedDict):
    name: NotRequired[str]
    type: NotRequired[Literal['IDENTITY', 'UUIDv4']]


class TableInfo(TypedDict):
    oid: int
    name: str
    schema: int
    description: NotRequired[str]
    owner_oid: int
    current_role_priv: list[Literal['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'TRUNCATE', 'REFERENCES', 'TRIGGER']]
    current_role_owns: bool


class PreviewableColumnInfo(TypedDict):
    id: int
    type: NotRequired[str]
    type_options: NotRequired[TypeOptions]


class AddedTableInfo(TypedDict):
    oid: int
    name: str
    renamed_columns: NotRequired[dict]


class JoinableTableRecord(TypedDict):
    base: int
    target: int
    join_path: list
    fkey_path: list
    depth: int
    multiple_results: bool


class JoinableTableInfo(TypedDict):
    joinable_tables: list[JoinableTableRecord]
    target_table_info: list


class SettableTableInfo(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    columns: NotRequired[list[SettableColumnInfo]]


class TableMetaDataRecord(TypedDict):
    id: int
    database_id: int
    table_oid: int
    data_file_id: NotRequired[int]
    import_verified: NotRequired[bool]
    column_order: NotRequired[list[int]]
    record_summary_template: NotRequired[dict[str, Union[str, list[int]]]]
    mathesar_added_pkey_attnum: NotRequired[int]


class TableMetaDataBlob(TypedDict):
    data_file_id: NotRequired[int]
    import_verified: NotRequired[bool]
    column_order: NotRequired[list[int]]
    record_summary_template: NotRequired[dict[str, Union[str, list[int]]]]
    mathesar_added_pkey_attnum: NotRequired[int]


class TablePrivileges(TypedDict):
    role_oid: int
    direct: list[Literal['INSERT', 'SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'REFERENCES', 'TRIGGER']]


class UserDef(TypedDict):
    username: str
    password: str
    is_superuser: bool
    email: NotRequired[str]
    full_name: NotRequired[str]
    display_language: NotRequired[str]


class UserInfo(TypedDict):
    id: int
    username: str
    is_superuser: bool
    email: str
    full_name: str
    display_language: str
