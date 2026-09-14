# CheckoutCaptured


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_uuid** | **str** |  | 
**merchant_order_id** | **str** |  | 
**status** | **str** |  | 
**captured_at** | **datetime** |  | 
**amount** | **int** |  | 
**currency** | **str** |  | 

## Example

```python
from maytes_api_client.models.checkout_captured import CheckoutCaptured

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCaptured from a JSON string
checkout_captured_instance = CheckoutCaptured.from_json(json)
# print the JSON string representation of the object
print(CheckoutCaptured.to_json())

# convert the object into a dict
checkout_captured_dict = checkout_captured_instance.to_dict()
# create an instance of CheckoutCaptured from a dict
checkout_captured_from_dict = CheckoutCaptured.from_dict(checkout_captured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


