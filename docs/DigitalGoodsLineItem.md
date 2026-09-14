# DigitalGoodsLineItem


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
**custom_data** | [**DigitalGoodsCustomData**](DigitalGoodsCustomData.md) |  | [optional] 

## Example

```python
from maytes_api_client.models.digital_goods_line_item import DigitalGoodsLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of DigitalGoodsLineItem from a JSON string
digital_goods_line_item_instance = DigitalGoodsLineItem.from_json(json)
# print the JSON string representation of the object
print(DigitalGoodsLineItem.to_json())

# convert the object into a dict
digital_goods_line_item_dict = digital_goods_line_item_instance.to_dict()
# create an instance of DigitalGoodsLineItem from a dict
digital_goods_line_item_from_dict = DigitalGoodsLineItem.from_dict(digital_goods_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


