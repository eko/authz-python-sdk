from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Attribute(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class AuthenticateRequest(_message.Message):
    __slots__ = ["client_id", "client_secret"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ...) -> None: ...

class AuthenticateResponse(_message.Message):
    __slots__ = ["expires_in", "token", "type"]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    expires_in: int
    token: str
    type: str
    def __init__(self, token: _Optional[str] = ..., type: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...

class Check(_message.Message):
    __slots__ = ["action", "principal", "resource_kind", "resource_value"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    action: str
    principal: str
    resource_kind: str
    resource_value: str
    def __init__(self, principal: _Optional[str] = ..., resource_kind: _Optional[str] = ..., resource_value: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...

class CheckAnswer(_message.Message):
    __slots__ = ["action", "is_allowed", "principal", "resource_kind", "resource_value"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    action: str
    is_allowed: bool
    principal: str
    resource_kind: str
    resource_value: str
    def __init__(self, principal: _Optional[str] = ..., resource_kind: _Optional[str] = ..., resource_value: _Optional[str] = ..., action: _Optional[str] = ..., is_allowed: bool = ...) -> None: ...

class CheckRequest(_message.Message):
    __slots__ = ["checks"]
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    checks: _containers.RepeatedCompositeFieldContainer[Check]
    def __init__(self, checks: _Optional[_Iterable[_Union[Check, _Mapping]]] = ...) -> None: ...

class CheckResponse(_message.Message):
    __slots__ = ["checks"]
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    checks: _containers.RepeatedCompositeFieldContainer[CheckAnswer]
    def __init__(self, checks: _Optional[_Iterable[_Union[CheckAnswer, _Mapping]]] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ["actions", "attribute_rules", "id", "resources"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_RULES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    attribute_rules: _containers.RepeatedScalarFieldContainer[str]
    id: str
    resources: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., actions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., attribute_rules: _Optional[_Iterable[str]] = ...) -> None: ...

class PolicyCreateRequest(_message.Message):
    __slots__ = ["actions", "attribute_rules", "id", "resources"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_RULES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    attribute_rules: _containers.RepeatedScalarFieldContainer[str]
    id: str
    resources: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., actions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., attribute_rules: _Optional[_Iterable[str]] = ...) -> None: ...

class PolicyCreateResponse(_message.Message):
    __slots__ = ["policy"]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]] = ...) -> None: ...

class PolicyDeleteRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PolicyDeleteResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class PolicyGetRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PolicyGetResponse(_message.Message):
    __slots__ = ["policy"]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]] = ...) -> None: ...

class PolicyUpdateRequest(_message.Message):
    __slots__ = ["actions", "attribute_rules", "id", "resources"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_RULES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    attribute_rules: _containers.RepeatedScalarFieldContainer[str]
    id: str
    resources: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., actions: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[str]] = ..., attribute_rules: _Optional[_Iterable[str]] = ...) -> None: ...

class PolicyUpdateResponse(_message.Message):
    __slots__ = ["policy"]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]] = ...) -> None: ...

class Principal(_message.Message):
    __slots__ = ["attributes", "id", "roles"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    id: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class PrincipalCreateRequest(_message.Message):
    __slots__ = ["attributes", "id", "roles"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    id: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class PrincipalCreateResponse(_message.Message):
    __slots__ = ["principal"]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    principal: Principal
    def __init__(self, principal: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class PrincipalDeleteRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PrincipalDeleteResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class PrincipalGetRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PrincipalGetResponse(_message.Message):
    __slots__ = ["principal"]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    principal: Principal
    def __init__(self, principal: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class PrincipalUpdateRequest(_message.Message):
    __slots__ = ["attributes", "id", "roles"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    id: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class PrincipalUpdateResponse(_message.Message):
    __slots__ = ["principal"]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    principal: Principal
    def __init__(self, principal: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...

class Resource(_message.Message):
    __slots__ = ["attributes", "id", "kind", "value"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    id: str
    kind: str
    value: str
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[str] = ..., value: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class ResourceCreateRequest(_message.Message):
    __slots__ = ["attributes", "id", "kind", "value"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    id: str
    kind: str
    value: str
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[str] = ..., value: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class ResourceCreateResponse(_message.Message):
    __slots__ = ["resource"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Resource
    def __init__(self, resource: _Optional[_Union[Resource, _Mapping]] = ...) -> None: ...

class ResourceDeleteRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceDeleteResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ResourceGetRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ResourceGetResponse(_message.Message):
    __slots__ = ["resource"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Resource
    def __init__(self, resource: _Optional[_Union[Resource, _Mapping]] = ...) -> None: ...

class ResourceUpdateRequest(_message.Message):
    __slots__ = ["attributes", "id", "kind", "value"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    id: str
    kind: str
    value: str
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[str] = ..., value: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class ResourceUpdateResponse(_message.Message):
    __slots__ = ["resource"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Resource
    def __init__(self, resource: _Optional[_Union[Resource, _Mapping]] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ["id", "policies"]
    ID_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    policies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., policies: _Optional[_Iterable[str]] = ...) -> None: ...

class RoleCreateRequest(_message.Message):
    __slots__ = ["id", "policies"]
    ID_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    policies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., policies: _Optional[_Iterable[str]] = ...) -> None: ...

class RoleCreateResponse(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class RoleDeleteRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RoleDeleteResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class RoleGetRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RoleGetResponse(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class RoleUpdateRequest(_message.Message):
    __slots__ = ["id", "policies"]
    ID_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    policies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., policies: _Optional[_Iterable[str]] = ...) -> None: ...

class RoleUpdateResponse(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...
