# TicketSeating


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | **str** |  | [optional] 
**row** | **str** |  | [optional] 
**seat** | **str** |  | [optional] 
**allocation** | **Dict[str, object]** |  | [optional] 

## Example

```python
from maytes_api_client.models.ticket_seating import TicketSeating

# TODO update the JSON string below
json = "{}"
# create an instance of TicketSeating from a JSON string
ticket_seating_instance = TicketSeating.from_json(json)
# print the JSON string representation of the object
print(TicketSeating.to_json())

# convert the object into a dict
ticket_seating_dict = ticket_seating_instance.to_dict()
# create an instance of TicketSeating from a dict
ticket_seating_from_dict = TicketSeating.from_dict(ticket_seating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


