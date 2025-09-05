from typing import Literal, Optional

from .classes import *
from .client import Client, api


class API(Client):
    @api("analytics.disable")
    def analytics_disable(self, **kwargs):
        """    
        Disable analytics collection and reporting in Mathesar
        
        Disabling analytics amounts to (for now) simply deleting the
        Installation ID, ensuring that it's impossible to save analytics
        reports. Any reports currently saved are removed when the
        Installation ID is deleted.
        """
        
        ...
    
    @api("analytics.get_state")
    def analytics_get_state(self, **kwargs) -> AnalyticsState:
        """    
        Returns:
            A boolean to identify if analytics is enabled.
        """
        
        ...
    
    @api("analytics.initialize")
    def analytics_initialize(self, **kwargs):
        """    
        Initialize analytics collection and reporting in Mathesar
        
        If initialized, analytics are gathered to a local model once per day,
        and uploaded.
        """
        
        ...
    
    @api("analytics.upload_feedback")
    def analytics_upload_feedback(self, /, message: str, **kwargs):
        """    
        Upload a feedback message to Mathesar's servers.
        
        Args:
            message: The feedback message to send.
        """
        
        ...
    
    @api("analytics.view_report")
    def analytics_view_report(self, **kwargs) -> AnalyticsReport:
        """    
        View an example analytics report, prepared with the same function
        that creates real reports that would be saved and uploaded.
        
        Returns:
            An analytics report.
        """
        
        ...
    
    @api("collaborators.add")
    def collaborators_add(self, /, database_id: int, user_id: int, configured_role_id: int, **kwargs) -> CollaboratorInfo:
        """    
        Set up a new collaborator for a database.
        
        Args:
            database_id: The Django id of the Database to associate with the collaborator.
            user_id: The Django id of the User model instance who'd be the collaborator.
            configured_role_id: The Django id of the ConfiguredRole model instance to associate with the collaborator.
        """
        
        ...
    
    @api("collaborators.delete")
    def collaborators_delete(self, /, collaborator_id: int, **kwargs):
        """    
        Delete a collaborator from a database.
        
        Args:
            collaborator_id: The Django id of the UserDatabaseRoleMap model instance of the collaborator.
        """
        
        ...
    
    @api("collaborators.list")
    def collaborators_list(self, /, database_id: int = None, **kwargs) -> list[CollaboratorInfo]:
        """    
        List information about collaborators. Exposed as `list`.
        
        If called with no `database_id`, all collaborators for all databases are listed.
        
        Args:
            database_id: The Django id of the database associated with the collaborators.
        
        Returns:
            A list of collaborators.
        """
        
        ...
    
    @api("collaborators.set_role")
    def collaborators_set_role(self, /, collaborator_id: int, configured_role_id: int, **kwargs) -> CollaboratorInfo:
        """    
        Set the role of a collaborator for a database.
        
        Args:
            collaborator_id: The Django id of the UserDatabaseRoleMap model instance of the collaborator.
            configured_role_id: The Django id of the ConfiguredRole model instance to associate with the collaborator.
        """
        
        ...
    
    @api("columns.add")
    def columns_add(self, /, column_data_list: list[CreatableColumnInfo], table_oid: int, database_id: int, **kwargs) -> list[int]:
        """    
        Add columns to a table.
        
        There are defaults for both the name and type of a column, and so
        passing `[{}]` for `column_data_list` would add a single column of
        type `CHARACTER VARYING`, with an auto-generated name.
        
        Args:
            column_data_list: A list describing desired columns to add.
            table_oid: Identity of the table to which we'll add columns.
            database_id: The Django id of the database containing the table.
        
        Returns:
            An array of the attnums of the new columns.
        """
        
        ...
    
    @api("columns.add_primary_key_column")
    def columns_add_primary_key_column(self, /, pkey_type: Literal['IDENTITY', 'UUIDv4'], table_oid: int, database_id: int, drop_existing_pkey_column: bool = False, name: str = id, **kwargs):
        """    
        Add a primary key column to a table of a predefined type.
        
        The column will be added, set as the primary key, and also filled
        for each preexisting row, using the default generating function or
        method associated with the given `pkey_type`.
        
        If there is a name collision for the new primary key column, we
        automatically generate a non-colliding name for the new primary key
        column, and leave the existing table column names as they are.
        
        Primary key types
        - 'UUIDv4': This results in a `uuid` primary key column, with
            default values generated by the `get_random_uuid()` function
            provided by PostgreSQL. This amounts to UUIDv4 uuid definitions.
        - 'IDENTITY': This results in an `integer` primary key column with
            default values created via an identity sequence, i.e., using
            `GENERATED BY DEFAULT AS IDENTITY`.
        
        Args:
            pkey_type: Defines the type and default of the primary key.
            table_oid: The OID of the table getting a primary key.
            database_id: The Django id of the database containing the table.
            drop_existing_pkey_column: Whether to drop the old pkey column.
            name: A custom name for the added primary key column.
        """
        
        ...
    
    @api("columns.delete")
    def columns_delete(self, /, column_attnums: list[int], table_oid: int, database_id: int, **kwargs) -> int:
        """    
        Delete columns from a table.
        
        Args:
            column_attnums: A list of attnums of columns to delete.
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
        
        Returns:
            The number of columns dropped.
        """
        
        ...
    
    @api("columns.list")
    def columns_list(self, /, table_oid: int, database_id: int, **kwargs) -> list[ColumnInfo]:
        """    
        List information about columns for a table. Exposed as `list`.
        
        Args:
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
        
        Returns:
            A list of column details.
        """
        
        ...
    
    @api("columns.list_with_metadata")
    def columns_list_with_metadata(self, /, table_oid: int, database_id: int, **kwargs) -> list:
        """    
        List information about columns for a table, along with the metadata associated with each column.
        Args:
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
        Returns:
            A list of column details.
        """
        
        ...
    
    @api("columns.patch")
    def columns_patch(self, /, column_data_list: list[SettableColumnInfo], table_oid: int, database_id: int, **kwargs) -> int:
        """    
        Alter details of preexisting columns in a table.
        
        Does not support altering the type or type options of array columns.
        
        Args:
            column_data_list: A list describing desired column alterations.
            table_oid: Identity of the table whose columns we'll modify.
            database_id: The Django id of the database containing the table.
        
        Returns:
            The number of columns altered.
        """
        
        ...
    
    @api("columns.metadata.list")
    def columns_metadata_list(self, /, table_oid: int, database_id: int, **kwargs) -> list[ColumnMetaDataRecord]:
        """    
        List metadata associated with columns for a table. Exposed as `list`.
        
        Args:
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
        
        Returns:
            A list of column meta data objects.
        """
        
        ...
    
    @api("columns.metadata.set")
    def columns_metadata_set(self, /, column_meta_data_list: list[ColumnMetaDataBlob], table_oid: int, database_id: int, **kwargs):
        """    
        Set metadata associated with columns of a table for a database. Exposed as `set`.
        
        Args:
            column_meta_data_list: A list describing desired metadata alterations.
            table_oid: Identity of the table whose metadata we'll modify.
            database_id: The Django id of the database containing the table.
        """
        
        ...
    
    @api("constraints.add")
    def constraints_add(self, /, table_oid: int, constraint_def_list: list[Union[ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint]], database_id: int, **kwargs) -> list[int]:
        """    
        Add constraint(s) on a table in bulk.
        
        Args:
            table_oid: Identity of the table to delete constraint for.
            constraint_def_list: A list describing the constraints to add.
            database_id: The Django id of the database containing the table.
        
        Returns:
            The oid(s) of all the constraints on the table.
        """
        
        ...
    
    @api("constraints.delete")
    def constraints_delete(self, /, table_oid: int, constraint_oid: int, database_id: int, **kwargs) -> str:
        """    
        Delete a constraint from a table.
        
        Args:
            table_oid: Identity of the table to delete constraint for.
            constraint_oid: The OID of the constraint to delete.
            database_id: The Django id of the database containing the table.
        
        Returns:
            The name of the dropped constraint.
        """
        
        ...
    
    @api("constraints.list")
    def constraints_list(self, /, table_oid: int, database_id: int, **kwargs) -> list[ConstraintInfo]:
        """    
        List information about constraints in a table. Exposed as `list`.
        
        Args:
            table_oid: The oid of the table to list constraints for.
            database_id: The Django id of the database containing the table.
        
        Returns:
            A list of constraint details.
        """
        
        ...
    
    @api("data_modeling.add_foreign_key_column")
    def data_modeling_add_foreign_key_column(self, /, column_name: str, referrer_table_oid: int, referent_table_oid: int, database_id: int, **kwargs):
        """    
        Add a foreign key column to a table.
        
        The foreign key column will be newly created, and will reference the
        `id` column of the referent table.
        
        Args:
            column_name: The name of the column to create.
            referrer_table_oid: The OID of the table getting the new column.
            referent_table_oid: The OID of the table being referenced.
        """
        
        ...
    
    @api("data_modeling.add_mapping_table")
    def data_modeling_add_mapping_table(self, /, table_name: str, mapping_columns: list[MappingColumn], schema_oid: int, database_id: int, **kwargs):
        """    
        Add a mapping table to give a many-to-many link between referents.
        
        The foreign key columns in the mapping table will reference the `id`
        column of the referent tables.
        
        Args:
            table_name: The name for the new mapping table.
            schema_oid: The OID of the schema for the mapping table.
            mapping_columns: The foreign key columns to create in the
                mapping table.
        """
        
        ...
    
    @api("data_modeling.change_primary_key_column")
    def data_modeling_change_primary_key_column(self, /, column_attnum: int, table_oid: int, database_id: int, default: Optional[Literal['IDENTITY', 'UUIDv4']] = None, drop_existing_pk_column: bool = False, **kwargs):
        """    
        Change which column is used for a single-column primary key.
        
        The `default` settings map as follows:
            - 'IDENTITY': `GENERATED BY DEFAULT AS IDENTITY`
            - 'UUIDv4': `gen_random_uuid()`
            - null: No default set
        
        Note that for clarity and safety, we *do not* drop any preexisitng
        default on the column targeted.
        
        Note that in cases where 'IDENTITY' is requested, but the column is
        not an integer, we first attempt to cast the column to `integer`,
        and then proceed only if that succeeds.
        
        Args:
            column_attnum: The attnum of the column to use for the pkey.
            table_oid: The OID of the table whose primary key we'll set.
            database_id: The Django id of the database containing the table.
            default: A flag specifying the default generating function.
            drop_existing_pk_column: Whether we should drop the current pkey
                column.
        """
        
        ...
    
    @api("data_modeling.move_columns")
    def data_modeling_move_columns(self, /, source_table_oid: int, target_table_oid: int, move_column_attnums: list[int], database_id: int, **kwargs):
        """    
        Extract columns from a table to a referent table, linked by a foreign key.
        
        Args:
            source_table_oid: The OID of the source table whose column(s) we'll extract.
            target_table_oid: The OID of the target table where the extracted column(s) will be added.
            move_column_attnums: The list of attnum(s) to move from source table to the target table.
            database_id: The Django id of the database containing the table.
        """
        
        ...
    
    @api("data_modeling.split_table")
    def data_modeling_split_table(self, /, table_oid: int, column_attnums: list, extracted_table_name: str, database_id: int, relationship_fk_column_name: str = None, **kwargs) -> SplitTableInfo:
        """    
        Extract columns from a table to create a new table, linked by a foreign key.
        
        Args:
            table_oid: The OID of the table whose columns we'll extract.
            column_attnums: A list of the attnums of the columns to extract.
            extracted_table_name: The name of the new table to be made from the extracted columns.
            database_id: The Django id of the database containing the table.
            relationship_fk_column_name: The name to give the new foreign key column in the remainder table (optional)
        
        Returns:
            The SplitTableInfo object describing the details for the created table as a result of column extraction.
        """
        
        ...
    
    @api("data_modeling.suggest_types")
    def data_modeling_suggest_types(self, /, table_oid: int, database_id: int, **kwargs) -> dict:
        """    
        Infer the best type for each column in the table.
        
        Currently we only suggest different types for columns which originate
        as type `text`.
        
        Args:
            table_oid: The OID of the table whose columns we're inferring types for.
            database_id: The Django id of the database containing the table.
        
        The response JSON will have attnum keys, and values will be the
        result of `format_type` for the inferred type of each column, i.e., the
        canonical string referring to the type.
        """
        
        ...
    
    @api("databases.delete")
    def databases_delete(self, /, database_oid: int, database_id: int, **kwargs):
        """    
        Drop a database from the server.
        
        Args:
            database_oid: The OID of the database to delete on the database.
            database_id: The Django id of the database to connect to.
        """
        
        ...
    
    @api("databases.get")
    def databases_get(self, /, database_id: int, **kwargs) -> DatabaseInfo:
        """    
        Get information about a database.
        
        Args:
            database_id: The Django id of the database.
        
        Returns:
            Information about the database, and the current user privileges.
        """
        
        ...
    
    @api("databases.upgrade_sql")
    def databases_upgrade_sql(self, /, database_id: int, username: str = None, password: str = None, **kwargs):
        """    
        Install, Upgrade, or Reinstall the Mathesar SQL on a database.
        
        If no `username` and `password` are submitted, we will determine the
        role which owns the `msar` schema on the database, then use that role
        for the upgrade.
        
        Args:
            database_id: The Django id of the database.
            username: The username of the role used for upgrading.
            password: The password of the role used for upgrading.
        """
        
        ...
    
    @api("databases.configured.disconnect")
    def databases_configured_disconnect(self, /, database_id: int, schemas_to_remove: list[str] = ('msar', '__msar', 'mathesar_types'), strict: bool = True, role_name: str = None, password: str = None, disconnect_db_server: bool = False, **kwargs):
        """    
        Disconnect a configured database, after removing Mathesar SQL from it.
        
        If no `role_name` and `password` are submitted, we will determine the
        role which owns the `msar` schema on the database, then use that role
        for the SQL removal.
        
        All removals are performed safely, and without `CASCADE`. This is to
        make sure the user can't accidentally lose data calling this
        function.
        
        Args:
            database_id: The Django id of the database.
            schemas_to_remove: Mathesar schemas we should remove SQL from.
            strict: If True, we throw an exception and roll back changes if
                we fail to remove any objects which we expected to remove.
            role_name: the username of the role used for upgrading.
            password: the password of the role used for upgrading.
            disconnect_db_server: If True, will delete the stored server
                metadata(host, port, role credentials) from Mathesar.
                This is intended for optional use while disconnecting the
                last database on the server.
        """
        
        ...
    
    @api("databases.configured.list")
    def databases_configured_list(self, /, server_id: int = None, **kwargs) -> list[ConfiguredDatabaseInfo]:
        """    
        List information about databases for a server. Exposed as `list`.
        
        If called with no `server_id`, all databases for all servers are listed.
        
        Args:
            server_id: The Django id of the server containing the databases.
        
        Returns:
            A list of database details.
        """
        
        ...
    
    @api("databases.configured.patch")
    def databases_configured_patch(self, /, database_id: int, patch: ConfiguredDatabasePatch, **kwargs) -> ConfiguredDatabaseInfo:
        """    
        Patch a configured database, given its id.
        
        Args:
            database_id: The Django id of the database
            patch: An object containing the fields to update.
        
        Returns:
            An object describing the database.
        """
        
        ...
    
    @api("databases.privileges.list_direct")
    def databases_privileges_list_direct(self, /, database_id: int, **kwargs) -> list[DBPrivileges]:
        """    
        List database privileges for non-inherited roles.
        
        Args:
            database_id: The Django id of the database.
        
        Returns:
            A list of database privileges.
        """
        
        ...
    
    @api("databases.privileges.replace_for_roles")
    def databases_privileges_replace_for_roles(self, /, privileges: list[DBPrivileges], database_id: int, **kwargs) -> list[DBPrivileges]:
        """    
        Replace direct database privileges for roles.
        
        Possible privileges are `CONNECT`, `CREATE`, and `TEMPORARY`.
        
        Only roles which are included in a passed `DBPrivileges` object are
        affected.
        
        WARNING: Any privilege included in the `direct` list for a role
        is GRANTed, and any privilege not included is REVOKEd.
        
        Attributes:
            privileges: The new privilege sets for roles.
            database_id: The Django id of the database.
        
        Returns:
            A list of all non-default privileges on the database after the
            operation.
        """
        
        ...
    
    @api("databases.privileges.transfer_ownership")
    def databases_privileges_transfer_ownership(self, /, new_owner_oid: int, database_id: int, **kwargs) -> DatabaseInfo:
        """    
        Transfers ownership of the current database to a new owner.
        
        Attributes:
            new_owner_oid: The OID of the role whom we want to be the new owner of the current database.
            database_id: The Django id of the database whose ownership is to be transferred.
        
        Note: To successfully transfer ownership of a database to a new owner the current user must:
            - Be a Superuser/Owner of the current database.
            - Be a `MEMBER` of the new owning role. i.e. The current role should be able to `SET ROLE`
              to the new owning role.
            - Have `CREATEDB` privilege.
        
        Returns:
            Information about the database, and the current user privileges.
        """
        
        ...
    
    @api("databases.setup.connect_existing")
    def databases_setup_connect_existing(self, /, host: str, database: str, role: str, password: str, port: Optional[int] = None, sample_data: list[str] = (), nickname: Optional[str] = None, **kwargs) -> DatabaseConnectionResult:
        """    
        Connect Mathesar to an existing database on a server.
        
        The calling user will get access to that database using the
        credentials passed to this function.
        
        Args:
            host: The host of the database server.
            port: The port of the database server.
            database: The name of the database on the server.
            role: The role on the server to use for the connection.
            password: A password valid for the role.
            sample_data: A list of strings requesting that some example data
                sets be installed on the underlying database. Valid list
                members are:
                - 'bike_shop'
                - 'hardware_store'
                - 'ice_cream_employees'
                - 'library_management'
                - 'library_makerspace'
                - 'museum_exhibits'
                - 'nonprofit_grants'
            nickname: An optional nickname for the database.
        """
        
        ...
    
    @api("databases.setup.create_new")
    def databases_setup_create_new(self, /, database: str, sample_data: list[str] = (), nickname: Optional[str] = None, **kwargs) -> DatabaseConnectionResult:
        """    
        Set up a new database on the internal server.
        
        The calling user will get access to that database using the default
        role stored in Django settings.
        
        Args:
            database: The name of the new database.
            sample_data: A list of strings requesting that some example data
                sets be installed on the underlying database. Valid list
                members are:
                - 'bike_shop'
                - 'hardware_store'
                - 'ice_cream_employees'
                - 'library_management'
                - 'library_makerspace'
                - 'museum_exhibits'
                - 'nonprofit_grants'
            nickname: An optional nickname for the database.
        """
        
        ...
    
    @api("explorations.add")
    def explorations_add(self, /, exploration_def: ExplorationDef, **kwargs) -> ExplorationInfo:
        """    
        Add a new exploration.
        
        Args:
            exploration_def: A dict describing the exploration to create.
        
        Returns:
            The exploration details for the newly created exploration.
        """
        
        ...
    
    @api("explorations.delete")
    def explorations_delete(self, /, exploration_id: int, **kwargs):
        """    
        Delete an exploration.
        
        Args:
            exploration_id: The Django id of the exploration to delete.
        """
        
        ...
    
    @api("explorations.get")
    def explorations_get(self, /, exploration_id: int, **kwargs) -> ExplorationInfo:
        """    
        List information about an exploration.
        
        Args:
            exploration_id: The Django id of the exploration.
        
        Returns:
            Exploration details for a given exploration_id.
        """
        
        ...
    
    @api("explorations.list")
    def explorations_list(self, /, database_id: int, schema_oid: int = None, **kwargs) -> list[ExplorationInfo]:
        """    
        List information about explorations for a database. Exposed as `list`.
        
        Args:
            database_id: The Django id of the database containing the explorations.
            schema_oid: The OID of the schema containing the base table(s) of the exploration(s).(optional)
        
        Returns:
            A list of exploration details.
        """
        
        ...
    
    @api("explorations.replace")
    def explorations_replace(self, /, new_exploration: ExplorationInfo, **kwargs) -> ExplorationInfo:
        """    
        Replace a saved exploration.
        
        Args:
            new_exploration: A dict describing the exploration to replace, including the updated fields.
        
        Returns:
            The exploration details for the replaced exploration.
        """
        
        ...
    
    @api("explorations.run")
    def explorations_run(self, /, exploration_def: ExplorationDef, limit: int = 100, offset: int = 0, **kwargs) -> ExplorationResult:
        """    
        Run an exploration.
        
        Args:
            exploration_def: A dict describing an exploration to run.
            limit: The max number of rows to return.(default 100)
            offset: The number of rows to skip.(default 0)
        
        Returns:
            The result of the exploration run.
        """
        
        ...
    
    @api("explorations.run_saved")
    def explorations_run_saved(self, /, exploration_id: int, limit: int = 100, offset: int = 0, **kwargs) -> ExplorationResult:
        """    
        Run a saved exploration.
        
        Args:
            exploration_id: The Django id of the exploration to run.
            limit: The max number of rows to return.(default 100)
            offset: The number of rows to skip.(default 0)
        
        Returns:
            The result of the exploration run.
        """
        
        ...
    
    @api("records.add")
    def records_add(self, /, record_def: dict, table_oid: int, database_id: int, return_record_summaries: bool = False, **kwargs) -> RecordAdded:
        """    
        Add a single record to a table.
        
        The form of the `record_def` is determined by the underlying table.
        Keys should be attnums, and values should be the desired value for
        that column in the created record. Missing keys will use default
        values (if set on the DB), and explicit `null` values will set null
        for that value regardless of default (with obvious exceptions where
        that would violate some constraint)
        
        Args:
            record_def: An object representing the record to be added.
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
            return_record_summaries: Whether to return summaries of the added
                record.
        
        Returns:
            The created record, along with some metadata.
        """
        
        ...
    
    @api("records.delete")
    def records_delete(self, /, record_ids: list[Any], table_oid: int, database_id: int, **kwargs) -> Optional[int]:
        """    
        Delete records from a table by primary key.
        
        Args:
            record_ids: The primary key values of the records to be deleted.
            table_oid: The identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
        
        Returns:
            The number of records deleted.
        """
        
        ...
    
    @api("records.get")
    def records_get(self, /, record_id: Any, table_oid: int, database_id: int, return_record_summaries: bool = False, table_record_summary_templates: dict[str, Any] = None, **kwargs) -> RecordList:
        """    
        Get single record from a table by its primary key.
        
        Args:
            record_id: The primary key value of the record to be gotten.
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
            return_record_summaries: Whether to return summaries of the
                retrieved record.
            table_record_summary_templates: A dict of record summary templates.
                If none are provided, then the templates will be take from the
                Django metadata. Any templates provided will take precedence on a
                per-table basis over the stored metadata templates. The purpose of
                this function parameter is to allow clients to generate record
                summary previews without persisting any metadata.
        Returns:
            The requested record, along with some metadata.
        """
        
        ...
    
    @api("records.list")
    def records_list(self, /, table_oid: int, database_id: int, limit: int = None, offset: int = None, order: list[OrderBy] = None, filter: Filter = None, grouping: Grouping = None, return_record_summaries: bool = False, **kwargs) -> RecordList:
        """    
        List records from a table, and its row count. Exposed as `list`.
        
        Args:
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
            limit: The maximum number of rows we'll return.
            offset: The number of rows to skip before returning records from
                following rows.
            order: An array of ordering definition objects.
            filter: An array of filter definition objects.
            grouping: An array of group definition objects.
            return_record_summaries: Whether to return summaries of retrieved
                records.
        
        Returns:
            The requested records, along with some metadata.
        """
        
        ...
    
    @api("records.patch")
    def records_patch(self, /, record_def: dict, record_id: Any, table_oid: int, database_id: int, return_record_summaries: bool = False, **kwargs) -> RecordAdded:
        """    
        Modify a record in a table.
        
        The form of the `record_def` is determined by the underlying table.
        Keys should be attnums, and values should be the desired value for
        that column in the modified record. Explicit `null` values will set
        null for that value (with obvious exceptions where that would violate
        some constraint).
        
        Args:
            record_def: An object representing the record to be added.
            record_id: The primary key value of the record to modify.
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
            return_record_summaries: Whether to return summaries of the
                modified record.
        
        Returns:
            The modified record, along with some metadata.
        """
        
        ...
    
    @api("records.search")
    def records_search(self, /, table_oid: int, database_id: int, search_params: list[SearchParam] = (), limit: int = 10, offset: int = 0, return_record_summaries: bool = False, **kwargs) -> RecordList:
        """    
        List records from a table according to `search_params`.
        
        
        Literals will be searched for in a basic way in string-like columns,
        but will have to match exactly in non-string-like columns.
        
        Records are assigned a score based on how many matches, and of what
        quality, they have with the passed search parameters.
        
        Args:
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
            search_params: Results are ranked and filtered according to the
                           objects passed here.
            limit: The maximum number of rows we'll return.
        
        Returns:
            The requested records, along with some metadata.
        """
        
        ...
    
    @api("roles.add")
    def roles_add(self, /, rolename: str, database_id: int, password: str = None, login: bool = None, **kwargs) -> RoleInfo:
        """    
        Add a new login/non-login role on a database server.
        
        Args:
            rolename: The name of the role to be created.
            database_id: The Django id of the database.
            password: The password for the rolename to set.
            login: Whether the role to be created could login.
        
        Returns:
            A dict describing the created role.
        """
        
        ...
    
    @api("roles.delete")
    def roles_delete(self, /, role_oid: int, database_id: int, **kwargs):
        """    
        Drop a role on a database server.
        
        Args:
            role_oid: The OID of the role to drop on the database.
            database_id: The Django id of the database.
        """
        
        ...
    
    @api("roles.get_current_role")
    def roles_get_current_role(self, /, database_id: int, **kwargs) -> dict:
        """    
        Get information about the current role and all the parent role(s) whose
        privileges are immediately available to current role without doing SET ROLE.
        
        Args:
            database_id: The Django id of the database.
        
        Returns:
            A dict describing the current role.
        """
        
        ...
    
    @api("roles.list")
    def roles_list(self, /, database_id: int, **kwargs) -> list[RoleInfo]:
        """    
        List information about roles for a database server. Exposed as `list`.
        Requires a database id inorder to connect to the server.
        
        Args:
            database_id: The Django id of the database.
        
        Returns:
            A list of roles present on the database server.
        """
        
        ...
    
    @api("roles.set_members")
    def roles_set_members(self, /, parent_role_oid: int, members: list, database_id: int, **kwargs) -> RoleInfo:
        """    
        Grant/Revoke direct membership to/from roles.
        
        Args:
          parent_role_oid: The OID of role whose membership will be granted/revoked to/from other roles.
          members: An array of role OID(s) whom we want to grant direct membership of the parent role.
                   Only the OID(s) present in the array will be granted membership of parent role,
                   Membership will be revoked for existing members not present in this array.
        
        Returns:
            A dict describing the updated information of the parent role.
        """
        
        ...
    
    @api("roles.configured.add")
    def roles_configured_add(self, /, server_id: int, name: str, password: str, **kwargs) -> ConfiguredRoleInfo:
        """    
        Configure a role in Mathesar for a database server.
        
        Args:
            server_id: The Django id of the Server to contain the configured role.
            name: The name of the role.
            password: The password for the role.
        
        Returns:
            The newly configured role.
        """
        
        ...
    
    @api("roles.configured.delete")
    def roles_configured_delete(self, /, configured_role_id: int, **kwargs):
        """    
        Delete a configured role for a server.
        
        Args:
            configured_role_id: The Django id of the ConfiguredRole model instance.
        """
        
        ...
    
    @api("roles.configured.list")
    def roles_configured_list(self, /, server_id: int, **kwargs) -> list[ConfiguredRoleInfo]:
        """    
        List information about roles configured in Mathesar. Exposed as `list`.
        
        Args:
            server_id: The Django id of the Server containing the configured roles.
        
        Returns:
            A list of configured roles.
        """
        
        ...
    
    @api("roles.configured.set_password")
    def roles_configured_set_password(self, /, configured_role_id: int, password: str, **kwargs):
        """    
        Set the password of a configured role for a server.
        
        Args:
            configured_role_id: The Django id of the ConfiguredRole model instance.
            password: The password for the role.
        """
        
        ...
    
    @api("schemas.add")
    def schemas_add(self, /, name: str, database_id: int, owner_oid: int = None, description: Optional[str] = None, **kwargs) -> SchemaInfo:
        """    
        Add a schema
        
        Args:
            name: The name of the schema to add.
            database_id: The Django id of the database containing the schema.
            owner_oid: The OID of the role who will own the new schema.
                If owner_oid is None, the current role will be the owner of the new schema.
            description: A description of the schema
        
        Returns:
            The SchemaInfo describing the user-defined schema in the database.
        """
        
        ...
    
    @api("schemas.delete")
    def schemas_delete(self, /, schema_oids: list[int], database_id: int, **kwargs):
        """    
        Safely drop all objects in each schema, then the schemas themselves.
        
        Does not work on the internal `msar` schema.
        
        If any passed schema doesn't exist, an exception will be raised. If
        any object exists in a schema which isn't passed, but which depends
        on an object in a passed schema, an exception will be raised.
        
        Args:
            schema_oids: The OIDs of the schemas to delete.
            database_id: The Django id of the database containing the schema.
        """
        
        ...
    
    @api("schemas.get")
    def schemas_get(self, /, schema_oid: int, database_id: int, **kwargs) -> SchemaInfo:
        """    
        Get information about a schema in a database.
        
        Args:
            schema_oid: The OID of the schema to get.
            database_id: The Django id of the database containing the table.
        
        Returns:
            The SchemaInfo describing the user-defined schema in the database.
        """
        
        ...
    
    @api("schemas.list")
    def schemas_list(self, /, database_id: int, **kwargs) -> list[SchemaInfo]:
        """    
        List information about schemas in a database. Exposed as `list`.
        
        Args:
            database_id: The Django id of the database containing the table.
        
        Returns:
            A list of SchemaInfo objects
        """
        
        ...
    
    @api("schemas.patch")
    def schemas_patch(self, /, schema_oid: int, database_id: int, patch: SchemaPatch, **kwargs) -> SchemaInfo:
        """    
        Patch a schema, given its OID.
        
        Args:
            schema_oid: The OID of the schema to delete.
            database_id: The Django id of the database containing the schema.
            patch: A SchemaPatch object containing the fields to update.
        
        Returns:
            The SchemaInfo describing the user-defined schema in the database.
        """
        
        ...
    
    @api("schemas.privileges.list_direct")
    def schemas_privileges_list_direct(self, /, schema_oid: int, database_id: int, **kwargs) -> list[SchemaPrivileges]:
        """    
        List direct schema privileges for roles.
        
        Args:
            schema_oid: The OID of the schema whose privileges we'll list.
            database_id: The Django id of the database containing the schema.
        
        Returns:
            A list of schema privileges.
        """
        
        ...
    
    @api("schemas.privileges.replace_for_roles")
    def schemas_privileges_replace_for_roles(self, /, privileges: list[SchemaPrivileges], schema_oid: int, database_id: int, **kwargs) -> list[SchemaPrivileges]:
        """    
        Replace direct schema privileges for roles.
        
        Possible privileges are `USAGE` and `CREATE`.
        
        Only roles which are included in a passed `SchemaPrivileges` object
        are affected.
        
        WARNING: Any privilege included in the `direct` list for a role
        is GRANTed, and any privilege not included is REVOKEd.
        
        Args:
            privileges: The new privilege sets for roles.
            schema_oid: The OID of the affected schema.
            database_id: The Django id of the database containing the schema.
        
        Returns:
            A list of all non-default privileges on the schema after the
            operation.
        """
        
        ...
    
    @api("schemas.privileges.transfer_ownership")
    def schemas_privileges_transfer_ownership(self, /, schema_oid: int, new_owner_oid: int, database_id: int, **kwargs) -> SchemaInfo:
        """    
        Transfers ownership of a given schema to a new owner.
        
        Attributes:
            schema_oid: The OID of the schema to transfer.
            new_owner_oid: The OID of the role whom we want to be the new owner of the schema.
        
        Note: To successfully transfer ownership of a schema to a new owner the current user must:
            - Be a Superuser/Owner of the schema.
            - Be a `MEMBER` of the new owning role. i.e. The current role should be able to `SET ROLE`
              to the new owning role.
            - Have `CREATE` privilege for the database.
        
        Returns:
            Information about the schema, and the current user privileges.
        """
        
        ...
    
    @api("servers.configured.list")
    def servers_configured_list(self, **kwargs) -> list[ConfiguredServerInfo]:
        """    
        List information about servers. Exposed as `list`.
        
        Returns:
            A list of server details.
        """
        
        ...
    
    @api("servers.configured.patch")
    def servers_configured_patch(self, /, server_id: int, patch: ConfiguredServerPatch, **kwargs) -> ConfiguredServerInfo:
        """    
        Patch a server, given its id.
        
        Args:
            server: The Django id of the server
            patch: An object containing the fields to update.
        
        Returns:
            An object describing the server.
        """
        
        ...
    
    @api("tables.add")
    def tables_add(self, /, schema_oid: int, database_id: int, table_name: str = None, pkey_column_info: CreatablePkColumnInfo = {}, column_data_list: list[CreatableColumnInfo] = (), constraint_data_list: list[list[Union[ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint]]] = (), owner_oid: int = None, comment: str = None, **kwargs) -> int:
        """    
        Add a table with a default id column.
        
        Args:
            schema_oid: Identity of the schema in the user's database.
            database_id: The Django id of the database containing the table.
            table_name: Name of the table to be created.
            pkey_column_info: A dict describing the primary key column to be created for the new table.
            column_data_list: A list describing columns to be created for the new table, in order.
            constraint_data_list: A list describing constraints to be created for the new table.
            owner_oid: The OID of the role who will own the new table.
                If owner_oid is None, the current role will be the owner of the new table.
            comment: The comment for the new table.
        
        Returns:
            The `oid`, `name`, and `renamed_columns` of the created table.
        """
        
        ...
    
    @api("tables.delete")
    def tables_delete(self, /, table_oid: int, database_id: int, cascade: bool = False, **kwargs) -> str:
        """    
        Delete a table from a schema.
        
        Args:
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
            cascade: Whether to drop the dependent objects.
        
        Returns:
            The name of the dropped table.
        """
        
        ...
    
    @api("tables.get")
    def tables_get(self, /, table_oid: int, database_id: int, **kwargs) -> TableInfo:
        """    
        List information about a table for a schema.
        
        Args:
            table_oid: Identity of the table in the user's database.
            database_id: The Django id of the database containing the table.
        
        Returns:
            Table details for a given table oid.
        """
        
        ...
    
    @api("tables.get_import_preview")
    def tables_get_import_preview(self, /, table_oid: int, columns: list[PreviewableColumnInfo], database_id: int, limit: int = 20, **kwargs) -> list[dict]:
        """    
        Preview an imported table.
        
        Args:
            table_oid: Identity of the imported table in the user's database.
            columns: List of settings describing the casts to be applied to the columns.
            database_id: The Django id of the database containing the table.
            limit: The upper limit for the number of records to return.
        
        Returns:
            The records from the specified columns of the table.
        """
        
        ...
    
    @api("tables.get_with_metadata")
    def tables_get_with_metadata(self, /, table_oid: int, database_id: int, **kwargs) -> dict:
        """    
        Get information about a table in a schema, along with the associated table metadata.
        
        Args:
            table_oid: The OID of the table in the user's database.
            database_id: The Django id of the database containing the table.
        
        Returns:
            A dict describing table details along with its metadata.
        """
        
        ...
    
    @api("tables.import")
    def tables_import(self, /, data_file_id: int, schema_oid: int, database_id: int, table_name: Optional[str] = None, comment: Optional[str] = None, **kwargs) -> AddedTableInfo:
        """    
        Import a CSV/TSV into a table.
        
        Args:
            data_file_id: The Django id of the DataFile containing desired CSV/TSV.
            schema_oid: Identity of the schema in the user's database.
            database_id: The Django id of the database containing the table.
            table_name: Name of the table to be imported.
            comment: The comment for the new table.
        
        Returns:
            The `oid`, `name`, and `renamed_columns` of the created table.
        """
        
        ...
    
    @api("tables.list")
    def tables_list(self, /, schema_oid: int, database_id: int, **kwargs) -> list[TableInfo]:
        """    
        List information about tables for a schema. Exposed as `list`.
        
        Args:
            schema_oid: Identity of the schema in the user's database.
            database_id: The Django id of the database containing the table.
        
        Returns:
            A list of table details.
        """
        
        ...
    
    @api("tables.list_joinable")
    def tables_list_joinable(self, /, table_oid: int, database_id: int, max_depth: int = 3, **kwargs) -> JoinableTableInfo:
        """    
        List details for joinable tables.
        
        Args:
            table_oid: Identity of the table to get joinable tables for.
            database_id: The Django id of the database containing the table.
            max_depth: Specifies how far to search for joinable tables.
        
        Returns:
            Joinable table details for a given table.
        """
        
        ...
    
    @api("tables.list_with_metadata")
    def tables_list_with_metadata(self, /, schema_oid: int, database_id: int, **kwargs) -> list:
        """    
        List tables in a schema, along with the metadata associated with each table
        
        Args:
            schema_oid: PostgreSQL OID of the schema containing the tables.
            database_id: The Django id of the database containing the table.
        
        Returns:
            A list of table details along with metadata.
        """
        
        ...
    
    @api("tables.patch")
    def tables_patch(self, /, table_oid: str, table_data_dict: SettableTableInfo, database_id: int, **kwargs) -> str:
        """    
        Alter details of a preexisting table in a database.
        
        Args:
            table_oid: Identity of the table whose name, description or columns we'll modify.
            table_data_dict: A list describing desired table alterations.
            database_id: The Django id of the database containing the table.
        
        Returns:
            The name of the altered table.
        """
        
        ...
    
    @api("tables.metadata.list")
    def tables_metadata_list(self, /, database_id: int, **kwargs) -> list[TableMetaDataRecord]:
        """    
        List metadata associated with tables for a database.
        
        Args:
            database_id: The Django id of the database containing the table.
        
        Returns:
            Metadata object for a given table oid.
        """
        
        ...
    
    @api("tables.metadata.set")
    def tables_metadata_set(self, /, table_oid: int, metadata: TableMetaDataBlob, database_id: int, **kwargs):
        """    
        Set metadata for a table.
        
        Args:
            table_oid: The PostgreSQL OID of the table.
            metadata: A TableMetaDataBlob object describing desired table metadata to set.
            database_id: The Django id of the database containing the table.
        """
        
        ...
    
    @api("tables.privileges.list_direct")
    def tables_privileges_list_direct(self, /, table_oid: int, database_id: int, **kwargs) -> list[TablePrivileges]:
        """    
        List direct table privileges for roles.
        Args:
            table_oid: The OID of the table whose privileges we'll list.
            database_id: The Django id of the database containing the table.
        Returns:
            A list of table privileges.
        """
        
        ...
    
    @api("tables.privileges.replace_for_roles")
    def tables_privileges_replace_for_roles(self, /, privileges: list[TablePrivileges], table_oid: int, database_id: int, **kwargs) -> list[TablePrivileges]:
        """    
        Replace direct table privileges for roles.
        
        Possible privileges are `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `TRUNCATE`, `REFERENCES` and `TRIGGER`.
        
        Only roles which are included in a passed `TablePrivileges` object
        are affected.
        
        WARNING: Any privilege included in the `direct` list for a role
        is GRANTed, and any privilege not included is REVOKEd.
        
        Args:
            privileges: The new privilege sets for roles.
            table_oid: The OID of the affected table.
            database_id: The Django id of the database containing the table.
        
        Returns:
            A list of all non-default privileges on the table after the
            operation.
        """
        
        ...
    
    @api("tables.privileges.transfer_ownership")
    def tables_privileges_transfer_ownership(self, /, table_oid: int, new_owner_oid: int, database_id: int, **kwargs) -> TableInfo:
        """    
        Transfers ownership of a given table to a new owner.
        
        Attributes:
            table_oid: The OID of the table to transfer.
            new_owner_oid: The OID of the role whom we want to be the new owner of the table.
        
        Note: To successfully transfer ownership of a table to a new owner the current user must:
            - Be a Superuser/Owner of the table.
            - Be a `MEMBER` of the new owning role. i.e. The current role should be able to `SET ROLE`
              to the new owning role.
            - Have `CREATE` privilege on the table's schema.
        
        Returns:
            Information about the table, and the current user privileges.
        """
        
        ...
    
    @api("users.add")
    def users_add(self, /, user_def: UserDef, **kwargs) -> UserInfo:
        """    
        Add a new mathesar user.
        
        Args:
            user_def: A dict describing the user to create.
        
        Privileges:
            This endpoint requires the caller to be a superuser.
        
        Returns:
            The information of the created user.
        """
        
        ...
    
    @api("users.delete")
    def users_delete(self, /, user_id: int, **kwargs):
        """    
        Delete a mathesar user.
        
        Args:
            user_id: The Django id of the user to delete.
        
        Privileges:
            This endpoint requires the caller to be a superuser.
        """
        
        ...
    
    @api("users.get")
    def users_get(self, /, user_id: int, **kwargs) -> UserInfo:
        """    
        List information about a mathesar user.
        
        Args:
            user_id: The Django id of the user.
        
        Returns:
            User information for a given user_id.
        """
        
        ...
    
    @api("users.list")
    def users_list(self, **kwargs) -> list[UserInfo]:
        """    
        List information about all mathesar users. Exposed as `list`.
        
        Returns:
            A list of information about mathesar users.
        """
        
        ...
    
    @api("users.patch_other")
    def users_patch_other(self, /, user_id: int, username: str, is_superuser: bool, email: str, full_name: str, display_language: str, **kwargs) -> UserInfo:
        """    
        Alter details of a mathesar user, given its user_id.
        
        Args:
            user_id: The Django id of the user.
            username: The username of the user.
            email: The email of the user.
            is_superuser: Specifies whether to set the user as a superuser.
            full_name: The full name of the user.
            display_language: Specifies the display language for the user, can be set to either `en` or `ja`.
        
        Privileges:
            This endpoint requires the caller to be a superuser.
        
        Returns:
            Updated user information for a given user_id.
        """
        
        ...
    
    @api("users.patch_self")
    def users_patch_self(self, /, username: str, email: str, full_name: str, display_language: str, **kwargs) -> UserInfo:
        """    
        Alter details of currently logged in mathesar user.
        
        Args:
            username: The username of the user.
            email: The email of the user.
            full_name: The full name of the user.
            display_language: Specifies the display language for the user, can be set to either `en` or `ja`.
        
        Returns:
            Updated user information of the caller.
        """
        
        ...
    
    @api("users.password.replace_own")
    def users_password_replace_own(self, /, old_password: str, new_password: str, **kwargs):
        """    
        Alter password of currently logged in mathesar user.
        
        Args:
            old_password: Old password of the currently logged in user.
            new_password: New password of the user to set.
        """
        
        ...
    
    @api("users.password.revoke")
    def users_password_revoke(self, /, user_id: int, new_password: str, **kwargs):
        """    
        Alter password of a mathesar user, given its user_id.
        
        Args:
            user_id: The Django id of the user.
            new_password: New password of the user to set.
        
        Privileges:
            This endpoint requires the caller to be a superuser.
        """
        
        ...
