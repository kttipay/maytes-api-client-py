# OAuthTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** |  | 
**client_id** | **UUID** |  | 
**client_secret** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from maytes_api_client.models.o_auth_token_request import OAuthTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthTokenRequest from a JSON string
o_auth_token_request_instance = OAuthTokenRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthTokenRequest.to_json())

# convert the object into a dict
o_auth_token_request_dict = o_auth_token_request_instance.to_dict()
# create an instance of OAuthTokenRequest from a dict
o_auth_token_request_from_dict = OAuthTokenRequest.from_dict(o_auth_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


