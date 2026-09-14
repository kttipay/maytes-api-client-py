# CreateRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Free-text reason; forwarded to Stripe as refund metadata. | [optional] 
**merchant_refund_ref** | **str** | Idempotency key scoped to the merchant. Repeating the same value returns the existing refund. | 

## Example

```python
from maytes_api_client.models.create_refund_request import CreateRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRefundRequest from a JSON string
create_refund_request_instance = CreateRefundRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRefundRequest.to_json())

# convert the object into a dict
create_refund_request_dict = create_refund_request_instance.to_dict()
# create an instance of CreateRefundRequest from a dict
create_refund_request_from_dict = CreateRefundRequest.from_dict(create_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


