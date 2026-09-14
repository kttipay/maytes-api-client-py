# FoodBeverageLineItem


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

## Example

```python
from maytes_api_client.models.food_beverage_line_item import FoodBeverageLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of FoodBeverageLineItem from a JSON string
food_beverage_line_item_instance = FoodBeverageLineItem.from_json(json)
# print the JSON string representation of the object
print(FoodBeverageLineItem.to_json())

# convert the object into a dict
food_beverage_line_item_dict = food_beverage_line_item_instance.to_dict()
# create an instance of FoodBeverageLineItem from a dict
food_beverage_line_item_from_dict = FoodBeverageLineItem.from_dict(food_beverage_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


