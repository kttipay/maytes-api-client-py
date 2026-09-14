# TicketLineItem


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
**custom_data** | [**TicketCustomData**](TicketCustomData.md) |  | 

## Example

```python
from maytes_api_client.models.ticket_line_item import TicketLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of TicketLineItem from a JSON string
ticket_line_item_instance = TicketLineItem.from_json(json)
# print the JSON string representation of the object
print(TicketLineItem.to_json())

# convert the object into a dict
ticket_line_item_dict = ticket_line_item_instance.to_dict()
# create an instance of TicketLineItem from a dict
ticket_line_item_from_dict = TicketLineItem.from_dict(ticket_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


