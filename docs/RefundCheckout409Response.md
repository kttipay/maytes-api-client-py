# RefundCheckout409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**error** | **str** |  | 
**code** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from maytes_api_client.models.refund_checkout409_response import RefundCheckout409Response

# TODO update the JSON string below
json = "{}"
# create an instance of RefundCheckout409Response from a JSON string
refund_checkout409_response_instance = RefundCheckout409Response.from_json(json)
# print the JSON string representation of the object
print(RefundCheckout409Response.to_json())

# convert the object into a dict
refund_checkout409_response_dict = refund_checkout409_response_instance.to_dict()
# create an instance of RefundCheckout409Response from a dict
refund_checkout409_response_from_dict = RefundCheckout409Response.from_dict(refund_checkout409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


