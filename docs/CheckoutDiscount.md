# CheckoutDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**scope** | **str** |  | 
**amount** | **int** |  | 
**currency** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**applies_to** | **List[str]** |  | [optional] 

## Example

```python
from maytes_api_client.models.checkout_discount import CheckoutDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutDiscount from a JSON string
checkout_discount_instance = CheckoutDiscount.from_json(json)
# print the JSON string representation of the object
print(CheckoutDiscount.to_json())

# convert the object into a dict
checkout_discount_dict = checkout_discount_instance.to_dict()
# create an instance of CheckoutDiscount from a dict
checkout_discount_from_dict = CheckoutDiscount.from_dict(checkout_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


