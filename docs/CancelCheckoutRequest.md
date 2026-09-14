# CancelCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_order_id** | **str** |  | [optional] 

## Example

```python
from maytes_api_client.models.cancel_checkout_request import CancelCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelCheckoutRequest from a JSON string
cancel_checkout_request_instance = CancelCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(CancelCheckoutRequest.to_json())

# convert the object into a dict
cancel_checkout_request_dict = cancel_checkout_request_instance.to_dict()
# create an instance of CancelCheckoutRequest from a dict
cancel_checkout_request_from_dict = CancelCheckoutRequest.from_dict(cancel_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


