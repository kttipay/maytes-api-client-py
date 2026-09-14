# GetSettlementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Settlement**](Settlement.md) |  | 

## Example

```python
from maytes_api_client.models.get_settlement_response import GetSettlementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSettlementResponse from a JSON string
get_settlement_response_instance = GetSettlementResponse.from_json(json)
# print the JSON string representation of the object
print(GetSettlementResponse.to_json())

# convert the object into a dict
get_settlement_response_dict = get_settlement_response_instance.to_dict()
# create an instance of GetSettlementResponse from a dict
get_settlement_response_from_dict = GetSettlementResponse.from_dict(get_settlement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


