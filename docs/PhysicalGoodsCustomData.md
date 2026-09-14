# PhysicalGoodsCustomData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**comments** | **str** |  | [optional] 

## Example

```python
from maytes_api_client.models.physical_goods_custom_data import PhysicalGoodsCustomData

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalGoodsCustomData from a JSON string
physical_goods_custom_data_instance = PhysicalGoodsCustomData.from_json(json)
# print the JSON string representation of the object
print(PhysicalGoodsCustomData.to_json())

# convert the object into a dict
physical_goods_custom_data_dict = physical_goods_custom_data_instance.to_dict()
# create an instance of PhysicalGoodsCustomData from a dict
physical_goods_custom_data_from_dict = PhysicalGoodsCustomData.from_dict(physical_goods_custom_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


