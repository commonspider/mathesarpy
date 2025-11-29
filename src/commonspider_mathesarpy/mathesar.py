from typing import Any

from .api import API
from .classes import SearchParam, RecordList, RecordAdded, UserDef, UserInfo, RoleInfo, ConfiguredRoleInfo, \
    CollaboratorInfo
from .exceptions import DuplicateObject, IntegrityError, UndefinedObject, DoesNotExist


class Columns:
    def __init__(self, mathesar: API, /, table_oid: int, database_id: int):
        self._columns: dict[str, int] = {
            col["name"]: col["id"]
            for col in mathesar.columns_list(
                table_oid=table_oid,
                database_id=database_id
            )
        }

    def __getitem__(self, item: str | int) -> int:
        if isinstance(item, str):
            return self._columns[item]
        elif isinstance(item, int):
            return item
        else:
            raise TypeError


class Mathesar(API):
    def records_search(
            self, /,
            table_oid: int,
            database_id: int,
            search_params: list[SearchParam] = (),
            search_literals: dict[str, str] = None,
            limit: int = 10,
            offset: int = 0,
            return_record_summaries: bool = False,
            **kwargs
    ) -> RecordList:
        if search_literals is not None:
            columns = Columns(self, table_oid=table_oid, database_id=database_id)
            search_params = list(search_params)
            search_params.extend(
                SearchParam(
                    attnum=columns[name],
                    literal=value
                )
                for name, value in search_literals.items()
            )
        return super().records_search(
            table_oid=table_oid,
            database_id=database_id,
            search_params=search_params,
            limit=limit,
            offset=offset,
            return_record_summaries=return_record_summaries
        )

    def records_add(
            self, /,
            record_def: dict[str | int, Any],
            table_oid: int,
            database_id: int,
            return_record_summaries: bool = False,
            **kwargs
    ) -> RecordAdded:
        columns = Columns(self, table_oid=table_oid, database_id=database_id)
        record_def = {
            columns[key]: value
            for key, value in record_def.items()
        }
        return super().records_add(
            database_id=database_id,
            table_oid=table_oid,
            record_def=record_def
        )

    def records_delete(
            self, /,
            table_oid: int,
            database_id: int,
            record_ids: list[Any] = (),
            record_list: RecordList = None,
            id_col: str = None,
            **kwargs
    ) -> list[Any]:
        if record_list is not None:
            columns = Columns(self, table_oid=table_oid, database_id=database_id)
            id_col = str(columns[id_col])
            record_ids = list(record_ids)
            record_ids.extend(
                record[id_col]
                for record in record_list
            )
        return super().records_delete(
            database_id=database_id,
            table_oid=table_oid,
            record_ids=record_ids
        )

    def users_get_id(self, /, user_id: int = None, username: str = None, **kwargs):
        if username is not None:
            for info in self.users_list():
                if info["username"] == username:
                    if user_id is None or user_id == info["id"]:
                        return info["id"]
                    else:
                        raise ValueError(f"User ID of {username} is not {user_id}")
            raise DoesNotExist(f"User matching query does not exist.")
        elif user_id is not None:
            return user_id
        else:
            raise TypeError("Missing either user_id or username")

    def users_get(self, /, user_id: int = None, username: str = None, **kwargs) -> UserInfo:
        for info in self.users_list():
            if info["username"] == username:
                if user_id is None or user_id == info["id"]:
                    return info
                else:
                    raise ValueError(f"Configured role ID of {username} is not {user_id}")
            elif info["id"] == user_id:
                return info
        if username is not None or user_id is not None:
            raise DoesNotExist("User matching query does not exist.")
        else:
            raise TypeError("Missing either configured_role_id or role_name")

    def users_add(self, /, user_def: UserDef, exists_ok: bool = False, **kwargs) -> UserInfo:
        try:
            return super().users_add(user_def=user_def)
        except IntegrityError:
            if exists_ok:
                return self.users_get(username=user_def["username"])
            else:
                raise

    def users_delete(
            self, /,
            user_id: int = None,
            username: str = None,
            missing_ok: bool = False,
            **kwargs
    ):
        try:
            user_id = self.users_get_id(user_id=user_id, username=username)
            return super().users_delete(user_id=user_id)
        except DoesNotExist:
            if not missing_ok:
                raise

    def collaborators_full_add(
            self, /,
            username: str,
            password: str,
            database_id: int,
            is_superuser: bool = False,
            email: str = None,
            full_name: str = None,
            display_language: str = None,
            rolename: str = None,
            role_password: str = None,
            exists_ok: bool = True,
            **kwargs
    ):
        rolename = rolename or username
        role_password = role_password or password
        self.roles_add(
            rolename=rolename,
            database_id=database_id,
            password=role_password,
            login=True,
            exists_ok=exists_ok
        )
        configured_role_info = self.roles_configured_add(
            server_id=database_id,
            name=rolename,
            password=role_password,
            exists_ok=exists_ok
        )
        user_def = UserDef(
            username=username,
            password=password,
            is_superuser=is_superuser,
            email=email,
            full_name=full_name,
            display_language=display_language
        )
        user_def = UserDef(**{
            k: v
            for k, v in user_def.items()
            if v is not None
        })
        user_info = self.users_add(
            user_def=user_def,
            exists_ok=exists_ok
        )
        return self.collaborators_add(
            database_id=database_id,
            user_id=user_info["id"],
            configured_role_id=configured_role_info["id"],
            exists_ok=exists_ok
        )

    def collaborators_full_delete(
            self, /,
            username: str,
            database_id: int,
            rolename: str = None,
            missing_ok: bool = True,
            **kwargs
    ):
        rolename = rolename or username
        self.collaborators_delete(
            username=username,
            database_id=database_id,
            missing_ok=missing_ok
        )
        self.users_delete(
            username=username,
            missing_ok=missing_ok
        )
        self.roles_configured_delete(
            rolename=rolename,
            server_id=database_id,
            missing_ok=missing_ok
        )
        self.roles_delete(
            database_id=database_id,
            rolename=rolename,
            missing_ok=missing_ok
        )

    def collaborators_get_id(
            self, /,
            collaborator_id: int = None,
            user_id: int = None,
            username: str = None,
            **kwargs
    ):
        if user_id is not None or username is not None:
            user_id = self.users_get(user_id=user_id, username=username)
            for info in self.collaborators_list():
                if info["user_id"] == user_id:
                    if collaborator_id is None or collaborator_id == info["id"]:
                        return info["id"]
                    else:
                        raise ValueError(f"Collaborator ID of {username} is not {collaborator_id}")
            raise DoesNotExist("Collaborator matching query does not exist.")
        elif collaborator_id is not None:
            return collaborator_id
        else:
            raise TypeError("Missing either collaborator_id or user_id or username")

    def collaborators_get(
            self, /,
            collaborator_id: int = None,
            user_id: int = None,
            username: str = None,
            database_id: int = None,
            **kwargs
    ) -> CollaboratorInfo:
        if username is not None:
            user_id = self.users_get_id(user_id=user_id, username=username)
        for info in self.collaborators_list(database_id=database_id):
            if user_id is not None and user_id == info["user_id"]:
                if collaborator_id is None or collaborator_id == info["id"]:
                    return info
                else:
                    raise ValueError(f"Collaborator ID of {username or user_id} is not {collaborator_id}")
            elif info["id"] == collaborator_id:
                return info
        if collaborator_id is not None or user_id is not None:
            raise DoesNotExist("Collaborator matching query does not exist.")
        else:
            raise TypeError("Missing either collaborator_id or user_id or username")

    def collaborators_add(
            self, /,
            database_id: int,
            user_id: int = None,
            username: str = None,
            configured_role_id: int = None,
            rolename: str = None,
            exists_ok: bool = False,
            **kwargs
    ) -> CollaboratorInfo:
        user_id = self.users_get_id(
            user_id=user_id,
            username=username
        )
        configured_role_id = self.roles_configured_get_id(
            configured_role_id=configured_role_id,
            rolename=rolename,
            server_id=database_id
        )
        try:
            return super().collaborators_add(
                database_id=database_id,
                user_id=user_id,
                configured_role_id=configured_role_id
            )
        except IntegrityError:
            if exists_ok:
                return self.collaborators_get(
                    username=username,
                    user_id=user_id,
                    database_id=database_id
                )
            else:
                raise

    def collaborators_delete(
            self, /,
            collaborator_id: int = None,
            username: str = None,
            database_id: int = None,
            missing_ok: bool = False,
            **kwargs
    ):
        try:
            collaborator_id = self.collaborators_get_id(
                collaborator_id=collaborator_id,
                username=username,
                database_id=database_id
            )
            super().collaborators_delete(collaborator_id=collaborator_id)
        except DoesNotExist:
            if not missing_ok:
                raise

    def roles_configured_get_id(
            self, /,
            configured_role_id: int = None,
            rolename: str = None,
            server_id: int = None,
            **kwargs
    ):
        if rolename is not None:
            for info in self.roles_configured_list(server_id=server_id):
                if info["name"] == rolename:
                    if configured_role_id is None or configured_role_id == info["id"]:
                        return info["id"]
                    else:
                        raise ValueError(f"Configured role ID of {rolename} is not {configured_role_id}")
            raise DoesNotExist(f"Configured Role matching query does not exist.")
        elif configured_role_id is not None:
            return configured_role_id
        else:
            raise TypeError("Missing either configured_role_id or configured_role_name")

    def roles_configured_get(
            self, /,
            configured_role_id: int = None,
            role_name: str = None,
            server_id: int = None,
            **kwargs
    ):
        for info in self.roles_configured_list(server_id=server_id):
            if info["name"] == role_name:
                if configured_role_id is None or configured_role_id == info["id"]:
                    return info
                else:
                    raise ValueError(f"Configured role ID of {role_name} is not {configured_role_id}")
            elif info["id"] == configured_role_id:
                return info
        if role_name is not None:
            raise UndefinedObject(f"Configured role with name {role_name} does not exist")
        elif configured_role_id is not None:
            raise UndefinedObject(f"Configured role with OID {configured_role_id} does not exist")
        else:
            raise TypeError("Missing either configured_role_id or role_name")

    def roles_configured_add(
            self, /,
            server_id: int,
            name: str,
            password: str,
            exists_ok: bool = False,
            **kwargs
    ) -> ConfiguredRoleInfo:
        try:
            return super().roles_configured_add(
                server_id=server_id,
                name=name,
                password=password
            )
        except IntegrityError:
            if exists_ok:
                return self.roles_configured_get(role_name=name, server_id=server_id)
            else:
                raise

    def roles_configured_delete(
            self, /,
            configured_role_id: int = None,
            rolename: str = None,
            server_id: int = None,
            missing_ok: bool = False,
            **kwargs
    ):
        try:
            configured_role_id = self.roles_configured_get_id(
                configured_role_id=configured_role_id,
                rolename=rolename,
                server_id=server_id
            )
            super().roles_configured_delete(configured_role_id=configured_role_id)
        except DoesNotExist:
            if not missing_ok:
                raise

    def roles_get_oid(self, /, role_oid: int = None, rolename: str = None, database_id: int = None, **kwargs):
        if rolename is not None:
            for info in self.roles_list(database_id=database_id):
                if info["name"] == rolename:
                    if role_oid is None or role_oid == info["oid"]:
                        return info["oid"]
                    else:
                        raise ValueError(f"Role OID of {rolename} is not {role_oid}")
            raise UndefinedObject(f"Role with name {rolename} does not exist")
        elif role_oid is not None:
            return role_oid
        else:
            raise TypeError("Missing either role_oid or role_name")

    def roles_get(self, /, database_id: int, role_oid: int = None, rolename: str = None, **kwargs):
        for info in self.roles_list(database_id=database_id):
            found = None
            if info["name"] == rolename:
                if role_oid is None or role_oid == info["oid"]:
                    found = info
                else:
                    raise ValueError(f"Role OID of {rolename} is not {role_oid}")
            elif info["oid"] == role_oid:
                found = info
            if found is not None:
                found["members"] = found["members"] or []
                return found
        if rolename is not None:
            raise UndefinedObject(f"Role with name {rolename} does not exist")
        elif role_oid is not None:
            raise UndefinedObject(f"Role with OID {role_oid} does not exist")
        else:
            raise TypeError("Missing either role_oid or role_name")

    def roles_add(
            self, /,
            rolename: str,
            database_id: int,
            password: str = None,
            login: bool = None,
            exists_ok: bool = False,
            **kwargs
    ) -> RoleInfo:
        try:
            return super().roles_add(
                rolename=rolename,
                database_id=database_id,
                password=password,
                login=login
            )
        except DuplicateObject:
            if exists_ok:
                return self.roles_get(database_id=database_id, rolename=rolename)
            else:
                raise

    def roles_delete(
            self, /,
            database_id: int,
            role_oid: int = None,
            rolename: str = None,
            missing_ok: bool = False,
            **kwargs
    ):
        try:
            role_oid = self.roles_get_oid(database_id=database_id, role_oid=role_oid, rolename=rolename)
            super().roles_delete(database_id=database_id, role_oid=role_oid)
        except UndefinedObject:
            if not missing_ok:
                raise

    def roles_append_member(
            self, /,
            database_id: int,
            parent_rolename: str = None,
            parent_role_oid: int = None,
            rolename: str = None,
            role_oid: str = None,
            **kwargs
    ):
        role_oid = self.roles_get_oid(
            role_oid=role_oid,
            rolename=rolename,
            database_id=database_id
        )
        parent_info = self.roles_get(
            database_id=database_id,
            rolename=parent_rolename,
            role_oid=parent_role_oid
        )
        members = [item["oid"] for item in parent_info["members"]]
        super().roles_set_members(
            parent_role_oid=parent_info["oid"],
            members=[*members, role_oid],
            database_id=database_id
        )
