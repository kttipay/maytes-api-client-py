# Checkout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_uuid** | **str** |  | 
**merchant_order_id** | **str** |  | 
**status** | **str** |  | 
**transaction_ref** | **str** |  | 
**checkout_url** | **str** |  | 
**merchant_expires_at** | **datetime** |  | 
**captured_at** | **datetime** |  | 
**return_url** | **str** |  | 
**cancel_url** | **str** |  | 
**amount** | **int** |  | 
**currency** | **str** |  | 
**service_fee** | [**Fee**](Fee.md) |  | 
**refunded_amount** | **int** |  | 
**merchant_processor_fee** | **int** |  | 
**merchant_service_fee** | **int** |  | 
**last_refund_at** | **datetime** |  | 

## Example

```python
from maytes_api_client.models.checkout import Checkout

# TODO update the JSON string below
json = "{}"
# create an instance of Checkout from a JSON string
checkout_instance = Checkout.from_json(json)
# print the JSON string representation of the object
print(Checkout.to_json())

# convert the object into a dict
checkout_dict = checkout_instance.to_dict()
# create an instance of Checkout from a dict
checkout_from_dict = Checkout.from_dict(checkout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


