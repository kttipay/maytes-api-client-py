# TicketCustomData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | 
**event_start_at** | **datetime** |  | 
**timezone** | **str** |  | 
**ticket_class** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**event_end_at** | **datetime** |  | [optional] 
**delivery_mode** | **str** |  | [optional] 
**venue_name** | **str** |  | [optional] 
**venue_address** | **Dict[str, object]** |  | [optional] 
**seating** | [**TicketSeating**](TicketSeating.md) |  | [optional] 
**terms_url** | **str** |  | [optional] 
**attendee_required** | **bool** |  | [optional] 

## Example

```python
from maytes_api_client.models.ticket_custom_data import TicketCustomData

# TODO update the JSON string below
json = "{}"
# create an instance of TicketCustomData from a JSON string
ticket_custom_data_instance = TicketCustomData.from_json(json)
# print the JSON string representation of the object
print(TicketCustomData.to_json())

# convert the object into a dict
ticket_custom_data_dict = ticket_custom_data_instance.to_dict()
# create an instance of TicketCustomData from a dict
ticket_custom_data_from_dict = TicketCustomData.from_dict(ticket_custom_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


