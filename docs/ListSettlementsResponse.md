# ListSettlementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Settlement]**](Settlement.md) |  | 

## Example

```python
from maytes_api_client.models.list_settlements_response import ListSettlementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSettlementsResponse from a JSON string
list_settlements_response_instance = ListSettlementsResponse.from_json(json)
# print the JSON string representation of the object
print(ListSettlementsResponse.to_json())

# convert the object into a dict
list_settlements_response_dict = list_settlements_response_instance.to_dict()
# create an instance of ListSettlementsResponse from a dict
list_settlements_response_from_dict = ListSettlementsResponse.from_dict(list_settlements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


