from typing import TypedDict, Optional, Literal, Union, Any


class AnalyticsReport(TypedDict):
    """
    A report with some statistics about the data accessible by Mathesar.
    
    Attributes:
        installation_id: Optional[str] - A unique ID for this Mathesar installation.
        mathesar_version: str - The version of Mathesar.
        user_count: int - The number of configured users in Mathesar.
        active_user_count: int - The number of users who have recently logged in.
        configured_role_count: int - The number of DB roles configured.
        connected_database_count: int - The number of databases configured.
        connected_database_schema_count: int - The number of all schemas in
    all connected databases.
        connected_database_table_count: int - The total number of tables in
    all connected databasees.
        connected_database_record_count: int - The total number of records in
    all connected databasees (approximated)
        exploration_count: int - The number of explorations.
    """
    
    installation_id: Optional[str]
    mathesar_version: str
    user_count: int
    active_user_count: int
    configured_role_count: int
    connected_database_count: int
    connected_database_schema_count: int
    connected_database_table_count: int
    connected_database_record_count: int
    exploration_count: int


class AnalyticsState(TypedDict):
    """
    Returns the current state of analytics.
    
    Attributes:
        enabled: bool - A boolean representing if analytics is enabled.
    """
    
    enabled: bool


class CollaboratorInfo(TypedDict):
    """
    Information about a collaborator.
    
    Attributes:
        id: int - the Django ID of the UserDatabaseRoleMap model instance.
        user_id: int - The Django ID of the User model instance of the collaborator.
        database_id: int - the Django ID of the Database model instance for the collaborator.
        configured_role_id: int - The Django ID of the ConfiguredRole model instance for the collaborator.
    """
    
    id: int
    user_id: int
    database_id: int
    configured_role_id: int


class CreatablePkColumnInfo(TypedDict):
    """
    Information needed to add a new PK column.
    
    
    No keys are required.
    
    Attributes:
        name: Optional[str] - The name of the column.
        type: Optional[Literal['IDENTITY', 'UUIDv4']] - The type of the pk column on the database.
    """
    
    name: Optional[str]
    type: Optional[Literal['IDENTITY', 'UUIDv4']]


class TypeOptions(TypedDict):
    """
    Options applied to a type. All attributes are optional.
    
    
    Take special care with the difference between numeric and date/time
    types w.r.t. precision. The attribute has a different meaning
    depending on the type to which it’s being applied.
    
    Attributes:
        precision: int - For numeric types, the number of significant digits.
           For date/time types, the number of fractional digits.
        scale: int - For numeric types, the number of fractional digits.
        fields: str - Which time fields are stored. See Postgres docs.
        length: int - The maximum length of a character-type field.
        item_type: str - The member type for arrays.
    """
    
    precision: int
    scale: int
    fields: str
    length: int
    item_type: str


class ColumnDefault(TypedDict):
    """
    A dictionary describing the default value for a column.
    
    Attributes:
        value: str - An SQL expression giving the default value.
        is_dynamic: bool - Whether the value is possibly dynamic.
    """
    
    value: str
    is_dynamic: bool


class ColumnMetaDataRecord(TypedDict):
    """
    Metadata for a column in a table.
    
    
    Only the database, table_oid, and attnum keys are required.
    
    Attributes:
        database_id: int - The Django id of the database containing the table.
        table_oid: int - The OID of the table containing the column.
        attnum: int - The attnum of the column in the table.
        bool_input: Optional[Literal['dropdown', 'checkbox']] - How the input for a boolean column should be shown.
        bool_true: Optional[str] - A string to display for true values.
        bool_false: Optional[str] - A string to display for false values.
        num_min_frac_digits: Optional[int] - Minimum digits shown after the decimal point.
        num_max_frac_digits: Optional[int] - Maximum digits shown after the decimal point.
        num_grouping: Optional[str] - Specifies how grouping separators are displayed for numeric values.
        num_format: Optional[str] - Specifies the locale-specific format for displaying numeric values.
        mon_currency_symbol: Optional[str] - The currency symbol shown for money value.
        mon_currency_location: Optional[Literal['after-minus', 'end-with-space']] - Where the currency symbol should be shown.
        time_format: Optional[str] - A string representing the format of time values.
        date_format: Optional[str] - A string representing the format of date values.
        duration_min: Optional[str] - The smallest unit for displaying durations.
        duration_max: Optional[str] - The largest unit for displaying durations.
        display_width: Optional[int] - The pixel width of the column
    """
    
    database_id: int
    table_oid: int
    attnum: int
    bool_input: Optional[Literal['dropdown', 'checkbox']]
    bool_true: Optional[str]
    bool_false: Optional[str]
    num_min_frac_digits: Optional[int]
    num_max_frac_digits: Optional[int]
    num_grouping: Optional[str]
    num_format: Optional[str]
    mon_currency_symbol: Optional[str]
    mon_currency_location: Optional[Literal['after-minus', 'end-with-space']]
    time_format: Optional[str]
    date_format: Optional[str]
    duration_min: Optional[str]
    duration_max: Optional[str]
    display_width: Optional[int]


class ColumnMetaDataBlob(TypedDict):
    """
    The metadata fields which can be set for a column in a table.
    
    Attributes:
        attnum: int - The attnum of the column in the table.
        bool_input: Optional[Literal['dropdown', 'checkbox']] - How the input for a boolean column should be shown.
        bool_true: Optional[str] - A string to display for true values.
        bool_false: Optional[str] - A string to display for false values.
        num_min_frac_digits: Optional[int] - Minimum digits shown after the decimal point.
        num_max_frac_digits: Optional[int] - Maximum digits shown after the decimal point.
        num_grouping: Optional[str] - Specifies how grouping separators are displayed for numeric values.
        num_format: Optional[str] - Specifies the locale-specific format for displaying numeric values.
        mon_currency_symbol: Optional[str] - The currency symbol shown for money value.
        mon_currency_location: Optional[Literal['after-minus', 'end-with-space']] - Where the currency symbol should be shown.
        time_format: Optional[str] - A string representing the format of time values.
        date_format: Optional[str] - A string representing the format of date values.
        duration_min: Optional[str] - The smallest unit for displaying durations.
        duration_max: Optional[str] - The largest unit for displaying durations.
        display_width: Optional[int] - The pixel width of the column
    """
    
    attnum: int
    bool_input: Optional[Literal['dropdown', 'checkbox']]
    bool_true: Optional[str]
    bool_false: Optional[str]
    num_min_frac_digits: Optional[int]
    num_max_frac_digits: Optional[int]
    num_grouping: Optional[str]
    num_format: Optional[str]
    mon_currency_symbol: Optional[str]
    mon_currency_location: Optional[Literal['after-minus', 'end-with-space']]
    time_format: Optional[str]
    date_format: Optional[str]
    duration_min: Optional[str]
    duration_max: Optional[str]
    display_width: Optional[int]


class ConfiguredDatabaseInfo(TypedDict):
    """
    Information about a database.
    
    Attributes:
        id: int - the Django ID of the database model instance.
        name: str - The name of the database on the server.
        server_id: int - the Django ID of the server model instance for the database.
        last_confirmed_sql_version: str - The last version of the SQL scripts which
    were confirmed to have been run on this database.
        needs_upgrade_attention: bool - This is True if the SQL version isn’t the
    same as the service version.
        nickname: Optional[str] - A optional user-configurable name for the database.
    """
    
    id: int
    name: str
    server_id: int
    last_confirmed_sql_version: str
    needs_upgrade_attention: bool
    nickname: Optional[str]


class ConfiguredDatabasePatch(TypedDict):
    """
    Information to be changed about a configured database
    
    Attributes:
        name: Optional[str] - The name of the database on the server.
        nickname: Optional[str] - A optional user-configurable name for the database.
    """
    
    name: Optional[str]
    nickname: Optional[str]


class ForeignKeyConstraint(TypedDict):
    """
    Information about a foreign key constraint.
    
    Attributes:
        type: str - The type of the constraint('f' for foreign key constraint).
        columns: list[int] - List of columns to set a foreign key on.
        fkey_relation_id: int - The OID of the referent table.
        fkey_columns: list[int] - List of referent column(s).
        name: Optional[str] - The name of the constraint.
        deferrable: Optional[bool] - Whether to postpone constraint checking until the end of the transaction.
        fkey_update_action: Optional[str] - Specifies what action should be taken when the referenced key is updated.
    Valid options include 'a'(no action)(default behavior), 'r'(restrict), 'c'(cascade), 'n'(set null), 'd'(set default)
        fkey_delete_action: Optional[str] - Specifies what action should be taken when the referenced key is deleted.
    Valid options include 'a'(no action)(default behavior), 'r'(restrict), 'c'(cascade), 'n'(set null), 'd'(set default)
        fkey_match_type: Optional[str] - Specifies how the foreign key matching should be performed.
    Valid options include 'f'(full match), 's'(simple match)(default behavior).
    """
    
    type: str
    columns: list[int]
    fkey_relation_id: int
    fkey_columns: list[int]
    name: Optional[str]
    deferrable: Optional[bool]
    fkey_update_action: Optional[str]
    fkey_delete_action: Optional[str]
    fkey_match_type: Optional[str]


class PrimaryKeyConstraint(TypedDict):
    """
    Information about a primary key constraint.
    
    Attributes:
        type: str - The type of the constraint('p' for primary key constraint).
        columns: list[int] - List of columns to set a primary key on.
        name: Optional[str] - The name of the constraint.
        deferrable: Optional[bool] - Whether to postpone constraint checking until the end of the transaction.
    """
    
    type: str
    columns: list[int]
    name: Optional[str]
    deferrable: Optional[bool]


class UniqueConstraint(TypedDict):
    """
    Information about a unique constraint.
    
    Attributes:
        type: str - The type of the constraint('u' for unique constraint).
        columns: list[int] - List of columns to set a unique constraint on.
        name: Optional[str] - The name of the constraint.
        deferrable: Optional[bool] - Whether to postpone constraint checking until the end of the transaction.
    """
    
    type: str
    columns: list[int]
    name: Optional[str]
    deferrable: Optional[bool]


class MappingColumn(TypedDict):
    """
    An object defining a foreign key column in a mapping table.
    
    Attributes:
        column_name: str - The name of the foreign key column.
        referent_table_oid: int - The OID of the table the column references.
    """
    
    column_name: str
    referent_table_oid: int


class SplitTableInfo(TypedDict):
    """
    Information about a table, created from column extraction.
    
    Attributes:
        extracted_table_oid: int - The OID of the table that is created from column extraction.
        new_fkey_attnum: int - The attnum of the newly created foreign key column
                 referring the extracted_table on the original table.
    """
    
    extracted_table_oid: int
    new_fkey_attnum: int


class DatabaseInfo(TypedDict):
    """
    Information about a database current user privileges on it.
    
    Attributes:
        oid: int - The oid of the database on the server.
        name: str - The name of the database on the server.
        owner_oid: int - The oid of the owner of the database.
        current_role_priv: list[Literal['CONNECT', 'CREATE', 'TEMPORARY']] - A list of privileges available to the user.
        current_role_owns: bool - Whether the user is an owner of the database.
    """
    
    oid: int
    name: str
    owner_oid: int
    current_role_priv: list[Literal['CONNECT', 'CREATE', 'TEMPORARY']]
    current_role_owns: bool


class DBPrivileges(TypedDict):
    """
    Information about database privileges.
    
    Attributes:
        role_oid: int - The oid of the role on the database server.
        direct: list[Literal['CONNECT', 'CREATE', 'TEMPORARY']] - A list of database privileges for the aforementioned role_oid.
    """
    
    role_oid: int
    direct: list[Literal['CONNECT', 'CREATE', 'TEMPORARY']]


class ExplorationInfo(TypedDict):
    """
    Information about an exploration.
    
    Attributes:
        id: int - The Django id of an exploration.
        database_id: int - The Django id of the database containing the exploration.
        name: str - The name of the exploration.
        base_table_oid: int - The OID of the base table of the exploration on the database.
        schema_oid: int - The OID of the schema containing the base table of the exploration.
        initial_columns: list - A list describing the columns to be included in the exploration.
        transformations: Optional[list] - A list describing the transformations to be made on the included columns.
        display_options: Optional[list] - A list describing metadata for the columns in the explorations.
        display_names: Optional[dict] - A map between the actual column names on the database and the alias to be displayed(if any).
        description: Optional[str] - The description of the exploration.
    """
    
    id: int
    database_id: int
    name: str
    base_table_oid: int
    schema_oid: int
    initial_columns: list
    transformations: Optional[list]
    display_options: Optional[list]
    display_names: Optional[dict]
    description: Optional[str]


class ExplorationDef(TypedDict):
    """
    Definition about a runnable exploration.
    
    Attributes:
        database_id: int - The Django id of the database containing the exploration.
        name: str - The name of the exploration.
        base_table_oid: int - The OID of the base table of the exploration on the database.
        schema_oid: int - The OID of the schema containing the base table of the exploration.
        initial_columns: list - A list describing the columns to be included in the exploration.
        transformations: Optional[list] - A list describing the transformations to be made on the included columns.
        display_options: Optional[list] - A list describing metadata for the columns in the explorations.
        display_names: Optional[dict] - A map between the actual column names on the database and the alias to be displayed(if any).
        description: Optional[str] - The description of the exploration.
    """
    
    database_id: int
    name: str
    base_table_oid: int
    schema_oid: int
    initial_columns: list
    transformations: Optional[list]
    display_options: Optional[list]
    display_names: Optional[dict]
    description: Optional[str]


class ExplorationResult(TypedDict):
    """
    Result of an exploration run.
    
    Attributes:
        query: dict - A dict describing the exploration that ran.
        records: dict - A dict describing the total count of records along with the contents of those records.
        output_columns: tuple - A tuple describing the names of the columns included in the exploration.
        column_metadata: dict - A dict describing the metadata applied to included columns.
        limit: Optional[int] - Specifies the max number of rows returned.(default 100)
        offset: Optional[int] - Specifies the number of rows skipped.(default 0)
    """
    
    query: dict
    records: dict
    output_columns: tuple
    column_metadata: dict
    limit: Optional[int]
    offset: Optional[int]


class RecordAdded(TypedDict):
    """
    Record from a table, along with some meta data
    
    
    The form of the object in the results array is determined by the
    underlying records being listed. The keys of each object are the
    attnums of the retrieved columns. The values are the value for the
    given row, for the given column.
    
    Attributes:
        results: list[dict] - An array of a single record objects (the one added).
        linked_record_summaries: dict[str, dict[str, str]] - Information for previewing foreign key
    values, provides a map of foreign key to a text summary.
        record_summaries: dict[str, str] - Information for previewing an added record.
    """
    
    results: list[dict]
    linked_record_summaries: dict[str, dict[str, str]]
    record_summaries: dict[str, str]


class OrderBy(TypedDict):
    """
    An object defining an ORDER BY clause.
    
    Attributes:
        attnum: int - The attnum of the column to order by.
        direction: Literal['asc', 'desc'] - The direction to order by.
    """
    
    attnum: int
    direction: Literal['asc', 'desc']


class Filter(TypedDict):
    """
    An object defining a filter to be used in a WHERE clause.
    
    
    For valid type values, see the msar.filter_templates table
    defined in mathesar/db/sql/05_msar.sql.
    
    Attributes:
        type: str - a function or operator to be used in filtering.
        args: list[Union[Filter, FilterAttnum, FilterLiteral]] - The ordered arguments for the function or operator.
    """
    
    type: str
    args: "list[Union[Filter, FilterAttnum, FilterLiteral]]"


class FilterAttnum(TypedDict):
    """
    An object choosing a column for a filter.
    
    Attributes:
        type: Literal['attnum'] - Must be "attnum"
        value: int - The attnum of the column to filter by
    """
    
    type: Literal['attnum']
    value: int


class FilterLiteral(TypedDict):
    """
    An object defining a literal for an argument to a filter.
    
    Attributes:
        type: Literal['literal'] - must be "literal".
        value: Any - The value of the literal.
    """
    
    type: Literal['literal']
    value: Any


class Grouping(TypedDict):
    """
    Grouping definition.
    
    
    The table involved must have a single column primary key.
    
    Attributes:
        columns: list[int] - The columns to be grouped by.
        preproc: list[str] - The preprocessing functions to apply (if any).
    """
    
    columns: list[int]
    preproc: list[str]


class Group(TypedDict):
    """
    Group definition.
    
    
    Note that the count is over all rows in the group, whether returned
    or not. However, result_indices is restricted to only the rows
    returned. This is to avoid potential problems if there are many rows
    in the group (e.g., the whole table), but we only return a few.
    
    Attributes:
        id: int - The id of the group. Consistent for same input.
        count: int - The number of items in the group.
        results_eq: list[dict] - The value the results of the group equal.
        result_indices: list[int] - The 0-indexed positions of group members in the
    results array.
    """
    
    id: int
    count: int
    results_eq: list[dict]
    result_indices: list[int]


class GroupingResponse(TypedDict):
    """
    Grouping response object. Extends Grouping with actual groups.
    
    Attributes:
        columns: list[int] - The columns to be grouped by.
        preproc: list[str] - The preprocessing functions to apply (if any).
        groups: list[Group] - The groups applicable to the records being returned.
    """
    
    columns: list[int]
    preproc: list[str]
    groups: list[Group]


class SearchParam(TypedDict):
    """
    Search definition for a single column.
    
    Attributes:
        attnum: int - The attnum of the column in the table.
        literal: Any - The literal to search for in the column.
    """
    
    attnum: int
    literal: Any


class RoleMember(TypedDict):
    """
    Information about a member role of a directly inherited role.
    
    Attributes:
        oid: int - The OID of the member role.
        admin: bool - Whether the member role has ADMIN option on the inherited role.
    """
    
    oid: int
    admin: bool


class ConfiguredRoleInfo(TypedDict):
    """
    Information about a role configured in Mathesar.
    
    Attributes:
        id: int - the Django ID of the ConfiguredRole model instance.
        name: str - The name of the role.
        server_id: int - The Django ID of the Server model instance for the role.
    """
    
    id: int
    name: str
    server_id: int


class SchemaInfo(TypedDict):
    """
    Information about a schema
    
    Attributes:
        oid: int - The OID of the schema
        name: str - The name of the schema
        description: Optional[str] - A description of the schema
        owner_oid: int - The OID of the owner of the schema
        current_role_priv: list[Literal['USAGE', 'CREATE']] - All privileges available to the calling role
    on the schema.
        current_role_owns: bool - Whether the current role is the owner of the
    schema (even indirectly).
        table_count: int - The number of tables in the schema
    """
    
    oid: int
    name: str
    description: Optional[str]
    owner_oid: int
    current_role_priv: list[Literal['USAGE', 'CREATE']]
    current_role_owns: bool
    table_count: int


class SchemaPatch(TypedDict):
    """
    Attributes:
        name: Optional[str] - The name of the schema
        description: Optional[str] - A description of the schema
    """
    
    name: Optional[str]
    description: Optional[str]


class SchemaPrivileges(TypedDict):
    """
    Information about schema privileges for a role.
    
    Attributes:
        role_oid: int - The oid of the role.
        direct: list[Literal['USAGE', 'CREATE']] - A list of schema privileges for the aforementioned role_oid.
    """
    
    role_oid: int
    direct: list[Literal['USAGE', 'CREATE']]


class TableInfo(TypedDict):
    """
    Information about a table.
    
    Attributes:
        oid: int - The oid of the table in the schema.
        name: str - The name of the table.
        schema: int - The oid of the schema where the table lives.
        description: Optional[str] - The description of the table.
        owner_oid: int - The OID of the direct owner of the table.
        current_role_priv: list[Literal['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'TRUNCATE', 'REFERENCES', 'TRIGGER']] - The privileges available to the user on the table.
        current_role_owns: bool - Whether the current role owns the table.
    """
    
    oid: int
    name: str
    schema: int
    description: Optional[str]
    owner_oid: int
    current_role_priv: list[Literal['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'TRUNCATE', 'REFERENCES', 'TRIGGER']]
    current_role_owns: bool


class AddedTableInfo(TypedDict):
    """
    Information about a newly created table.
    
    Attributes:
        oid: int - The oid of the table in the schema.
        name: str - The name of the table.
        renamed_columns: Optional[dict] - A dictionary giving the names of columns which
    were renamed due to collisions.
    """
    
    oid: int
    name: str
    renamed_columns: Optional[dict]


class JoinableTableRecord(TypedDict):
    """
    Information about a singular joinable table.
    
    Attributes:
        base: int - The OID of the table from which the paths start
        target: int - The OID of the table where the paths end.
        join_path: list - A list describing joinable paths in the following form:
    [
      [[L_oid0, L_attnum0], [R_oid0, R_attnum0]],
      [[L_oid1, L_attnum1], [R_oid1, R_attnum1]],
      [[L_oid2, L_attnum2], [R_oid2, R_attnum2]],
      …
    ]
    Here, [L_oidN, L_attnumN] represents the left column of a join, and [R_oidN, R_attnumN] the right.
        fkey_path: list - Same as join_path expressed in terms of foreign key constraints in the following form:
    [
        [constraint_id0, reversed],
        [constraint_id1, reversed],
    ]
    In this form, constraint_idN is a foreign key constraint, and reversed is a boolean giving
    whether to travel from referrer to referent (when False) or from referent to referrer (when True).
        depth: int - Specifies how far to search for joinable tables.
        multiple_results: bool - Specifies whether the path included is reversed.
    """
    
    base: int
    target: int
    join_path: list
    fkey_path: list
    depth: int
    multiple_results: bool


class JoinableTableInfo(TypedDict):
    """
    Information about joinable table(s).
    
    Attributes:
        joinable_tables: list[JoinableTableRecord] - List of reachable joinable table(s) from a base table.
        target_table_info: list - Additional info about target table(s) and its column(s).
    """
    
    joinable_tables: list[JoinableTableRecord]
    target_table_info: list


class TableMetaDataBlob(TypedDict):
    """
    The metadata fields which can be set on a table
    
    Attributes:
        data_file_id: Optional[int] - Specifies the DataFile model id used for the import.
        import_verified: Optional[bool] - Specifies whether a file has been successfully imported into a table.
        column_order: Optional[list[int]] - The order in which columns of a table are displayed.
        record_summary_template: Optional[dict[str, Union[str, list[int]]]] - The record summary template
        mathesar_added_pkey_attnum: Optional[int] - The attnum of the most recently-set pkey column.
    """
    
    data_file_id: Optional[int]
    import_verified: Optional[bool]
    column_order: Optional[list[int]]
    record_summary_template: Optional[dict[str, Union[str, list[int]]]]
    mathesar_added_pkey_attnum: Optional[int]


class TableMetaDataRecord(TypedDict):
    """
    Metadata for a table in a database.
    
    
    Only the database and table_oid keys are required.
    
    Attributes:
        id: int - The Django id of the TableMetaData object.
        database_id: int - The Django id of the database containing the table.
        table_oid: int - The OID of the table in the database.
        data_file_id: Optional[int] - Specifies the DataFile model id used for the import.
        import_verified: Optional[bool] - Specifies whether a file has been successfully imported into a table.
        column_order: Optional[list[int]] - The order in which columns of a table are displayed.
        record_summary_template: Optional[dict[str, Union[str, list[int]]]] - The record summary template.
        mathesar_added_pkey_attnum: Optional[int] - The attnum of the most recently-set pkey column.
    """
    
    id: int
    database_id: int
    table_oid: int
    data_file_id: Optional[int]
    import_verified: Optional[bool]
    column_order: Optional[list[int]]
    record_summary_template: Optional[dict[str, Union[str, list[int]]]]
    mathesar_added_pkey_attnum: Optional[int]


class TablePrivileges(TypedDict):
    """
    Attributes:
        role_oid: Any - The oid of the role.
        direct: Any - A list of table privileges for the aforementioned role_oid.
    """
    
    role_oid: Any
    direct: Any


class UserInfo(TypedDict):
    """
    Information about a mathesar user.
    
    Attributes:
        id: int - The Django id of the user.
        username: str - The username of the user.
        is_superuser: bool - Specifies whether the user is a superuser.
        email: str - The email of the user.
        full_name: str - The full name of the user.
        display_language: str - Specifies the display language for the user, can be either en or ja.
    """
    
    id: int
    username: str
    is_superuser: bool
    email: str
    full_name: str
    display_language: str


class UserDef(TypedDict):
    """
    Definition for creating a mathesar user.
    
    Attributes:
        username: str - The username of the user.
        password: str - The password of the user.
        is_superuser: bool - Whether the user is a superuser.
        email: Optional[str] - The email of the user.
        full_name: Optional[str] - The full name of the user.
        display_language: Optional[str] - Specifies the display language for the user, can be set to either en or ja.
    """
    
    username: str
    password: str
    is_superuser: bool
    email: Optional[str]
    full_name: Optional[str]
    display_language: Optional[str]


class ColumnInfo(TypedDict):
    """
    Information about a column. Extends the settable fields.
    
    Attributes:
        id: int - The attnum of the column in the table.
        name: str - The name of the column.
        type: str - The type of the column on the database.
        type_options: TypeOptions - The options applied to the column type.
        nullable: bool - Whether or not the column is nullable.
        primary_key: bool - Whether the column is in the primary key.
        default: ColumnDefault - The default value and whether it’s dynamic.
        has_dependents: bool - Whether the column has dependent objects.
        description: str - The description of the column.
        current_role_priv: list[Literal['SELECT', 'INSERT', 'UPDATE', 'REFERENCES']] - The privileges available to the user for the column.
    """
    
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


class CreatableColumnInfo(TypedDict):
    """
    Information needed to add a new column.
    
    
    No keys are required.
    
    Attributes:
        name: Optional[str] - The name of the column.
        type: Optional[str] - The type of the column on the database.
        type_options: Optional[TypeOptions] - The options applied to the column type.
        nullable: Optional[bool] - Whether or not the column is nullable.
        default: Optional[ColumnDefault] - The default value.
        description: Optional[str] - The description of the column.
    """
    
    name: Optional[str]
    type: Optional[str]
    type_options: Optional[TypeOptions]
    nullable: Optional[bool]
    default: Optional[ColumnDefault]
    description: Optional[str]


class PreviewableColumnInfo(TypedDict):
    """
    Information needed to preview a column.
    
    Attributes:
        id: int - The attnum of the column in the table.
        type: Optional[str] - The new type to be applied to a column.
        type_options: Optional[TypeOptions] - The options to be applied to the column type.
    """
    
    id: int
    type: Optional[str]
    type_options: Optional[TypeOptions]


class SettableColumnInfo(TypedDict):
    """
    Information about a column, restricted to settable fields.
    
    
    When possible, Passing null for a key will clear the underlying
    setting. E.g.,
    
    
    
    default = null clears the column default setting.
    type_options = null clears the type options for the column.
    description = null clears the column description.
    
    
    
    Setting any of name, type, or nullable is a noop.
    
    
    Only the id key is required.
    
    Attributes:
        id: int - The attnum of the column in the table.
        name: Optional[str] - The name of the column.
        type: Optional[str] - The type of the column on the database.
        type_options: Optional[TypeOptions] - The options applied to the column type.
        nullable: Optional[bool] - Whether or not the column is nullable.
        default: Optional[ColumnDefault] - The default value.
        description: Optional[str] - The description of the column.
    """
    
    id: int
    name: Optional[str]
    type: Optional[str]
    type_options: Optional[TypeOptions]
    nullable: Optional[bool]
    default: Optional[ColumnDefault]
    description: Optional[str]


class DatabaseConnectionResult(TypedDict):
    """
    Info about the objects resulting from calling the setup functions.
    
    
    These functions will get or create an instance of the Server,
    Database, and ConfiguredRole models, as well as a UserDatabaseRoleMap entry.
    
    Attributes:
        server: Any - Information on the Server model instance.
        database: ConfiguredDatabaseInfo - Information on the Database model instance.
        configured_role: ConfiguredRoleInfo - Information on the ConfiguredRole model instance.
    """
    
    server: Any
    database: ConfiguredDatabaseInfo
    configured_role: ConfiguredRoleInfo


class RecordList(TypedDict):
    """
    Records from a table, along with some meta data
    
    
    The form of the objects in the results array is determined by the
    underlying records being listed. The keys of each object are the
    attnums of the retrieved columns. The values are the value for the
    given row, for the given column.
    
    Attributes:
        count: int - The total number of records in the table.
        results: list[dict] - An array of record objects.
        grouping: GroupingResponse - Information for displaying grouped records.
        linked_record_smmaries: GroupingResponse - Information for previewing foreign key
    values, provides a map of foreign key to a text summary.
        record_summaries: dict[str, str] - Information for previewing returned records.
    """
    
    count: int
    results: list[dict]
    grouping: GroupingResponse
    linked_record_smmaries: GroupingResponse
    record_summaries: dict[str, str]


class RoleInfo(TypedDict):
    """
    Information about a role.
    
    Attributes:
        oid: int - The OID of the role.
        name: str - Name of the role.
        super: bool - Whether the role has SUPERUSER status.
        inherits: bool - Whether the role has INHERIT attribute.
        create_role: bool - Whether the role has CREATEROLE attribute.
        create_db: bool - Whether the role has CREATEDB attribute.
        login: bool - Whether the role has LOGIN attribute.
        description: Optional[str] - A description of the role
        members: Optional[list[RoleMember]] - The member roles that directly inherit the role.
    """
    
    oid: int
    name: str
    super: bool
    inherits: bool
    create_role: bool
    create_db: bool
    login: bool
    description: Optional[str]
    members: Optional[list[RoleMember]]


class SettableTableInfo(TypedDict):
    """
    Information about a table, restricted to settable fields.
    
    
    When possible, Passing null for a key will clear the underlying
    setting. E.g.,
    
    
    
    description = null clears the table description.
    
    
    
    Setting any of name, columns to null is a noop.
    
    Attributes:
        name: Optional[str] - The new name of the table.
        description: Optional[str] - The description of the table.
        columns: Optional[list[SettableColumnInfo]] - A list describing desired column alterations.
    """
    
    name: Optional[str]
    description: Optional[str]
    columns: Optional[list[SettableColumnInfo]]


CreatableConstraintInfo = list[
    Union[
        ForeignKeyConstraint,
        PrimaryKeyConstraint,
        UniqueConstraint,
    ]
]