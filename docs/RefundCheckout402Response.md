# RefundCheckout402Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**error** | **str** |  | 
**code** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from maytes_api_client.models.refund_checkout402_response import RefundCheckout402Response

# TODO update the JSON string below
json = "{}"
# create an instance of RefundCheckout402Response from a JSON string
refund_checkout402_response_instance = RefundCheckout402Response.from_json(json)
# print the JSON string representation of the object
print(RefundCheckout402Response.to_json())

# convert the object into a dict
refund_checkout402_response_dict = refund_checkout402_response_instance.to_dict()
# create an instance of RefundCheckout402Response from a dict
refund_checkout402_response_from_dict = RefundCheckout402Response.from_dict(refund_checkout402_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


