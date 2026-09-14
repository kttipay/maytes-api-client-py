# DonationLineItem


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
from maytes_api_client.models.donation_line_item import DonationLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of DonationLineItem from a JSON string
donation_line_item_instance = DonationLineItem.from_json(json)
# print the JSON string representation of the object
print(DonationLineItem.to_json())

# convert the object into a dict
donation_line_item_dict = donation_line_item_instance.to_dict()
# create an instance of DonationLineItem from a dict
donation_line_item_from_dict = DonationLineItem.from_dict(donation_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


