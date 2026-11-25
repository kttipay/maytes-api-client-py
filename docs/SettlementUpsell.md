# SettlementUpsell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_amount** | **int** | Upsell order totals paid out in this settlement, gross, minor units | 
**fee_amount** | **int** | Upsell fees kept by Maytes in this window, minor units | 
**net_amount** | **int** | sales_amount minus fee_amount: the upsell part of the payout | 
**order_count** | **int** |  | 

## Example

```python
from maytes_api_client.models.settlement_upsell import SettlementUpsell

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementUpsell from a JSON string
settlement_upsell_instance = SettlementUpsell.from_json(json)
# print the JSON string representation of the object
print(SettlementUpsell.to_json())

# convert the object into a dict
settlement_upsell_dict = settlement_upsell_instance.to_dict()
# create an instance of SettlementUpsell from a dict
settlement_upsell_from_dict = SettlementUpsell.from_dict(settlement_upsell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


