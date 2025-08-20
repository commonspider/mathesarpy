from .classes import *
from .client import Client, api


class Mathesar(Client):
    @api("analytics.get_state")
    def analytics_get_state(self) -> AnalyticsState:
        """
        :return: A boolean to identify if analytics is enabled.
        """
        
        ...
    
    @api("analytics.initialize")
    def analytics_initialize(self):
        """
        Initialize analytics collection and reporting in Mathesar
        If initialized, analytics are gathered to a local model once per day,
        and uploaded.
        """
        
        ...
    
    @api("analytics.disable")
    def analytics_disable(self):
        """
        Disable analytics collection and reporting in Mathesar
        Disabling analytics amounts to (for now) simply deleting the
        Installation ID, ensuring that it’s impossible to save analytics
        reports. Any reports currently saved are removed when the
        Installation ID is deleted.
        """
        
        ...
    
    @api("analytics.view_report")
    def analytics_view_report(self) -> AnalyticsReport:
        """
        View an example analytics report, prepared with the same function
        that creates real reports that would be saved and uploaded.
        
        :return: An analytics report.
        """
        
        ...
    
    @api("analytics.upload_feedback")
    def analytics_upload_feedback(self, *, message: str):
        """
        Upload a feedback message to Mathesar’s servers.
        
        :param message: The feedback message to send.
        """
        
        ...
    
    @api("collaborators.list")
    def collaborators_list(self, *, database_id: int = None) -> list[CollaboratorInfo]:
        """
        List information about collaborators. Exposed as list.
        If called with no database_id, all collaborators for all databases are listed.
        
        :param database_id: The Django id of the database associated with the collaborators.
        :return: A list of collaborators.
        """
        
        ...
    
    @api("collaborators.add")
    def collaborators_add(self, *, database_id: int, user_id: int, configured_role_id: int):
        """
        Set up a new collaborator for a database.
        
        :param database_id: The Django id of the Database to associate with the collaborator.
        :param user_id: The Django id of the User model instance who’d be the collaborator.
        :param configured_role_id: The Django id of the ConfiguredRole model instance to associate with the collaborator.
        """
        
        ...
    
    @api("collaborators.delete")
    def collaborators_delete(self, *, collaborator_id: int):
        """
        Delete a collaborator from a database.
        
        :param collaborator_id: The Django id of the UserDatabaseRoleMap model instance of the collaborator.
        """
        
        ...
    
    @api("collaborators.set_role")
    def collaborators_set_role(self, *, collaborator_id: int, configured_role_id: int):
        """
        Set the role of a collaborator for a database.
        
        :param collaborator_id: The Django id of the UserDatabaseRoleMap model instance of the collaborator.
        :param configured_role_id: The Django id of the ConfiguredRole model instance to associate with the collaborator.
        """
        
        ...
    
    @api("columns.list")
    def columns_list(self, *, table_oid: int, database_id: int) -> list[ColumnInfo]:
        """
        List information about columns for a table. Exposed as list.
        
        :param table_oid: Identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :return: A list of column details.
        """
        
        ...
    
    @api("columns.add")
    def columns_add(self, *, column_data_list: list[CreatableColumnInfo], table_oid: int, database_id: int) -> list[int]:
        """
        Add columns to a table.
        There are defaults for both the name and type of a column, and so
        passing [{}] for column_data_list would add a single column of
        type CHARACTER VARYING, with an auto-generated name.
        
        :param column_data_list: A list describing desired columns to add.
        :param table_oid: Identity of the table to which we’ll add columns.
        :param database_id: The Django id of the database containing the table.
        :return: An array of the attnums of the new columns.
        """
        
        ...
    
    @api("columns.add_primary_key_column")
    def columns_add_primary_key_column(self, *, pkey_type: Literal['IDENTITY', 'UUIDv4'], table_oid: int, database_id: int, drop_existing_pkey_column: bool = False, name: str = 'id'):
        """
        Add a primary key column to a table of a predefined type.
        The column will be added, set as the primary key, and also filled
        for each preexisting row, using the default generating function or
        method associated with the given pkey_type.
        If there is a name collision for the new primary key column, we
        automatically generate a non-colliding name for the new primary key
        column, and leave the existing table column names as they are.
        Primary key types
        - ‘UUIDv4’: This results in a uuid primary key column, with
            default values generated by the get_random_uuid() function
            provided by PostgreSQL. This amounts to UUIDv4 uuid definitions.
        - ‘IDENTITY’: This results in an integer primary key column with
            default values created via an identity sequence, i.e., using
            GENERATED BY DEFAULT AS IDENTITY.
        
        :param pkey_type: Defines the type and default of the primary key.
        :param table_oid: The OID of the table getting a primary key.
        :param database_id: The Django id of the database containing the table.
        :param drop_existing_pkey_column: Whether to drop the old pkey column.
        :param name: A custom name for the added primary key column.
        """
        
        ...
    
    @api("columns.patch")
    def columns_patch(self, *, column_data_list: list[SettableColumnInfo], table_oid: int, database_id: int) -> int:
        """
        Alter details of preexisting columns in a table.
        Does not support altering the type or type options of array columns.
        
        :param column_data_list: A list describing desired column alterations.
        :param table_oid: Identity of the table whose columns we’ll modify.
        :param database_id: The Django id of the database containing the table.
        :return: The number of columns altered.
        """
        
        ...
    
    @api("columns.delete")
    def columns_delete(self, *, column_attnums: list[int], table_oid: int, database_id: int) -> int:
        """
        Delete columns from a table.
        
        :param column_attnums: A list of attnums of columns to delete.
        :param table_oid: Identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :return: The number of columns dropped.
        """
        
        ...
    
    @api("columns.list_with_metadata")
    def columns_list_with_metadata(self):
        """
        List information about columns for a table, along with the metadata associated with each column.
        Args:
            table_oid: Identity of the table in the user’s database.
            database_id: The Django id of the database containing the table.
        Returns:
            A list of column details.
        """
        
        ...
    
    @api("columns.metadata.list")
    def columns_metadata_list(self, *, table_oid: int, database_id: int) -> list[ColumnMetaDataRecord]:
        """
        List metadata associated with columns for a table. Exposed as list.
        
        :param table_oid: Identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :return: A list of column meta data objects.
        """
        
        ...
    
    @api("columns.metadata.set")
    def columns_metadata_set(self, *, column_meta_data_list: list[ColumnMetaDataBlob], table_oid: int, database_id: int):
        """
        Set metadata associated with columns of a table for a database. Exposed as set.
        
        :param column_meta_data_list: A list describing desired metadata alterations.
        :param table_oid: Identity of the table whose metadata we’ll modify.
        :param database_id: The Django id of the database containing the table.
        """
        
        ...
    
    @api("databases.configured.list")
    def databases_configured_list(self, *, server_id: int = None) -> list[ConfiguredDatabaseInfo]:
        """
        List information about databases for a server. Exposed as list.
        If called with no server_id, all databases for all servers are listed.
        
        :param server_id: The Django id of the server containing the databases.
        :return: A list of database details.
        """
        
        ...
    
    @api("databases.configured.patch")
    def databases_configured_patch(self, *, database_id: int, patch: ConfiguredDatabasePatch) -> ConfiguredDatabaseInfo:
        """
        Patch a configured database, given its id.
        
        :param database_id: The Django id of the database
        :param patch: An object containing the fields to update.
        :return: An object describing the database.
        """
        
        ...
    
    @api("databases.configured.disconnect")
    def databases_configured_disconnect(self, *, database_id: int, schemas_to_remove: list[str] = ['msar', '__msar', 'mathesar_types'], strict: bool = True, role_name: str = None, password: str = None, disconnect_db_server: bool = False):
        """
        Disconnect a configured database, after removing Mathesar SQL from it.
        If no role_name and password are submitted, we will determine the
        role which owns the msar schema on the database, then use that role
        for the SQL removal.
        All removals are performed safely, and without CASCADE. This is to
        make sure the user can’t accidentally lose data calling this
        function.
        
        :param database_id: The Django id of the database.
        :param schemas_to_remove: Mathesar schemas we should remove SQL from.
        :param strict: If True, we throw an exception and roll back changes if
        we fail to remove any objects which we expected to remove.
        :param role_name: the username of the role used for upgrading.
        :param password: the password of the role used for upgrading.
        :param disconnect_db_server: If True, will delete the stored server
        metadata(host, port, role credentials) from Mathesar.
        This is intended for optional use while disconnecting the
        last database on the server.
        """
        
        ...
    
    @api("constraints.list")
    def constraints_list(self, *, table_oid: int, database_id: int) -> list[Any]:
        """
        List information about constraints in a table. Exposed as list.
        
        :param table_oid: The oid of the table to list constraints for.
        :param database_id: The Django id of the database containing the table.
        :return: A list of constraint details.
        """
        
        ...
    
    @api("constraints.add")
    def constraints_add(self, *, table_oid: int, constraint_def_list: CreatableConstraintInfo, database_id: int) -> list[int]:
        """
        Add constraint(s) on a table in bulk.
        
        :param table_oid: Identity of the table to delete constraint for.
        :param constraint_def_list: A list describing the constraints to add.
        :param database_id: The Django id of the database containing the table.
        :return: The oid(s) of all the constraints on the table.
        """
        
        ...
    
    @api("constraints.delete")
    def constraints_delete(self, *, table_oid: int, constraint_oid: int, database_id: int) -> str:
        """
        Delete a constraint from a table.
        
        :param table_oid: Identity of the table to delete constraint for.
        :param constraint_oid: The OID of the constraint to delete.
        :param database_id: The Django id of the database containing the table.
        :return: The name of the dropped constraint.
        """
        
        ...
    
    @api("data_modeling.add_foreign_key_column")
    def data_modeling_add_foreign_key_column(self, *, column_name: str, referrer_table_oid: int, referent_table_oid: int):
        """
        Add a foreign key column to a table.
        The foreign key column will be newly created, and will reference the
        id column of the referent table.
        
        :param column_name: The name of the column to create.
        :param referrer_table_oid: The OID of the table getting the new column.
        :param referent_table_oid: The OID of the table being referenced.
        """
        
        ...
    
    @api("data_modeling.add_mapping_table")
    def data_modeling_add_mapping_table(self, *, table_name: str, schema_oid: int, mapping_columns: list[MappingColumn]):
        """
        Add a mapping table to give a many-to-many link between referents.
        The foreign key columns in the mapping table will reference the id
        column of the referent tables.
        
        :param table_name: The name for the new mapping table.
        :param schema_oid: The OID of the schema for the mapping table.
        :param mapping_columns: The foreign key columns to create in the
        mapping table.
        """
        
        ...
    
    @api("data_modeling.suggest_types")
    def data_modeling_suggest_types(self):
        """
        Infer the best type for each column in the table.
        Currently we only suggest different types for columns which originate
        as type text.
        Parameters:
        
        
        
        Name
        Type
        Description
        Default
        
        
        
        
        
        table_oid
        
        
        int
        
        
        
        The OID of the table whose columns we’re inferring types for.
        
        
        
        required
        
        
        
        
        database_id
        
        
        int
        
        
        
        The Django id of the database containing the table.
        
        
        
        required
        
        
        
        
        The response JSON will have attnum keys, and values will be the
        result of format_type for the inferred type of each column, i.e., the
        canonical string referring to the type.
        """
        
        ...
    
    @api("data_modeling.split_table")
    def data_modeling_split_table(self, *, table_oid: int, column_attnums: list, extracted_table_name: str, database_id: int, relationship_fk_column_name: str = None) -> SplitTableInfo:
        """
        Extract columns from a table to create a new table, linked by a foreign key.
        
        :param table_oid: The OID of the table whose columns we’ll extract.
        :param column_attnums: A list of the attnums of the columns to extract.
        :param extracted_table_name: The name of the new table to be made from the extracted columns.
        :param database_id: The Django id of the database containing the table.
        :param relationship_fk_column_name: The name to give the new foreign key column in the remainder table (optional)
        :return: The SplitTableInfo object describing the details for the created table as a result of column extraction.
        """
        
        ...
    
    @api("data_modeling.move_columns")
    def data_modeling_move_columns(self, *, source_table_oid: int, target_table_oid: int, move_column_attnums: list[int], database_id: int):
        """
        Extract columns from a table to a referent table, linked by a foreign key.
        
        :param source_table_oid: The OID of the source table whose column(s) we’ll extract.
        :param target_table_oid: The OID of the target table where the extracted column(s) will be added.
        :param move_column_attnums: The list of attnum(s) to move from source table to the target table.
        :param database_id: The Django id of the database containing the table.
        """
        
        ...
    
    @api("databases.get")
    def databases_get(self, *, database_id: int) -> DatabaseInfo:
        """
        Get information about a database.
        
        :param database_id: The Django id of the database.
        :return: Information about the database, and the current user privileges.
        """
        
        ...
    
    @api("databases.delete")
    def databases_delete(self, *, database_oid: int, database_id: int):
        """
        Drop a database from the server.
        
        :param database_oid: The OID of the database to delete on the database.
        :param database_id: The Django id of the database to connect to.
        """
        
        ...
    
    @api("databases.upgrade_sql")
    def databases_upgrade_sql(self, *, database_id: int, username: str = None, password: str = None):
        """
        Install, Upgrade, or Reinstall the Mathesar SQL on a database.
        If no username and password are submitted, we will determine the
        role which owns the msar schema on the database, then use that role
        for the upgrade.
        
        :param database_id: The Django id of the database.
        :param username: The username of the role used for upgrading.
        :param password: The password of the role used for upgrading.
        """
        
        ...
    
    @api("databases.privileges.list_direct")
    def databases_privileges_list_direct(self, *, database_id: int) -> list[DBPrivileges]:
        """
        List database privileges for non-inherited roles.
        
        :param database_id: The Django id of the database.
        :return: A list of database privileges.
        """
        
        ...
    
    @api("databases.privileges.replace_for_roles")
    def databases_privileges_replace_for_roles(self, *, privileges: Any, database_id: Any) -> list[DBPrivileges]:
        """
        Replace direct database privileges for roles.
        Possible privileges are CONNECT, CREATE, and TEMPORARY.
        Only roles which are included in a passed DBPrivileges object are
        affected.
        WARNING: Any privilege included in the direct list for a role
        is GRANTed, and any privilege not included is REVOKEd.
        
        :param privileges: The new privilege sets for roles.
        :param database_id: The Django id of the database.
        :return: A list of all non-default privileges on the database after theoperation.
        """
        
        ...
    
    @api("databases.privileges.transfer_ownership")
    def databases_privileges_transfer_ownership(self, *, new_owner_oid: Any, database_id: Any) -> DatabaseInfo:
        """
        Transfers ownership of the current database to a new owner.
        
        :param new_owner_oid: The OID of the role whom we want to be the new owner of the current database.
        :param database_id: The Django id of the database whose ownership is to be transferred.
        :return: Information about the database, and the current user privileges.
        """
        
        ...
    
    @api("databases.setup.create_new")
    def databases_setup_create_new(self, *, database: str, sample_data: list[str] = [], nickname: Optional[str] = None):
        """
        Set up a new database on the internal server.
        The calling user will get access to that database using the default
        role stored in Django settings.
        
        :param database: The name of the new database.
        :param sample_data: A list of strings requesting that some example data
        sets be installed on the underlying database. Valid list
        members are:
        - ‘bike_shop’
        - ‘hardware_store’
        - ‘ice_cream_employees’
        - ‘library_management’
        - ‘library_makerspace’
        - ‘museum_exhibits’
        - ‘nonprofit_grants’
        :param nickname: An optional nickname for the database.
        """
        
        ...
    
    @api("databases.setup.connect_existing")
    def databases_setup_connect_existing(self, *, host: str, port: Optional[int] = None, database: str, role: str, password: str, sample_data: list[str] = [], nickname: Optional[str] = None):
        """
        Connect Mathesar to an existing database on a server.
        The calling user will get access to that database using the
        credentials passed to this function.
        
        :param host: The host of the database server.
        :param port: The port of the database server.
        :param database: The name of the database on the server.
        :param role: The role on the server to use for the connection.
        :param password: A password valid for the role.
        :param sample_data: A list of strings requesting that some example data
        sets be installed on the underlying database. Valid list
        members are:
        - ‘bike_shop’
        - ‘hardware_store’
        - ‘ice_cream_employees’
        - ‘library_management’
        - ‘library_makerspace’
        - ‘museum_exhibits’
        - ‘nonprofit_grants’
        :param nickname: An optional nickname for the database.
        """
        
        ...
    
    @api("explorations.list")
    def explorations_list(self, *, database_id: int, schema_oid: int = None) -> list[ExplorationInfo]:
        """
        List information about explorations for a database. Exposed as list.
        
        :param database_id: The Django id of the database containing the explorations.
        :param schema_oid: The OID of the schema containing the base table(s) of the exploration(s).(optional)
        :return: A list of exploration details.
        """
        
        ...
    
    @api("explorations.get")
    def explorations_get(self, *, exploration_id: int) -> ExplorationInfo:
        """
        List information about an exploration.
        
        :param exploration_id: The Django id of the exploration.
        :return: Exploration details for a given exploration_id.
        """
        
        ...
    
    @api("explorations.add")
    def explorations_add(self, *, exploration_def: ExplorationDef) -> ExplorationInfo:
        """
        Add a new exploration.
        
        :param exploration_def: A dict describing the exploration to create.
        :return: The exploration details for the newly created exploration.
        """
        
        ...
    
    @api("explorations.delete")
    def explorations_delete(self, *, exploration_id: int):
        """
        Delete an exploration.
        
        :param exploration_id: The Django id of the exploration to delete.
        """
        
        ...
    
    @api("explorations.replace")
    def explorations_replace(self, *, new_exploration: ExplorationInfo) -> ExplorationInfo:
        """
        Replace a saved exploration.
        
        :param new_exploration: A dict describing the exploration to replace, including the updated fields.
        :return: The exploration details for the replaced exploration.
        """
        
        ...
    
    @api("explorations.run")
    def explorations_run(self, *, exploration_def: ExplorationDef, limit: int = 100, offset: int = 0) -> ExplorationResult:
        """
        Run an exploration.
        
        :param exploration_def: A dict describing an exploration to run.
        :param limit: The max number of rows to return.(default 100)
        :param offset: The number of rows to skip.(default 0)
        :return: The result of the exploration run.
        """
        
        ...
    
    @api("explorations.run_saved")
    def explorations_run_saved(self, *, exploration_id: int, limit: int = 100, offset: int = 0) -> ExplorationResult:
        """
        Run a saved exploration.
        
        :param exploration_id: The Django id of the exploration to run.
        :param limit: The max number of rows to return.(default 100)
        :param offset: The number of rows to skip.(default 0)
        :return: The result of the exploration run.
        """
        
        ...
    
    @api("records.list")
    def records_list(self, *, table_oid: int, database_id: int, limit: int = None, offset: int = None, order: list[OrderBy] = None, filter: Filter = None, grouping: Grouping = None, return_record_summaries: bool = False) -> RecordList:
        """
        List records from a table, and its row count. Exposed as list.
        
        :param table_oid: Identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :param limit: The maximum number of rows we’ll return.
        :param offset: The number of rows to skip before returning records from
        following rows.
        :param order: An array of ordering definition objects.
        :param filter: An array of filter definition objects.
        :param grouping: An array of group definition objects.
        :param return_record_summaries: Whether to return summaries of retrieved
        records.
        :return: The requested records, along with some metadata.
        """
        
        ...
    
    @api("records.get")
    def records_get(self):
        """
        Get single record from a table by its primary key.
        Parameters:
        
        
        
        Name
        Type
        Description
        Default
        
        
        
        
        
        record_id
        
        
        Any
        
        
        
        The primary key value of the record to be gotten.
        
        
        
        required
        
        
        
        
        table_oid
        
        
        int
        
        
        
        Identity of the table in the user’s database.
        
        
        
        required
        
        
        
        
        database_id
        
        
        int
        
        
        
        The Django id of the database containing the table.
        
        
        
        required
        
        
        
        
        return_record_summaries
        
        
        bool
        
        
        
        Whether to return summaries of the
        retrieved record.
        
        
        
        False
        
        
        
        
        table_record_summary_templates
        
        
        dict[str, Any]
        
        
        
        A dict of record summary templates.
        If none are provided, then the templates will be take from the
        Django metadata. Any templates provided will take precedence on a
        per-table basis over the stored metadata templates. The purpose of
        this function parameter is to allow clients to generate record
        summary previews without persisting any metadata.
        
        
        
        None
        
        
        
        
        Returns:
            The requested record, along with some metadata.
        """
        
        ...
    
    @api("records.add")
    def records_add(self, *, record_def: dict, table_oid: int, database_id: int, return_record_summaries: bool = False) -> RecordAdded:
        """
        Add a single record to a table.
        The form of the record_def is determined by the underlying table.
        Keys should be attnums, and values should be the desired value for
        that column in the created record. Missing keys will use default
        values (if set on the DB), and explicit null values will set null
        for that value regardless of default (with obvious exceptions where
        that would violate some constraint)
        
        :param record_def: An object representing the record to be added.
        :param table_oid: Identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :param return_record_summaries: Whether to return summaries of the added
        record.
        :return: The created record, along with some metadata.
        """
        
        ...
    
    @api("records.patch")
    def records_patch(self, *, record_def: dict, record_id: Any, table_oid: int, database_id: int, return_record_summaries: bool = False) -> RecordAdded:
        """
        Modify a record in a table.
        The form of the record_def is determined by the underlying table.
        Keys should be attnums, and values should be the desired value for
        that column in the modified record. Explicit null values will set
        null for that value (with obvious exceptions where that would violate
        some constraint).
        
        :param record_def: An object representing the record to be added.
        :param record_id: The primary key value of the record to modify.
        :param table_oid: Identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :param return_record_summaries: Whether to return summaries of the
        modified record.
        :return: The modified record, along with some metadata.
        """
        
        ...
    
    @api("records.delete")
    def records_delete(self, *, record_ids: list[Any], table_oid: int, database_id: int) -> Optional[int]:
        """
        Delete records from a table by primary key.
        
        :param record_ids: The primary key values of the records to be deleted.
        :param table_oid: The identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :return: The number of records deleted.
        """
        
        ...
    
    @api("records.search")
    def records_search(self, *, table_oid: int, database_id: int, search_params: list[SearchParam] = [], limit: int = 10) -> RecordList:
        """
        List records from a table according to search_params.
        Literals will be searched for in a basic way in string-like columns,
        but will have to match exactly in non-string-like columns.
        Records are assigned a score based on how many matches, and of what
        quality, they have with the passed search parameters.
        
        :param table_oid: Identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :param search_params: Results are ranked and filtered according to the
                   objects passed here.
        :param limit: The maximum number of rows we’ll return.
        :return: The requested records, along with some metadata.
        """
        
        ...
    
    @api("roles.list")
    def roles_list(self, *, database_id: int) -> list[RoleInfo]:
        """
        List information about roles for a database server. Exposed as list.
        Requires a database id inorder to connect to the server.
        
        :param database_id: The Django id of the database.
        :return: A list of roles present on the database server.
        """
        
        ...
    
    @api("roles.add")
    def roles_add(self, *, rolename: str, database_id: int, password: str = None, login: bool = None) -> RoleInfo:
        """
        Add a new login/non-login role on a database server.
        
        :param rolename: The name of the role to be created.
        :param database_id: The Django id of the database.
        :param password: The password for the rolename to set.
        :param login: Whether the role to be created could login.
        :return: A dict describing the created role.
        """
        
        ...
    
    @api("roles.delete")
    def roles_delete(self, *, role_oid: int, database_id: int):
        """
        Drop a role on a database server.
        
        :param role_oid: The OID of the role to drop on the database.
        :param database_id: The Django id of the database.
        """
        
        ...
    
    @api("roles.get_current_role")
    def roles_get_current_role(self, *, database_id: int) -> dict:
        """
        Get information about the current role and all the parent role(s) whose
        privileges are immediately available to current role without doing SET ROLE.
        
        :param database_id: The Django id of the database.
        :return: A dict describing the current role.
        """
        
        ...
    
    @api("roles.set_members")
    def roles_set_members(self, *, parent_role_oid: int, members: list) -> RoleInfo:
        """
        Grant/Revoke direct membership to/from roles.
        
        :param parent_role_oid: The OID of role whose membership will be granted/revoked to/from other roles.
        :param members: An array of role OID(s) whom we want to grant direct membership of the parent role.
               Only the OID(s) present in the array will be granted membership of parent role,
               Membership will be revoked for existing members not present in this array.
        :return: A dict describing the updated information of the parent role.
        """
        
        ...
    
    @api("roles.configured.list")
    def roles_configured_list(self, *, server_id: int) -> list[ConfiguredRoleInfo]:
        """
        List information about roles configured in Mathesar. Exposed as list.
        
        :param server_id: The Django id of the Server containing the configured roles.
        :return: A list of configured roles.
        """
        
        ...
    
    @api("roles.configured.add")
    def roles_configured_add(self, *, server_id: int, name: str, password: str) -> ConfiguredRoleInfo:
        """
        Configure a role in Mathesar for a database server.
        
        :param server_id: The Django id of the Server to contain the configured role.
        :param name: The name of the role.
        :param password: The password for the role.
        :return: The newly configured role.
        """
        
        ...
    
    @api("roles.configured.delete")
    def roles_configured_delete(self, *, configured_role_id: int):
        """
        Delete a configured role for a server.
        
        :param configured_role_id: The Django id of the ConfiguredRole model instance.
        """
        
        ...
    
    @api("roles.configured.set_password")
    def roles_configured_set_password(self, *, configured_role_id: int, password: str):
        """
        Set the password of a configured role for a server.
        
        :param configured_role_id: The Django id of the ConfiguredRole model instance.
        :param password: The password for the role.
        """
        
        ...
    
    @api("schemas.list")
    def schemas_list(self, *, database_id: int) -> list[SchemaInfo]:
        """
        List information about schemas in a database. Exposed as list.
        
        :param database_id: The Django id of the database containing the table.
        :return: A list of SchemaInfo objects
        """
        
        ...
    
    @api("schemas.get")
    def schemas_get(self, *, schema_oid: int, database_id: int) -> SchemaInfo:
        """
        Get information about a schema in a database.
        
        :param schema_oid: The OID of the schema to get.
        :param database_id: The Django id of the database containing the table.
        :return: The SchemaInfo describing the user-defined schema in the database.
        """
        
        ...
    
    @api("schemas.add")
    def schemas_add(self, *, name: str, database_id: int, owner_oid: int = None, description: Optional[str] = None) -> SchemaInfo:
        """
        Add a schema
        
        :param name: The name of the schema to add.
        :param database_id: The Django id of the database containing the schema.
        :param owner_oid: The OID of the role who will own the new schema.
        If owner_oid is None, the current role will be the owner of the new schema.
        :param description: A description of the schema
        :return: The SchemaInfo describing the user-defined schema in the database.
        """
        
        ...
    
    @api("schemas.delete")
    def schemas_delete(self, *, schema_oids: list[int], database_id: int):
        """
        Safely drop all objects in each schema, then the schemas themselves.
        Does not work on the internal msar schema.
        If any passed schema doesn’t exist, an exception will be raised. If
        any object exists in a schema which isn’t passed, but which depends
        on an object in a passed schema, an exception will be raised.
        
        :param schema_oids: The OIDs of the schemas to delete.
        :param database_id: The Django id of the database containing the schema.
        """
        
        ...
    
    @api("schemas.patch")
    def schemas_patch(self, *, schema_oid: int, database_id: int, patch: SchemaPatch) -> SchemaInfo:
        """
        Patch a schema, given its OID.
        
        :param schema_oid: The OID of the schema to delete.
        :param database_id: The Django id of the database containing the schema.
        :param patch: A SchemaPatch object containing the fields to update.
        :return: The SchemaInfo describing the user-defined schema in the database.
        """
        
        ...
    
    @api("schemas.privileges.list_direct")
    def schemas_privileges_list_direct(self, *, schema_oid: int, database_id: int) -> list[SchemaPrivileges]:
        """
        List direct schema privileges for roles.
        
        :param schema_oid: The OID of the schema whose privileges we’ll list.
        :param database_id: The Django id of the database containing the schema.
        :return: A list of schema privileges.
        """
        
        ...
    
    @api("schemas.privileges.replace_for_roles")
    def schemas_privileges_replace_for_roles(self, *, privileges: list[SchemaPrivileges], schema_oid: int, database_id: int) -> list[SchemaPrivileges]:
        """
        Replace direct schema privileges for roles.
        Possible privileges are USAGE and CREATE.
        Only roles which are included in a passed SchemaPrivileges object
        are affected.
        WARNING: Any privilege included in the direct list for a role
        is GRANTed, and any privilege not included is REVOKEd.
        
        :param privileges: The new privilege sets for roles.
        :param schema_oid: The OID of the affected schema.
        :param database_id: The Django id of the database containing the schema.
        :return: A list of all non-default privileges on the schema after theoperation.
        """
        
        ...
    
    @api("schemas.privileges.transfer_ownership")
    def schemas_privileges_transfer_ownership(self, *, schema_oid: Any, new_owner_oid: Any) -> SchemaInfo:
        """
        Transfers ownership of a given schema to a new owner.
        
        :param schema_oid: The OID of the schema to transfer.
        :param new_owner_oid: The OID of the role whom we want to be the new owner of the schema.
        :return: Information about the schema, and the current user privileges.
        """
        
        ...
    
    @api("tables.list")
    def tables_list(self, *, schema_oid: int, database_id: int) -> list[TableInfo]:
        """
        List information about tables for a schema. Exposed as list.
        
        :param schema_oid: Identity of the schema in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :return: A list of table details.
        """
        
        ...
    
    @api("tables.get")
    def tables_get(self, *, table_oid: int, database_id: int) -> TableInfo:
        """
        List information about a table for a schema.
        
        :param table_oid: Identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :return: Table details for a given table oid.
        """
        
        ...
    
    @api("tables.add")
    def tables_add(self, *, schema_oid: int, database_id: int, table_name: str = None, pkey_column_info: CreatablePkColumnInfo = {}, column_data_list: list[CreatableColumnInfo] = [], constraint_data_list: list[CreatableConstraintInfo] = [], owner_oid: int = None, comment: str = None) -> int:
        """
        Add a table with a default id column.
        
        :param schema_oid: Identity of the schema in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :param table_name: Name of the table to be created.
        :param pkey_column_info: A dict describing the primary key column to be created for the new table.
        :param column_data_list: A list describing columns to be created for the new table, in order.
        :param constraint_data_list: A list describing constraints to be created for the new table.
        :param owner_oid: The OID of the role who will own the new table.
        If owner_oid is None, the current role will be the owner of the new table.
        :param comment: The comment for the new table.
        :return: The oid, name, and renamed_columns of the created table.
        """
        
        ...
    
    @api("tables.delete")
    def tables_delete(self, *, table_oid: int, database_id: int, cascade: bool = False) -> str:
        """
        Delete a table from a schema.
        
        :param table_oid: Identity of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :param cascade: Whether to drop the dependent objects.
        :return: The name of the dropped table.
        """
        
        ...
    
    @api("tables.patch")
    def tables_patch(self, *, table_oid: str, table_data_dict: SettableTableInfo, database_id: int) -> str:
        """
        Alter details of a preexisting table in a database.
        
        :param table_oid: Identity of the table whose name, description or columns we’ll modify.
        :param table_data_dict: A list describing desired table alterations.
        :param database_id: The Django id of the database containing the table.
        :return: The name of the altered table.
        """
        
        ...
    
    @api("tables.import")
    def tables_import(self, *, data_file_id: int, schema_oid: int, database_id: int, table_name: Optional[str] = None, comment: Optional[str] = None) -> AddedTableInfo:
        """
        Import a CSV/TSV into a table.
        
        :param data_file_id: The Django id of the DataFile containing desired CSV/TSV.
        :param schema_oid: Identity of the schema in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :param table_name: Name of the table to be imported.
        :param comment: The comment for the new table.
        :return: The oid, name, and renamed_columns of the created table.
        """
        
        ...
    
    @api("tables.get_import_preview")
    def tables_get_import_preview(self, *, table_oid: int, columns: list[PreviewableColumnInfo], database_id: int, limit: int = 20) -> list[dict]:
        """
        Preview an imported table.
        
        :param table_oid: Identity of the imported table in the user’s database.
        :param columns: List of settings describing the casts to be applied to the columns.
        :param database_id: The Django id of the database containing the table.
        :param limit: The upper limit for the number of records to return.
        :return: The records from the specified columns of the table.
        """
        
        ...
    
    @api("tables.list_joinable")
    def tables_list_joinable(self, *, table_oid: int, database_id: int, max_depth: int = 3) -> JoinableTableInfo:
        """
        List details for joinable tables.
        
        :param table_oid: Identity of the table to get joinable tables for.
        :param database_id: The Django id of the database containing the table.
        :param max_depth: Specifies how far to search for joinable tables.
        :return: Joinable table details for a given table.
        """
        
        ...
    
    @api("tables.list_with_metadata")
    def tables_list_with_metadata(self, *, schema_oid: int, database_id: int) -> list:
        """
        List tables in a schema, along with the metadata associated with each table
        
        :param schema_oid: PostgreSQL OID of the schema containing the tables.
        :param database_id: The Django id of the database containing the table.
        :return: A list of table details along with metadata.
        """
        
        ...
    
    @api("tables.get_with_metadata")
    def tables_get_with_metadata(self, *, table_oid: int, database_id: int) -> dict:
        """
        Get information about a table in a schema, along with the associated table metadata.
        
        :param table_oid: The OID of the table in the user’s database.
        :param database_id: The Django id of the database containing the table.
        :return: A dict describing table details along with its metadata.
        """
        
        ...
    
    @api("tables.metadata.list")
    def tables_metadata_list(self, *, database_id: int) -> list[TableMetaDataRecord]:
        """
        List metadata associated with tables for a database.
        
        :param database_id: The Django id of the database containing the table.
        :return: Metadata object for a given table oid.
        """
        
        ...
    
    @api("tables.metadata.set")
    def tables_metadata_set(self, *, table_oid: int, metadata: TableMetaDataBlob, database_id: int):
        """
        Set metadata for a table.
        
        :param table_oid: The PostgreSQL OID of the table.
        :param metadata: A TableMetaDataBlob object describing desired table metadata to set.
        :param database_id: The Django id of the database containing the table.
        """
        
        ...
    
    @api("tables.privileges.list_direct")
    def tables_privileges_list_direct(self):
        """
        List direct table privileges for roles.
        Args:
            table_oid: The OID of the table whose privileges we’ll list.
            database_id: The Django id of the database containing the table.
        Returns:
            A list of table privileges.
        """
        
        ...
    
    @api("tables.privileges.replace_for_roles")
    def tables_privileges_replace_for_roles(self, *, privileges: list[TablePrivileges], table_oid: int, database_id: int) -> list[TablePrivileges]:
        """
        Replace direct table privileges for roles.
        Possible privileges are INSERT, SELECT, UPDATE, DELETE, TRUNCATE, REFERENCES and TRIGGER.
        Only roles which are included in a passed TablePrivileges object
        are affected.
        WARNING: Any privilege included in the direct list for a role
        is GRANTed, and any privilege not included is REVOKEd.
        
        :param privileges: The new privilege sets for roles.
        :param table_oid: The OID of the affected table.
        :param database_id: The Django id of the database containing the table.
        :return: A list of all non-default privileges on the table after theoperation.
        """
        
        ...
    
    @api("tables.privileges.transfer_ownership")
    def tables_privileges_transfer_ownership(self, *, table_oid: Any, new_owner_oid: Any) -> TableInfo:
        """
        Transfers ownership of a given table to a new owner.
        
        :param table_oid: The OID of the table to transfer.
        :param new_owner_oid: The OID of the role whom we want to be the new owner of the table.
        :return: Information about the table, and the current user privileges.
        """
        
        ...
    
    @api("users.list")
    def users_list(self) -> list[UserInfo]:
        """
        List information about all mathesar users. Exposed as list.
        
        :return: A list of information about mathesar users.
        """
        
        ...
    
    @api("users.get")
    def users_get(self, *, user_id: int) -> UserInfo:
        """
        List information about a mathesar user.
        
        :param user_id: The Django id of the user.
        :return: User information for a given user_id.
        """
        
        ...
    
    @api("users.add")
    def users_add(self, *, user_def: UserDef) -> UserInfo:
        """
        Add a new mathesar user.
        
        :param user_def: A dict describing the user to create.
        :return: The information of the created user.
        """
        
        ...
    
    @api("users.delete")
    def users_delete(self, *, user_id: int):
        """
        Delete a mathesar user.
        
        :param user_id: The Django id of the user to delete.
        """
        
        ...
    
    @api("users.patch_self")
    def users_patch_self(self, *, username: str, email: str, full_name: str, display_language: str) -> UserInfo:
        """
        Alter details of currently logged in mathesar user.
        
        :param username: The username of the user.
        :param email: The email of the user.
        :param full_name: The full name of the user.
        :param display_language: Specifies the display language for the user, can be set to either en or ja.
        :return: Updated user information of the caller.
        """
        
        ...
    
    @api("users.patch_other")
    def users_patch_other(self, *, user_id: int, username: str, email: str, is_superuser: bool, full_name: str, display_language: str) -> UserInfo:
        """
        Alter details of a mathesar user, given its user_id.
        
        :param user_id: The Django id of the user.
        :param username: The username of the user.
        :param email: The email of the user.
        :param is_superuser: Specifies whether to set the user as a superuser.
        :param full_name: The full name of the user.
        :param display_language: Specifies the display language for the user, can be set to either en or ja.
        :return: Updated user information for a given user_id.
        """
        
        ...
    
    @api("users.replace_own")
    def users_replace_own(self, *, old_password: str, new_password: str):
        """
        Alter password of currently logged in mathesar user.
        
        :param old_password: Old password of the currently logged in user.
        :param new_password: New password of the user to set.
        """
        
        ...
    
    @api("users.revoke")
    def users_revoke(self, *, user_id: int, new_password: str):
        """
        Alter password of a mathesar user, given its user_id.
        
        :param user_id: The Django id of the user.
        :param new_password: New password of the user to set.
        """
        
        ...