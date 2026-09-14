# ServiceLineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ref** | **str** |  | 
**parent_ref** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**quantity** | **int** |  | 
**unit_price** | **int** |  | 
**currency** | **str** |  | 
**category** | **str** |  | 
**custom_data** | [**ServiceCustomData**](ServiceCustomData.md) |  | [optional] 

## Example

```python
from maytes_api_client.models.service_line_item import ServiceLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLineItem from a JSON string
service_line_item_instance = ServiceLineItem.from_json(json)
# print the JSON string representation of the object
print(ServiceLineItem.to_json())

# convert the object into a dict
service_line_item_dict = service_line_item_instance.to_dict()
# create an instance of ServiceLineItem from a dict
service_line_item_from_dict = ServiceLineItem.from_dict(service_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


