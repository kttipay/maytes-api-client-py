# PhysicalGoodsLineItem


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
**custom_data** | [**PhysicalGoodsCustomData**](PhysicalGoodsCustomData.md) |  | 

## Example

```python
from maytes_api_client.models.physical_goods_line_item import PhysicalGoodsLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalGoodsLineItem from a JSON string
physical_goods_line_item_instance = PhysicalGoodsLineItem.from_json(json)
# print the JSON string representation of the object
print(PhysicalGoodsLineItem.to_json())

# convert the object into a dict
physical_goods_line_item_dict = physical_goods_line_item_instance.to_dict()
# create an instance of PhysicalGoodsLineItem from a dict
physical_goods_line_item_from_dict = PhysicalGoodsLineItem.from_dict(physical_goods_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


