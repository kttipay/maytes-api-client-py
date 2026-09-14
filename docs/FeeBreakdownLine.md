# FeeBreakdownLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**label** | **str** |  | 
**amount** | **int** |  | 

## Example

```python
from maytes_api_client.models.fee_breakdown_line import FeeBreakdownLine

# TODO update the JSON string below
json = "{}"
# create an instance of FeeBreakdownLine from a JSON string
fee_breakdown_line_instance = FeeBreakdownLine.from_json(json)
# print the JSON string representation of the object
print(FeeBreakdownLine.to_json())

# convert the object into a dict
fee_breakdown_line_dict = fee_breakdown_line_instance.to_dict()
# create an instance of FeeBreakdownLine from a dict
fee_breakdown_line_from_dict = FeeBreakdownLine.from_dict(fee_breakdown_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


