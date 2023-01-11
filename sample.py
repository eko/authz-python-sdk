import grpc;
import authz_sdk.client as authz
import authz_sdk.api_pb2 as proto

# Initialize client
client = authz.Client('localhost:8081', '91f50c68-91e2-11ed-b84d-acde48001122', 'pvXX89f7L4257jogy3-r--XGvs3TrH6laR8i5zwAIEcqMLQm')

# Retrieve or create principal
try:
    principal = client.stub.PrincipalGet(proto.PrincipalGetRequest(id='user-123'))
    print('principal retrieved: {}', principal)
except grpc.RpcError as e:
        response = client.stub.PrincipalCreate(proto.PrincipalCreateRequest(
            id='user-123',
            attributes=[
                proto.Attribute(key='email', value='johndoe@acme.tld'),
            ],
        ))

        print('principal created: {}', response)

# Retrieve or create resource
try:
    resource = client.stub.ResourceGet(proto.ResourceGetRequest(id='post.123'))
    print('resource retrieved: {}', resource)
except grpc.RpcError as e:
    response = client.stub.ResourceCreate(proto.ResourceCreateRequest(
        id='post.123',
        kind='post',
        value='123',
        attributes=[
            proto.Attribute(key='owner_email', value='johndoe@acme.tld'),
        ],
    ))

    print('resource created: {}', response)

# Retrieve or create policy
try:
    policy = client.stub.PolicyGet(proto.PolicyGetRequest(id='post-owners'))
    print('policy retrieved: {}', policy)
except grpc.RpcError as e:
    response = client.stub.PolicyCreate(proto.PolicyCreateRequest(
        id='post-owners',
        resources=['post.*'],
        actions=['edit', 'delete'],
        attribute_rules=[
            'principal.email == resource.owner_email',
        ],
    ))
    print('policy created: {}', response)
else:
    print('policy retrieved: {}', policy)

# Check if principal is allowed
result = client.IsAllowed(
    principal='user-123',
    resource_kind='post',
    resource_value='123',
    action='edit',
)

print(result)