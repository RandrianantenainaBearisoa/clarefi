mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.335.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.335.1/actions-runner-linux-x64-2.335.1.tar.gz
echo "4ef2f25285f0ae4477f1fe1e346db76d2f3ebf03824e2ddd1973a2819bf6c8cf  actions-runner-linux-x64-2.335.1.tar.gz" | shasum -a 256 -c
tar xzf ./actions-runner-linux-x64-2.335.1.tar.gz
./config.sh --url https://github.com/RandrianantenainaBearisoa/clarefi --token AXMKLCF25GLWIQYUPWYXLWTKITPLY
./run.sh