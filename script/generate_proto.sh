#!/bin/bash

src="../all_proto"
dst="../milvus_connector/protocol"

files=$(find "$src" -type f -name "*.proto")

for file in $files; do
  filename=$(basename "$file" .proto)

  python -m grpc_tools.protoc -I "$src" --python_out="$dst" --grpc_python_out="$dst" --pyi_out="$dst" "$src/$filename.proto"
done

files=$(find "$dst" -type f -name "*.py*")

if [[ $(uname -s) == "Darwin" ]]; then
    if ! brew --prefix --installed gnu-sed >/dev/null 2>&1; then
        brew install gnu-sed
    fi
    export PATH="/usr/local/opt/gsed/libexec/gnubin:$PATH"
fi

for file in $files; do
  sed -i '/^import.*_pb2/ s/^/from . /' $file
done

echo "generate_proto done."