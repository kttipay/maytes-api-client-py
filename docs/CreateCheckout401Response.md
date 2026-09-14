# CreateCheckout401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**error** | **str** |  | 
**code** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from maytes_api_client.models.create_checkout401_response import CreateCheckout401Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCheckout401Response from a JSON string
create_checkout401_response_instance = CreateCheckout401Response.from_json(json)
# print the JSON string representation of the object
print(CreateCheckout401Response.to_json())

# convert the object into a dict
create_checkout401_response_dict = create_checkout401_response_instance.to_dict()
# create an instance of CreateCheckout401Response from a dict
create_checkout401_response_from_dict = CreateCheckout401Response.from_dict(create_checkout401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


