# OAuthTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**refresh_token** | **str** |  | [optional] 
**expires_in** | **float** |  | 
**token_type** | **str** |  | 
**scope** | **str** |  | 

## Example

```python
from maytes_api_client.models.o_auth_token_response import OAuthTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthTokenResponse from a JSON string
o_auth_token_response_instance = OAuthTokenResponse.from_json(json)
# print the JSON string representation of the object
print(OAuthTokenResponse.to_json())

# convert the object into a dict
o_auth_token_response_dict = o_auth_token_response_instance.to_dict()
# create an instance of OAuthTokenResponse from a dict
o_auth_token_response_from_dict = OAuthTokenResponse.from_dict(o_auth_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


