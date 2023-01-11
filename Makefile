.PHONY: deploy proto

deploy:
	python3 setup.py sdist
	twine upload dist/*

proto:
	python3 -m grpc_tools.protoc \
		-I$(GOPATH)/src/github.com/eko/authz/backend/api/proto \
		--python_out=authz_sdk \
		--pyi_out=authz_sdk \
		--grpc_python_out=authz_sdk \
		api.proto
