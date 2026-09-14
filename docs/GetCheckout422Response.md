# GetCheckout422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**error** | **str** |  | 
**code** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from maytes_api_client.models.get_checkout422_response import GetCheckout422Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCheckout422Response from a JSON string
get_checkout422_response_instance = GetCheckout422Response.from_json(json)
# print the JSON string representation of the object
print(GetCheckout422Response.to_json())

# convert the object into a dict
get_checkout422_response_dict = get_checkout422_response_instance.to_dict()
# create an instance of GetCheckout422Response from a dict
get_checkout422_response_from_dict = GetCheckout422Response.from_dict(get_checkout422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


