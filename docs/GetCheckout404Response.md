# GetCheckout404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**error** | **str** |  | 
**code** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from maytes_api_client.models.get_checkout404_response import GetCheckout404Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCheckout404Response from a JSON string
get_checkout404_response_instance = GetCheckout404Response.from_json(json)
# print the JSON string representation of the object
print(GetCheckout404Response.to_json())

# convert the object into a dict
get_checkout404_response_dict = get_checkout404_response_instance.to_dict()
# create an instance of GetCheckout404Response from a dict
get_checkout404_response_from_dict = GetCheckout404Response.from_dict(get_checkout404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


