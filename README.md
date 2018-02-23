# Serverless Accessioning Examples
Uses serverless AWS to provide accession numbers using a combination of API Gateway, Lambda and DynamoDB.

No servers, highly scalable, highly available. 

Cost approx $0.50 per million calls.

## Get Sequenced Accession
```
curl -X GET \
  https://nycxgji7w3.execute-api.us-east-1.amazonaws.com/dev/accession \
```
## Get UUID:
```
curl -X GET \
  https://nycxgji7w3.execute-api.us-east-1.amazonaws.com/dev/uuid
```

## Get Sha1 (POST):
```
curl -X POST \
  https://nycxgji7w3.execute-api.us-east-1.amazonaws.com/dev/sha1 \
  -d '{
    "hello": "world"
}'
```
