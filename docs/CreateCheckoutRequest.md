# CreateCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_order_id** | **str** |  | [optional] 
**merchant_expires_at** | **datetime** |  | [optional] 
**total_amount** | **int** |  | 
**currency** | **str** |  | 
**return_url** | **str** |  | 
**cancel_url** | **str** |  | 
**items** | [**List[LineItem]**](LineItem.md) |  | 
**fees** | [**List[CheckoutFee]**](CheckoutFee.md) |  | [optional] 
**discounts** | [**List[CheckoutDiscount]**](CheckoutDiscount.md) |  | [optional] 
**tax** | [**Tax**](Tax.md) |  | [optional] 
**shipping_amount** | **int** |  | [optional] 
**customer_data** | [**CustomerData**](CustomerData.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**allocation_model** | **str** |  | [optional] 

## Example

```python
from maytes_api_client.models.create_checkout_request import CreateCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCheckoutRequest from a JSON string
create_checkout_request_instance = CreateCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCheckoutRequest.to_json())

# convert the object into a dict
create_checkout_request_dict = create_checkout_request_instance.to_dict()
# create an instance of CreateCheckoutRequest from a dict
create_checkout_request_from_dict = CreateCheckoutRequest.from_dict(create_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


